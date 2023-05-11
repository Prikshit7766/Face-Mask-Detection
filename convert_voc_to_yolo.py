import xml.etree.ElementTree as ET
import os

def convert_voc_to_yolo(images_dir, annotations_dir, output_dir):
    # Create YOLO annotations directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    classes = get_class_list_from_voc(annotations_dir)

    # Generate classes.txt file
    classes_file = os.path.join(output_dir, "classes.txt")
    with open(classes_file, "w") as f:
        for class_name in classes:
            f.write(f"{class_name}\n")

    # Generate data.yaml file
    data_content = f"train: {os.path.abspath(images_dir)}/\n" \
                   f"val: {os.path.abspath(images_dir)}/\n" \
                   f"nc: {len(classes)}\n" \
                   f"names: {classes}"
    data_file = os.path.join(output_dir, "data.yaml")
    with open(data_file, "w") as f:
        f.write(data_content)

    # Convert Pascal VOC annotations to YOLO format
    for filename in os.listdir(annotations_dir):
        if filename.endswith(".xml"):
            xml_file = os.path.join(annotations_dir, filename)
            image_name = os.path.splitext(filename)[0]
            image_file = os.path.join(images_dir, f"{image_name}.jpg")
            yolo_file = os.path.join(output_dir, f"{image_name}.txt")

            tree = ET.parse(xml_file)
            root = tree.getroot()

            image_width = int(root.find("size/width").text)
            image_height = int(root.find("size/height").text)

            with open(yolo_file, "w") as f:
                for obj in root.iter("object"):
                    class_name = obj.find("name").text
                    class_id = classes.index(class_name)
                    bbox = obj.find("bndbox")
                    xmin = int(bbox.find("xmin").text)
                    ymin = int(bbox.find("ymin").text)
                    xmax = int(bbox.find("xmax").text)
                    ymax = int(bbox.find("ymax").text)

                    x = (xmin + xmax) / (2 * image_width)
                    y = (ymin + ymax) / (2 * image_height)
                    width = (xmax - xmin) / image_width
                    height = (ymax - ymin) / image_height

                    f.write(f"{class_id} {x} {y} {width} {height}\n")

def get_class_list_from_voc(annotations_dir):
    classes = set()

    for filename in os.listdir(annotations_dir):
        if filename.endswith(".xml"):
            xml_file = os.path.join(annotations_dir, filename)
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for obj in root.iter("object"):
                class_name = obj.find("name").text
                classes.add(class_name)

    return sorted(list(classes))

# Example usage
images_dir = "images/"
annotations_dir = "annotations/"
output_dir = "yolo_annotations/"

convert_voc_to_yolo(images_dir, annotations_dir, output_dir)



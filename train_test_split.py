import os
import shutil
from sklearn.model_selection import train_test_split

# Set the path to the directory containing the images and labels
data_dir = "data/"

# Get a list of all the image file names (without the extension)
image_names = [os.path.splitext(f)[0] for f in os.listdir(os.path.join(data_dir, "images")) if f.endswith(".png")]

# Split the data into a training set and a test set
train_names, test_names = train_test_split(image_names, test_size=0.2, random_state=42)

# Create the train directory and its subdirectories
train_dir = os.path.join(data_dir, "train")
os.makedirs(os.path.join(train_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "labels"), exist_ok=True)

# Create the test directory and its subdirectories
test_dir = os.path.join(data_dir, "test")
os.makedirs(os.path.join(test_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(test_dir, "labels"), exist_ok=True)

# Copy the image and label files for the training set
for name in train_names:
    # Copy the image file
    src_image = os.path.join(data_dir, "images", name + ".png")
    dst_image = os.path.join(train_dir, "images", name + ".png")
    shutil.copy(src_image, dst_image)
    
    # Copy the label file
    src_label = os.path.join(data_dir, "yolo_annotations", name + ".txt")
    dst_label = os.path.join(train_dir, "labels", name + ".txt")
    shutil.copy(src_label, dst_label)

# Copy the image and label files for the test set
for name in test_names:
    # Copy the image file
    src_image = os.path.join(data_dir, "images", name + ".png")
    dst_image = os.path.join(test_dir, "images", name + ".png")
    shutil.copy(src_image, dst_image)
    
    # Copy the label file
    src_label = os.path.join(data_dir, "yolo_annotations", name + ".txt")
    dst_label = os.path.join(test_dir, "labels", name + ".txt")
    shutil.copy(src_label, dst_label)

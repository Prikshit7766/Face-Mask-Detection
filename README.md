# Face Mask Detection using YOLOv5

This repository contains the code for training and testing a YOLOv5 model for face mask detection. The model is trained to classify images into the following classes:

- mask_weared_incorrect
- with_mask
- without_mask

## Dataset

The dataset used for training the model is available on Kaggle: [Face Mask Detection Dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection). It consists of images in PNG format along with corresponding annotations in XML files (in Pascal VOC format).

## Demo




https://github.com/Prikshit7766/Face-Mask-Detection/assets/101416953/8b63fce2-660b-4a61-bc8f-815b3089ae65






## Converting Pascal VOC to YOLO

To use the Pascal VOC dataset format with YOLOv5, the annotations need to be converted to YOLO format. To achieve this, a Python script called `convert_voc_to_yolo.py` is provided in this repository. Run the script to convert the annotations, which will generate YOLO-formatted labels and create `data.yaml` and `classes.txt` files. Move these files outside the dataset folder.

## Data Preparation

Before training the model, the data needs to be prepared in the following way:

1. Split the dataset into training and validation sets, and organize the files as follows:

train:
├── images
└── labels

val:
├── images
└── labels


2. Make sure the images and labels are correctly placed in their respective directories.

## Setup

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Install the required dependencies:
    pip install -r requirements.txt

## Training
To train the YOLOv5 model on your custom dataset, follow these steps:
1. Download the YOLOv5 repository:
```shell
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
```
2. Customize the model configuration file based on your dataset:
```shell
cat models/yolov5s.yaml

```
3. Modify the data.yaml file to match the number of classes and other dataset details.

4. Start training the model:
```shell
    python train.py --img-size 640 --batch-size 16 --epochs 50 --data path/to/data.yaml --weights path/to/weights --name your-experiment-name
```

5. The trained model will be saved in the runs/train/your-experiment-name directory.

## Inference
To perform inference using the trained model, follow these steps:

1. Copy the best.pt file from the trained model directory to the yolov5 directory.

2. Use the following command to detect faces in images:
```
python detect.py --weights path/to/best.pt --img-size 640 --source path/to/images
```


## Local Testing with Webcam

To test the trained model on your local machine using the webcam, follow these steps:

1. Clone the YOLOv5 repository to your local machine:
   ```shell
   git clone https://github.com/ultralytics/yolov5.git
2. Copy the run.py and best.pt files from your trained model directory to the yolov5 directory.

3. Open the run.py file in a text editor and add the following code snippet:
```
import os
os.system("python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
```

4. Save the run.py file.

5. Open a terminal or command prompt and navigate to the yolov5 directory.

6. Run the run.py file using the following command:
7. This command will open your webcam and start detecting face masks in real-time.

8. Press Ctrl+C to stop the webcam detection.

Note: Make sure you have the necessary dependencies installed for running the YOLOv5 code locally.

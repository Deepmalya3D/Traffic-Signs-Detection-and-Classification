# Traffic Signs Detection and Classification
This is the course project for the Applied Machine Learning Course of the M.Sc. Data Science program at the Chennai Mathematical Institute.

**Group members:**  
D Siva Manoj  
Deepmalya Dutta  
Vaishali Agarwal  
Varun Agrawal

## Introduction
Traffic sign detection and classification play a crucial role in improving road safety and preventing accidents. This project utilizes the YOLOv8 model, a state-of-the-art object detection algorithm, to accurately detect and classify various traffic signs in real time.

## Dataset
The dataset used for training and evaluation consists of 4,969 traffic sign images, divided into three parts: train, validation, and test. The dataset covers 15 different classes of traffic signs, including:

Green Light,
Red Light,
Speed Limit (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120),
Stop

![Dataset](https://github.com/Deepmalya3D/Traffic-Signs-Detection-and-Classification/blob/main/data/dataset.png)

## Usage

Prepare the dataset by organizing the images into the appropriate directories (train, valid, test) and update the data.yaml file with the correct paths and class names.  

  
Train the YOLOv8 model:  
```python train.py --data data.yaml --model yolov8m.pt --epochs 30```  
[Reference](https://github.com/Deepmalya3D/Traffic-Signs-Detection-and-Classification/blob/main/src/training.ipynb)

Evaluate the trained model on the test set:  
```python test.py --data data.yaml --weights runs/train/exp/weights/best.pt```  
[Reference](https://github.com/Deepmalya3D/Traffic-Signs-Detection-and-Classification/blob/main/src/testing.ipynb)

Run the Flask app for real-time detection:  
```python app.py```

Access the web interface at http://localhost:5000 to upload an image and perform traffic sign detection.

## Results
The trained YOLOv8 model achieves high accuracy in detecting and classifying traffic signs. The evaluation metrics and plots can be found in the [log](https://github.com/Deepmalya3D/Traffic-Signs-Detection-and-Classification/tree/main/log) directory.    

![recall-confidence](https://github.com/Deepmalya3D/Traffic-Signs-Detection-and-Classification/blob/main/log/1.jpeg)
![f1-confidence](https://github.com/Deepmalya3D/Traffic-Signs-Detection-and-Classification/blob/main/log/3.jpeg)  

  [Link](https://github.com/Deepmalya3D/Traffic-Signs-Detection-and-Classification/blob/main/presentation/Presentation.pdf) to the presentation.

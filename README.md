# Infrared-Temperature-and-Mask-Detection-System
![](https://img.shields.io/badge/Language-Python-green) ![](https://img.shields.io/badge/Hardware-RPi-red) ![](https://img.shields.io/badge/Framework-OpenCV-yellow)

## Description:
Our project aims to create an integrated system combined with mask recognition and infrared thermometer. The system is able to tell the difference whether an individual is wearing a mask or not. Moreover, it can measure an individual's temperature at the same time. The camera and infrared probe will be utilized to implement our project.

## Configuration
1. Tensorflow 2.3.0
2. Python 3.8
3. OpenCV 4.5
4. Raspberry Pi 4B+

## Implementation
### Infrared Temperature Detection
In this part, 


### Mask Detection
In this part, I used **Tensorflow2.3.0** to construct my model, specificly, I used **MobileNet** and **Transfer Learning**.

## Meeting Logging  
2021.4.11  
Discussed the basic timetable and the hardware platform we need(**Raspberry Pi**). In addition, we decided to use **OpenCV** to recongnize the mask.

2021.4.28  
Installed TensorFlow and MiniConda. Tried simple models implemented in TensorFlow. Machine Learning is still in progress.

2021.5.13 - 2021.5.27  
Choose the model and technique. I decided to use MobileNet and Transfer Learning to construct my model.   
Then use the dataset(https://github.com/manish-1305/facemask_detection) to train my model.  
Save it as **.h5** file, make sure that I can use it later on.


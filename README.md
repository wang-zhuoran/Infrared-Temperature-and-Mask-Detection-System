# Infrared-Temperature-and-Mask-Detection-System
![](https://img.shields.io/badge/Language-Python-green) ![](https://img.shields.io/badge/Hardware-RPi-red) ![](https://img.shields.io/badge/Framework-OpenCV-yellow)
![](https://img.shields.io/badge/Framework-Tensorflow2.3-orange)

## Description:
Our project aims to create an integrated system combined with mask recognition and infrared thermometer. The system is able to tell the difference whether an individual is wearing a mask or not. Moreover, it can measure an individual's temperature at the same time. The camera and infrared probe will be utilized to implement our project

## Configuration & Environment
1. Tensorflow 2.3.0
2. Python 3.8
3. OpenCV 4.5
4. Raspberry Pi 4B+

## Implementation
### Infrared Temperature Detection
In this part, MLX90614 was used as the infrared body surface temperature detection module.


### Mask Detection
In this part, I used **Tensorflow2.3.0** to construct my model, specificly, I used **MobileNet** and **Transfer Learning**.

## Project Logging  
2021.4.11  
Discussed the basic timetable and the hardware platform we need(**Raspberry Pi**). In addition, I decided to use **OpenCV** to recongnize the human face.

2021.4.28  
Installed TensorFlow and MiniConda. Tried simple models implemented in TensorFlow. Machine Learning studying is still in progress.

2021.5.13 - 2021.5.27  
Choose the model and technique. I decided to use MobileNet and Transfer Learning to construct my model.   
Then use the dataset(https://github.com/manish-1305/facemask_detection) to train my model.  
Save it as **.h5** file, make sure that I can use it later on.

## Training Model
![image](https://github.com/wang-zhuoran/Infrared-Temperature-and-Mask-Detection-System/blob/main/images/image.png)  

Noted that the directories of dataset should organized as follows:  
-Project directory  
  |-- Dataset  
  |---|-- No_Mask  
  |---|-- With_Mask  
  |-- train_model.py  

## Test Model
Noted that the directory and file should organized as follows:  
-Project directory  
  |-- Dataset  
  |---|-- No_Mask  
  |---|-- With_Mask  
  |-- train_model.py  
  |-- test_model.py  
  |-- haarcascade_frontalface_default.xml  
    
 #### Actual running:  
![image](https://github.com/wang-zhuoran/Infrared-Temperature-and-Mask-Detection-System/blob/main/images/test_model.jpg)

## Reference and Furthur Reading  
[1]Howard A G, Zhu M, Chen B, et al. Mobilenets: Efficient convolutional neural networks for mobile vision applications[J]. arXiv preprint arXiv:1704.04861, 2017.  
[2]Pan S J, Yang Q. A survey on transfer learning[J]. IEEE Transactions on knowledge and data engineering, 2009, 22(10): 1345-1359.  
[3]https://hackcv.com/posts/%E7%BF%BB%E8%AF%91-%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E7%9A%84%E7%9B%B4%E8%A7%82%E8%A7%A3%E9%87%8A/




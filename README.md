# Measuring Unit Conversion from Pound to Kilogram in ROS 
## Publish and Subscribe Method with ROS Parameter - Intelligent Systems and Robotics

* Introduction
  ------------

In this project, we developed a system for conversion from one measuring unit to another. This method allow users to convert amount from pound to kilogram using ROS parameter. It also allow user to change the conversion rate from parameter file (param.yaml) to get desired output.


* Python Files Description
  ------------

We have developed this system in ROS using publisher, subscriber nodes and the parameter where:

1. Converter_pub.py: a publisher node where user will be asked to enter the amount for conversion which will be published on a topic named as ‘Convert’.

2. Converter_sub.py: a subscriber node which will subscribe to this ‘Convert’ topic for reading the published message and fetch the converting rate from the user-defined parameter using get_param feature. This value is changeable as we created param.yaml file in order to modify settings in our program without having to re-compile anything.


* Requirements
  ------------

1.	Linux OS - Ubuntu 20.04 

2.	Python 3.7 or above 


* Output Results
  ------------
  
First, we need to load the param.yaml file as given in the above description section and follow the same steps as provided in Live Weather Update repository to run this code as well. Following shows the output of the program.

![alt text](https://github.com/WaniaKhance/Measuring_Unit_Conversion_using_ROS_Parameters/blob/main/Picture2.png?raw=true)



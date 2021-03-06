﻿# Self-Driving-Car-using-Raspberry-Pi

## Applications

The existing system of driving a car is the manual one. From steering to speed control and lane detection, everything is controlled by human. And humans are erroneous leading to fatal accidents. 
The main purpose of our project is to automate the driving system through image processing so that it could drive the car along the lane and detect any obstacle coming in its way using ultrasonic sensor, thus reducing the chances of accidents

## Requirements

### Code

knowledge of python 3.5 coding.

### Hardware

1) Raspberry Pi 3
2) Motor Driver(L298N)
3) HC-SR04 Ultrasonic Sensor
4) Chassis
5) Camera Module

## Dependencies

1) import RPi
3) import picamera
2) import pygame
3) import numpy
4) import cv2

## Algorithm or Steps of working

1) Check for an obstacle using HC-SR04.
2) If no obstacle is present continue with the next steps, otherwise set all motor outputs to FALSE.
3) The camera module detects the image.
4) Image is converted to greyscale.
5) Gaussian noise kernel is applied to remove
6) the noise around the image of the lane.
7) Canny edge detection is implemented to highlight sharp edges in the picture.
8) Region masking is used to separate the lane edges from other edges obtained in above step.
9) Hough Transform is applied to map the edges on the picture.
10) Finally, left and right lanes are highlighted using red lines.
11) Accordingly, a threshold value decides the direction of movement of the car.
12) Repeat steps 1-11 in an infinite loop.

## Execution

1) Run **a.py** (This file contains code for pygame which is used to make the movement of car depending on direction detected)
2) Run **final.py** (This file contains main code)


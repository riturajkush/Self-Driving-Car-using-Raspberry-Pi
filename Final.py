from picamera.array import PiRGBArray
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import cv2
import numpy as np
import math
GPIO.setmode(GPIO.BOARD)
TRIG = 16
ECHO = 18
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
def dist():
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  while GPIO.input(ECHO)==0:
     pulse_start = time.time()
  while GPIO.input(ECHO)==1:
     pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  print( "Distance:",distance,"cm")
  return distance   

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
p = GPIO.PWM(32,100)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
q = GPIO.PWM(35,100) 
p.start(0)
q.start(0)
theta=0
minLineLength = 5
maxLineGap = 10
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
   
   image = frame.array
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   blurred = cv2.GaussianBlur(gray, (5, 5), 0)
   edged = cv2.Canny(blurred, 85, 85)
   lines = cv2.HoughLinesP(edged,1,np.pi/180,10,minLineLength,maxLineGap)
   if(lines !=None):
       for x in range(0, len(lines)):
           for x1,y1,x2,y2 in lines[x]:
               cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
               theta=theta+math.atan2((y2-y1),(x2-x1))
   #print(theta)GPIO pins were connected to arduino for servo steering control
   threshold=6
   if dist()<=25:
       p.start(0)
       q.start(0)
       print("obstacle")
   else: 
    if(theta>threshold):
       q.start(5)
       p.start(50)
       print("ld")
       GPIO.output(7,True)
       GPIO.output(8,False)
       GPIO.output(12,True)
       GPIO.output(11,False)
       print("left")
    if(theta<-threshold):
       p.start(5)
       q.start(50)
       GPIO.output(7,True)
       GPIO.output(8,False)
       GPIO.output(11,False)
       GPIO.output(12,True)
       print("right")
    if(abs(theta)<threshold):
      p.start(20)
      q.start(20)
      GPIO.output(7,True)
      GPIO.output(8,False)
      GPIO.output(12,True)
      GPIO.output(11,False)
      print("straight")
   theta=0
   cv2.imshow("Frame",image)
   key = cv2.waitKey(30) & 0xFF
   rawCapture.truncate(0)
   if key == ord("q"):
       break

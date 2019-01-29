
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import *
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
p = GPIO.PWM(32,100)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
q = GPIO.PWM(35,100) 
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('pygame Caption')
pygame.mouse.set_visible(0)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == (K_DOWN):
                print("dd")
                p.start(100)
                q.start(100)
                GPIO.output(8,True)
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(12,False)
                print("REVERSE")

            if event.key == (K_UP):
                print("ud")
                p.start(100)
                q.start(100)
                GPIO.output(7,True)
                GPIO.output(8,False)
                GPIO.output(12,True)
                GPIO.output(11,False)
                print("FORWARD")
            if event.key == (K_RIGHT):
                print("rd")
                p.start(15)
                q.start(100)
                GPIO.output(7,True)
                GPIO.output(8,False)
                GPIO.output(11,False)
                GPIO.output(12,True)
                print("RIGHT")

            if event.key == (K_LEFT):
                q.start(15)
                p.start(100)
                print("ld")
                GPIO.output(7,True)
                GPIO.output(8,False)
                GPIO.output(12,True)
                GPIO.output(11,False)
                print("LEFT")


        if event.type == KEYUP:
            if event.key == (K_UP):
                print("uu")
                GPIO.output(7,False)
                GPIO.output(8,False)
                GPIO.output(11,False)
                GPIO.output(12,False)
                print("STOP YOU ASSHOLE")
            if event.key == (K_DOWN):
                print("du")
                GPIO.output(7,False)
                GPIO.output(8,False)
                GPIO.output(11,False)
                GPIO.output(12,False)
                print("STOP YOU ASSHOLE")
            if event.key == (K_LEFT):
                print("lu")
                GPIO.output(7,False)
                GPIO.output(8,False)
                GPIO.output(11,False)
                GPIO.output(12,False)
                print("STOP YOU ASSHOLE")

            if event.key == (K_RIGHT):
                print("ru")
                GPIO.output(7,False)
                GPIO.output(8,False)
                GPIO.output(11,False)
                GPIO.output(12,False)
                print("STOP YOU ASSHOLE")
            
        
            if (event.key == K_ESCAPE):
                done = Tru
                e   
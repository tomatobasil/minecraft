import RPi.GPIO as GPIO  
from time import sleep 
from mcpi import minecraft
import time
mc = minecraft.Minecraft.create()
 

pin = 11

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)
 

while True:
    sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 4 and pos.z == 9:
            for i in range(0,50):
                     GPIO.output(pin,GPIO.HIGH)
    else:
            GPIO.output(pin,GPIO.LOW) 
            
                         
        

GPIO.cleanup()  



        

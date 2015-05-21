import RPi.GPIO as GPIO  
from time import sleep 
from mcpi import minecraft
import time
mc = minecraft.Minecraft.create()

def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return  

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)
 

while True:
    sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 4 and pos.z == 10:
            for i in range(0,50):
                        blink(11)  
        
GPIO.cleanup()  

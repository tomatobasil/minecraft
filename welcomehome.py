from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()

while True:
    sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 39 and pos.z == 120:
        mc.postToChat("Welcome Home")
    
    

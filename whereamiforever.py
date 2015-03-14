from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    mc.postToChat(pos)
    sleep(0.1)
    

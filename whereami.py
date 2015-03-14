from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()


pos = mc.player.getPos()
mc.postToChat(pos)

    

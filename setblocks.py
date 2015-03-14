from mcpi import minecraft
from time import sleep


mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

for a in range(50):
    mc.setBlock(pos.x+3, pos.y+a, pos.z, 1)
    

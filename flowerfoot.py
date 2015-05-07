from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()

flower = 8
while True:
    x, y, z, = mc.player.getPos()
    mc.setBlock(x, y-1, z, flower)
    sleep(0.1)

from mcpi import minecraft
from time import sleep

block = 0

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

mc.setBlocks(pos.x, pos.y, pos.z, pos.x+3, pos.y+3, pos.z+3, block)
mc.postToChat("Boom Baby!")

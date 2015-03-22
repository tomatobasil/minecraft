from mcpi import minecraft
import time
mc = minecraft.Minecraft.create()

players = mc.getPlayerEntityIds()
mc.camera.setFollow(players[0])
time.sleep(10)
mc.camera.setNormal()



    

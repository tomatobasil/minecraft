
    
from mcpi import minecraft
from time import sleep
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
def stackTNT (x, y, z):
    tnt = 46
    
    for a in range(10):
       
        mc.setBlock(pos.x, pos.y+a, pos.z, tnt, 2)
        mc.setBlock(pos.x+a, pos.y, pos.z, tnt, 1)
        mc.setBlock(pos.x, pos.y, pos.z+a, tnt, 1)
        mc.setBlock(pos.x+1, pos.y+a, pos.z, tnt, 1)
    else:
        mc.postToChat("Error!")
        
stackTNT(pos.x, pos.y, pos.z)
mc.postToChat("Stacked and ready")



    
    

    








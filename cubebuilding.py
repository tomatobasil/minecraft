
    
from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

def stackTNT (x, y, z):
    a = 0
    i = 1
    tnt = 46
    dimension = 4;
    while a <= dimension:
     mc.setBlock(pos.x+a, pos.y, pos.z, tnt, 1)
     mc.setBlock(pos.x, pos.y+a, pos.z, tnt, 1)
     mc.setBlock(pos.x, pos.y, pos.z+a, tnt, 1)
     mc.setBlock(pos.x+a, pos.y, pos.z+(dimension-1), tnt, 1)
     mc.setBlock(pos.x+(dimension-1), pos.y, pos.z+a, tnt, 1)
     mc.setBlock(pos.x, pos.y+(dimension-1), pos.z, tnt, 1)
     mc.setBlock(pos.x+a, pos.y, pos.z+(dimension-2), tnt, 1)
     mc.setBlock(pos.x+(dimension-2), pos.y, pos.z+a, tnt, 1)
     mc.setBlock(pos.x, pos.y+(dimension-2), pos.z, tnt, 1)
     mc.setBlock(pos.x+a, pos.y, pos.z+(dimension-3), tnt, 1)
     mc.setBlock(pos.x+(dimension-3), pos.y, pos.z+a, tnt, 1)
     mc.setBlock(pos.x, pos.y+(dimension-3), pos.z, tnt, 1)
    

    

    
    
     
    
     a = a+1
   

     

     
               
stackTNT(pos.x, pos.y+1, pos.z+1)
mc.postToChat("Stacked and ready")



    
    

    








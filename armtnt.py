from mcpi import minecraft
mc = minecraft.Minecraft.create()


def armTNT (x, y, z):
    tnt = 46
    block = mc.getBlock(x, y, z)
    if block == tnt:
        mc.setBlock(x, y, z, tnt, 1)
        mc.postToChat("TNT ARMED!")
    else:
        mc.postToChat("Block is not TNT")

pos = mc.player.getTilePos()
armTNT(pos.x, pos.y - 1, pos.z)

    

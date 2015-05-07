import mcpi.minecraft as minecraft

import time

mc = minecraft.Minecraft.create()


states = [0, 5, 6, 11, 3, 8, 9, 2, 12, 7, 4, 16]

pos = mc.player.getPos()

x = pos.x + 2
y = pos.y
z = pos.z
blockId = 63


for state in states:
        mc.setBlock(x, y, z, blockId, state)
        time.sleep(0.3)

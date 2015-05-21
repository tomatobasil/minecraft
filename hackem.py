from mcpi import minecraft
mc = minecraft.Minecraft.create()


#mc.player.postToChat('hahahahahahha')

#hacked.setting("world_immutable", False)

i = ["192.168.1.148", "192.168.1.71", "192.168.1.168", "192.168.1.205", "192.168.1.218"]
c = 0
while True:

    hacked = minecraft.Minecraft.create(i[c])
    hacked.player.setPos(16, -150, 16)
    c = c + 1
    if(c == 4):
        break
    
      

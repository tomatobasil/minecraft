from mcpi import minecraft
mc = minecraft.Minecraft.create()

hacked = minecraft.Minecraft.create("192.168.1.145")


hacked.setting("world_immutable", False )
mc.postToChat('hahahahahahha')

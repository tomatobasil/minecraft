from mcpi import minecraft
mc = minecraft.Minecraft.create()

username = raw_input("Enter a username: ")
mc.postToChat(username + " has entered chat")
message = raw_input("Message: ")

while message != "/exit":
    mc.postToChat(username +": " + message)
    message = raw_input("Message: ")
else:
    mc.postToChat(username + " has left the chat")
    

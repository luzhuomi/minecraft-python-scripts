# source
# https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi/2&hl=en-SG&f=1&tk=5662585833732583976&rqid=BP8sXvP3DZjghgGfk6DwCQ&pid=2ith-minecraft-pi/2&hl=en-SG&f=1&tk=5662585833732583976&rqid=BP8sXvP3DZjghgGfk6DwCQ&pid=2

from mcpi import minecraft, block

mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")
x,y,z = mc.player.getPos()


mc.setBlock(x+1, y, z, block.CRAFTING_TABLE.id)

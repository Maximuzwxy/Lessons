import random
import time

from mcpi import minecraft
from mcpi import block
from mcpi import entity

mc = minecraft.Minecraft.create('192.168.66.207')
# mc = minecraft.Minecraft.create()
player = mc.player

time.sleep(3)
x, y, z = player.getTilePos()

# pillar
i = 0
while i <= 50:
    mc.setBlock(x, y + i, z, 41)
    i += 1
    time.sleep(0.1)

# bridge
# i = 0
# while i <= 20:
#     mc.setBlock(x + i, y, z, 41)
#     i += 1
#     time.sleep(0.1)
#
# bridge-2
# i = 0
# while i <= 50:
#     if i % 2 == 0:
#         mc.setBlock(x + i, y, z, 41)
#     else:
#         mc.setBlock(x + i, y, z, 57)
#     i += 1
#     time.sleep(0.1)

# random teleport--near
# radius = 200
# while True:
#     dx = random.randint(-radius, radius)
#     dy = random.randint(-20, 50)
#     dz = random.randint(-radius, radius)
#
#     # mc.setBlock(x + dx, y + dy, z + dz, 0)
#     # mc.setBlock(x + dx, y + dy + 1, z + dz, 0)
#     player.setPos(x + dx, y + dy, z + dz)
#
#     time.sleep(5)

# random teleport--anywhere
# radius = 5000
# while True:
#     x = random.randint(-radius, radius)
#     z = random.randint(-radius, radius)
#
#     mc.setBlock(x, y, z, 0)
#     mc.setBlock(x, y + 1, z, 0)
#     player.setPos(x, y, z)
#
#     time.sleep(10)

# flower walker-yellow
# while True:
#     x, y, z = player.getTilePos()
#     mc.setBlock(x, y, z, 37)
#     time.sleep(0.1)

# flower walker-random color
# while True:
#     x, y, z = player.getTilePos()
#     mc.setBlock(x, y, z, 38, random.randint(0, 9))
#     time.sleep(0.2)

# flower walker-flower sea
# while True:
#     x, y, z = player.getTilePos()
#     dx = random.randint(-5, 5)
#     dz = random.randint(-5, 5)
#     mc.setBlock(x + dx, y, z + dz, 38, random.randint(0, 9))
#     time.sleep(0.01)

# radius = 50
# while True:
#     dx = random.randint(-radius, radius)
#     dy = random.randint(0, 10)
#     dz = random.randint(-radius, radius)
#
#     # mc.spawnEntity(x + dx, y + dy, z + dz, entity.PRIMED_TNT)
#     mc.spawnEntity(x + dx, y + dy, z + dz, 20)
#     time.sleep(1)





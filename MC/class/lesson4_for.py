import random
import time
import math

from mcpi import minecraft
from mcpi import block
from mcpi import entity

# mc = minecraft.Minecraft.create('192.168.66.207')
mc = minecraft.Minecraft.create('192.168.43.206')
# mc = minecraft.Minecraft.create()

# blocks = [block.STONE.id, block.GRASS.id, block.WOOD.id, block.GLASS.id, block.GOLD_BLOCK.id]

time.sleep(3)

x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, 41)


# 依次生成blocks
# blocks = [1, 2, 17, 20, 41, 57, 35]

# for i in blocks:
#     mc.setBlock(x, y, z, )
#     time.sleep(1)
#     x = x + 1

# x方向生成block
# for i in range(10):
#     mc.setBlock(x + i, y, z, 41)
#     time.sleep(0.2)

# 每隔一个生成block
# for i in range(20):
#     if i % 2 == 0:
#         mc.setBlock(x + i, y, z, 41)
#     else:
#         mc.setBlock(x + i, y, z, 57)
#     time.sleep(0.2)

# for i in range(0, 20, 2):
#     mc.setBlock(x + i, y, z, 41)
#     time.sleep(0.2)

# 3种block交替生成
# for i in range(20):
#     if i % 3 == 0:
#         mc.setBlock(x + i, y, z, 41)
#     elif i % 3 == 1:
#         mc.setBlock(x + i, y, z, 57)
#     elif i % 3 == 2:
#         mc.setBlock(x + i, y, z, 73)
#     time.sleep(0.2)

# 平面
# for i in range(10):
#     for j in range(10):
#         mc.setBlock(x + j, y, z + i, 41)
#         time.sleep(0.1)

# 墙
# for i in range(10):
#     for j in range(10):
#         mc.setBlock(x + j, y + i, z, 41)
#         time.sleep(0.1)

# 立方体
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             mc.setBlock(x + k, y + i, z + j, 41)
#             time.sleep(0.1)


# chicken rocket
# for i in range(30):
#     mc.spawnEntity(x, y + i, z, entity.CHICKEN)
#     mc.player.setPos(x, y + i + 2, z)
#     time.sleep(0.1)

# stairs
# for i in range(30):
#     mc.setBlock(x + i, y + i, z, 41)
#     time.sleep(0.1)

# for j in range(3):
#     for i in range(30):
#         mc.setBlock(x + i, y + i, z + j, 41)
#         time.sleep(0.1)

# 实体楼梯
# for i in range(10):
#     for j in range(10 - i):
#         mc.setBlock(x + i + j, y + i, z, 41)
#         time.sleep(0.1)

# for i in range(10):
#     for j in range(10):
#         mc.setBlock(x + j, y + i, z, 41)
#         time.sleep(0.1)


# for k in range(3):
#     for i in range(10):
#         for j in range(10 - i):
#             mc.setBlock(x + i + j, y + i, z + k, 41)
#             time.sleep(0.1)
#
# # Pyramid-setBlock
# def pyramid(n):
#     for i in range(n):
#         for j in range(n - 2 * i):
#             for k in range(n - 2 * i):
#                 mc.setBlock(x + i + k, y + i, z + i + j, 41)
#                 time.sleep(0.01)
# pyramid(20)

# setBlocks
# mc.setBlocks(x, y, z, x + 3, y, z, 41)
# mc.setBlocks(x, y, z, x + 3, y, z + 3, 41)
# mc.setBlocks(x, y, z, x + 3, y + 3, z + 3, 41)

# what will happen
# mc.setBlocks(x-3, y-3, z-3, x+3, y+3, z+3, 2)

# platform under
# n = 5
# mc.setBlocks(x - n, y - 1, z - n, x + n, y - 1, z + n, 41)


#
# Pyramid-setBlocks
# n = 5
# for i in range(n, -1, -1):
#     mc.setBlocks(x - i, y - 1 - i, z - i, x + i, y - 1 - i, z + i, 41)  # 建造⼀层⾦字
#     time.sleep(0.1)

# rainbow street
# for i in range(5):  # 获取玩家坐标
#     c1 = random.randint(0, 15)  #获取第⼀个随机颜⾊
#     mc.setBlocks(x + 1, y, z + 1, x + 5, y + 3, z + 5, 35, c1)
#
#     c2 = random.randint(0, 15)  #获取第⼆个随机颜⾊
#     mc.setBlocks(x + 1, y, z - 5, x + 5, y + 3, z - 9, 35, c2)
#
#     x = x + 6


# rainbow
# rb_x, rb_y, rb_z = 1200, 47, -1030
# def build_platform(px, py, pz, radius):
#     mc.setBlocks(px - radius, py - radius, pz - radius, px + radius, py + radius, pz + radius, block.AIR)
#     mc.setBlocks(px - radius, py, pz - radius, px + radius, py, pz + radius, block.GLASS)
#
# build_platform(rb_x, rb_y, rb_z, 30)
#
# # 画垂直于地面的空心圆圈（xy平面，z不变）
# def draw_vertical_circle(center_mc, center_x, center_y, center_z, radius, block_id, block_data=0):
#     for angle in range(0, 360, 2):
#         rad = math.radians(angle)
#         cur_x = round(center_x + radius * math.sin(rad))
#         cur_y = round(center_y + radius * math.cos(rad))
#         center_mc.setBlock(cur_x, cur_y, center_z, block_id, block_data)
#         time.sleep(0.01)
# # draw_vertical_circle(mc, rb_x, rb_y, rb_z, 15, block.WOOL, 14)
#
# # rainbow
# def build_rainbow():
#     colors = [14, 1, 4, 5, 3, 11, 10]  # 红橙黄绿蓝靛紫
#     for index, color in enumerate(colors):
#         draw_vertical_circle(mc, rb_x, rb_y, rb_z, 20 + index, block.WOOL.id, color)
# build_rainbow()

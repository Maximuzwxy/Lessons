import time

from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()
player = mc.player

time.sleep(3)

RED = 14
GREEN = 13

# platform xyz
px, py, pz = -946, 19, -17

# Task0: build a platform
def build_platform(n):
    # clear blocks
    mc.setBlocks(px, py, pz, px + n, py + 4, pz + n, 0)
    time.sleep(1)
    # rebuild platform
    mc.setBlocks(px, py, pz, px + n, py, pz + n, 17)
build_platform(18)

# Task1: build the lane
# lane xyz--car start position
sx, sy, sz = px + 4, py, pz + 4
def build_lane():
    mc.setBlocks(sx, sy, sz, sx + 10, sy, sz, 1)
    mc.setBlocks(sx + 10, sy, sz, sx + 10, sy, sz + 10, 1)
    mc.setBlocks(sx + 10, sy, sz + 10, sx, sy, sz + 10, 1)
    mc.setBlocks(sx, sy, sz + 10, sx, sy, sz, 1)
build_lane()

# Task2: build the moving car demo
cx, cy, cz = sx, sy + 1, sz
def init_car():
    mc.setBlock(cx, cy, cz, 35)

def car_move_demo():
    global cx, cy, cz
    dx = 1

    while True:
        mc.setBlock(cx, cy, cz, 0)
        cx = cx + dx
        mc.setBlock(cx, cy, cz, 35)
        time.sleep(0.2)

        if cx >= sx + 10:
            mc.setBlock(cx, cy, cz, 0)
            cx = sx

init_car()
# car_move_demo()

# Task3: build the moving car
dx, dz = 0, 0
def car_move():
    global cx, cy, cz
    global dx, dz
    if cx == sx and cz == sz:
        dx = 1
        dz = 0
    elif cx == sx + 10 and cz == sz:
        dx = 0
        dz = 1
    elif cx == sx + 10 and cz == sz + 10:
        dx = -1
        dz = 0
    elif cx == sx and cz == sz + 10:
        dx = 0
        dz = -1

    mc.setBlock(cx, cy, cz, 0)
    cx = cx + dx
    cz = cz + dz
    mc.setBlock(cx, cy, cz, 35)

def test_car():
    while True:
        car_move()
        time.sleep(0.2)
# test_car()

# Task4: Build the traffic light, get xyz
# light xyz
lx, ly, lz = px + 3, py + 1, pz + 3
def build_light(x, y, z):
    # A
    mc.setBlock(x, y, z, 35, 10)
    # B
    mc.setBlock(x, y + 1, z, 35, 10)
    # LIGHT
    mc.setBlock(x, y + 2, z, 35, RED)
build_light(lx, ly, lz)

# Task5: Change the light
light_green = False

while True:
    hits = mc.events.pollBlockHits()
    for h in hits:
        hx, hy, hz = h.pos
        if hx == lx and hy == ly + 2 and hz == lz:
            b = mc.getBlockWithData(hx, hy, hz)
            mc.postToChat(f'x y z: {hx} {hy} {hz}')

            if b.data == GREEN:
                mc.setBlock(hx, hy, hz, 35, RED)
                light_green = False
            elif b.data == RED:
                mc.setBlock(hx, hy, hz, 35, GREEN)
                light_green = True

    if light_green:
        car_move()

    time.sleep(0.2)





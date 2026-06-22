# USACO 2015 December Contest, Bronze
# Problem 2. Speeding Ticket
# https://usaco.org/index.php?page=viewproblem2&cpid=568

import sys

# sys.stdin = open('speeding.in', 'r')
# sys.stdout = open('speeding.out', 'w')

n, m = map(int, input().split())

seg_limit = []
seg_bessie = []

# limit = [0] * 101
# bessie = [0] * 101
limit = []
bessie = []

for i in range(n):
    seg_limit.append(input())

for i in range(m):
    seg_bessie.append(input())

# print(seg_limit, seg_bessie)

# def set_speed(dest, origin, num):
#     start = 1
#     for j in range(num):
#         dis, speed = map(int, origin[j].split())
#         for k in range(start, start + dis):
#             dest[k] = speed
#         start += dis

def set_speed(dest, origin, num):
    for j in range(num):
        dis, speed = map(int, origin[j].split())
        for k in range(dis):
            dest.append(speed)

set_speed(limit, seg_limit, n)
set_speed(bessie, seg_bessie, m)

# for x in range(len(limit)):
#     print(x, limit[x])
#
# for x in bessie:
#     print(x, bessie[x])

max_v = 0
for x in range(101):
    max_v = max(max_v, bessie[x] - limit[x])

print(max_v)


# solution 2
# import sys
#
# sys.stdin = open('speeding.in', 'r')
# sys.stdout = open('speeding.out', 'w')
#
# n, m = map(int, input().split())
#
# limit = []
# bessie = []
#
# for i in range(n):
#     limit.append(list(map(int, input().split())))
#
# for j in range(m):
#     bessie.append(list(map(int, input().split())))
#
# x = y = 0
# max_v = 0
#
# while x < n and y < m:
#     max_v = max(max_v, bessie[y][1] - limit[x][1])
#     if limit[x][0] > bessie[y][0]:
#         limit[x][0] -= bessie[y][0]
#         y += 1
#     elif limit[x][0] < bessie[y][0]:
#         bessie[y][0] -= limit[x][0]
#         x += 1
#     else:
#         x += 1
#         y += 1
#
# print(max_v)


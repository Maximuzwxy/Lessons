# USACO 2018 December Contest, Bronze
# Problem 1. Mixing Milk
# https://usaco.org/index.php?page=viewproblem2&cpid=855

import sys

sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

c = [0] * 3
m = [0] * 3

for i in range(3):
    c[i], m[i] = map(int, input().split())

origin = dest = 0

for i in range(1, 101):
    if i % 3 == 1:
        origin = 0
        dest = 1
    elif i % 3 == 2:
        origin = 1
        dest = 2
    else:
        origin = 2
        dest = 0

    if m[origin] + m[dest] <= c[dest]:
        m[dest] += m[origin]
        m[origin] = 0
    else:
        m[origin] = m[origin] + m[dest] - c[dest]
        m[dest] = c[dest]

for j in m:
    print(j)


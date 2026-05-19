# USACO 2020 February Contest, Bronze
# Problem 1. Triangles
# https://usaco.org/index.php?page=viewproblem2&cpid=1011

from itertools import combinations
import sys
sys.stdin = open('triangles', 'r')
sys.stdout = open('triangles', 'w')

n = int(input())
posts = []
triangles = []

for _ in range(n):
    posts.append(list(map(int, input().split())))

triangles = combinations(posts, 3)

def get_area(a, b, c):
    x = y = 0

    if a[1] == b[1]:
        x = abs(a[0] - b[0])
    elif a[1] == c[1]:
        x = abs(a[0] - c[0])
    elif b[1] == c[1]:
        x = abs(b[0] - c[0])

    if a[0] == b[0]:
        y = abs(a[1] - b[1])
    elif a[0] == c[0]:
        y = abs(a[1] - c[1])
    elif b[0] == c[0]:
        y = abs(b[1] - c[1])

    return x * y

max_area = 0

for i, j, k in triangles:
    max_area = max(max_area, get_area(i, j, k))

print(max_area)

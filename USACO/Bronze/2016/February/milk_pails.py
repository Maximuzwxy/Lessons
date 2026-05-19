# USACO 2016 February Contest, Bronze
# Problem 1. Milk Pails
# https://usaco.org/index.php?page=viewproblem2&cpid=615

# solution 1
# import sys
# sys.stdin = open('pails.in', 'r')
# sys.stdout = open('pails.out', 'w')
#
# x, y, m = map(int, input().split())
#
# a = m // x
# b = m // y
#
# max_v = 0
#
# for i in range(0, a + 1):
#     for j in range(0, b + 1):
#         p = x * i + y * j
#         if p <= m:
#             max_v = max(max_v, p)
#
# # Optimization plan
# # for i in range(0, a + 1):
# #     j = (m - x * i) // y
# #     max_v = max(max_v, x * i + y * j)
#
# print(max_v)


# solution 2
import sys
# sys.stdin = open('pails.in', 'r')
# sys.stdout = open('pails.out', 'w')

x, y, m = map(int, input().split())

pail = [False] * (m + 1)
pail[0] = True
max_v = 0

for i in range(m + 1):
    if pail[i]:
        if i + x <= m:
            pail[i + x] = True
        if i + y <= m:
            pail[i + y] = True

        max_v = max(max_v, i)

print(max_v)

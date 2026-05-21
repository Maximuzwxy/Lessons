# USACO 2016 US Open Contest, Bronze
# Problem 1. Diamond Collector
# https://usaco.org/index.php?page=viewproblem2&cpid=639

# solution 1
# import sys
# sys.stdin = open('diamond.in', 'r')
# sys.stdout = open('diamond.out', 'w')
#
# n, k = map(int, input().split())
# diamonds = []
#
# for _ in range(n):
#     diamonds.append(int(input()))
#
# max_v = 0
# for i in range(n):
#     count = 1
#     for j in range(n):
#         if i == j:
#             continue
#         if 0 <= diamonds[j] - diamonds[i] <= k:
#             count += 1
#     max_v = max(max_v, count)
#
# print(max_v)

# solution 2
import sys
sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')

n, k = map(int, input().split())
diamonds = []

for _ in range(n):
    diamonds.append(int(input()))

diamonds.sort()

max_v = 0
for i in range(n):
    count = 1
    for j in range(i + 1, n):
        if diamonds[j] - diamonds[i] <= k:
            count += 1
    max_v = max(max_v, count)

print(max_v)

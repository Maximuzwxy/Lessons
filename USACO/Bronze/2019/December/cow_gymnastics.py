# USACO 2019 December Contest, Bronze
# Problem 1. Cow Gymnastics
# https://usaco.org/index.php?page=viewproblem2&cpid=963

# solution 1
import sys
from itertools import permutations
from itertools import combinations
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())
sessions = []
for _ in range(k):
    sessions.append(list(map(int, input().split())))

com = list(permutations([i for i in range(1, n + 1)], 2))
pairs = []
num = 0

for s in sessions:
    pairs.append(list(combinations(s, 2)))

for c in com:
    flag = True
    for p in pairs:
        if c not in p:
            flag = False
            break
    if flag:
        num += 1

print(num)

# solution 2
# import sys
# sys.stdin = open('gymnastics.in', 'r')
# sys.stdout = open('gymnastics.out', 'w')
#
# k, n = map(int, input().split())
# sessions = []
# for _ in range(k):
#     sessions.append(list(map(int, input().split())))
# # print(sessions)
#
# pairs = []
# num = 0
#
# for i in range(k):
#     t = []
#     for j in range(n - 1):
#         for k in range(j + 1, n):
#             t.append((sessions[i][j], sessions[i][k]))
#     pairs.append(t)
# # print(pairs)
#
# for t in pairs[0]:
#     ret = True
#     for x in range(1, len(pairs)):
#         if t not in pairs[x]:
#             ret = False
#             break
#     if ret:
#         num += 1
# print(num)


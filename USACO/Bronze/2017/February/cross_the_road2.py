# USACO 2017 February Contest, Bronze
# Problem 2. Why Did the Cow Cross the Road II
# https://usaco.org/index.php?page=viewproblem2&cpid=712

# solution 1
# from collections import Counter
# import sys
# sys.stdin = open('circlecross.in', 'r')
# sys.stdout = open('circlecross.out', 'w')
#
# s = input()
# stack = []
# cnt = 0
#
# def check_cross(cow):
#     index_in = stack.index(cow)
#     index_out = stack.index(cow, index_in + 1)
#
#     d = Counter(stack[index_in + 1:index_out])
#     num = 0
#     for k, v in d.items():
#         if v == 1:
#            num += 1
#     return num
#
# for c in s:
#     if stack:
#         if stack[-1] == c:
#             stack.pop()
#         else:
#             if c not in stack:
#                 stack.append(c)
#             else:
#                 stack.append(c)
#                 cnt += check_cross(c)
#     else:
#         stack.append(c)
# print(cnt // 2)

# solution 2
import sys
sys.stdin = open('circlecross.in', 'r')
sys.stdout = open('circlecross.out', 'w')

cross = list(input())
cows = []
cnt = 0

for i in range(26):
    cows.append(chr(ord('A') + i))
# print(cows)

for i in range(26):
    for j in range(i + 1, 26):
        index_i = []
        index_j = []
        for k in range(len(cross)):
            if cows[i] == cross[k]:
                index_i.append(k)
            if cows[j] == cross[k]:
                index_j.append(k)

        if index_i[0] < index_j[0] < index_i[1] < index_j[1] \
            or index_j[0] < index_i[0] < index_j[1] < index_i[1]:
            cnt += 1

print(cnt)


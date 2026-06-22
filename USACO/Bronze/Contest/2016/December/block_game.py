import sys

# solution 1 -- timeout
# sys.stdin = open('blocks.in', 'r')
# sys.stdout = open('blocks.out', 'w')
#
# final = [0] * 26
# board = []
# possible = []
#
# n = int(input())
# for i in range(n):
#     board.append(input().split())
#
# def refresh(ss):
#     tmp = [0] * 26
#     for c in ss:
#         index = ord(c) - ord('a')
#         tmp[index] += 1
#
#     for x in range(26):
#         final[x] = max(final[x], tmp[x])
#
# def get_list(l, d):
#     if d == 0:
#         s = ''
#         for q in range(n):
#             s += board[q][l[q]]
#         refresh(s)
#
#         l.pop()
#         return
#
#     for j in range(2):
#         l.append(j)
#         get_list(l, d - 1)
#
#     if l:
#         l.pop()
#
# get_list([], n)
#
# for _ in final:
#     print(_)

# solution 2
import sys
# sys.stdin = open('blocks.in', 'r')
# sys.stdout = open('blocks.out', 'w')

final = [0] * 26
board = []

n = int(input())
for i in range(n):
    board.append(input().split())

lines = [[0] * 26 for _ in range(n)]

for j in range(n):
    s = board[j][0]
    tmp1 = [0] * 26
    for c in board[j][0]:
        index = ord(c) - ord('a')
        tmp1[index] += 1

    tmp2 = [0] * 26
    for c in board[j][1]:
        index = ord(c) - ord('a')
        tmp2[index] += 1

    for k in range(26):
        lines[j][k] = max(tmp1[k], tmp2[k])

for x in range(26):
    for y in range(n):
        final[x] += lines[y][x]

for z in final:
    print(z)

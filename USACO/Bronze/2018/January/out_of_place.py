# USACO 2018 January Contest, Bronze
# Problem 3. Out of Place
# https://usaco.org/index.php?page=viewproblem2&cpid=785

# solution 1
# import sys
#
# sys.stdin = open('outofplace.in', 'r')
# sys.stdout = open('outofplace.out', 'w')
#
# n = int(input())
# line = []
#
# for i in range(n):
#     line.append(int(input()))
# bessie = 0
#
# left = True
# for i in range(n - 1):
#     if line[i] > line[i + 1]:
#         if i == 0:
#             bessie = 0
#             left = False
#         else:
#             if line[i - 1] < line[i + 1]:
#                 bessie = i
#                 left = False
#             else:
#                 bessie = i + 1
#         break
#
# cnt = 0
# if left:
#     for j in range(bessie, -1, -1):
#         target = j - 1
#         if line[target] > line[bessie]:
#             if line[target] == line[target - 1]:
#                 continue
#             line[bessie], line[target] = line[target], line[bessie]
#             bessie = target
#             cnt += 1
#         else:
#             break
# else:
#     for j in range(bessie, n - 1):
#         target = j + 1
#         if line[target] < line[bessie]:
#             if line[target] == line[target + 1]:
#                 continue
#             line[bessie], line[target] = line[target], line[bessie]
#             bessie = target
#             cnt += 1
#         else:
#             break
#
# print(cnt)

# solution 2
import sys

# sys.stdin = open('outofplace.in', 'r')
# sys.stdout = open('outofplace.out', 'w')

n = int(input())
line = []

for i in range(n):
    line.append(int(input()))

new_line = sorted(line)

start = -1
end = -1

for i in range(n):
    if line[i] != new_line[i]:
        start = i
        break

for i in range(n - 1, -1, -1):
    if line[i] != new_line[i]:
        end = i
        break

cnt = end - start

for i in range(start, end):
    if line[i] == line[i + 1]:
        cnt -= 1

print(cnt)



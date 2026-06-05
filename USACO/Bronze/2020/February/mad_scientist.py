# USACO 2020 February Contest, Bronze
# Problem 2. Mad Scientist
# https://usaco.org/index.php?page=viewproblem2&cpid=1012

# # solution 1 - for loop
# import sys
# sys.stdin = open('breedflip.in', 'r')
# sys.stdout = open('breedflip.out', 'w')
#
# n = int(input())
# a = input()
# b = input()
#
# count = 0
# flag = True
#
# for i in range(n):
#     if a[i] != b[i] and flag:
#         count += 1
#         flag = False
#     elif a[i] == b[i]:
#         flag = True
#
# print(count)

# solution 2 - while loop
import sys
# sys.stdin = open('breedflip.in', 'r')
# sys.stdout = open('breedflip.out', 'w')

n = int(input())
a = list(input())
b = list(input())

count = 0

i = 0
l = 0

while i < n:
    if a[i] != b[i]:
        l += 1
    else:
        if l > 0:
            count += 1
        l = 0
    i += 1

if i == n and l > 0:
    count += 1

print(count)


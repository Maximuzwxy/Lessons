# USACO 2017 February Contest, Bronze
# Problem 1. Why Did the Cow Cross the Road
# https://usaco.org/index.php?page=viewproblem2&cpid=711

# solution 1 - list
# import sys
#
# sys.stdin = open('crossroad.in', 'r')
# sys.stdout = open('crossroad.out', 'w')
#
# lst = []
# n = int(input())
# for i in range(n):
#     lst.append(input().strip())
#
# def cross(nums):
#     count = 0
#     a = [-1] * 11
#     for line in nums:
#         index, side = list(map(int, line.split()))
#         if a[index] == -1:
#             a[index] = side
#         elif a[index] != side:
#             a[index] = side
#             count += 1
#     return count
#
# ret = cross(lst)
# print(ret)


# solution 2 - dict
import sys

sys.stdin = open('crossroad.in', 'r')
sys.stdout = open('crossroad.out', 'w')

lst = []
n = int(input())
for i in range(n):
    lst.append(input().strip())

def cross(nums):
    count = 0
    d = {}
    for line in nums:
        index, side = list(map(int, line.split()))
        if index not in d:
            d[index] = side
        elif d[index] != side:
            d[index] = side
            count += 1
    return count

ret = cross(lst)
print(ret)

# USACO 2017 February Contest, Bronze
# Problem 1. Why Did the Cow Cross the Road
# https://usaco.org/index.php?page=viewproblem2&cpid=711

# solution 1 - list
# def cross(nums):
#     count = 0
#     a = [-1] * 11
#     for line in nums:
#         index, side = list(map(int, line.split()))
#         # print(index, side)
#         if a[index] == -1:
#             a[index] = side
#         elif a[index] != side:
#             a[index] = side
#             count += 1
#
#     return count
#
# lst = []
# ret = 0
# try:
#     with open('crossroad.in', 'r') as f:
#         n = int(f.readline().strip())
#         for i in range(n):
#             lst.append(f.readline().strip())
# except FileNotFoundError:
#     n = int(input())
#     lst = []
#     for i in range(n):
#         lst.append(input().strip())
#
# ret = cross(lst)
# with open('crossroad.out', 'w') as f:
#     f.write(f'{ret}')
# print(ret)


# solution 2 - dict
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

lst = []
ret = 0

try:
    with open('crossroad.in', 'r') as f:
        n = int(f.readline().strip())
        for i in range(n):
            lst.append(f.readline().strip())

except FileNotFoundError:
    n = int(input())
    for i in range(n):
        lst.append(input().strip())

ret = cross(lst)

with open('crossroad.out', 'w') as f:
    f.write(f'{ret}')
print(ret)

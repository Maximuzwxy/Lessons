# input:
# 4
# 2 3
# 6 5
# 7 6
# 1 8

# combinations
# n = int(input())
# x = []
# y = []
# for i in range(n):
#     a, b = map(int, input().split())
#     x.append(a)
#     y.append(b)
#
# max_dis = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         dx = x[j] - x[i]
#         dy = y[j] - y[i]
#         dis = dx * dx + dy * dy
#         print(i, j, dis)
#         max_dis = max(max_dis, dis)
# print(max_dis)

# permutations
# Output all the permutations of the elements in the following list
# l = ['a', 'b', 'c']
# ret = []
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i == j or i == k or j == k:
#                 continue
#             ret.append([l[i], l[j], l[k]])
# for s in ret:
#     print(s)

# def perm(arr, n):
#     def dfs(l):
#         if len(l) == n:
#             res.append(l.copy())
#             return
#
#         for item in arr:
#             if item not in l:
#                 l.append(item)
#                 dfs(l)
#                 l.pop()
#
#     res = []
#     dfs([])
#
#     return res
#
# a = [i for i in range(3)]
# print(perm(a, 3))

# combinations
# def comb(arr, n):
#     def dfs(l, start):
#         if len(l) == n:
#             res.append(l.copy())
#             return
#
#         if start == len(arr) -n + 1:
#             return
#
#         for i in range(start, len(arr)):
#             l.append(arr[i])
#             dfs(l, i + 1)
#             l.pop()
#
#     res = []
#     dfs([], 0)
#
#     return res
#
# a = [i for i in range(5)]
# print(comb(a, 2))

# USACO 2016 February Contest, Bronze
# Problem 1. Milk Pails
# https://usaco.org/index.php?page=viewproblem2&cpid=615

# USACO 2016 US Open Contest, Bronze
# Problem 1. Diamond Collector
# https://usaco.org/index.php?page=viewproblem2&cpid=639







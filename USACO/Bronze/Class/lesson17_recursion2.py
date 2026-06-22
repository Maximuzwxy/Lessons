# n, m = map(int, input().split())
# total = 0
# while m >= n:
#     cnt = m // n
#     total += cnt
#     m = m % n + cnt * 0.5 * n
# print(int(total))

# n, m = map(int, input().split())
# total = m // n
# remain = m // n
#
# while remain >= n:
#     cur = remain // n
#     total += cur
#     remain = remain % 2 + cur
# print(total)

# n, m = map(int, input().split())
# total = m // n
# remain = m // n
#
# def f(r):
#     if r < n:
#         return 0
#     return f(r % n + r // n) + r // n
#
# total += f(remain)
# print(total)

# def f(n):
#     if n == 1:
#         return 0
#
#     ret = 0
#     for i in range(1, n // 2 + 1):
#         ret += f(i) + 1
#
#     return ret
# print(f(6))

# 欧几里得算法（辗转相除法）
# a = 240
# b = 160
#
# def f(n, m):
#     if m == 1 or n % m == 0:
#         return m
#     return f(m, n % m)
# print(f(b, a))

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


# a = [1, 2, 3, 4]
# res = []
# def per(s, k, n, l):
#     if k == n:
#         res.append(l)
#         return
#     else:
#         for c in s:
#             if c not in l:
#                 per(s, k + 1, n, l + [c])
#
# per(a, 0, 2, [])
# print(res)


a = [1, 2, 3, 4]
# a = [1, 2, 3]
res = []
def com(s, k, n, l):
    if len(l) == n:
        res.append(l)
        return
    else:
        for i in range(k, len(s)):
            k += 1
            com(s, k, n, l + [s[i]])

com(a, 0, 2, [])
print(res)


# USACO 2017 February Contest, Bronze
# Problem 2. Why Did the Cow Cross the Road II
# https://usaco.org/index.php?page=viewproblem2&cpid=712


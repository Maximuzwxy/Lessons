# USACO 2024 December Contest, Bronze
# Problem 1. Roundabout Rounding
# https://usaco.org/index.php?page=viewproblem2&cpid=1443

# solution 1 Partially passed
# def bessie(num, b):
#     # Bessie's rounding to 10^b
#     power = 10 ** b
#     remainder = num % power
#     if remainder >= power // 2:
#         num += (power - remainder)
#     else:
#         num -= remainder
#     return num
#
# def elsie(num, p):
#     # Elsie's chain rounding
#     for i in range(1, p + 1):
#         num = bessie(num, i)
#     return num
#
# def solve(n):
#     count = 0
#     p = 0
#     for x in range(2, n + 1):
#     # Find the smallest power of 10 >= x
#         while 10 **p < x:
#             p += 1
#         if bessie(x, p) != elsie(x, p):
#             count += 1
#     print(count)
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     solve(n)
#
# solution 2 All passed
# def alg(N):
#     digits = 0
#     while 10 ** digits < N:
#         digits += 1
#
#     answer = 0
#     for curdigits in range(1, digits + 1):
#         upper = int('5' + '0' * (curdigits - 1)) - 1
#         upper = min(N, upper)
#         lower = int('4' * curdigits)
#         answer += max(0, upper - lower)
#     return answer
#
# T = int(input().strip())
# for _ in range(T):
#     N = int(input().strip())
#     print(alg(N))
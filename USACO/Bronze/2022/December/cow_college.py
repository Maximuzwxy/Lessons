# USACO 2022 December Contest, Bronze
# Problem 1. Cow College
# https://usaco.org/index.php?page=viewproblem2&cpid=1251

# solution 1 timeout
# from collections import Counter
#
# n = int(input())
# cows = Counter(map(int, input().split()))
#
# max_t = tuition = 0
# cur = 0
#
# for k, v in cows.items():
#     cur = k
#     total = 0
#     for key, value in cows.items():
#         if key >= k:
#             total += k * value
#     if total > max_t:
#         max_t = total
#         tuition = k
#     elif total == max_t:
#         tuition = min(tuition, k)
#
# print(max_t, tuition)

# solution 2
# n = int(input())
# max_cow = 1000001
# cows = [0] * max_cow
# origin = list(map(int, input().split()))
#
# for i in origin:
#     cows[i] += 1
#
# max_t = tuition = 0
# past = 0
# for j in range(max_cow):
#     total = 0
#     if cows[j] != 0:
#         total = (n - past) * j
#         past += cows[j]
#
#     if total > max_t:
#         max_t = total
#         tuition = j
#     elif total == max_t:
#         tuition = min(tuition, j)
#
# print(max_t, tuition)

# solution 3
n = int(input())
cows = list(map(int, input().split()))
cows.sort()

max_pay = tuition = 0
for i in range(n):
    total = cows[i] * (n - i)
    if total > max_pay:
        max_pay = total
        tuition = cows[i]
print(max_pay, tuition)


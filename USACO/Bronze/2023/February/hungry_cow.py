# USACO 2023 February Contest, Bronze
# Problem 1. Hungry Cow
# https://usaco.org/index.php?page=viewproblem2&cpid=1299

# solution 1
n, t = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

l.append([t + 1, 0])

total = 0
last_d = 0
remain = 0

for d, b in l:
    total += b
    remain -= d - last_d
    last_d = d
    remain = max(remain, 0) + b
print(total - remain)

# solution 2
# n, t = map(int, input().split())
# # print(n, t)
#
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split())))
#
# days = 0
# count = 0
# start = 1
#
# for d, b in l:
#     if d > start:
#         days += d - start
#         if days >= t:
#             break
#         start = d
#
#     count += b
#     days += b
#     if days >= t:
#         count -= days - t
#         break
#     start += b
#
# print(count)



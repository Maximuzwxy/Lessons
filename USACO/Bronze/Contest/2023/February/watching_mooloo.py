n, k = map(int, input().split())
days = list(map(int, input().split()))

start = 0
spend = 0

for i in range(n - 1):
    if days[i + 1] - days[i] > k + 1:
        spend += days[i] - days[start] + 1 + k
        start = i + 1

spend += days[n - 1] - days[start] + 1 + k

print(spend)

# n, k = map(int, input().split())
# days = list(map(int, input().split()))
#
# start = cur = 0
# spend = 0
#
# while True:
#     cur += 1
#     if cur == n:
#         spend += days[cur - 1] - days[start] + 1 + k
#         start = cur
#         break
#     if days[cur] - days[start] <= k + 1:
#         continue
#     else:
#         spend += days[cur - 1] - days[start] + 1 + k
#         start = cur
#
# print(spend)


# USACO 2016 January Contest, Bronze
# Problem 2. Angry Cows
# https://usaco.org/index.php?page=viewproblem2&cpid=592

import sys
sys.stdin = open('angry.in', 'r')
sys.stdout = open('angry.out', 'w')

n = int(input())

line = []
for _ in range(n):
    line.append(int(input()))
line.sort()

max_v = 0
for i in range(n):
    cnt = 1
    radius = 1
    begin = i
    cur = begin - 1
    found = False
    while begin > 0 and cur >= 0:
        if line[begin] - line[cur] <= radius:
            cnt += 1
            found = True
            cur -= 1
        else:
            if found:
                begin = cur + 1
                radius += 1
                found = False
            else:
                break

    radius = 1
    begin = i
    cur = begin + 1
    found = False
    while begin < n - 1 and cur <= n - 1:
        if line[cur] - line[begin] <= radius:
            cnt += 1
            found = True
            cur += 1
        else:
            if found:
                begin = cur - 1
                radius += 1
                found = False
            else:
                break

    max_v = max(max_v, cnt)

print(max_v)


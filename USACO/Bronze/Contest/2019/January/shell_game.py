# USACO 2019 January Contest, Bronze
# Problem 1. Shell Game
# https://usaco.org/index.php?page=viewproblem2&cpid=891

# solution 1
import sys
sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

max_v = 0
for pebble in range(1, 4):
    arr = [0] * 4
    arr[pebble] = 1
    cnt = 0
    for a, b, g in lst:
        arr[a], arr[b] = arr[b], arr[a]
        if arr[g] == 1:
            cnt += 1
    max_v = max(max_v, cnt)
print(max_v)


# solution 2
import sys
sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

shells = [0, 1, 2, 3]
times = [0] * 4
for a, b, g in lst:
    shells[a], shells[b] = shells[b], shells[a]
    times[shells[g]] += 1

print(max(times))







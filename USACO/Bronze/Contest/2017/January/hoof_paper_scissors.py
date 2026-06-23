import sys
from itertools import permutations

sys.stdin = open('hps.in', 'r')
sys.stdout = open('hps.out', 'w')

n = int(input())
series = []

for i in range(n):
    series.append(input().split())

per = list(permutations('123', 3))

def judge(l, a, b):
    hoof, paper, scissors = l

    if a == hoof and b == scissors \
            or a == scissors and b == paper \
            or a == paper and b == hoof:
        return 1
    else:
        return 0

max_num = 0
for p in per:
    num = 0
    for x, y in series:
        num += judge(p, x, y)
    max_num = max(max_num, num)

print(max_num)

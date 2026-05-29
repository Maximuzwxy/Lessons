# USACO 2019 December Contest, Bronze
# Problem 1. Cow Gymnastics
# https://usaco.org/index.php?page=viewproblem2&cpid=963

# solution 1
import sys
from itertools import permutations
from itertools import combinations
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())
sessions = []
for _ in range(k):
    sessions.append(list(map(int, input().split())))

per = list(permutations([i for i in range(1, n + 1)], 2))
pairs = []
num = 0

for s in sessions:
    pairs.append(list(combinations(s, 2)))

for c in per:
    flag = True
    for p in pairs:
        if c not in p:
            flag = False
            break
    if flag:
        num += 1

print(num)

# solution 2
import sys
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')
from itertools import combinations

k, n = map(int, input().split())
sessions = []
for _ in range(k):
    sessions.append(list(map(int, input().split())))

pairs = []
num = 0

for s in sessions:
    pairs.append(list(combinations(s, 2)))

for c in pairs[0]:
    ret = True
    for p in pairs:
        if c not in p:
            ret = False
            break
    if ret:
        num += 1
print(num)


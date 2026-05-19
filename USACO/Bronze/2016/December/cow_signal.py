# USACO 2016 December Contest, Bronze
# Problem 3. The Cow-Signal
# https://usaco.org/index.php?page=viewproblem2&cpid=665

import sys

# sys.stdin = open('cowsignal.in', 'r')
# sys.stdout = open('cowsignal.out', 'w')

m, n, k = map(int, input().split())
origin = []
amplify = []
for i in range(m):
    origin.append(input())
print(origin)

for line in origin:
    s = ''
    for c in line:
        s += c * k
    for i in range(k):
        amplify.append(s)

for i in amplify:
    print(i)


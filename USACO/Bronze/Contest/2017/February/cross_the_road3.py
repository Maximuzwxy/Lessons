# USACO 2017 February Contest, Bronze
# Problem 3. Why Did the Cow Cross the Road III
# https://usaco.org/index.php?page=viewproblem2&cpid=713

import sys
sys.stdin = open('cowqueue.in', 'r')
sys.stdout = open('cowqueue.out', 'w')

n = int(input())
q = []

for i in range(n):
    q.append(list(map(int, input().split())))
q.sort()

end = 0

for arrive, question in q:
    if arrive > end:
        end = arrive + question
    else:
        end += question
print(end)



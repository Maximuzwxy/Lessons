import sys
from collections import Counter

sys.stdin = open('notlast.in', 'r')
sys.stdout = open('notlast.out', 'w')

d = {
    'Bessie': 0,
    'Elsie': 0,
    'Daisy': 0,
    'Gertie': 0,
    'Annabelle': 0,
    'Maggie': 0,
    'Henrietta': 0
}

l = []

n = int(input())
for i in range(n):
    name, amount = input().split()
    d[name] += int(amount)

for k, v in d.items():
    l.append(v)

min_v = min(l)
max_v = max(l)

c = Counter(l)

if min_v == max_v:
    print('Tie')
else:
    ll = sorted(list(set(l)))
    r = ll[1]
    if c[r] > 1:
        print('Tie')
    elif c[r] == 1:
        for k, v in d.items():
            if v == r:
                print(k)


import sys

sys.stdin = open('milkorder.in', 'r')
sys.stdout = open('milkorder.out', 'w')

n, m, k = map(int, input().split())
seq = list(map(int, input().split()))
order = [0] * (n + 1)
pos = []

for _ in range(k):
    c, p = map(int, input().split())
    order[p] = c

for o in order:
    if o != 0:
        pos.append(o)

# print(order)

if 1 in seq:
    cur_seq = 0
    for i in range(1, n + 1):
        if cur_seq == len(seq):
            break
        if order[i] == seq[cur_seq]:
            cur_seq += 1
        elif order[i] == 0:
            # Don't place a hierarchy cow that's already fixed elsewhere
            if seq[cur_seq] not in order:
                order[i] = seq[cur_seq]
                cur_seq += 1
    print(order.index(1))
else:
    cur_seq = 0
    seq.append(1)
    for i in range(1, n + 1):
        if cur_seq == len(seq):
            break
        if order[i] == seq[cur_seq]:
            cur_seq += 1
        elif order[i] == 0:
            # Don't place a hierarchy cow that's already fixed elsewhere
            if seq[cur_seq] in order:
                continue
            if i < n and cur_seq < len(seq) - 1 and order[i + 1] != seq[cur_seq + 1]:
                continue
            order[i] = seq[cur_seq]
            cur_seq += 1
    print(order[1:].index(0) + 1)
# print(order)
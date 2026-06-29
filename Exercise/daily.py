import sys

sys.stdin = open('milkorder.in', 'r')
sys.stdout = open('milkorder.out', 'w')

n, m, k = map(int, input().split())
seq = list(map(int, input().split()))
order = [0] * (n + 1)

for _ in range(k):
    c, p = map(int, input().split())
    order[p] = c

def check_seq(o):
    print(o)
    for a in range(len(seq) - 1):
        # print(o.index(seq[a]), o.index(seq[a + 1]))
        if o.count(seq[a]) > 1:
            return False

        if seq[a] in o and seq[a + 1] in o:
            if o.index(seq[a]) > o.index(seq[a + 1]):
                return False

    return True

def check(o):
    cur = 1
    for x in range(len(seq)):
        for y in range(cur, n + 1):
            print(x, y, seq, o)
            if o[y] == 0:
                if seq[x] in o:
                    continue

                o[y] = seq[x]

                if not check_seq(o):
                    return False
                # cur += 1
                break
            if o[y] == seq[x]:
                # cur += 1
                break

    return True

for i in range(1, n + 1):
    if order[i] == 0:
        oo = order.copy()
        oo[i] = 1

        if not check_seq(oo):
            continue

        if check(oo):
            print(oo)
            print(oo.index(1))
            break




import sys

sys.stdin = open('family.in', 'r')
sys.stdout = open('family.out', 'w')

n, a, b = input().split()
n = int(n)

d = {}

for i in range(n):
    m, c = input().split()
    if c not in d and m not in d:
        node_c = [0, m, []]
        node_m = [0, '', [c]]
        d[c] = node_c
        d[m] = node_m
    elif c not in d and m in d:
        node_c = [0, m, []]
        d[m][2].append(c)
        d[c] = node_c
    elif c in d and m not in d:
        node_m = [0, '', [c]]
        d[c][1] = m
        d[m] = node_m
    else:
        d[c][1] = m
        d[m][2].append(c)

def dfs(node, g, r):
    node[0] = g
    node.append(r)

    if not node[2]:
        return

    for children in node[2]:
        dfs(d[children], g + 1, r)

roots = []
for k, v in d.items():
    if v[1] == '':
        roots.append(k)
        dfs(v, 1, k)

# for k, v in d.items():
#     print(k, v)

def is_mother(x, y, diff):
    mom = d[y][1]
    for _ in range(diff - 1):
        mom = d[mom][1]

    return True if mom == x else False

def is_aunt(x, y, diff):
    mom = d[y][1]
    for _ in range(diff):
        mom = d[mom][1]

    return True if mom == d[x][1] else False

def my_print():
    if d[a][0] < d[b][0]:
        old = a
        young = b
    else:
        old = b
        young = a

    diff = d[young][0] - d[old][0]
    if is_mother(old, young, d[young][0] - d[old][0]):
        title = 'mother'
        if diff == 1:
            pre = ''
        elif diff == 2:
            pre = 'grand-'
        else:
            pre = 'great-' * (diff - 2) + 'grand-'

        print(f'{old} is the {pre+title} of {young}')
    elif is_aunt(old, young, d[young][0] - d[old][0]):
        title = 'aunt'
        if diff == 1:
            pre = ''
        else:
            pre = 'great-' * (diff - 1)
        print(f'{old} is the {pre+title} of {young}')
    else:
        print('COUSINS')

if d[a][3] != d[b][3]:
    print('NOT RELATED')
else:
    if d[a][1] == d[b][1]:
        print('SIBLINGS')
    else:
        my_print()




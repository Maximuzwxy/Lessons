import sys
# sys.stdin = open('bcs.in', 'r')
# sys.stdout = open('bcs.out', 'w')

n, k = map(int, input().split())

origin = []
pieces = []
cnt = 0

for i in range(n):
    s = input()
    cnt += s.count('#')
    origin.append(list(s))

for j in range(k):
    p = []
    for m in range(n):
        p.append(list(input()))
    pieces.append(p)

def get_num(piece):
    ret = 0
    for l in piece:
        ret += l.count('#')
    return ret

def move_figurine(fig):
    fs = [fig]
    count = get_num(fig)

    def left_up(f):
        # left
        l = [['.'] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                l[i][j] = f[i][j + 1]
        if get_num(l) == count:
            fs.append(l)
            left_up(l)

        # up
        l = [['.'] * n for _ in range(n)]
        for i in range(n - 1):
            for j in range(n):
                l[i][j] = f[i + 1][j]
        if get_num(l) == count:
            if l not in fs:
                fs.append(l)
                left_up(l)


    def right_down(f):
        # right
        l = [['.'] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                l[i][j + 1] = f[i][j]

        if get_num(l) == count:
            if l not in fs:
                fs.append(l)
                right_down(l)

        # down
        l = [['.'] * n for _ in range(n)]
        for i in range(n - 1):
            for j in range(n):
                l[i + 1][j] = f[i][j]
        if get_num(l) == count:
            if l not in fs:
                fs.append(l)
                right_down(l)

    left_up(fig)
    right_down(fig)

    return fs


def check(p1, p2):
    l1 = move_figurine(p1)
    l2 = move_figurine(p2)

    for f1 in l1:
        for f2 in l2:
            f = [['.'] * n for _ in range(n)]
            # for _ in f1:
            #     print(_)
            # for _ in f2:
            #     print(_)
            # print()
            for i in range(n):
                for j in range(n):
                    if f1[i][j] == f2[i][j] == '#':
                        break
                    elif f1[i][j] == '#':
                        f[i][j] = '#'
                    elif f2[i][j] == '#':
                        f[i][j] = '#'
            if f == origin:
                return True
    return False

a = b = 0
for x in range(k - 1):
    for y in range(x + 1, k):
        piece1 = pieces[x]
        piece2 = pieces[y]
        if get_num(piece1) + get_num(piece2) == cnt:
            print(x, y)
            if check(piece1, piece2):
                a = x + 1
                b = y + 1
                break
print(a, b)
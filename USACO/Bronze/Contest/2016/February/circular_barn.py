import sys
sys.stdin = open('cbarn.in', 'r')
sys.stdout = open('cbarn.out', 'w')

n = int(input())

circle = []
min_dis = 0

def get_distance(l):
    dis = 0
    for j in range(n - 1):
        dis += l[j] * (j + 1)
    return dis

for i in range(n):
    circle.append(int(input()))

for i in range(n):
    tmp_circle = circle[i + 1:] + circle[:i]
    if min_dis == 0:
        min_dis = get_distance(tmp_circle)
    else:
        min_dis = min(get_distance(tmp_circle), min_dis)
    # print(tmp_circle)

print(min_dis)


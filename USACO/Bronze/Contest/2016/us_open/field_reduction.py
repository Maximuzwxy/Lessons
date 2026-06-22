import sys

sys.stdin = open('reduce.in', 'r')
sys.stdout = open('reduce.out', 'w')

n = int(input())
cows = []
s_x = set()
s_y = set()
l_x = [0] * 40001
l_y = [0] * 40001

for i in range(n):
    # cows.append(list(map(int, input().split())))
    x, y = map(int, input().split())
    cows.append([x, y])
    s_x.add(x)
    s_y.add(y)
    l_x[x] += 1
    l_y[y] += 1

cows_x = list(s_x)
cows_x.sort()
cows_y = list(s_y)
cows_y.sort()

min_area = 40000 * 40000
if [cows_x[0], cows_y[0]] in cows:
    min_area = min(min_area, (cows_x[-1] - cows_x[1]) * (cows_y[-1] - cows_y[1]))
elif [cows_x[0], cows_y[-1]] in cows:
    min_area = min(min_area, (cows_x[-1] - cows_x[1]) * (cows_y[-2] - cows_y[0]))
else:
    if l_x[cows_x[0]] > 1:
        min_area = min(min_area, (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area, (cows_x[-1] - cows_x[1]) * (cows_y[-1] - cows_y[0]))

    if l_y[cows_y[0]] > 1:
        min_area = min(min_area, (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area, (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[1]))

if [cows_x[-1], cows_y[-1]] in cows:
    min_area = min(min_area, (cows_x[-2] - cows_x[0]) * (cows_y[-2] - cows_y[0]))
elif [cows_x[-1], cows_y[0]] in cows:
    min_area = min(min_area, (cows_x[-2] - cows_x[0]) * (cows_y[-1] - cows_y[1]))
else:
    if l_x[cows_x[-1]] > 1:
        min_area = min(min_area, (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area, (cows_x[-2] - cows_x[0]) * (cows_y[-1] - cows_y[0]))

    if l_y[cows_y[-1]] > 1:
        min_area = min(min_area, (cows_x[-1] - cows_x[0]) * (cows_y[-1] - cows_y[0]))
    else:
        min_area = min(min_area, (cows_x[-1] - cows_x[0]) * (cows_y[-2] - cows_y[0]))

print(min_area)


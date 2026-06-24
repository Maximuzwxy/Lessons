import sys

sys.stdin = open('lostcow.in', 'r')
sys.stdout = open('lostcow.out', 'w')

x, y = map(int, input().split())

flag = True
distance = 0
times = 0
offset = 0
cur_pos = x

while True:
    if flag:
        offset = 2 ** times
    else:
        offset = - 2 ** times

    next_pos = x + offset

    if x < y:
        if next_pos < y:
            distance += abs(cur_pos - next_pos)
            flag = not flag
            cur_pos = next_pos
            times += 1
        else:
            distance += abs(y - cur_pos)
            break
    else:
        if next_pos > y:
            distance += abs(cur_pos - next_pos)
            flag = not flag
            cur_pos = next_pos
            times += 1
        else:
            distance += abs(y - cur_pos)
            break

print(distance)

import sys

sys.stdin = open('square.in', 'r')
sys.stdout = open('square.out', 'w')

f_x1, f_y1, f_x2, f_y2 = map(int, input().split())
s_x1, s_y1, s_x2, s_y2 = map(int, input().split())

x1 = min(f_x1, f_x2, s_x1, s_x2)
x2 = max(f_x1, f_x2, s_x1, s_x2)

y1 = min(f_y1, f_y2, s_y1, s_y2)
y2 = max(f_y1, f_y2, s_y1, s_y2)

side = max((x2 - x1), (y2 - y1))
print(side ** 2)


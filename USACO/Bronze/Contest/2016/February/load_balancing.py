import sys
sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')

n, b = map(int, input().split())

locations_x = []
locations_y = []
locations = []

for i in range(n):
    px, py = map(int, input().split())
    locations_x.append(px)
    locations_y.append(py)
    locations.append([px, py])

locations_x.sort()
locations_y.sort()

def get_max_num(cross_x, cross_y):
    left_top = 0
    left_bottom = 0
    right_top = 0
    right_bottom = 0

    for x, y in locations:
        if x < cross_x and y > cross_y:
            left_top += 1
        elif x < cross_x and y < cross_y:
            left_bottom += 1
        elif x > cross_x and y > cross_y:
            right_top += 1
        elif x > cross_x and y < cross_y:
            right_bottom += 1

    return max(left_top, left_bottom, right_top, right_bottom)

smallest = 101

for pos_x in locations_x:
    for pos_y in locations_y:
        smallest = min(smallest, get_max_num(pos_x + 1, pos_y + 1))

print(smallest)

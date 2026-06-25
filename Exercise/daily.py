import sys
sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

xl1 = min(x1, x3)
xl2 = min(x2, x4)
yl1 = y1 if xl1 == x1 else y2
yl2 = y2 if xl2 == x2 else y1

xr1 = max(x1, x3)
xr2 = max(x2, x4)
yr1 = y3 if xr1 == x3 else y4
yr2 = y4 if xr2 == x4 else y3

# print(xl1, yl1, xl2, yl2)
# print(xr1, yr1, xr2, yr2)

ls_x = set(range(xl1, xl2 + 1))
ls_y = set(range(yl1, yl2 + 1))
rs_x = set(range(xr1, xr2 + 1))
rs_y = set(range(yr1, yr2 + 1))
ts_x = set(range(x5, x6 + 1))
ts_y = set(range(y5, y6 + 1))

ls_c_x = sorted(list(ls_x & ts_x))
ls_c_y = sorted(list(ls_y & ts_y))
rs_c_x = sorted(list(rs_x & ts_x))
rs_c_y = sorted(list(rs_y & ts_y))
# print(ls_c_x, ls_c_y, rs_c_x, rs_c_y)

covered_area = 0

if len(ls_c_x) != 0 and len(ls_c_y) != 0:
    covered_area += (ls_c_x[-1] - ls_c_x[0]) * (ls_c_y[-1] - ls_c_y[0])

if len(rs_c_x) != 0 and len(rs_c_y) != 0:
    covered_area += (rs_c_x[-1] - rs_c_x[0]) * (rs_c_y[-1] - rs_c_y[0])

area = (x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3) - covered_area
print(area)






# def covered(x, y, xx1, yy1, xx2, yy2):
#     if xx1 < x < xx2 and yy1 < y < yy2:
#         return True
#     return False
#
# corners = [1 if covered(x5, y5, xl1, yl1, xl2, yl2) else 0,
#            1 if covered(x5, y6, xl1, yl1, xl2, yl2) else 0,
#            1 if covered(x6, y6, xr1, yr1, xr2, yr2) else 0,
#            1 if covered(x6, y5, xr1, yr1, xr2, yr2) else 0]
#
# print(corners)
#
# covered_area = 0
# if corners[0] == 1 and corners[1] == 0:
#     covered_area += (xl2 - x5) * (yl2 - y5)
# elif corners[0] == 0 and corners[1] == 1:
#     covered_area += (xl2 - x5) * (y6 - yl1)
# elif corners[1] == 1 and corners[1] == 1:
#     covered_area += (xl2 - x5) * (y6 - y5)
#
# if corners[2] == 1 and corners[3] == 0:
#     covered_area += (x6 - xr1) * (y6 - yr1)
# elif corners[2] == 0 and corners[3] == 1:
#     covered_area += (x6 - xr1) * (yr2 - y5)
# elif corners[1] == 1 and corners[1] == 1:
#     covered_area += (x6 - xr1) * (y6 - y5)
# # print(covered_area)
#
# print((x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3) - covered_area)

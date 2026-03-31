def double(lst):
    for i in range(len(lst)):
        lst[i] *= 2
    return lst

# l = [i for i in range(5)]
# print(double(l))

def reverse(lst):
    new_lst = []
    for i in range(-1, -len(lst) - 1, -1):
        new_lst.append(lst[i])
    return new_lst

# l = [i for i in range(5)]
# print(reverse(l))

# def change_type(lst):
#     for i in range(len(lst)):
#         lst[i] = int(lst[i])
#
# def get_time(h1, m1, h2, m2):
#     t1 = h1 * 60 + m1
#     t2 = h2 * 60 + m2
#
#     t = t2 - t1
#     print(t // 60, t % 60)
#
# times = input('time: ').split()
# change_type(times)
# print(times)
#
# get_time(times[0], times[1], times[2], times[3])

def get_time(h1, m1, h2, m2):
    h, m = 0, 0
    if m2 < m1:
        m = m2 - m1 + 60
        h = -1
    else:
        m = m2 - m1
    h += h2 - h1

    print(h, m)

a, b, c, d = map(int, input('time: ').split())
get_time(a, b, c, d)



































# creature = ('cat', 'dog', 'tiger', 'human')
# print(creature)
#
# color = (0x001100, 'blue', creature)
# print(color)

# tup = (1)
# print(tup, type(tup))

# t = 1,
# print(t, type(t))
#
# t = (1, 2)
# # print(t, type(t))
# t[0] = 3

# l = [1, 2, 3]
# t = tuple(l)
# print(t)
# l1 = list(t)
# print(l1)



# l = [1, 2, 3, 4, 5]
# l[0] = 9
# print(l)
#
# t = (1, 2, 3, 4, 5)
# t[0] = 9
# print(t)

# t = (1, 2, 3, 4, 5)
# print(t[1])

# t = (1, 2, 3, 4, 5, 6, 7)
# print(t[1: 5: 2])
# print(t[5: 1: -2])
# print(t + t)

#
# if 1 in t:
#     print(True)
# else:
#     print(False)

# def ret_tuple():
#     a = 1
#     b = 2
#     return a, b
#
# c = ret_tuple()
# print(c, type(c))

# l = ['a', 'b', 'c']
# for i in enumerate(l):
#     print(i, type(i))

import random
# l = [random.randint(1, 9) for i in range(7)]
# t = tuple(l)
# print(t)
# t = ()
# for i in range(7):
#     t += (random.randint(1, 9), )
# print(t)

tup = (2, 8, 7, 11, 14, 6, 7, 5, 3)
t = tup[2: 7]
total = 0
total += sum(t)
print(total)

max_v = max(tup)
min_v = min(tup)

if tup.index(max_v) < 2 or tup.index(max_v) > 6:
    total += max_v

if tup.index(min_v) < 2 or tup.index(min_v) > 6:
    total += min_v

print(total)







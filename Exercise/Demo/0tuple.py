# creature = ('cat', 'dog', 'tiger', 'human')
# print(creature, type(creature))
#
# colors = (0x001100, 'blue', creature)
# print(colors)
#
# tup = (1)
# print(type(tup))
#
# tup = 1,
# print(type(tup))
#
# tup = (1, )
# print(type(tup))
# print(tup[0])
# tup[0] = 2

# t = (1, 2, 3)
# print(t[2])

import random

# tup = tuple(i + 1 for i in range(7))
# print(tup)
#
# print(tup[::2])
# print(tup[1:6:2])
# print(tup[7:1:-2])
#
# if 2 in tup:
#     print('yes')
#
# lst = [i for i in range(5)]
# if 1 in lst:
#     print('yes')
# print(min(lst))
# print(max(lst))
#
# lst.append('a')
# print(lst)

# 类型不同会报错
# print(min(lst))
# print(max(lst))

# lst = ['a', '0b11', 'c']
# print(max(lst))
# print(min(lst))

# lst = [1, 2, 3, 4, 5, 6, 7, 2]
# print(lst.index(2))
# print(lst.count(2))
# print(lst.index(2, 2, 9))

# lst = [random.randint(1, 9) for _ in range(7)]
# print(lst)
#
# tup = tuple(lst)
# print(tup)

# lst = [1, 3, 4, 0, 0, 6, 0, 5, 4, 6, 7, 0, 5]
# # 这样对么？
# for i in lst:
#     if i == 0:
#         lst.remove(0)
# print(lst)
#
# while 0 in lst:
#     lst.remove(0)
#     # lst.pop(lst.index(0))
# print(lst)

# lst1 = [1, 4, 2, 3, 2, 4]
# lst2 = [1, 3, 2, 3, 5]
# lst1 += lst2
# lst3 = []
# for i in lst1:
#     if i not in lst3:
#         lst3.append(i)
# print(lst3)

# lst = [random.randint(0, 9) for _ in range(10)]
# print(lst)
# ans = []
# for i in lst:
#     if i % 2 == 0:
#         ans.insert(0, i)
#     else:
#         ans.append(i)
# print(ans)

# lst = [random.randint(50, 100) for _ in range(10)]
# print(lst)
# total = 0
# for i in lst:
#     total += i
# print(total)
#
# for j in range(len(lst)):
#     lst[j] *= 2
# print(lst)

# lst1 = [random.randint(0, 9) for _ in range(10)]
# lst2 = [random.randint(0, 9) for _ in range(10)]
# print(lst1)
# print(lst2)
# ans = []
#
# for i in lst1:
#     if i in lst2 and i not in ans:
#         ans.append(i)
# print(ans)





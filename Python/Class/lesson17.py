# t = (1, 2, 3)
# print(t)
# t1 = ('a', 'b', t)
# print(t1)
#
# a = (1)
# print(a, type(a))
#
# b = (1, )
# print(b, type(b))
#
# c = 1, 2
# print(c, type(c))
#
# d = 1,
# print(d, type(d))

# t = (i for i in range(5))
# t = tuple(i for i in range(10))
# print(t, type(t))
#
# print(t[1])
#
# print(t[1:5:2])
# print(t[5:1:-2])
#
# if 10 in t:
#     print(True)
# else:
#     print(False)
#
# print(t * 2)

# lst = ['a', 'b', 'c']
# for i in enumerate(lst):
#     print(i)
#
# for key, value in enumerate(lst):
#     print(key, value)
#
# for i in enumerate(lst):
#     print(i[0], i[1])

# import random
# lst = [random.randint(1, 9) for i in range(7)]
# t = tuple(lst)
# print(t)

# lst = [1, 3, 4, 0, 0, 6, 0, 5, 4, 6, 7, 0, 5]
# while 0 in lst:
#     lst.remove(0)
# print(lst)

# i = 0
# while i < len(lst):
#     if lst[i] == 0:
#         lst.pop(i)
#     else:
#         i += 1
# print(lst)

# lst1 = [1, 4, 2, 3, 2, 4]
# lst2 = [1, 3, 2, 3, 5]
# lst = []
#
# lst1 += lst2
# for i in lst1:
#     if i not in lst:
#         lst.append(i)
# print(lst)

############

tup = (2, 8, 7, 11, 14, 6, 7, 5, 3)

total = sum(tup[2:7])
print(total)

min_v = min(tup)
max_v = max(tup)

if tup.index(min_v) < 2 or tup.index(min_v) > 6:
    total += min_v

if tup.index(max_v) < 2 or tup.index(max_v) > 6:
    total += max_v

print(total)

############

# lst1 = [1,11,5,7,8,3,6]
# lst2 = [2,7,6, 8, 11,10, 9]
# lst = []
#
# for i in lst1:
#     if i in lst2:
#        lst.append(i)
# print(lst)

# Homework
# 第一题：
# 合并2个列表，并且去掉其中重复的元素
# lst1 = [1, 4, 2, 3, 2, 4]
# lst2 = [1, 3, 2, 3, 5]
# 输出：[1, 4, 2, 3, 5]
#
# 第二题：
# 现在有如下的一个只有整数元素的元组:
# tup =(2, 8, 7, 11, 14, 6, 7, 5, 3)
# 要求累加以下各部分的和:
# (1) index为2到index为6元素
# (2) 元组最大值和最小值
# 如果元组最大值和最小值的index在2到6之间则不需要重复累加
# 输出：47
#
# Note:
# 题中，元组中最大的值是14，index是在2~6之间的，因此不重复累加
# 可使用 max、min、index 等函数
#
# 第三题：
# 有两个列表，每个列表元素各不相同，找出两个列表中相同的元素,并保存在新列表lst中。
# Ist1=[1,11,5,7,8,3,6]
# Ist2=[2,7,6, 8, 11,10, 9]
#
# 输出:
# [7,6,8,11]















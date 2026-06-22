import random

# s = {1, 2, 3, 4, 5, 6, 6}
# print(s)
# print(type(s))
#
# a = set()
# b = {}
# print(type(a), type(b))

# tup = 1, 2, 3
# tup1 = (1, 2, 3)
# print(tup, tup1)
# print(tup)
# tup = 'apple', 'banana', 'cherry'
# print(tup)
# # 反复执行，会发现set是无序的
# s1 = set(tup)
# print(s1)
#
# s2 = {'apple'}
# print(type(s2))
# print(s2)
# 无序
# s3 = set('apple')
# print(s3)
#
# 这个顺序是0~9，因为构建的时候的顺序是0~9，
# s4 = set(i for i in range(10))
# print(s4)
#
# # 以下也是有序的，因为是数字
# lst = [i for i in range(10)]
# print(set(lst))
#
# # 以下是无序的，因为是字符串
# lst = [str(i) for i in range(10)]
# print(set(lst))

# 集合（set）里的元素必须是可哈希的（hashable），也就是内容不能变，比如数字、字符串、元组等。
# 如果你把可变类型（比如列表）放进集合，会报错，因为列表内容可以变，不可哈希。
# 元组可以，但是元组内也不能有可变类型，如list
# s1 = {1, 'a', (2, 'b')}
# 声明的时候会报错
# s2 = {1, [2, 3]}
# print(s1)
# print(s2)

# tup = (2, 'b', [1, 2])
# print(tup)
# s3 = {1, 'a', tup}
# print(s3)

# # 遍历
# s = {1, 2, 3, 1}
# print(s, len(s))
# for i in s:
#     print(i)

# # 下面的不对
# a = set(1, 2, 3)
# # list也不可以
# lst = list(1, 2, 3)
# # tuple也不可以
# a = tuple(1, 2, 3)







# 构造集合
# s = {'a', 'b', 'c'}
# print(s)
# s = set('abc')
# print(s)

# t = ('a', 'b', 'c')
# s = set(t)
# print(s)

# l = ['a', 'b', 'c']
# s = set(l)
# print(s)

# 无序，不可索引，不能重复，元素不可变，如列表不行

# 遍历集合
# s = {1, 2, 3, 1}
# print(s, len(s))
# for i in s:
#     print(i)
# 如何判断一个元素是否在集合内
# if 1 in s:
#     print('yes')

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}

# s1增加4,然后把s1打印出来
# 把s2所有元素放到s1里面,并打印








# s1.add(4)
# print(s1)
# s1.update(s2)
# print(s1)
#
# if 1 in s1:
#     s1.remove(1)
# # s1.remove(9) # 报错
# s1.discard(9) # discard不会
# print(s1)
#
# a = s1.pop() # 由于set无序的，所以pop是随机的一个被pop了（数字除外）,list是pop哪个?
# print(a)
# print(s1)
# map也可以，可迭代对象
# s2 = set(map(str, s1))
# print(s2)
# print(s2.pop())
#
# s2.clear()
# print(s2)

# 1. 使用for循环，生成一个列表lst1，包含10个元素，每个元素是一个1~10的随机数
# 2. 使用map()函数把列表中的整数都替换成字符串,生成一个新的列表lst2,打印出来
# 3. 把lst2的元素join()成一个字符串，以空格间隔，在一行打印出来
# 4. 通过set()的特性把lst2去重,生成一个集合s,并打印去重后的集合s
# 5. 然后用sorted对s排序,生成一个新的列表lst3,打印出来
# 6. 然后把lst3的元素join()成一个字符串，以空格间隔，在一行打印出来

# 逐步完成
# lst1 = []
# for _ in range(10):
#     a = random.randint(1, 9)
#     lst1.append(a)
# print(lst1)
#
# lst2 = list(map(str, lst1))
# print(lst2)
# print(' '.join(lst2))
#
# s = set(lst2)
# print(s)
# lst3 = sorted(s)
# print(lst3)
#
# print(' '.join(lst3))
#
# # 简洁方法
# lst = [random.randint(1, 10) for i in range(10)]
# print(len(lst))
# print(' '.join(map(str, lst)))
# s = sorted(set(lst))
# print(len(s))
# print(' '.join(map(str, s)))

# n = int(input())
# s = set()
#
# for _ in range(n):
#     a = tuple(sorted(input()))
#     # a = ''.join(sorted(input()))
#     print(a)
#     s.add(a)
# print(len(s))







# set1 = {random.randint(1, 10) for _ in range(10)}
# set2 = {random.randint(1, 10) for _ in range(10)}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# print(set1)
# print(set2)
#
# 并集
# set3 = set1 | set2
# print('union')
# print(set3)
# print(set1.union(set2))
# print(set2.union(set1))
#
# 交集
# set4 = set1 & set2
# print('intersection')
# print(set4)
# print(set1.intersection(set2))
# print(set2.intersection(set1))
#
# 差集
# print('difference')
# print(set1 - set2)
# print(set1.difference(set2))
# print(set2 - set1)
# print(set2.difference(set1))
#
# 补集
# print('symmetric_difference')
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# print(set2.symmetric_difference(set1))

# A = {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# B = {1, 2, 3, 4, 6, 8, 12, 16, 24, 48}
# # 1. 并集
# print('union')
# print(A.union(B))  # 或 print(A | B)
# print(A | B)
# print()
#
# # 2. 差集（A中有但B中没有的）
# print('difference')
# print(A.difference(B))  # 或 print(A - B)
# print(A - B)
# print()
#
# # 3. 交集
# print('intersection')
# print(A.intersection(B))  # 或 print(A & B)
# print(A & B)
# print()
#
# # 4. 对称差集
# print(A.symmetric_difference(B))  # 或 print(A ^ B)
# print('symmetric_difference')
# print(A ^ B)
# print()

# isdisjoint
# print(set1.isdisjoint(set2))
# print({1, 2} < set1)
# print({1, 2} <= set1)

def union(a, b):
    ret = set(a)
    for e in b:
        ret.add(e)
    print(ret)
    return ret

def deference(a, b):
    ret = set()
    for e in a:
        if e not in b:
            ret.add(e)
    print(ret)
    return ret

def intersection(a, b):
    ret = set()
    for e in a:
        if e in b:
            ret.add(e)
    print(ret)
    return ret







def symmetric_difference(a, b):
    ret = set()
    for e in a:
        if e not in b:
            ret.add(e)
    for e in b:
        if e not in a:
            ret.add(e)
    print(ret)
    return ret

# union(set1, set2)
# deference(set1, set2)
# intersection(set1, set2)
# symmetric_difference(set1, set2)

# 使用集合的特性，找出列表中重复出现的数字
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# s = set()
# lst = list()
# for e in nums:
#     if e not in s:
#         s.add(e)
#     else:
#         lst.append(e)
# print(lst)

# nums = [4, 3, 2, 7, 8, 2, 3, 1]
# s = set()
# lst = list()
# for e in nums:
#     if e in s:
#         lst.append(e)
#     else:
#         s.add(e)
# print(lst)


# 使用set的特性，在字符串中，找到第一个重复出现的字母
# str1 = 'abccbaacz'
# s1 = set()
# for e in str1:
#     if e in s1:
#         print(e)
#         break
#     s1.add(e)


# map
# l = [1, 2, 3]
#
# def my_map(func, lst):
#     ret = []
#     for i in lst:
#         ret.append(func(i))
#     return ret
# print(my_map(str, l))
#
# def square(a):
#     return a**2
# print(my_map(square, l))

# join
# l = ['a', 'b', 'c']
# s = 'abc'
# t = ('a', 'b', 'c')
# set3 = {'a', 'b', 'c'}
#
# # print(' '.join(set1))
# # 这里可以用for in range么？
# def my_join(sep, sequence):
#     ret = ''
#     index = 0 # index
#     for item in sequence:
#         ret += item
#         if index != len(sequence) - 1:
#             ret += sep
#         index += 1
#     return ret
#
# def my_join2(sep, sequence):
#     ret = ''
#     for i, item in enumerate(sequence):
#         ret += item
#         if i != len(sequence) - 1:
#             ret += sep
#     return ret
#
#
# print(my_join('', l))
# print(my_join('-', s))
# print(my_join2('_', t))


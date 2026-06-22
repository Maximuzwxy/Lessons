# d = {1:1, 2:2, 3:3, '4':4}
# # print(d)
#
# car = {'brand': 'Tesla',
#        'model': 'Y',
#        'year': 2019,}
# # print(car)
#
# keys = ['brand', 'model', 'year']
# values = ['Tesla', 'Y', 2019]
# car2 = dict(zip(keys, values))
# print(car2)
#
# print(d[1])
# # print(d[4])
# print(d['4'])

# car = {'brand': 'Tesla',
#        'model': 'Y',
#        'year': 2019,
#        'colors': ['red', 'white', 'blue']}

# for i in car:
#     print(i)
#
# for i in car:
#     print(car[i])

# print(car)
# print(car['brand'])
# print(len(car))
# print(car.get('year'))
# print(car.get('price'))
# print(car.get('price', 50))
# print(car)
# print(car['brand': 'year'])
#
# car['year'] = 2020
# print(car)
#
# car.update({'model': 'X'})
# print(car)
#
# car['name'] = 'aaa'
# print(car)
#
# car.pop('name')
# print(car)
#
# car.popitem()
# print(car)
#
# del car['year']
# print(car)
#
#
#
# if 'model' in car:
#     print('yes')


# a = dict(foo=1, bar=2)
# print(a)
#
# b = {(3 + 2j):1}
# print(b)

# 第一题
# n = int(input('n: '))
# dic = {}
# for i in range(1, n + 1):
#     dic[i] = i ** 2
# print(dic)
#
# for i in range(1, n + 1):
#     dic.update({i: i ** 2})
# print(dic)
#
# dic = {i: i ** 2 for i in range(1, n + 1)}
# print(dic)

# 第二题
# for i in s:
#     dic[i] = dic.get(i, 0) + 1
# print(dic)

# dic = {}
# for i in range(1, 11):
#     dic[i] = 2 ** i
# print(dic)
#
# for i in dic:
#     dic[i] = str(dic[i])
# print(dic)
#
# for i in range(2, 11, 2):
#     dic.pop(i)
# print(dic)

# 第三题
# s = 'aabcdaabcdaabcdxyz'
# dic = {}
# for i in s:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# print(dic)

# from collections import Counter
# c = Counter(s)
# print(dict(c))
# from collections import defaultdict
# d = defaultdict(int)
# d = defaultdict(lambda: 0)
# for i in s:
#     d[i] += 1
# print(d)

# 第四题
# lst = [0, 1]
# for i in range(2, 10):
#     lst.append(lst[i - 1] + lst[i - 2])
# print(lst)

# dic = {1: 0, 2: 1}
# for i in range(3, 11):
#     dic[i] = dic[i - 1] + dic[i - 2]
# print(dic)







# car = {'brand': 'Tesla',
#        'model': 'Y',
#        'year': 2019,
#        'colors': ['red', 'white', 'blue']}

# car2 = {}
# car2.update(car)
# print(car2)
# for k, v in car.items():
#     car2.update({k: v})
# print(car2)

# car2 = dict(car.items())
# print(car.items())
# print(car2)

# print(car.keys())
# car['price'] = 50
# print(car.keys())

# for i in car.keys():
#     print(i)

# print(car.values())
# car['price'] = 100
#
# for i in car.values():
#     print(i)

# print(car.items())
# car['price'] = 200
# for i,j in car.items():
#     print(i, j)

# car2 = car
# print(car2)
# car['price'] = 200
# print(car2)
# car2 = car.copy()
# print(car2)
# car['price'] = 100
# print(car)
# print(car2)

# 构造dict
# print(dict.fromkeys(['colors', 'price'], 1))

# d = {}
# d.setdefault('x', 1)
# print(d)
# d.setdefault('x', 2)
# print(d)


from collections import Counter
# a = Counter('abbccc')
# print(a)
# print(a['c'])
# print(a['d'])

# a = Counter(list('abbccc'))
# print(a)
# print(a['c'])
# print(a['d'])

from collections import defaultdict
# get a missing one will add this key into dic
# a = 'abbccc'
# b = defaultdict(int)
# print(b)
# for i in a:
#     b[i] += 1
# print(b)
# b['a'] = 'a'
# print(b)

# dic = defaultdict(list)
# dic['a'] = 1
# print(dic)
#
# print(dic['b'])
# print(dic)
# dic['c'].append(10)
# print(dic)


# 第五题
# s = 'abaccdeff'
# s = 'xxyyzz'
# s = ''
# c = Counter(s)
# for i in s:
#     if c[i] == 1:
#         print(i)
#         break
# else:
#     print('no')

# ret = 'no'
# c = Counter(s)
# for i in s:
#     if c[i] == 1:
#         print(i)
#         ret = i
#         break
# print(ret)

# dic = {}
# for i in s:
#     dic[i] = dic.get(i, 0) + 1
# print(dic)
#
# for k, v in dic.items():
#     if v == 1:
#         print(k)
#         break


# 第六题
# nums = [0, 1, 2, 2, 4, 4, 1]
# # nums = [0, 1, 4, 4, -2, -2, 1]
# # nums = [1, 3, 5, 7]
# dic = Counter(nums)
# print(dic)
#
# key, value = None, -1
#
# for k, v in dic.items():
#     if k % 2 == 0:
#         if v > value:
#             key, value = k, v
#         elif v == value:
#             if k < key:
#                 key = k
#
# print(key, value)

# 第七题
# s1 = ['python', 'is', 'amazing', 'as', 'is']
# s2 = ['amazing', 'python', 'is']
#
# dic1 = Counter(s1)
# dic2 = Counter(s2)
# print(dic1)
# print(dic2)
#
# lst = []
# for k, v in dic1.items():
#     if v == 1 and dic2[k] == 1:
#         print(k)
#         lst.append(k)
# print(lst)

# 第八题
# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False
#
#     dic_s = Counter(s)
#     dic_t = Counter(t)
#
#     return dic_s == dic_t

# def is_anagram(s, t):
#     ret = True
#     if len(s) != len(t):
#         ret =  False
#
#     s1 = sorted(s)
#     t1 = sorted(t)
#
#     if s1 != t1:
#         ret = False
#
#     return ret
# print(is_anagram('anagram', 'nagaram'))
# print(is_anagram('rat', 'car'))

# s = 'anagram'
# t = 'nagaram'
#
# if sorted(s) == sorted(t):
#     print('yes')
# else:
#     print('no')
#
# if Counter(s) == Counter(t):
#     print('yes')
# else:
#     print('no')

# 第九题
# nums = [1, 2, 9, 0, 3, 4, 7, 5]
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == 10:
#             print(i, j)
#
# dic = {}
# for index, value in enumerate(nums):
#     dic[value] = index
#
# for index, value in enumerate(nums):
#     tmp = 10 - value
#     if tmp in dic and index < dic[tmp]:
#         print(index, dic[tmp])
#
# dic = {}
# for i in range(len(nums)):
#     if 10 - nums[i] in dic:
#         print(dic[10 - nums[i]], i)
#         # break
#     dic[nums[i]] = i

# 第十题
# n = int(input('n: '))
# dic1 = {}
# dic2 = {}
#
# for i in range(n):
#     cow, side = input('line: ').split(' ')
#     if cow not in dic1:
#         dic1[cow] = side
#     else:
#         if dic1[cow] != side:
#             dic1[cow] = side
#             dic2[cow] = dic2.get(cow, 0) + 1
#
# print(dic1)
# print(dic2)
#
# max_v = 0
# key = 0
# for k, v in dic2.items():
#     if v > max_v:
#         key, max_v = k, v
# print(key, max_v)

# def solve(lst):
#     dic = dict()
#     cnt = 0
#     for cow_id, pos in lst:
#         if cow_id not in dic:
#             dic[cow_id] = pos
#         elif dic[cow_id] != pos:
#             cnt += 1
#             dic[cow_id] = pos
#     return cnt
#
# # n = int(input())
# # lst = [list(map(int, input().split())) for _ in range(n)]
# # print(lst)
# lst = [[3, 1], [3, 0], [6, 0], [2, 1], [4, 1], [3, 0], [4, 0], [3, 1]]
# print(solve(lst))


# a = 1
# print(a, id(a))
# b = a
# print(b, id(b))
# a = 2
# print(id(a))
# print(id(b))
# print(b)


# a = -1
# if a > 0:
#     print('1')
#     print('2')
#     print('over')





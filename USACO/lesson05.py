# d = dict()
# d1 = {}
# print(d, type(d))
# print(d1, type(d1))

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019
# }
# print(d)

# keys = ['brand', 'model', 'year']
# values = ['Tesla', 'Y', 2019]
# d = dict(zip(keys, values))
# print(d)
#
# z = zip(keys, values)
# print(z, type(z))
#
# for i in z:
#     print(i)
#
# x = zip('abcd', '12345')
# for i in x:
#     print(i)

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019
# }
# print(d['brand'])
# print(d['brand1'])

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019,
#     'year': 2020
# }
# print(d)

# d = {
#     1: 'a',
#     1.1: 'b',
#     'ss': 'd',
#     (1, 2): 'e',
#     # [1, 2]: 'f'
#     'abc': [1, 2, 3]
# }
# print(d)

# d = dict(a = 1, b = 2, c = 3)
# print(d)

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019
# }
# # print(len(d))
# print(d.get('brand'))
# print(d.get('a'))
# print(d.get('a', 'car'))
#
# if 'model' in d:
#     print('yes')
#
# if 'car' not in d:
#     print('no')
#
# # print(d['model', 'Tesla'])

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019
# }
#
# d['year'] = 2020
# print(d)
#
# d.update({'year': 2021})
# print(d)
#
# d['color'] = 'red'
# print(d)
#
# d.pop('color')
# print(d)
#
# # d.pop('price')
# # print(d)
#
# d.popitem()
# print(d)
#
# del d['model']
# print(d)
#
# d.clear()
# print(d)

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019
# }
#
# for i in d:
#     print(i)
#
# for i in d:
#     print(i, d[i])

# d = {('brand', 'Tesla'), ('model', 'Y'), ('year', 2019)}
# print(type(d))

# n = int(input('n: '))
# d = {}
# for i in range(1, n + 1):
#     d[i] = i ** 2
# print(d)

# Dict comprehension
# d = {i: i ** 2 for i in range(1, n + 1)}
# print(d)

# # List comprehension
# l = [i ** 2 for i in range(5)]
# print(l)
#
# # Set comprehension
# s = {i ** 2 for i in range(5)}
# print(s)

# solution 1 - set
# s = 'aabcdaabcdaabcdxyz'
# lst = sorted(set(s))
# d = {}
# for i in lst:
#     d[i] = s.count(i)
# print(d)

# solution 2
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

# solution 3
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
# print(d)

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019
# }
#
# print(d.keys(), type(d.keys()))
# d['color'] = 'red'
# print(d.keys())
#
# for i in d.keys():
#     print(i)
#
# for i in d:
#     print(i)
#
# print(d.values(), type(d.values()))
#
# for i in d.values():
#     print(i)
#
# d['year'] = 2020
# print(d.values())
#
# print(d.items(), type(d.items()))
#
# for i in d.items():
#     print(i)
#
# for k, v in d.items():
#     print(k, v)

# d = {
#     'brand': 'Tesla',
#     'model': 'Y',
#     'year': 2019
# }
# d1 = d.copy()
# d2 = dict(d)
# print(d1)
# print(d2)


from collections import Counter
# c = Counter('mississippi')
# print(c)
#
# c = Counter(list('mississippi'))
# print(c)
#
# print(c['a'])
# print(c)

# exercise 1
# s = 'abaccdeff'
# s = ''
# d = Counter(s)
# for i in s:
#     if d[i] == 1:
#         print(i)
#         break
# else:
#     print('-')
#
# d = Counter(s)
# ret = '-'
# for i in s:
#     if d[i] == 1:
#         ret = i
#         break
# print(ret)

# exercise 2
# def get_even(nums):
#     c = Counter(nums)
#     max_count = 0
#     ret = -1
#     for k, v in c.items():
#         if k % 2 == 0:
#             if v > max_count or (v == max_count and k < ret):
#                 max_count = v
#                 ret = k
#     return ret
#
# nums1 = [0, 1, 2, 2, 4, 4, 1]
# nums2 = [1, 3, 5, 7, 9]
# nums3 = [0, 1, 2, 2, 4, 4, 1, 4]
#
# print(get_even(nums2))

# exercise 3
# s1 = ['python', 'is', 'amazing', 'as', 'is']
# s2 = ['amazing', 'python', 'is']
#
# c1 = Counter(s1)
# c2 = Counter(s2)
#
# lst = []
#
# for k, v in c1.items():
#     if k in c2 and v == c2[k] == 1:
#         lst.append(k)
# print(lst)
# print(len(lst))

# exercise 4
# def is_anagram(s, t):
#     c1 = Counter(s)
#     c2 = Counter(t)
#
#     if len(c1) != len(c2):
#         return False
#
#     if c1 != c2:
#         return False
#     else:
#         return True

# def is_anagram(s, t):
#     l1 = sorted(s)
#     l2 = sorted(t)
#
#     if len(l1) != len(l2):
#         return False
#
#     if l1 != l2:
#         return False
#     else:
#         return True
#
# print(is_anagram('anagram', 'nagaram'))
# print(is_anagram('rat', 'car'))

# exercise 5
# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 print(i, j)
#
# l = [1, 2, 9, 0, 3, 4, 7, 5]
# t = 10
# two_sum(l, t)

# key = value in nums and value = index in nums
# def two_sum(nums, target):
#     d = {}
#     for i in range(len(nums)):
#         if target - nums[i] not in d:
#             d[nums[i]] = i
#         else:
#             print(d[target - nums[i]], i)
#
#
# l = [1, 2, 9, 0, 3, 4, 7, 5]
# t = 10
# two_sum(l, t)

a = {1, 2}
b = {a, 3}
print(b)














































































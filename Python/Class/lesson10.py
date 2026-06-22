# lst = []
# for i in range(10):
#     lst.append(i + 1)
# print(lst)
#
# total = 0
# for i in lst:
#     total += i
# print(total)
#
# for i in range(len(lst)):
#     total += lst[i]
# print(total)

# import random
# lst1 = [random.randint(1, 10) for _ in range(10)]
# print(lst1)
#
# lst = []
# for i in range(10, 0, -1):
#     lst.append(i)
# print(lst)
#
# lst1 = []
# for i in range(10, 0, -2):
#     lst1.append(str(i))
# print(lst1)

# lst = [0, 1]
# for i in range(10):
#     n = len(lst)
#     lst.append(lst[n - 1] + lst[n - 2])
# print(lst)

# remove
# lst = [1, 2, 3, 2, 4]
# lst.remove(2)
# print(lst)
#
# lst.pop()
# print(lst)
#
# item = lst.pop(0)
# print(item)
# print(lst)
#
# lst.clear()
# print(lst)

# 生成一个列表1~10
# lst = []
# for i in range(10):
#     lst.append(i + 1)
# print(lst)

# lst = [i for i in range(10)]
# # lst = [10 - i for i in range(10)]
# print(lst)

# 返回新列表
# s1 = lst[1:7:2]
# print(s1)
# s2 = lst[7:1:-2]
# print(s2)
# print(lst)
#
# #
# print(list(range(1, 7, 2)))
# print(list(range(7, 1, -2)))

# print(lst[::])
# print(lst[:])
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[3::])
# print(lst[3:6])
# print(lst[6:3:-1])
# print(lst[100:])
# print(lst[100::-1])
# print(lst[100])


# a = []
# for i in range(1, 12, 3):
#     a.append(i)
# print(a)
#
# b = [i + 1 for i in range(12)]
# print(b)
# c = b[::3]
# print(c)

# lst = [i + 1 for i in range(9)]
# print(lst)

# print(lst[1:9:0])
# print(lst[1:9:2])
# print(lst[6:9:2])
# print(lst[6:9:-2])

# lst1 = lst
# lst.pop()
# print(id(lst), lst)
# print(id(lst1), lst1)

# lst1 = []
# for i in lst:
#     lst1.append(i)
# print(lst1)
#
# lst.pop()
# print(id(lst), lst)
# print(id(lst1), lst1)
#

# lst1 = lst.copy()
# lst1 = list(lst)


# lst = [2, 3, 2, 1, 4, 2, 3, 2, 4, 5]
# target = 0
#
# cnt = 0
# if target not in lst:
#     cnt = -1
# else:
#     for i in lst:
#         if i == target:
#             cnt += 1
# print(cnt)

# print(lst.count(target))

# for i in lst:
#     if i == target:
#         print(i)
#         break
# else:
#     print(-1)

# if target in lst:
#     print(lst.index(target))
# else:
#     print(-1)
#
# ll = []
# for i in range(10, -1, -2):
#     ll.append(str(i))
# print(ll)


# Homework
# lst = [str(i) for i in range(1, 6)]
# print(lst)
#
# lst1 = []
# for i in lst:
#     lst1.append(i)
# print(lst1)

# lst = [i for i in range(1, 10, 2)]
# print(lst)
#
# for i in range(2, 11, 2):  # 2 4 6 8 10
#     lst.insert(i - 1, i) # 1 2 3 4 5 6 7 8 9 10
# print(lst)

# lst = [2, 3, 2, 1, 4, 2, 3, 2, 4, 5]
# target = 21
# total = 0
# for i in lst:
#     if i == target:
#         total += 1
# if total == 0:
#     total = -1
# print(total)

# lst = [i for i in range(1, 9+1, 2)]
# print(lst)
# for i in range(5):
#     lst.insert(i*2+1, (i+1)*2)
# print(lst)


# lst = [str(i) for i in range(1, 6)]
# lst1 = []
# for element in lst:
#    lst1.append(element)
# print(lst1)



# lst = [i for i in range(1, 10, 2)]
# print(lst)
# for i in range(2, 11, 2):
#    index = (i - 1)
#    lst.insert(index, i)
# print(lst)


# lst = [2, 3, 2, 1, 4, 2, 3, 2, 4, 5]
# target = 2
# count = lst.count(target)
# if count == 0:
#     result = -1
# else:
#     result = count
# print(result)





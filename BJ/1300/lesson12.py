# 列表推导式生成lst1，包含5个1~10的随机数，打印lst1
# 列表推导式生成lst2，包含5个1~10的随机数，打印lst2
# 找出2个列表中相同的数字，加入到lst3中，打印lst3

# Use list comprehension to create lst1 with 5 random integers (1-10), then print lst1.
# Use list comprehension to create lst2 with 5 random integers (1-10), then print lst2.
# Find common numbers in the two lists, append them to lst3, and print lst3.
# import random
# lst1 = [random.randint(1, 10) for _ in range(5)]
# print(lst1)
#
# lst2 = [random.randint(1, 10) for _ in range(5)]
# print(lst2)
#
# lst3 = []
# for i in lst2:
#     if i in lst1:
#         lst3.append(i)
# print(lst3)

################################

# 列表推导式生成lst，包含1~10的7个随机数，打印lst
# 找出lst中出现过的数字，加入到列表visited中，每个元素在visited中只出现一次
#
# Generate lst with 7 random integers (1-10) using list comprehension, then print lst.
# Extract unique numbers from lst and add them to the visited list (each number only once).
# import random
# lst = [random.randint(1, 10) for _ in range(7)]
# print(lst)
#
# visited = []
# for i in lst:
#     if i not in visited:
#         visited.append(i)
# print(visited)

################################

# 列表推导式生成lst，包含1~10的10个随机数，打印lst
# 找出lst中出现超过1次的数字，加入到列表duplicate中
#
# Generate lst with 10 random integers (1-10) using list comprehension, then print lst.
# Find numbers that appear more than once in lst and append them to the duplicate list.

# import random
# lst = [random.randint(1, 10) for _ in range(10)]
# print(lst)
#
# visited = []
# duplicate = []
# for i in lst:
#     if i not in visited:
#         visited.append(i)
#     else:
#         if i not in duplicate:
#             duplicate.append(i)
# print(duplicate)

################################

# 交换2个变量的值

# Swap the values of two variables
# Way 1
# a = 1
# b = 2
#
# temp = a
# a = b
# b = temp
# print(a, b)
#
# # Way 2
# c = 1
# d = 2
# c, d = d, c
# print(c, d)
#
# # 交换列表中的2个元素
#
# # Swap two elements in the list
# # Way 1
# lst = [1, 2, 3, 4]
# temp = lst[0]
# lst[0] = lst[3]
# lst[3] = temp
# print(lst)
#
# # Way 2
# lst = [1, 2, 3, 4]
# lst[0], lst[3] = lst[3], lst[0]
# print(lst)

################################

# 生成一个7到8的随机数n
# 列表推导式生成lst，元素是1~n，打印lst
# 通过列表元素置换的方式实现列表中的元素逆序，不可以使用列表切片，打印lst

# Generate random number n (7-8).
# Create lst via list comprehension (elements: 1 to n), then print lst.
# Reverse lst by swapping elements (list slicing forbidden), then print lst.

# import random
# n = random.randint(7, 8)
# lst = [i for i in range(1, n + 1)]
# print(lst)
#
# for i in range(n//2):
#     lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
# print(lst)

################################
# 列表推导式生成lst，包含7个1~100的随机数，打印lst
# 交换最小的数和最大的数，如果最小的数或者最大的数个数不止一个，选择index小的作为交换对象，打印lst
# 提示：使用min(), max(), list.index()
#
# Generate lst with 7 random integers (1-100) via list comprehension, print lst.
# Swap the min and max values in lst: if multiple mins/maxes exist, choose the one with the smaller index for swapping.
# Hint: Use min(), max(), list.index()

# import random
# lst = [random.randint(1, 100) for _ in range(7)]
# print(lst)
# min_index = lst.index(min(lst))
# max_index = lst.index(max(lst))
#
# lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
# print(lst)

################################
# 给定3个列表：
# lst1 = [3, 5, 7, 6, 11]
# lst2 = [3, 7, 7, 9, 11]
# lst3 = [3, 5, 7, 9, 11]
# 判断3个列表中的整数是否递增，如果是则打印True，否则打印False
#
# Given three lists:
# lst1 = [3, 5, 7, 6, 11]
# lst2 = [3, 7, 7, 9, 11]
# lst3 = [3, 5, 7, 9, 11]
# Check if each list's integers are strictly increasing. Print True if it is, else print False.

# lst1 = [3, 5, 7, 6, 11]
# lst2 = [3, 7, 7, 9, 11]
# lst3 = [3, 5, 7, 9, 11]
# lst = lst1
#
# ret = True
# for i in range(len(lst) - 1):
#     if lst[i] >= lst[i + 1]:
#         ret = False
#         break
# print(ret)

################################
# 给定列表lst = [3, 7, 4, 5, 9, 2, 6]
# 找出比前一个数字大并且比后一个数字大的元素的个数，打印满足条件的数字的个数

# Given lst = [3, 7, 4, 5, 9, 2, 6]
# Count elements that are larger than both the previous and next elements, then print the count.

# lst = [3, 7, 4, 5, 9, 2, 6]
# count = 0
# for i in range(1, len(lst) - 1):
#     if lst[i - 1] < lst[i] > lst[i + 1]:
#         count += 1
# print(count)

################################

# 给定一个列表lst = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
# 找出连续出现同样数字最长的个数，打印结果
#
# Given lst = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
# Find the maximum count of consecutive identical numbers and print the result.

# lst = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
# # lst = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6]
# count = 1
# max_count = 0
# num = 0
# for i in lst:
#     if i == num:
#         count += 1
#         if count > max_count:
#             max_count = count
#             # print(i)
#     else:
#         num = i
#         count = 1
# print(max_count)

################################

# 列表推导式生成整数0~9的列表lst
# 随机生成1~8的整数n，打印n
# 把lst中n后面对应的数字依次向前移动，然后把n放到lst的末尾，打印lst
#
# Create lst (integers 0-9) with list comprehension.
# Generate random integer n (1-8).
# Shift elements after n in lst forward in order, append n to lst's end, then print lst.
#
# import random
# lst = [i for i in range(10)]
# n = random.randint(1, 8)
# print(n)
#
# # solution 1
# tmp = lst[n]
# for i in range(n, len(lst) - 1):
#     lst[i] = lst[i + 1]
# lst[-1] = tmp
# print(lst)
#
# # solution 2
# for i in range(n, len(lst) - 1):
#     lst[i], lst[i + 1] = lst[i + 1], lst[i]
# print(lst)
#
# # solution 3
# lst = lst[:n] + lst[n + 1:] + lst[n: n + 1]
# print(lst)

################################

# 给定一个列表lst = [2, 3, 5, 7, 6, 8, 1, 9]
# 找到所有2个元素加起来等于10的组合，打印对应的索引
#
# Given a list lst = [2, 3, 5, 7, 6, 8, 1, 9]
# Find all combinations of two elements whose sum equals 10, and print the corresponding indices of these elements.

lst = [2, 3, 5, 7, 6, 8, 1, 9]
n = len(lst)
for i in range(n - 1):
    for j in range(i + 1, n):
        if lst[i] + lst[j] == 10:
            print(i, j)

################################

# 约瑟夫环
# 编号1~6的五个人排列成一个环形
# 从编号1的人开始报数，数到3的人出列，剩余的人继续排列成环形，然后从出列的下一个人继续报数，直到所有的人都出列
# 打印出列的人的编号顺序

# Josephus problem
# Five people numbered from 1 to 6 are arranged in a circle.
# Start counting from the person with number 1: the person who counts to 3 is eliminated.
# The remaining people are rearranged into a circle, then counting continues from the next person after the eliminated one until all people are eliminated.
# Print the order of the numbers of the eliminated people.

# lst = [1, 2, 3, 4, 5, 6]
# n = 3
# ret = []
# while lst:
#     for i in range(n - 1):
#         lst.append(lst.pop(0))
#     ret.append(lst.pop(0))
# print(ret)


# homework
# lst = [3, 7, 4, 5, 9, 2, 6]
# n = 0
# for i in range(len(lst)):
#     if i == 0 or i == lst[len(lst)-1]:
#         if not lst[i-1] > lst[i-2] and lst[i-1] > lst[i]:
#             n += 1
#     elif i == 0:
#         if lst[i-2] > lst[i-1]:
#             n += 1
#     else:
#         if lst[i-1] > lst[i]:
#             n += 1
# print(n)
#
# lst1 = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
# lst2 = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6]
# a = []
# b = []
# c = []
# d = []
# for i in lst1:
#     if i not in a:
#         b.append(lst1.count(i))
#         a.append(i)
# print(max(b))
# for i in lst2:
#     if i not in c:
#         d.append(lst2.count(i))
#         c.append(i)
# print(max(d))
#
#
# lst = [i for i in range(10)]
# print(lst)
# import random
# n = random.randint(1,8)
# print(n)
# lst.pop(n)
# lst.append(n)
# print(lst)
#
# lst = [2, 3, 5, 7, 6, 8, 1, 9]
# for i in lst:
#     if 10 - i in lst and 10 - i != i and 10 - i > i:
#         print(lst.index(i), lst.index(10-i))


# for i in range(3):
#     print('out', i)
#     for i in range(3):
#         print('inner', i)





import random

# a = [random.randint(1, 10) for i in range(10)]
# print(a)
#
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
#
# a.extend([3, 3, 3])
# print(a)
# c = []
# for i in a:
#     if i in a[a.index(i) + 1:]:
#         if i not in c:
#             c.append(i)
# print(c)
#
# once = []
# multi = []
# for i in a:
#     if i not in once:
#         once.append(i)
#     else:
#         if i not in multi:
#             multi.append(i)
# print(once)
# print(multi)

# 等同于slice
# a = [i for i in range(10)]
# print(a)
#
# for i in range(len(a) // 2):
#     a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
# print(a)

# a = random.sample(range(100) ,10)
# print(a)
# max_index = a.index(max(a))
# min_index = a.index(min(a))
#
# a[max_index], a[min_index] = a[min_index], a[max_index]
# print(a)

# a = random.sample(range(100), 10)
# print(a)
# b = sorted(a)
# print(b)
#
# for i in range(len(a) - 1):
#     if a[i] >= a[i + 1]:
#         print('No')
#         break
#     if i == len(a) - 2:
#         print('Yes')
#
# for i in range(len(b) - 1):
#     if b[i] >= b[i + 1]:
#         print('No')
#         break
#     if i == len(b) - 2:
#         print('Yes')

# a = [random.randint(1, 6) for _ in range(12)]
# print(a)
#
# max_cnt = 0
# cnt = 1
# for i in range(1, len(a)):
#     if a[i - 1] == a[i]:
#         cnt += 1
#         # if cnt > max_cnt:
#         #     max_cnt = cnt
#         max_cnt = max(max_cnt, cnt)
#     else:
#         cnt = 1
# print(max_cnt)

# a = [1, 2, 3]
# a.pop()
# print(a)
# a.append(4)
# print(a)
# print(a[-1])
# print(a[len(a) - 1])

# 4种方法实现把第2位的元素放到最后面
# a = [_ for _ in range(10)]
# print(a)
# index = 2

# 1
# x = a[index]
# a.pop(index)
# a.append(x)
# print(a)

# 2
# x = a[index]
# for i in range(index, len(a) - 1):
#     a[i] = a[i + 1]
# a[-1] = x
# print(a)

# 3
# for i in range(index, len(a) - 1):
#     a[i], a[i + 1] = a[i + 1], a[i]
# print(a)

# 4
# b = a[:index] + a[index + 1:] + [a[index]]
# print(b)

# a = random.sample(range(20), 10)
# print(a)
#
# c, d = random.sample(range(10), 2)
# print(c, d)
#
# total = a[c] + a[d]
# print(total)
#
# for i in range(0, len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if a[i] + a[j] == total:
#             print([i, j])

# a = [i for i in range(1, 10)]
# print(a)
# k = 5
# ret = []
#
# while a:
#     for i in range(k - 1):
#         a.append(a.pop(0))
#     ret.append(a.pop(0))
#
# print(ret)
#
# x = [1, 2, 3]
# print(x[4:])


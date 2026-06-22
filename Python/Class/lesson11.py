# 1. 创建一个空列表lst
# 2. 通过for循环，依次添加4个字符串
# 3. 使用len()打印列表的元素个数
# 4. 使用for循环遍历列表，并打印所有的元素
#
# Let's first create an empty list called lst.
# Next, we'll use a for loop to add four strings to this list one after another.
# Then, we'll use the built-in len() function to print how many elements are in the list.
# Finally, we'll iterate through the list with another for loop and print out all the elements.
# import random

# lst = []
# for i in range(4):
#     s = input('input a string: ')
#     lst.append(s)
# print(len(lst))
#
# for j in lst:
#     print(j)

#################################
# 指定一个都是整数的列表lst=[3, 1, 2, 4, 6, 8, 7, 9]
# 创建一个新的列表，把lst的元素重新排列，要求偶数排在前面，奇数排在后面，不考虑奇数偶数的顺序
# 打印重新排序的列表
#
# Define a list lst containing only integers: lst = [3, 1, 2, 4, 6, 8, 7, 9]
# Create a new list and reorder the elements of lst with the following rule: even numbers come first, followed by odd numbers (the order of even/odd numbers themselves does not matter).
# Print the reordered list.
# lst = [3, 1, 2, 4, 6, 8, 7, 9]
# lst1 = []
# for i in lst:
#     if i % 2 == 0:
#         lst1.append(i)
#
# for j in lst:
#     if j % 2 == 1:
#         lst1.append(j)
#
# print(lst1)

###############################
# 使用列表推导式，生成两个列表，分别是[1, 3, 5, 7, 9]， [2, 4, 6, 8, 10]
# 使用for，把index相同的2个元素在同一行打印
#
# Use list comprehension to generate two lists: [1, 3, 5, 7, 9] and [2, 4, 6, 8, 10] respectively.
# Use a for loop to print the elements with the same index from the two lists on the same line.
# lst1 = [i for i in range(1, 10, 2)]
# lst2 = [i for i in range(2, 11, 2)]
# for j in range(len(lst1)):
#     print(lst1[j], lst2[j])

################################
# 使用range()函数生成一个数字序列1~10，并且赋值给a
# 使用for循环用a作为iterable，for in a的方式打印所有的元素
# 使用list函数，用a作为参数输入，生成lst
# 使用2种for循环的方法，一种是和range结合，一种是直接in iterable来逐个打印结果
#
# Use the range() function to generate a number sequence from 1 to 5, and assign it to variable a.
# Use a for loop to iterate over a (as the iterable) in the form of for...in a, and print all elements of a
# Use the list() function, take a as the input parameter, and generate a list named lst.
# Use two different methods of for loop to print each element of lst one by one:
# Method 1: Combine the for loop with range();
# Method 2: Directly use for...in with the iterable (lst) to print elements one by one.
# a = range(1, 6)
# for i in a:
#     print(i)
# lst = list(a)
# for j in lst:
#     print(j)
# for k in range(len(lst)):
#     print(lst[k])

################################
# 使用random.randint生成10个1~20的整数，并且存放在一个列表中（最好使用列表推导式，也可以使用for），并打印列表
# 算出列表中大于10的数字的个数，并打印结果
#
# Use random.randint() to generate 10 integers between 1 and 20, store them in a list (preferably using list comprehension; a for loop is also acceptable), and print the list.
# Calculate the number of integers greater than 10 in the list, and print the result.
# import random
# lst = [random.randint(1, 20) for i in range(10)]
# print(lst)
# total = 0
# for j in lst:
#     if j > 10:
#         total += 1
# print(total)

################################
# 随机生成10个1~100的整数，并且存放在一个列表中，并打印列表
# 找出列表中最大的数字，并且打印出它的index和数值
# Randomly generate 10 integers between 1 and 100, and store them in a list, then print the list.
# Find the largest number in the list, and print out its index and value.
# import random
#
# lst = [random.randint(1, 100) for _ in range(10)]
# print(lst)
# index, max_num = 0, 0
# for i, e in enumerate(lst):
#     if e > max_num:
#         index, max_num = i, e
# print(index, max_num)

################################
# 随机生成3个1~100的整数，存放在列表lst中
# 用for遍历lst，如果有偶数，则输出yes，如果全部都是奇数，则输出no
# Randomly generate 3 integers between 1 and 100, and store them in a list named lst. Print the list
# Iterate over lst with a for loop: if there is any even number in lst, output yes; if all elements are odd numbers, output no.
# import random
# lst = [random.randint(1, 100) for _ in range(3)]
# print(lst)
# ret = 'no'
# for i in lst:
#     if i % 2 == 0:
#         ret = 'yes'
#         break
# print(ret)

################################
# 列表推导式生成一个列表lst1，元素是1~10，并打印lst1
# 使用切片逆序lst1返回一个新的列表lst2，，并打印lst2
# 使用sum函数结合切片，求和lst1中index2~5的4个数字的和，并打印结果
# Generate a list lst1 using list comprehension, where the elements are integers from 1 to 10, and print lst1.
# Use slicing to reverse lst1 and return a new list lst2, then print lst2.
# Use the sum() function combined with slicing to calculate the sum of the 4 numbers with indices 2 to 5 in lst1. Print the result.
# lst1 = [i for i in range(1, 11)]
# print(lst1)
#
# lst2 = lst1[::-1]
# print(lst2)
#
# print(sum(lst1[2:6]))

################################
# 使用列表推导式，生成两个列表，分别是lst1=[1, 3, 5, 7, 9]， lst2=[2, 4, 6, 8, 10]
# 使用for循环，把lst2的每一个元素顺序依次插入到lst2的每一个元素的后面，并打印此时的lst1
# 使用列表推导式，生成一个新的列表，把lst1中的每一个元素都使用str转换成string
#
# Use list comprehension to generate two lists: lst1 = [1, 3, 5, 7, 9] and lst2 = [2, 4, 6, 8, 10] respectively.
# Use a for loop to insert each element of lst2 into lst1 right after the corresponding element (by order), then print the modified lst1.
# Use list comprehension to generate a new list, converting every element in the modified lst1 to a string using the str() function.
# lst1 = [i for i in range(1, 10, 2)]
# lst2 = [i for i in range(2, 11, 2)]
#
# for i in range(len(lst2)):
#     lst1.insert(i * 2 + 1, lst2[i])
# print(lst1)
#
# lst3 = [str(j) for j in lst1]
# print(lst3)









# recipy = []
# for i in range(4):
#     recipy.append(input('material: '))
# print('amount: ', len(recipy))
# for n in recipy:
#     print('material:', n)

# from random import randint
# a = [randint(1, 10) for i in range(10)]
# print(a)

# tmp = []
# ret = []
#
# for i in a:
#     if i % 2 == 0:
#         ret.append(i)
# for i in a:
#     if i % 2 == 1:
#         ret.append(i)
# print(ret)

# tmp = []
# ret = []
#
# for i in a:
#     if i % 2 == 0:
#         ret.append(i)
#     else:
#         tmp.append(i)
# ret.extend(tmp)
# print(ret)

# import random
# odd = [i for i in range(1, 10, 2)]
# print(odd)
#
# even = [i for i in range(2, 11, 2)]
# print(even)
#
# ret = []
# for i in range(len(odd)):
#     ret.append(odd[i])
#     ret.append(even[i])
# print(ret)

# a = random.randint(1, 100)
# print(a)
# for i in range(2, a):
#     if a % i == 0:
#         print('yes', i)
#         break
#     if i == a - 1:
#         print('no')

# lst = [random.randint(1, 100) for i in range(8)]
# print(lst)
#
# count = 0
# for i in lst:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         if j == i - 1:
#             print(i)
#             count += 1
#
# print(count)





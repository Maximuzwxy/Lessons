#################### variable ####################
# 1. 通过input输入一个整数的n,输出n/3的float类型的值
# 2. 把3个n/3的值以-为间隔连接,并且输出.字符串连接可以使用+
# input:
# 6
# output:
# 2.0
# 2.0-2.0-2.0
#
# input:
# 5
# output:
# 1.6666666666666667
# 1.6666666666666667-1.6666666666666667-1.6666666666666667

# n = int(input('n: '))
# k = n / 3
# print(k)
# s = str(k)
# print(s + '-' + s + '-' + s)



#################### for ####################
# 输入一个任意字符串，打印出每一个字符的索引和对应的当前的字符
# Input an arbitrary string, then print the index and the corresponding character for each character in the string.
# input:
# s: abc
#
# output:
# 0 a
# 1 b
# 2 c

# s = input('s: ')
# for i in range(len(s)):
#     print(i, s[i])



# 任意输入一个正整数n，再输入一个正整数k，输出从-n到n范围内的以k为间隔的等差数列，k<n
# Input positive integers n and k. Output the arithmetic sequence from -n to n with step k, k < n
# n: 8
# k: 3
# -8 -5 -2 1 4 7

# n = int(input('n: '))
# k = int(input('k: '))
# for i in range(-n, n + 1, k):
#     print(i, end=' ')


# 以空格为间隔,输入3个正整数a,b,c,其中b > a， b - a > c
# 计算a到b所有的整数,包括a和b,有多少个整数可以被c整除,打印这些数字,并且计算有多少个,需要用到字符串函数split
# Input three positive integers a, b, c separated by spaces, where b > a and b - a > c.
# Calculate how many integers from a to b (inclusive) are divisible by c, and print all these integers.
# Knowledge of split() and map() functions is required.
# input:
# 1 81 3
# output:
# 3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75 78 81
# 27

# a, b, c = map(int, input('int: ').split())
# print(a, b, c)
# count = 0
# for i in range(a, b + 1):
#     if i % c == 0:
#         print(i, end=' ')
#         count += 1
# print()
# print(count)




#################### while ####################
# Problem Description:
# A glass of pure fruit juice with an initial volume of 100 milliliters (100% concentration)
# is diluted according to the following rules:
# 1. Each operation: Pour out 10 milliliters of the current juice mixture,
# then add 10 milliliters of pure water and stir well.
# 2. After each operation, the juice concentration decreases proportionally
# 3. Enter a target concentration C (0 < C ≤ 100).
# 4. Use a while loop to calculate:
# at least how many dilution operations are required to make the juice concentration
# less than or equal to the target concentration C?
#
# Input and Output Examples:
# Input: 80
# Output: 3
#
# Input: 59
# Output: 6
#
# Input: 100
# Output: 0

# count = 0
# cur = 100
# target = int(input('target: '))
#
# while cur > target:
#     count += 1
#     cur *= 0.9
#
# print(count, cur)

#################### list ####################
# 输入5个整数,以空格间隔,把5个整数存到列表l1中
# 再输入5个整数,以空格间隔,把5个整数存到列表l2中
# 定义一个函数sum_list(a, b), 返回一个新的列表l3,每个元素对应l1和l2的同样位置的值的和
# 并且输出返回的列表的整数的和
# input:
# 1 2 3 4 5
# 6 7 8 9 10
#
# output:
# [7, 9, 11, 13, 15]
# 55

# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))
#
# def sum_list(a, b):
#     lst = []
#     for i in range(5):
#         lst.append(a[i] + b[i])
#     return lst
#
# l3 = sum_list(l1, l2)
# print(l3)
# print(sum(l3))


# 输入3个整数a, b, c, 其中，a > 0， b > 1, c > 5,以空格间隔
# 定义一个函数,get_series(a, b, c),返回一个列表:
# 以a为首项, b为倍数, c为项数的等比数列, 把数列的每一项放到列表中, 并且返回这个列表
# 打印列表, 并打印列表中第3个数字到倒数第三个数字的和
# input:
# 3 2 8
#
# output:
# [3, 6, 12, 24, 48, 96, 192, 384]
# 180

# a, b, c = map(int, input().split())
# print(a, b, c)
#
# def gen_series(x, y, z):
#     lst = []
#     for i in range(z):
#         lst.append(x * (y ** i))
#     return lst
#
# l = gen_series(a, b, c)
# print(l)
# print(sum(l[2 : c - 2]))

# 输入3个整数a, b, c, c > 5,以空格间隔
# 使用列表推导式生成列表:
# 以a为首项,b为倍数,c为项数的等比数列,把数列的每一项放到列表中

# a, b, c = map(int, input().split())
# l = [a * (b ** i) for i in range(c)]
# print(l)



#################### str ####################
# 输入一个任意字符串s
# 在s的每个字符中间加一个'-',并打印新的字符串

# s = input('s: ')
# a = '-'.join(s)
# print(a)

# 输入一个任意字符串s
# 把s的每个小写字母a都替换成大写A

s = input('s: ')
a = s.replace('a', 'A')
print(a)










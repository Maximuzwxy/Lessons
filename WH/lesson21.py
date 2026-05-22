import random

# def my_func():
#     print('my function')
# my_func()

# 定义函数，生成10个1~100的随机数，放到nums中
# import random
# def gen_nums():
#     for i in range(10):
#         nums.append(random.randint(1, 100))
#
# print('begin')
# nums = []
# gen_nums()
# print(nums)

# def my_func():
#     return 5 * 5
#     print(2 * 6)
# print(my_func())

# def my_func():
#     quotient = 5 // 2
#     remainder = 5 % 2
#     return quotient, remainder
#
# print(my_func())
# print(type(my_func()))

def gen_random():
    n = random.randint(1, 3)
    return n

# while True:
#     m = gen_random()
#     g = int(input('guess: '))
#     if m == g:
#         print('Got it!')
#         break
#     else:
#         print('try again!')

# def my_func(name):
#     print('name is ' + name)
#
# my_func('HZ')
# my_func('NX')
# my_func('Harry')

# def my_func(f_name, l_name):
#     print('name is ', f_name, l_name)
#
# my_func('HZ', 'Zhang')
# my_func('NX', 'Fu')
# my_func('Harry', 'Xu')

# def my_func(name='Max'):
#     print('name is ' + name)
#
# my_func('HZ')
# my_func('NX')
# my_func('Harry')
# my_func()

def my_func(x):
    return 5 * x

print(my_func(3))
print(my_func(my_func(4)))
print(my_func((my_func(my_func(5)))))

import math
def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('n: '))
count = 0
for i in range(2, n + 1):
    if is_prime(i):
        count += 1
        print(i, end=' ')
print()
print(count)

# count = 0
# for i in range(2, 1001):
#     if is_prime(i):
#         count += 1
# print(count)

def count_num(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1

    return count

lst1 = [random.randint(1, 5) for _ in range(10)]
print(lst1)
print(count_num(lst1, 1))






def double(lst):
    for i in range(len(lst)):
        lst[i] *= 2
    return lst

# l = [i for i in range(5)]
# print(double(l))

def reverse(lst):
    new_lst = []
    for i in range(-1, -len(lst) - 1, -1):
        new_lst.append(lst[i])
    return new_lst

# l = [i for i in range(5)]
# print(reverse(l))

def change_type(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])

def get_time(h1, m1, h2, m2):
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2

    t = t2 - t1
    print(t // 60, t % 60)

# times = input('time: ').split()
# change_type(times)
# print(times)

# get_time(times[0], times[1], times[2], times[3])

def get_time(h1, m1, h2, m2):
    if m2 < m1:
        m = m2 - m1 + 60
        h = h2 - h1 - 1
    else:
        m = m2 - m1
        h = h2 - h1

    print(h, m)

# a, b, c, d = map(int, input('time: ').split())
# get_time(a, b, c, d)


# lambda (anonymous functions)
# One-line minimalistic functions used for simple operations, avoiding the overhead of defining a full def function
# add = lambda a, b: a + b
# print(add(2, 3))

# map + lambda
# s = [1, 2, 3, 4, 5]
# s1 = list(map(str, s))
# print(s1)
#
# def my_func(x):
#     return x ** 2
#
# s2 = list(map(my_func, s))
# print(s2)

# s2 = list(map(lambda x: x ** 2, s))
# print(s2)

# nums = [(1, 3), (2, 1), (4, 2), (3, 4)]
# nums.sort()
# print(nums)
#
# nums.sort(key=lambda x: x[1])

# def set_key(i):
#     return i[1]
# nums.sort(key=set_key)
# print(nums)

# 1. 函数引用
# 1.1 函数作为参数传递
# def add(a, b):
#     return a + b
# print(add)
# print(add(2, 3))
#
# func = add
# print(func)
# print(func(2, 3))

def execute_func(func, *args):
    return func(*args)

def add(a, b, c = 0):
    return a + b + c

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

print(execute_func(add, 1, 2, 3))
print(execute_func(multiply, 4, 5))
print(execute_func(power, 5, 3))

# 1.2 函数引用列表、字典，管理一组功能相似的函数，实现 “按需调用”（如菜单功能、策略模式)
# func_list = [add, multiply, power]
# for func in func_list:
#     print(func(2, 3))


# 2. Thread
# A simple sample
import time
import threading

def callback(name=''):
    while True:
        print('I am a thread~~~' + name)
        time.sleep(5)

def new_task():
    # new_thread = threading.Thread(target=callback, daemon=True)
    new_thread = threading.Thread(target=callback, args=('haha',), daemon=True)
    new_thread.start()

# while True:
#     new_task()
#     a = input('a: ')
#     print(a)



































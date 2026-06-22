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

# print(execute_func(add, 1, 2, 3))
# print(execute_func(multiply, 4, 5))
# print(execute_func(power, 5, 3))

# 1.2 函数引用列表、字典，管理一组功能相似的函数，实现 “按需调用”（如菜单功能、策略模式)
# func_list = [add, multiply, power]
# for func in func_list:
#     print(func(2, 3))

# func_dict = {'add': add,
#              'mul': multiply,
#              'pow': power}
# print(func_dict['add'](2, 3))
# print(func_dict['mul'](2, 3))
# print(func_dict['pow'](2, 3))

# 1.3 回调函数，异步编程、事件驱动（如按钮点击、网络请求完成后执行回调函数）
# import time
# def async_task(name, callback):
#     print('task:', name)
#     time.sleep(1)
#     callback(name)
#
# def task_callback(name):
#     for i in range(5):
#         print(i, end=' ')
#     print()
#     print(f'{name} finished')
#
# async_task('loop task', task_callback)

# 2. Thread
# A simple sample
# import time
# import threading
#
# def callback():
#     while True:
#         print('I am a thread, lalala')
#         time.sleep(2)
#
# def new_task():
#     new_thread = threading.Thread(target=callback, daemon=True)
#     new_thread.start()
#
# while True:
#     new_task()
#     a = input('a: ')
#     print(a)


# Create a main function that runs an infinite while True loop.
# In each loop, receive a command via input(). The command consists of two strings:
# First string: name (thread name)
# Second string: switch (0 or 1)
#
# Command Rules:
# If the switch is 1:
# Start a new thread with the given name.
# The task of the thread:
# Every 3 seconds, print its own name and the total elapsed seconds since it started.
#
# If the switch is 0:
# Stop the thread with the given name.If the thread does not exist, display: "No such thread".
# If the input is neither 0 nor 1:
# Show an error message.

import threading
import time
import sys

# Dictionary to store active threads: {thread_name: (thread_object, stop_flag, start_time)}
active_threads = {}

def thread_task(name, stop_flag):
    start_time = time.time()
    print(f'Thread {name} started successfully')

    while not stop_flag.is_set():
        elapsed_time = round(time.time() - start_time, 1)
        print(f'Thread {name} total running time {elapsed_time}s')
        if not stop_flag.is_set():
            time.sleep(3)

    elapsed_time = round(time.time() - start_time, 1)
    print(f'Thread {name} stopped successfully, total running time {elapsed_time}s')

def new_task(name):
    stop_flag = threading.Event()
    new_thread = threading.Thread(
        target=thread_task,
        args=(name, stop_flag),
        name=name,
        daemon=True)
    new_thread.start()
    active_threads[name] = (new_thread, stop_flag)

def del_task(name):
    # Get thread info and set stop flag
    thread_obj, stop_flag = active_threads[name]
    stop_flag.set()

    # Wait for thread to finish (optional, for clean termination)
    thread_obj.join(timeout=1)

    del active_threads[name]


def main_task():
    print("Thread Control Program")
    print("Press Ctrl+C to exit the program\n")

    while True:
        try:
            user_input = input('Enter command: ').strip()
            if not user_input:
                print('empty command! retry!')
                continue

            command = user_input.split()

            if len(command) != 2:
                print('invalid command! retry!')
                continue

            name, switch = command

            if switch == '1':
                if name in active_threads:
                    print(f'thread {name} already exists!')
                    continue

                new_task(name)
            elif switch == '0':
                if name not in active_threads:
                    print(f'thread {name} does not exist!')
                    continue
                del_task(name)
            else:
                print('invalid command')

        except KeyboardInterrupt:
            for name in active_threads:
                thread_obj, stop_flag = active_threads[name]
                stop_flag.set()
                thread_obj.join(timeout=1)

                print('all threads stopped')
                sys.exit(0)

# main_task()












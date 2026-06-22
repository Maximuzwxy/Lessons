# 练习1
# 使用while循环计算1~100所有偶数的和

# Exercise 1
# Calculate the sum of even numbers 1-100 with a while loop, then print the result.

# sum_even = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         sum_even += i
#     i += 1
# print(sum_even)

######################################################

# 练习2
# 使用while True，来判断用户输入的任意正整数是否为质数
# 如果用户输入0，则退出循环
# 只能使用while循环

# Exercise 2:
# Use while True to check if the user's input positive integer is a prime (print result).
# Exit the loop if input is 0.
# Only while loops are permitted.

# import math
# while True:
#     n = int(input('n: '))
#     if n == 0:
#         break
#
#     i = 2
#     is_prime = True
#     while i <= int(math.sqrt(n)):
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1
#
#     if is_prime:
#         print('n is prime')
#     else:
#         print('n is not prime')

######################################################

# 练习 3
# 使用while True，来解题鸡兔同笼
# 用户分别输入头的数量和腿的数量，要求都是正整数
# 如果用户输入的值无解，则提示输入错误
# 如果用户的值任意为0，退出循环

# Exercise 3:
# Use while True to solve the Chicken and Rabbit in the Same Cage problem (print result).
# User inputs heads/legs (both positive integers).
# Prompt input error if no result.
# Exit loop if either input is 0.

# while True:
#     head = int(input('head: '))
#     leg = int(input('leg: '))
#
#     if head == 0 or leg == 0:
#         break
#
#     if leg - 2 * head < 0 or (leg - 2 * head) % 2 != 0:
#         print('no result')
#         continue
#
#     rabbit = (leg - 2 * head) // 2
#     chicken = head - rabbit
#
#     if chicken < 0:
#         print('no result')
#         continue
#
#     print(f'rabbit is {rabbit}, chicken is {chicken}')


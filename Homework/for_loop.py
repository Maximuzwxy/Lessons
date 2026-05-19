######################################################
# 练习1
# 1. 输入任意整数n
# 2. 使用for循环以及step，输出0~n的所有偶数
# 3. 输出要求使用print(i, end=' ')，将输出放到一行
#
# 练习2
# 1. 使用for循环以及step，输出100~50的所有能被10整除的数
# 2. 输出要求使用print(i, end=' ')，将输出放到一行
#
# 练习3
# 1. 任意输入一个字符串s
# 2. 使用for循环以及step，逆序输出s
# 3. 输出要求使用print(i, end=' ')，将输出放到一行

# Exercise 1
# 1. Input any integer n.
# 2. Use a for loop with step to output all even integers from 0 to n.
# 3. For output, use print(i, end=' ') to display all numbers on a single line.
#
# Exercise 2
# 1. Use a for loop with step to output all numbers divisible by 10 from 100 down to 50.
# 2. For output, use print(i, end=' ') to display all numbers on a single line.
#
# Exercise 3
# 1. Input any string s.
# 2. Use a for loop with step to output s in reverse order.
# 3. For output, use print(i, end=' ') to display all characters on a single line.

# n = int(input('n: '))
# for i in range(0, n + 1, 2):
#     print(i, end=' ')

# for i in range(100, 49, -10):
#     print(i, end=' ')

# s = input('s: ')
# for i in range(len(s) - 1, -1, -1):
#     print(s[i], end=' ')

######################################################
# 练习1
# 通过for循环计算1~100中所有偶数的和，以及所有奇数的和，并且打印2个结果
#
# Exercise 1
# Use a for loop to calculate the sum of even numbers and odd numbers from 1 to 100.
# Print the two sums (even sum & odd sum).

# sum_odd = 0
# sum_even = 0
#
# for i in range(1, 101):
#     if i % 2 == 1:
#         sum_odd += i
#     else:
#         sum_even += i
# print(sum_odd, sum_even)

######################################################
# 练习2
# 任意输入一个正整数n，判断n是否是质数
#
# Exercise 2
# Enter any positive integer n (via input()).
# Check if n is a prime number and print the result.
# A prime is a positive integer > 1 that can only be divided evenly by 1 and itself.

# n = int(input('n: '))
# is_prime = True
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         is_prime = False
#         break
# print(is_prime)
#
#
#
# import math
# is_prime = True
# for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         is_prime = False
#         break
# print(is_prime)




######################################################
# 练习1
# 使用input()输入一个正整数n
# 打印1~n所有的质数，输出要求使用print(i, end=' ')，将输出放到一行
# 统计1~n中，所有质数的个数，打印结果
#
# Exercise 1
# Use the input() function to enter a positive integer n.
# Print all prime numbers from 1 to n.
# For the output requirement, use print(i, end=' ') to display all results in a single line.
# Count the number of all prime numbers from 1 to n, and print the result.

# import math
# n = int(input('n: '))
# total = 0
#
# for i in range(2, n + 1):
#     is_prime = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         total += 1
#         print(i, end=' ')
#
# print()
# print('prime count:', total)

######################################################

# 练习2
# 使用input()输入一个正整数n
# 使用input()输入一个正整数m，m不等于n
# 求两个正整数的最大公约数（GCD）与最小公倍数（LCM），打印结果
#
# Exercise 2
# Use the input() function to enter a positive integer n.
# Use the input() function to enter a positive integer m, where m is not equal to n.
# Calculate the Greatest Common Divisor (GCD) and the Least Common Multiple (LCM) of the two positive integers, and print the results.

# n = int(input('n: '))
# m = int(input('m: '))
#











# gcd = 1
# for i in range(min(n, m), 0, -1):
#     if n % i == 0 and m % i == 0:
#         gcd = i
#         break
# lcm = int(n * m / gcd)
# print('gcd: ', gcd)
# print('lcm: ', lcm)

######################################################

# 使用input()输入一个正整数n
# 1. 使用for循环以及%的方式，打印1~n中所有7的倍数，打印7的倍数的个数，打印所有7的倍数的和以及乘积
# 2. 使用for循环以及step的方式，打印1~n中所有7的倍数，打印7的倍数的个数，打印所有7的倍数的和以及乘积
# 例如：
# 输入：
# 25
# 输出：
# 7
# 14
# 21
# number: 3
# sum: 42
# product: 2058

# Exercise 1
# Enter a positive integer n using input().
# Using a for loop and the modulo operator (%), print all multiples of 7 from 1 to n.
# Also print the count of these multiples, their sum, and their product.
#
# Exercise 2
# Enter a positive integer n using input().
# Using a for loop and step iteration, print all multiples of 7 from 1 to n.
# Also print the count of these multiples, their sum, and their product.
#
# Input:
# 25
#
# Output:
# 7
# 14
# 21
# count: 3
# sum: 42
# product: 2058
#
# n = int(input('n: '))
# count = 0
# total = 0
# product = 1
#
# for i in range(1, n + 1):
#     if i % 7 == 0:
#         print(i)
#         count += 1
#         total += i
#         product *= i
# print('count:', count)
# print('sum:', total)
# print('product:', product)
#
# for i in range(7, n + 1, 7):
#     print(i)
#     count += 1
#     total += i
#     product *= i
# print('count:', count)
# print('sum:', total)
# print('product:', product)


# Exercise 1
# 任意输入一个正整数n，再输入一个正整数k，输出从-n到n范围内的以k为间隔的等差数列，k<n
# Input positive integers n and k. Output the arithmetic sequence from -n to n with step k, k < n

# n = int(input('n: '))
# k = int(input('k: '))
# for i in range(-n, n + 1, k):
#     print(i, end=' ')


# Exercise 2
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





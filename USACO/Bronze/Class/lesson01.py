# def bessie(num, b):
#     # Bessie's rounding to 10^b
#     power = 10 ** b
#     remainder = num % power
#     if remainder >= power // 2:
#         num += (power - remainder)
#     else:
#         num -= remainder
#     return num
#
# def elsie(num, p):
#     # Elsie's chain rounding
#     for i in range(1, p + 1):
#         num = bessie(num, i)
#     return num
#
# def solve(n):
#     count = 0
#     p = 0
#     for x in range(2, n + 1):
#     # Find the smallest power of 10 >= x
#         while 10 **p < x:
#             p += 1
#         if bessie(x, p) != elsie(x, p):
#             count += 1
#     print(count)
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     solve(n)
#
#
# def alg(N):
#     digits = 0
#     while 10 ** digits < N:
#         digits += 1
#
#     answer = 0
#     for curdigits in range(1, digits + 1):
#         upper = int('5' + '0' * (curdigits - 1)) - 1
#         upper = min(N, upper)
#         lower = int('4' * curdigits)
#         answer += max(0, upper - lower)
#     return answer
#
# T = int(input().strip())
# for _ in range(T):
#     N = int(input().strip())
#     print(alg(N))


# Exercise 1
# Enter any positive integer n (via input()).
# Create a function to check if n is a prime number and print the result.
# A prime is a positive integer > 1 that can only be divided evenly by 1 and itself.
# You can use math.sqrt()
# test_cases = [-2, 0, 1, 2, 4, 7, 9, 19]

import math
def is_prime(n):
    if n <= 1:
        return False

    ret = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret = False
            break
    return ret

test_cases = [-2, 0, 1, 2, 4, 7, 9, 19]
# for i in test_cases:
#     print(is_prime(i), end=' ')

# Exercise 2
# Use the input() function to enter a positive integer n.
# Print all prime numbers from 1 to n.
# For the output requirement, use print(i, end=' ') to display all results in a single line.
# n = int(input('n: '))
# for i in range(2, n + 1):
#     if is_prime(i):
#         print(i, end=' ')

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


# juice dilution
# count = 0
# cur_concentration = 100
# target_concentration = int(input('target concentration: '))
#
# while cur_concentration > target_concentration:
#     count += 1
#     cur_concentration *= 0.9
#
# print(count, cur_concentration)


# cow eating grass problem
# cur_grass = 100
# daily_consume = 3 * 4
# daily_grow = 5
# day = 0
#
# while True:
#     cur_grass -= daily_consume
#     day += 1
#     if cur_grass <= 0:
#         cur_grass += daily_consume
#         break
#     cur_grass += daily_grow
# print(day, cur_grass)



# Given a list lst = [2, 3, 5, 7, 6, 8, 1, 9]
# Find all combinations of two elements whose sum equals 10, and print the corresponding indices of these elements.

# lst = [2, 3, 5, 7, 6, 8, 1, 9]
# n = len(lst)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if lst[i] + lst[j] == 10:
#             print(i, j)



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

# Given a list lst = [23, 10, 3, 63, 100, 201, 71]
# Define a function get_min_index(nums, start, stop) that returns the index of the minimum value from start to stop (excluding stop, following the logic of range).
# Use this function to implement selection sort.



# selection sort
# def get_min_index(nums, start, stop):
#     min_index = start
#     for j in range(start + 1, stop):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     return min_index
#
# lst = [23, 10, 3, 63, 100, 201, 71]
# for i in range(len(lst)):
#     index = get_min_index(lst, i, len(lst))
#     lst[index], lst[i] = lst[i], lst[index]
# print(lst)



# def my_round(num, p):
#     big = 10 ** p
#
#     if num >= big // 2:
#         return big
#     else:
#         return 0
#
# # print(my_round(500))
#
# def chain_round(num, p):
#     for i in range(1, p + 1):
#         remainder = num % (10 ** i)
#         next_num = my_round(remainder, i)
#
#         if next_num != 0:
#             num = (num // (10 ** i)) * (10 ** i) + (10 ** i)
#
#     # print(num)
#
#     if num >= 10 ** p // 2:
#         return 10 ** p
#     else:
#         return 0
#
# # print(my_round(405, 3))
# # print(chain_round(445, 3))
#
# def compare(num):
#     count = 0
#
#     for i in range(2, num + 1):
#         p = 1
#         while 10 ** p < i:
#             p += 1
#         if my_round(i, p) != chain_round(i, p):
#             count += 1
#             # print(i, end=' ')
#     print(count)
#
# n = int(input())
# for _ in range(n):
#     number = int(input())
#     compare(number)

# def compare(num):
#     count = 0
#     if num > 10:
#         p = 1
#         while 10 ** p < num:
#             p += 1
#
#         for i in range(1, p):
#             upper = int('5' + '0' * i) - 1
#             lower = int('4' * (i + 1))
#
#             if lower <= num:
#                 count += (min(upper, num) - lower)
#                 # print(upper, lower)
#
#     print(count)
#
# n = int(input())
# for _ in range(n):
#     number = int(input())
#     compare(number)



import random
lst = []
for i in range(10):
    lst.append(random.randint(1, 100))

print(lst)

lst = [random.randint(1, 100) for _ in range(10)]
# lst1 = [i for i in range(10)]

_ = 1
print(_)








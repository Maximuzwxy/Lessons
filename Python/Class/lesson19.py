# strip
# s = ' Hello, World! '
# print(len(s))
# # print(s.split())
# s1 = s.strip()
# print(s1)
# print(len(s1))
#
# s2 = s.lstrip()
# print(s2)
# print(len(s2))
#
# s3 = s.rstrip()
# print(s3)
# print(len(s3))

# s = 'hello,world'
# sp = s.split(',')
# print(sp, type(sp))
#
# s = 'hello world   hola'
# print(s.split())

# s = 'Python is awesome'
# s1 = 'om'
#
# print(s.find(s1))
# print(s.find(s1, 2, 5))
# print(s.find(s1, 10))
#
# print(s.find('o'))
# print(s.rfind('o'))
# print(s.rfind('Python'))

# aa = '***'
# lst = ['apple', 'banana', 'pear']
# s = aa.join(lst)
# print(s)
#
# print(' and '.join(lst))
#
# b = 'Ethan has a balloon'
# print(','.join(b))
# s = 'abcde'
#
# print(' '.join(s[::-1]))
# print(' '.join(reversed(s)))
#
# print(b.replace('has', 'had'))
# print(b.replace('a', 'A'))

# s = 'Ethan Felix Sylvia TM'
# print(s.upper())
# print(s.lower())
# print(s.capitalize())

# num = '5'
# letter = 'abcde'
#
# print(num.isnumeric())
# print(num.isalnum())
# print(num.isalpha())
# print(letter.isalpha())
# print('    '.isspace())

movie = "2001: A SAMMY ODYSSEY"
book = "A Thousand Splendid Sharks"
poem = "sammy lived in a pretty how town"

print(movie.islower())
print(movie.isupper())

print(book.istitle())
print(book.isupper())

print(poem.istitle())
print(poem.islower())



# Exercise 1
# Given a string, print the length of last word in the string.
# If the last word does not exist, print 0.
#
# Example:
# Input: "Hello World"
# Output: 5
#
# input:
# output: 0

# s = input('str: ')
#
# lst = s.split()
# if len(lst) == 0:
#     print(0)
# else:
#     print(len(lst[-1]))


# Exercise 2
# Read a single letter from the keyboard, which can be either uppercase or lowercase.
# If the letter is uppercase, output its corresponding lowercase letter.
# If the letter is lowercase, output its corresponding uppercase letter.
# For example:
# the uppercase letter corresponding to 'a' is 'A', and the lowercase letter corresponding to 'M' is 'm'.
# s = input('s: ')
# if s.isupper():
#     print(s.lower())
# else:
#     print(s.upper())



# Exercise 3
# Given two strings composed only of uppercase or lowercase letters,
# their relationship falls into one of the following four cases:
# 1. The two strings have different lengths.
# For example: Beijing and Hebei.

# 2. The two strings have the same length, and the characters at corresponding positions are completely identical (case-sensitive).
# For example: Beijing and Beijing.

# 3. The two strings have the same length, and the characters at corresponding positions are identical only when case is ignored (i.e., they do not satisfy case 2).
# For example: beijing and BEijing.

# 4. The two strings have the same length, but they are not identical even when case is ignored.
# For example: Beijing and Nanjing.

# Write a program to determine which of the four cases the relationship between the two input strings belongs to, and output the corresponding case number.
# Input:
# Two lines, each containing one string.
# Output:
# A single digit representing the relationship number of the two strings.

# while True:
#     s1 = input('s1: ')
#     s2 = input('s2: ')
#
#     ret = 0
#     if len(s1) != len(s2):
#         ret = 1
#     else:
#         if s1 == s2:
#             ret = 2
#         else:
#             if s1.upper() == s2.upper():
#                 ret = 3
#             else:
#                 ret = 4
#
#     print(ret)



# Exercise 4
# Input a string composed of lowercase letters (length ≤ 100).
# Output the lowercase letter that appears most frequently.
# Note: If multiple letters have the same highest frequency, output the one with the largest ASCII value.
# Input
# aaabbbbbbbbbcdxs
# Output
# b

# while True:
#     lst = [0] * 26
#
#     s = input('s: ')
#     for i in s:
#         index = ord(i) - ord('a')
#         lst[index] += 1
#
#     max_index = 0
#     for i in range(len(lst)):
#         if lst[i] >= lst[max_index]:
#             max_index = i
#
#     print(max(lst), chr(ord('a') + max_index))



# Exercise 5
# Given a string, determine if it does not change either reading from left or right.
# You can't use slice
# Input:
# malayalam
# Output:
# True
#
# Input:
# hello
# Output:
# False

# solution 1
# s = input('s: ')
# ret = True
# for i in range(len(s) // 2):
#     if s[i] != s[len(s) - i - 1]:
#         ret = False
#         break
# print(ret)

# solution 2
# s = input('s: ')
# ret = True
# left, right = 0, len(s) - 1
# while left < right:
#     if s[left] != s[right]:
#         ret = False
#         break
#     left += 1
#     right -= 1
# print(ret)


# 1. 写一个while循环
# 2. 输入一个任意字符串s
# 3. 判断s是不是满足回文，如果是，则输出True
# 4. 如果s不满足，如果删除其中一个字母之后，可以满足回文，输出True，否则输出False

# while True:
#     s = input('s: ')
#     if s == s[::-1]:
#         print(True)
#     else:
#         ret = False
#         for i in range(len(s)):
#             lst = list(s)
#             lst.pop(i)
#             if lst == lst[::-1]:
#                 ret = True
#                 break
#         print(ret)






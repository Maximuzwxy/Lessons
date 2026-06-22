# 第一题
# 回文判断
# 1. 通过input输入一个任意长度的字符串
# 2. 判断字符串是否满足回文，即左右对称，如abcdcba，或者abcddcba
# 3. 如果满足打印True，不满足打印False

# Exercise 1
# Palindrome Judgment
# Input a string of any length using input().
# Determine whether the string is a palindrome (symmetric left and right), such as abcdcba or abcddcba.
# Print True if it is a palindrome; otherwise, print False.
# s = input('s: ')
# if s == s[::-1]:
#     print(True)
# else:
#     print(False)


##########################################

# 第二题
# 1. 给定一个字符串，这是一个文件的路径以及文件名，path = "C:\Users\Alice\Documents\homework.txt"
# 2. 用print输出path对应的路径以及文件名(使用转义字符)
# 3. 把\分割的部分，放到列表中，并且打印这个列表，使用切片
#
# 输出：['C:', 'Users', 'Alice', 'Documents', 'homework.txt']

# Exercise 2
# Given a string representing a file path and file name:path = "C:\Users\Alice\Documents\homework.txt"
# Print the complete path with escape characters.
# Split the path by the backslash symbol \, store each part in a list, and print the list, using slice.
# Sample output:
# ['C:', 'Users', 'Alice', 'Documents', 'homework.txt']

path = "C:\\Users\\Alice\\Documents\\homework.txt"
print(path)
lst = []
start = end = 0
for i, v in enumerate(path):
    if v == '\\':
        end = i
        lst.append(path[start:end])
        start = end + 1
lst.append(path[start:])
print(lst)

##########################################

# 第三题
# 1. 输入的一句英文（只包含小写字母和空格）
# 2. 加密，加密规则为：每个字母向后移动 3 位，输出加密之后的字符串
# 3. 然后解密，将加密后的字符串恢复为原文，输出原文
#
# 输出：
# s: hello world
# khoor#zruog
# hello world

# Exercise 3
# Input an English sentence containing only lowercase letters and spaces.
# Encryption Rule: Shift each letter 3 positions backward in the alphabet.
# Output the encrypted string.
# Decryption: Restore the encrypted string back to the original text and print the result.

# Sample output:
# s: hello world
# khoor zruog
# hello world

# s = input('s: ')
# s_encode = ''
# s_decode = ''
#
# for c in s:
#     s_encode += chr(ord(c) + 3)
# print(s_encode)
#
# for c in s_encode:
#     s_decode += chr(ord(c) - 3)
# print(s_decode)



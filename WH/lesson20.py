# 1
# 1. 输入一个整数n
# 2. 输入一个字符串s
# 3. 输出s再接上s后面的n个字符n次
# 4. len(s) > n
#
# 输入：
# n = 3
# s = 'abcde'
# 输出：
# abcdecdecdecde

# n = int(input('n: '))
# s = input('s: ')
# suffix = s[-n:]
# print(s, suffix)
# print(s + suffix * n)

# def repeat(n, s):
#     if n > len(s):
#         print('invalid input')
#
#     suffix = s[-n:]
#     print(s, suffix)
#     print(s + suffix * n)
#
# n = int(input())
# print(repeat(n, input()))


################### ECHO ###################
# 2
# 1. 输入一个整数n
# 2. 输入一个字符串s
# 3. 输出s再接上s后面的n个字符1次，n-1个字符，一直到只有1个字符
# 4. len(s) > n
#
# 输入：
# n = 3
# s = 'abcde'
# 输出：
# abcdecdedee

# n = int(input('n: '))
# s = input('s: ')
#
# res = s
# for i in range(n, 0, -1):
#     res += s[-i:]
#
# print(res)


# def repeat(n, s):
#     res = s
#     if n > len(s):
#         print('invalid input')
#
#     for i in range(n, 0, -1):
#         res += s[-i:]
#
#     print(res)
#
# n = int(input())
# print(repeat(n, input()))


#######################################
# 3
# 1. 给定字符串
# '@There@is@no@royal@road@to@learning.@'
# 2. 把@改成空格，并且把首位的@去掉
# 3. 分别用replace和split实现

# s = '@There@is@no@royal@road@to@learning.@'
# s1 = s.replace('@', ' ')
# print(s1)
# s2 = s1.strip()
# print(s2)

# print(s.replace('@', ' ').strip())


# s = '@There@is@no@royal@road@to@learning.@'
# s1 = s.strip('@')
# print(s1)
# lst = s1.split('@')
# print(lst)
# s3 = ' '.join(lst)
# print(s3)

#######################################
# 4
# 1. 给定3个列表
# l1 = ['1', '2', '3']
# l2 = ['a', 'b', 'c']
# l3 = ['x', 'y', 'z']
# 2. 生成一个字符串，是每个列表中的某一个元素的随机组合
# 3. 列表中选随机值可以用random.choice(l1)

# import random
# l1 = ['1', '2', '3']
# l2 = ['a', 'b', 'c']
# l3 = ['x', 'y', 'z']
#
# s = random.choice(l1) + random.choice(l2) + random.choice(l3)
# print(s)

#######################################
# 5
# 1. 单词接龙游戏
# 2. 使用while循环
# 3. 初始输入一个单词，然后while循环开始
# 4. 如果输入的单词的首字母是刚才输入的最后一个字母，则循环继续，否则退出循环，显示你输了

# s = input('first word: ')
# while True:
#     s1 = input('next: ')
#     if s[-1] == s1[0]:
#         s = s1
#         print('go on!')
#     else:
#         print('you lose!')
#         break

# while True:
#     s1, s2 = input('s: ').split()
#     if s1[-1] == s2[0]:
#         print('continue')
#     else:
#         break


#######################################
# 6
# 1. 如何判断质数
# 2. 打印出A~Z和a~z中，对应的ASCII是质数的字母

import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# for i in range(ord('A'), ord('Z') + 1):
#     if is_prime(i):
#         print(i, chr(i))
#
# for i in range(ord('a'), ord('z') + 1):
#     if is_prime(i):
#         print(i, chr(i))

# for i in range(ord('A'), ord('Z') + 1):
#     is_prime = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             is_prime = False
#     if is_prime:
#         print(i, chr(i))
#
# for i in range(ord('a'), ord('z') + 1):
#     is_prime = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             is_prime = False
#     if is_prime:
#         print(i, chr(i))


######################################

# s = input('s: ')
# n = 0
# cur = ''
# ret = ''
# tmp = ''
# for i in s:
#     if cur != i:
#         tmp = i
#         cur = i
#         n = 1
#         ret += tmp
#     else:
#         if n == 1:
#             ret = ret[:len(ret) - 1]
#         else:
#             ret = ret[:len(ret) - 2]
#         n += 1
#         tmp = str(n) + i
#         ret += tmp
#
# print(ret)

# s = input()
# if not s:
#     print('none')
#     exit()
#
# res = []
# count = 1
# cur_char = s[0]
#
# for c in s[1:]:
#     if cur_char == c:
#         count += 1
#     else:
#         if count == 1:
#             res.append(cur_char)
#         else:
#             res.append(str(count) + cur_char)
#
#         count = 1
#         cur_char = c
#
# if count == 1:
#     res.append(cur_char)
# else:
#     res.append(str(count) + cur_char)
#
# print(''.join(res))

######################################

def com_dict(a, b):
    s1 = a.lower()
    s2 = b.lower()

    if s1 == s2:
        return a
    else:
        len1 = len(s1)
        len2 = len(s2)

        for i in range(min(len1, len2)):
            if ord(s1[i]) < ord(s2[i]):
                return a
            elif ord(s1[i]) == ord(s2[i]):
                continue
            else:
                return b

        if len1 < len2:
            return a
        else:
            return b

# n = int(input())
# lst = []
# for s in range(n):
#     lst.append(input())
# print(lst)

# lst = [input().strip() for _ in range(n)]
# print(lst)

# min_str = lst[0]
# for s in lst[1:]:
#     min_str = com_dict(min_str, s)
# print(min_str)

# ret = min(lst, key=lambda x: x.lower())
# print(ret)

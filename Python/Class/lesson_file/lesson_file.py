# f = open('test.txt', 'w')
# f.write('come on!\n')
# f.close()

# f = open('test.txt', 'r')
# s = f.read()
# print(s)
# f.close()

# f = open('test.txt', 'r')
# s = f.read(10)
# print(s)
# f.close()

# with open('test.txt', 'r') as f:
#     s = f.read(10)
#     print(s)

# with open('test.txt', 'r') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

# with open('test.txt', 'r') as f:
#     while True:
#         s = f.readline()
#         if s:
#             print(s, end='')
#         else:
#             break

# with open('test.txt', 'r') as f:
#     lst = f.readlines()
# print(lst)


# 使用while，写一段程序，可以一直输入文字，回车代表输入下一行，并且把回车之前的一段字符写入文件
# 如果输入的是'!quit'，则表示停止输入
# 读取文件，并且打印所有内容

# with open('a.txt', 'w') as f:
#     while True:
#         s = input()
#         if s == '!quit':
#             break
#         f.write(s + '\n')
#
# with open('a.txt', 'r') as f:
#     print(f.read())

# 在刚才的文件，用readline()读取每一行，并且以'-'间隔，拼接成一个字符串，并且打印结果
# with open('a.txt', 'r') as f:
#     lines = f.readlines()
#     print(lines)
#
#     ll = []
#     for i in lines:
#         ll.append(i.strip())
#
#     print(ll)
#
#     s = '-'.join(ll)
#     print(s)
#
#
#
# l = []
# with open('a.txt', 'r') as f:
#     while True:
#         s = f.readline()
#
#         if s:
#             l.append(s.strip())
#         else:
#             break
#
# print('-'.join(l))

# 统计刚才的文件中的字符的数量，空格的数量，和a出现的次数
# with open('a.txt', 'r') as f:
#     s = f.read()
#     print(len(s), s.count(' '), s.count('a'))

# 统计刚才的文件中总共有多少行，最长的一行多少字符，并且输出这一行
# max_s = ''
# max_len = 0
# with open('a.txt', 'r') as f:
#     while True:
#         s = f.readline()
#
#         if not s:
#             break
#
#         if len(s) > max_len:
#             max_len = len(s)
#             max_s = s
#
# print(max_len)
# print(max_s)
#
# #########################################
# with open('a.txt', 'r') as f:
#     lst = f.readlines()
# print(lst)
#
# max_index = 0
# for i in range(1, len(lst)):
#     if len(lst[i]) > len(lst[max_index]):
#         max_index = i
#
# print(lst[max_index])

# homework
# 创建一个列表，包含几个字符串，分别是：name, age, gender, grade, school
# 创建一个文件，名字是info.txt，然后通过input输入你的信息，并且把输入的内容保存到文件中，最好读取文件内容，并且打印出来

info = ['name', 'age', 'gender', 'grade', 'school']
with open('info.txt', 'w') as f:
    for i in info:
        s = input(i + ': ')
        ss = i + ': ' + s + '\n'
        f.write(ss)

with open('info.txt', 'r') as f:
    print(f.read())





# def bessie(l, k):
#     ll = []
#     cur_s = []
#     n = len(l)
#     cur_len = 0
#
#     for i in range(n):
#         if cur_len + len(l[i]) > k:
#             ll.append(' '.join(cur_s))
#             cur_s.clear()
#             cur_len = 0
#         cur_s.append(l[i])
#         cur_len += len(l[i])
#
#     if len(cur_s) != 0:
#         ll.append(' '.join(cur_s))
#
#     return ll
#
# a, b = map(int, input().split())
# lst = list(input().split())
# s = bessie(lst, b)
# print(s)














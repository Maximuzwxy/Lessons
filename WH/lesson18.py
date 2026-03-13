# message = 'hello 你好'
# print(message)
#
# s_msg_8 = message.encode('utf-8')
# print(s_msg_8)
#
# s_msg_16 = message.encode('utf-16')
# print(s_msg_16)
#
# r_msg_8 = s_msg_8.decode('utf-8')
# print(r_msg_8)
#
# r_msg_16 = s_msg_16.decode('utf-16')
# print(r_msg_16)
#
# # utf-8 英文 1Byte 中文3Byte，灵活，绝对主流，web，文档，代码等等
# # utf-16 2Byte
#
#
# ########### decode error ###########
# r_msg_8 = s_msg_8.decode('utf-16')
# print(r_msg_8)

# r_msg_16 = s_msg_16.decode('utf-8')
# print(r_msg_16)


# ch = 'b'
# print(type(ch))
#
# print(ord(ch))
# print(chr(97))
# print(chr(ord(ch) - 1))
#
# for i in range(26):
#     print(chr(97 + i), end=' ')
# print()
#
# print(ord('a') - ord('A'))

# s = 'Hello World'
# for i in range(11):
#     print(s[i], end='')
# print()
#
# for i in range(-11, 0):
#     print(s[i], end='')
# print()
#
# print(s[10])
# print(s[-1])

# s = 'hello\nworld'
# print(s)
#
# s = '''hello
# world'''
# print(s)

# s = 'He said, \"what\'s there?\"'
# print(s)

# s = 'a\
# b\
# c'
# print(s)

# s = 'Python string is a sequence'
# print('length:', len(s))
# print(s[3])
# print(s[-2])

# s = 'string slicing example'
# print(s[1:3])
# print(s[-5:-1])
# print(s[:4])
# print(s[8:])
# print(s[-3:])

# print(s[::-1])
# print(s[3:1:-1])
# print(s[-1:-5:-1])
# print(s[4::-1])
# print(s[8::-1])
# print(s[-3::-1])

# print(s[1:10:3])
# print(s[-5:-1:2])
# print(s[:4:2])
# print(s[8::2])
# print(s[-5::3])

# s = 'hello world'
# s[0] = 'H'
# print(s)

# s[:5] = 'Hello'
# print(s)

# n = int(input('n: '))
# s1 = 'go' * 3
# s2 = (s1 + '!') * n
# print(s1)
# print(s2)



# lst = [1, 2, 3, 4, 5]
# print(id(lst))
# lst[1:2] = [10]
# print(id(lst))
# print(lst)

# homework
# hw = str(input())
# if hw[0:len(hw)-1] == hw[len(hw):0:-1]:
#     print('True')
# else:
#     print('False')

# hw = str(input())
# if hw == hw[::-1]:
#     print('True')
# else:
#     print('False')


path = "C:\\Users\\Alice\\Documents\\homework.txt"
print(path)
print(path.split("\\"))

s = input('s: ')
s_encode = []
s_decode = ''
for i in s:
    s_encode += chr(ord(i) + 3)

print(s_encode)

for i in s_encode:
    s_decode += chr(ord(i) - 3)

print(s_decode)

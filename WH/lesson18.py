# binary
# octal
# decimal
# hexadecimal
# ordinal
# character

# c = 'a'
# c = '你'
# code = ord(c)
# print(code)
# print(chr(code))
# print(hex(code), bin(code))
#
# c_8 = c.encode('utf-8')
# print(c_8)
#
# for i in c_8:
#     print(i, hex(i), bin(i))
#
# s_8 = c_8.decode('utf-8')
# print(s_8)


# 1. UTF-16 编码数据（小端/大端都能处理，这里按BE处理）
# utf16_bytes = bytes.fromhex("2D30 2D63 2D53 2D4D 0021")
# utf16_str = utf16_bytes.decode("utf-16-be")
# print("UTF-16 decoded:", utf16_str)
#
# # 2. UTF-8 编码数据
# utf8_bytes = bytes.fromhex("E2 B4 B0 E2 B5 A3 E2 B5 93 E2 B5 8D 21")
# utf8_str = utf8_bytes.decode("utf-8")
# print("UTF-8 decoded:", utf8_str)
#
# # 3. UTF-32 编码数据（按BE处理）
# utf32_bytes = bytes.fromhex("00 00 2D 30 00 00 2D 63 00 00 2D 53 00 00 2D 4D 00 00 00 21")
# utf32_str = utf32_bytes.decode("utf-32-be")
# print("UTF-32 decoded:", utf32_str)


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
# utf-8 英文 1Byte 中文3Byte，灵活，绝对主流，web，文档，代码等等
# utf-16 2Byte
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






#不能以数字开头
#1aaa = 12

#标识符会变，在CPython中，是对应的内存地址，但是有的不是地址，只是一个唯一标识
# C语言变量是“存储单元”，地址固定。
# Python变量是“名字”，指向对象，赋值时引用变，地址也变。
# a = 1
# print(id(a))
# print(hex(id(a)))
# a = 2
# print(id(a))
# print(hex(id(a)))

#type
# a = 1
# print(type(a))
# b = 1.1
# print(type(b))
# c = True
# print(type(c))
# d = []
# print(type(d))
# e = ''
# print(type(e))
# #complex必须是j
# f = 2 + 3j
# print(type(f))
#
# #字符串，"""也可以
# a = """lalala"""
# print(a)

# 进制转换
# 将base对应的进制转换成十进制，得到一个十进制数字，但是a必须是str
# a = '127'
# print(int(a, base = 8))
# print(bin(127))
# print(oct(127))
# print(hex(127))

# 可以这样赋值
# a = 1
# b = 2
# c, d = a, b
# print(c, d)

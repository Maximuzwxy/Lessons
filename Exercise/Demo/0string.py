# string和list都可以回文
# a = 'asdfghjkl'
# b = a[::-1]
# print(b)

# 切片：s[start:end:step]
# 用切片进行浅拷贝，针对list，b=a[:]，a和b的id()是2个地址，但是如果是str，则一样
# a = [1, 2, 3]
# print(a[::-1])
# b = a[:]
# print(f'a id: {id(a)}, b id: {id(b)}')
#
# c = '123456'
# print(c[::-1])
# d = c[:]
# print(f'c id: {id(c)}, d id: {id(d)}')

# str(a)返回的是一个string，因此可以后面直接跟[::-1]
# a = 123456
# b = str(a)[::-1]
# print(b)

# str不能直接a[0]=’x’，要用替换
# a = '1234563'
# b = a.replace('3', 'a')
# print(b)
# 如果想替换index的某个值，有2个办法，一个是slice，一个是转换成list之后，替换完了之后再转换回来
# a = '123456'
# b = a[:1] + 'x' + a[2:]
# print(b)
#
# c = list(a)
# c[1] = 'x'
# d = ''.join(c)
# print(d)


# split只针对str，不写参数默认是空格*n，如果写，则是对应的字符
# a = 'a b c'
# print(a.split())
# b = 'a, b, c'
# print(b.split(','))

# lstrip() 是字符串方法，用于去除字符串左侧（开头）的指定字符，默认去除所有空白字符（空格、换行、制表符等）
# a = '  123'
# print(a.lstrip())
# b = '00111'
# print(b.lstrip('0'))
# c = 'x y z'
# print(c.replace(' ', ''))
# d = c.replace(' ', '')
# print(d)

# strip用于去除首位的某些字符，lstrip只去左边的，rstrip只去右边的，replace是更改字符串种所有的，strip可以取出任何首位的字符，如二进制转换种的0
# a = '  abc  '
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())

# # join: join() 是字符串方法，用于把可迭代对象（如列表、元组）中的元素连接成一个字符串。
# a = '-'.join(['a', 'b', 'c'])
# print(a)
# b = ','.join(['aa', 'bb', 'cc'])
# print(b)
# c = [1, 2, 3]
# d = ''.join(map(str, c))
# print(d)

# 判断一个字符串为空，2种办法，但是python社区推荐后者
# a = ''
# if a == '':
#     print('None')
# if not a:
#     print('None')

# startswith endswith
a = 'aaa789.txt'
if a.startswith('aaa'):
    print('got it')
if a.endswith('.txt'):
    print('got it')
# a = []和a = list()，都可以创建一个空列表
# a = list()
# print(a)

# 以下会报错
# a = list('12345')
# b = list()
# for i in range(5):
#     b[i] = a[i]
#     print(b)
# 空列表不能直接a[1]等于另一个列表值，因为未分配空间
# 空列表分配空间，需要用a=[None]*5，或者a=[‘’]*5才可以
# 最好使用append给空列表增加新元素

# append
# a = ['1', '2', '3']
# a.append('4')
# print(a)

# insert
# a = ['1', '2', '3']
# a.insert(1, 'a')
# print(a)

# extend
# a = ['1', '2', '3']
# a.extend(['a', 'b'])
# print(a)

# +
# a = ['1', '2', '3']
# a = a + [4, 5]
# print(a)

# slice
# a = ['1', '2', '3']
# a[len(a):len(a) + 2] = [4, 5]
# print(a)

# # next是一个内置函数，针对可迭代对象, 下面这样是会报错，因为列表不是一个对象，需要转换成迭代对象
# a = [1, 2, 3]
# # print(next(a))
# # 下面这样也不会顺序输出，因为每次都从a的开始开始，因此得声明一个新的变量才可以
# print(next(iter(a)))
# print(next(iter(a)))
# it = iter(a)
# print(next(it))
# print(next(it))

## str作为list的参数，会变成一个字符的列表
# a = 'abc'
# print(list(a))

# # 切片是针对可迭代对象，如果a[-1]，是倒着找第一个元素
# a = [1, 2, 3]
# # print(a[3]) # 报错
# print(a[2:1:-1])
# print(a[-3])

# 遍历，index和元素都拿到
# a = [1, 2, 3]
# for i, v in enumerate(a):
#     print(i, v)

# # 查看list中是否包含某个元素，用关键字in，没有list的函数
# a = [1, 2, 3]
# if 1 in a:
#     print('index', a.index(1)) # index只返回找到的第一个元素的index，如果有多个的话

# # insert，extend，sum
# # 查看list中是否包含某个元素，用关键字in，没有list的函数
# a = [1, 2, 3]
# a.insert(1, 5)
# print(a)
# b = [7, 8]
# a.extend(b) # 等于a + b
# # print(a.extend(b)) # 这样不可以，因为extend没有返回值
# print(a)
# print(sum(a))
# print(range(0, 10))

# remove
# a = [1, 1, 3]
# a.remove(1) # 只删除第一个，如果有多个
# print(a)

# # pop，移除最后一个，但是pop()可以指定
# a = [1, 2, 3]
# # a.pop()
# a.pop(2)
# print(a)
#
# # clear清空
# a.clear()
# print(a)

# # 切片越界不会报错，list的切片是返回了一个新的列表
# a = [1, 2, 3, 4, 5]
# print(a[1:5:2])
# print(a[4::-2])

# 对比列表和slice
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(b[1:7:2])
# print(b[7:1:-2])
#
# print(list(range(1, 7, 1)))
# print(list(range(7, 1, -1)))

# slice
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # a = '123456789'
# print(a[::]) # 返回新列表
# print(a[:]) # 返回新列表
# print(a[::-1]) # 返回逆序列表
# print(a[::2]) # 偶数位元素列表
# print(a[1::2]) # 奇数位元素列表
# print(a[3::]) # 从index3开始的列表
# print(a[3:6]) # index3~5的列表
# print(a[6:3:-1]) # index6~4的列表
# print(a[0:100:1]) # 不会越界，超出索引，自动截断
# print(a[100:]) # 超出索引，自动截断
# print(a[100::-1]) # 超出截断，逆序
# # print(a[100]) # 越界报错

# max min，针对可迭代对象，比如字符串，列表，比较规则是按字符串的字母顺序（ASCII/Unicode）
# a = [1, 2, 3] # 3
# print(max(a))
# b = ['1', '2', '3', 'a'] # a
# print(max(b))

a = [1, 2, 3]
# 这俩一个效果
print(a[-1])
print(a[len(a) - 1])


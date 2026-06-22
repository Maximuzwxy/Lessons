a = ['a', 'b', 'c']
# print(a[3])
# print(a[-3])
# print(len(a))
# print(a)

# 1. 遍历
# 2种遍历方法

# for i in a:
#     print(i)
#
# for i in range(len(a)):
#     print(i)
#     print(a[i])
#     print()

# for index, element in enumerate(a):
#     print(index, element)


# for i in a:
#     if '1' not in i:
#         print('ok')

# if '1' in a:
#     print('yes')

# 2. 构建一个空列表names，for循环5次，随机选出其中一人的名字并打印出来
# import random
#
# names = ['harry', 'hz', 'nx']
# for i in range(5):
#     index = random.randint(0, 2)
#     print(names[index])

# 增删改查读
names = ['harry', 'hz', 'nx']
# 增
# append
# names.append('teacher wang')
# print(names)
#
# # insert
# names.insert(0, 'Yamal')
# print(names)
#
# # extend
# lst = ['Jordan', 'Curry', 'James']
# names.extend(lst)
# print(names)
#
# # extend string
# s1 = 'abcdef'
# names.extend(s1)
# print(names)
#
# # 改
# names[1] = 'Harry'
# print(names)


# 创建一个空列表，通过for，input把3个名字加到列表里面，最后打印列表

# 3.
# names = []
# for i in range(3):
#     name = input('input name: ')
#     names.append(name)
# print(names)


# 4. 创建一个新的列表，把上面的列表中的元素，依次把名字前面增加一个序号和冒号，放到新的列表中，序号从1~3，输出结果是：['1:a', '2:b', '3:c']

# lst = []
# for i, v in enumerate(names):
#     lst.append(str(i + 1) + ':' + v)
# print(lst)



# 5. 写2个for循环，第一个for，输入5个整数，放到列表中，第二个for，对刚才列表中的数字求和，最后输出结果

# lst = []
# for i in range(5):
#     num = int(input('input int: '))
#     lst.append(num)
#
# # 方法一
# ret = 0
# for j in lst:
#     ret += j
# print(ret)
#
# # 方法二
# ret = 0
# for n in range(len(lst)):
#     ret += lst[n]
# print(ret)
#
# # 方法三
# # sum()
# print(sum(lst))

# 6. 合并列表
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 9, 8, 9, 0]

# extend
# print(lst1.extend(lst2))

# append
# for i in lst2:
#     lst1.append(i)
# print(lst1)

# +
# print(lst1 + lst2)

# Homework
# 创建一个10个0的列表

# lst = []
# for i in range(10):
#     lst.append(0)
# print(lst)

# 算出2出现的次数

# lst = [1, 2, 3, 1, 4, 2, 3, 2, 4, 5]
# num = 0
# for i in lst:
#     if i == 2:
#         num += 1
# print(num)

# 找出4的所有index

# lst = [2, 3, 2, 1, 4, 2, 3, 2, 4, 5]
# for i, v in enumerate(lst):
#     if v == 4:
#         print(i)

#lst = []
#for i in range(5):
#    num = int(input("请输入一个整数："))
#    lst.append(num)
#a = 0
#for i in range(len(lst)):
#    a += lst[i]
#print()


#lst = [1, 2, 3, 1, 4, 2, 3, 2, 4, 5]
#a = 0
#for num in lst:
#    if num == 2:
#        a += 1

#print(a)


#lst = [2, 3, 2, 1, 4, 2, 3, 2, 4, 5]

#for i in range(len(lst)):
#    if lst[i] == 4:
#        print(i)





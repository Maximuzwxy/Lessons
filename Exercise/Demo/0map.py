# map的作用是对可迭代对象（如列表、字符串等）中的每个元素应用一个函数，并返回一个新的可迭代对象
# map对象如果打印，会是：<map object at 0x000001C5C2C58850>
# 如果想打印出里面的内容，需要使用list转换一下，str不可以，打印出来还是map对象，或者通过for去打印map的迭代内容
# a = ['1', '2', '3']
# b = map(int, a)
# c = list(b)
# d = str(b)
# print(b)
# print(c)
# print(d)
# # 以下for无结果，因为b = map(int, a)，已经遍历了依次map a，map对象就会被耗尽，再遍历就是空的迭代器
# for i in b:
#     print(i)
# 因此，map要跟在list中使用最好

# upper在map中的使用，map的第一个参数，是一个函数引用，因此不带括号
# a = ['aaa', 'bbb', 'ccc']
# print(list(map(str.upper, a)))
# # 上面的IDE会有误报，可以换成lambda，就不会有了
# print(list(map(lambda x: x.upper(), a)))


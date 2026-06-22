# range返回一个可迭代对象，0~9
# a = range(10)
# print(list(a))
# # 因此，可以直接在可迭代对象的后面跟切片
# b = '12345'
# print(b[::-1])
# print(b[2:])
#
# c = [str(i) for i in range(10)]
# print(''.join(c))

# for range的逆序用法，输出53210
for i in range(5, -1, -1):
    print(i, end=' ')

# 但是slice，第二个stop，不能是-1，得为空，才能取到0号元素
a = [1, 2, 3, 4, 5]
print(a[4::-1])




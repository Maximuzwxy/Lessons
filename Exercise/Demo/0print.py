#print占位符:% f format
# %中间没有,
# name = 'maximuz'
# print('my name: %s' % name)
#
# my_id = 123
# print('my id is %d' %my_id)
#
# #如果多个参数，需要用元组，也不需要逗号分割
# #整数可以用%s，但是字符串不能%d，会报错
# print('my name is %s, my id is %d' %(name,my_id))
# print('my name is %s, my id is %6d' %(name,my_id))
# print('my name is %s, my id is %06d' %(name,my_id))
# print('my name is %s, my id is %2d' %(name,my_id))

# # float默认输出6位，如果超出6位，则四舍五入
# a = 1.61
# print('float is %d' %a)
# print('float is %f' %a)
# a = 1.2345678
# print('float is %f' %a)
# print('float is %3f' %a)
# print('float is %.3f' %a)
# print('float is %.10f%%' %a)

# a = 123
# b = 'bbb'
# print(f'a is {a}, b is {b}')

# print()打印会默认加一个换行符，readline会读到一个换行符，这样就有了2个换行符，所以会多一行，如果想少换行符，要用rstrip
with open('aa.txt', 'r') as f:
    print(f.readline())
    print(f.readline().rstrip())
    print(f.readline().rstrip())
# 或者用print(xxx, end='')来约束end的地方是啥，其实就是把print默认end加的\n，换成了end中的字符串
with open('aa.txt', 'r') as f:
    print(f.readline(), end='')
    print(f.readline(), end='1')
    print(f.readline(), end='\n')

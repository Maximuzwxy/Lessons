# input返回的是一个字符串
# a = input('input: ')
# print(a)
# print(type(a))

# a, b, c = map(int, input().split()) 这种写法叫“序列解包”或“多变量赋值”。
# 解释如下：
# map(int, input().split()) 返回一个可迭代对象（iterator），里面有多个元素（如 3 个整数）。
# a, b, c = ... 让这 3 个变量分别接收迭代对象里的 3 个值。
# Python 会自动把迭代对象拆开，依次赋值给左边的变量。
# a, b, c = map(int, input('input 3 number:').split())
# print(f'{a} {b} {c}')

# a, b, c = list(map(int, input('input 3 number:').split()))
# print(f'{a} {b} {c}')

# 如果abc个数不够，会怎样
# 解包时，变量数量必须和可迭代对象的元素数量完全一致，否则会抛出 ValueError
# ValueError: too many values to unpack (expected 2)
# a, b = list(map(int, input('input 3 number:').split()))
# print(f'{a} {b}')
# a, b = map(int, input('input 2 number:').split())
# print(f'{a} {b}')

# std.stdin，std.stdout
# import sys
# sys.stdin = open('aa.txt', 'r')
# print(input())

# sys.stdout = open('aa.txt', 'a')
# print(input())
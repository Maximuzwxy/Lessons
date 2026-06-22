# 观察for和while的一些区别
# for i in range(1, 11):
#     print(i)
#
# a = 0
# while a < 10:
#     a += 1
#     print(a)
# #
# a = 0
# while True:
#     a += 1
#     print(a)
#     if a > 9:
#         break

# 字符串
# a = '12345'
# for i in a:
#     print(i)
#
# for i in range(len(a)):
#     print(a[i])

# j = 0
# while j < len(a):
#     print(a[j])
#     j += 1

# 打印13579
# for i in range(1, 11, 2):
#     print(i)

# a = 1
# while a < 10:
#     print(a)
#     a += 2
# print('Done')

# a会不会变，试试
# for a in range(1, 10):
#     print(a)
#     a += 2
# print('Done')
#
# for a in range(1, 10):
#     a += 2
#     print(a)
# print('Done')

# 直角三角形
# height = int(input('input: '))
# row = 1
# while row <= height:
#     print('*' * row)
#     row += 1

# for i in range(1, height + 1):
#     print('*' * i)


# 打印1~10，但是能被3整除的不打印
# a = 0
# while a < 10:
#     a += 1
#     if a % 3 == 0:
#         continue
#     print(a)

# 找到能被3和7整除，且个位是5的数字
# a = 0
# while True:
#     a += 1
#     if a % 3 == 0 and a % 7 == 0 and a % 10 == 5:
#         print(a)
#         break
#
# a = 1
# while a % 3 != 0 or a % 7 != 0 or a % 10 != 5:
#     a += 1
# print(a)
#
# a = 0
# while not (a % 3 == 0 and a % 7 == 0 and a % 10 == 5):
#     a += 1
# print(a)

# 随机一个整数，如果不能被7整除，则继续随机一个整数，直到随机到能被7整除的数字，并且算出总共随机了几次
# import random
# total = 0
# while True:
#     a = random.randint(1, 100)
#     print(a)
#     total += 1
#     if a % 7 == 0:
#         break
# print('total:', total)

# 输入一个数字，如果>=0，则输出数字的平方，如果小于0，则退出
# while True:
#     number = input('input: ')
#     if int(number) < 0:
#         break
#     print(int(number) ** 2)

# 随机一个数字，你来猜，看看几次可以猜到
# import random
# a = random.randint(1, 100)
# total = 0
# # print(a)
# while True:
#     b = input('input a number: ')
#     c = int(b)
#     total += 1
#
#     if c == a:
#         print('you are right! exit')
#         print('total is ', total)
#         break
#     elif c < a:
#         print('please try a larger one')
#     else:
#         print('please try a smaller one')


# Homework
# while True:
#     a = int(input("Enter a number: "))
#     if a > 0:
#         print(a**2)
#     else:
#         print('exit')
#         break

# import random
# n = 0
# while True:
#     i = random.randint(1,100)
#     print(i)
#     n += 1
#     if i % 7 == 0:
#         print('using')
#         print(n)
#         print('times')
#         print('exit')
#         break


# Homework
# total = 0
# a = 1
# while True:
#     total += a
#     a += 1
#     if a > 100:
#         break
# print(total)

# while True:
#    user_input = input("请输入字符：")
#    if user_input == "exit":
#        print("退出程序。")
#        break
#    print(user_input)

# a = 0
# b = 0
# while True:
#     a += 1
#     b = a + b
#     if a == 100:
#         break
# print(b)

# while True:
#     a = input('printing:')
#     print(a)
#     if a == 'exit':
#         break
#
#
# while True:
#     a = input('GF')
#     print(a)
#     if a == exit:
#         break

# i = 5
# for i in range(5):
#     print(i)
# print(i)

# Homework
# while True:
#     num_input = input("请输入一个数字：")
#     num = int(num_input)
#     if num > 0:
#         print(num**2)
#     elif num < 0:
#         print('输入错误')
#         break
#     else:
#         print(' try another number')

# import random
#
# count = 0
# while True:
#     num = random.randint(1, 100)
#     count += 1
#     if num % 7 == 0:
#         break
#
# print("The number is:", num)
# print("time used:", count)
# def f(n):
#     if n == 0:
#         print(n)
#     else:
#         print(n)
#         f(n - 1)
#         print(n)
# f(10)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         print(n)
#         return factorial(n - 1) * n
# # print(factorial(5))
#
# def factorial2(n):
#     total = 1
#     for i in range(2, n + 1):
#         total *= i
#     return total
# # print(factorial2(5))

# def fibonacci(n):
#     print(n)
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(5))

# hanoi
# def hanoi(n, src, tmp, dest):
#     if n == 1:
#         print(n, src, '->', dest)
#         return
#
#     # print('1', n, src, '->', dest)
#     hanoi(n - 1, src, dest, tmp)
#     print(n, src, '->', dest)
#     hanoi(n - 1, tmp, src, dest)
#
# hanoi(4, 'src', 'tmp', 'dest')




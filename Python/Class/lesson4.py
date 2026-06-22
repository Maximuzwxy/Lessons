# total = 0
# for i in range(1, 101):
#     total += i
# print(total)



# for i in range(6):
#     print(i)

# for i in range(2, 6):
#     print(i)

# for i in range(1, 20, 3):
#     print(i)

# for i in range(10, -10, -3):
#     print(i)

# a = 'banana'
# for i in a:
#     print(i)
# print()
#
# for i in range(len(a)):
#     print(a[i])

# a = '0123456789'
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i])
#
# for i in range(0, len(a), 2):
#     print(a[i])

# for i in range(len(a) // 2):
#     print(a[i])

# for i in range(len(a)//2, len(a)):
#     print(a[i])

# for i in range(10, 100):
#     if 69 % i == 0:
#         print(i)
#         break

# # 从1~100，3的倍数，和数字里面带3的，都排除
# n = int(input('n:'))
# total = 0
# if 1 <= n <= 100:
#     for i in range(n + 1):
#         if i % 3 == 0:
#             continue
#         if '3' in str(i):
#             continue
#         print(i)

count = 0
for i in range(1, 101):
    if i % 2 == 0 and i % 5 != 0:
        print(i)
        count += 1
print(count)


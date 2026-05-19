# import time
# total = 0
# while True:
#     total += 1
#     time.sleep(1)
#     print(total)

# import random
# while True:
#     n = random.randint(1, 100)
#     print(n)
#
#     if n % 2 == 0 and n % 3 == 0:
#         break

# while True:
#     number = input('input: ')
#     if int(number) < 0:
#         break
#     print(int(number) ** 2)

# a = 1
# while a < 10:
#     print(a)
#     a += 1
# print("Done with while loop!")

# for i in range(1, 10):
#     i += 2
#     print(i)

# num = 1
# while not (num % 3 == 0 and num % 7 == 0 and num % 10 == 5):
#     num += 1
# print(num)
#
# num = 1
# while num % 3 != 0 or num % 7 != 0 or num % 10 != 5:
#     num += 1
# print(num)

# n = int(input('n: '))
# i = 1
# while i <= n:
#     print('*' * i)
#     i += 1



# import random
# a = random.randint(1, 100)
# total = 0
# print(a)
# upper = 100
# lower = 1
# while True:
#     guess = (upper + lower) // 2
#     total += 1
#
#     if guess == a:
#         print('right! exit')
#         print('total is ', total)
#         break
#     elif guess < a:
#         print(guess, 'try a larger one')
#         lower = guess + 1
#     else:
#         print(guess, 'try a smaller one')
#         upper = guess - 1


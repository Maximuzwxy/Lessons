# a = 1
# b = 'xyz'
# # c = input('input a integer: ')
# # print(a, b, c)
# print(a)
#
# a = 1
# print(a, type(a))
#
# d = 1.5
# e = a + d
# print(e, type(e))
#
# name = 'max'
# print(name, type(name))
#
# c = input('input a integer: ')
# print(c, type(c))
#
# c = int(c)
# print(c, type(c))



# day = input("Enter the day of the week: ")
#
# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend! Time to relax.")
# else:
#     print("It's a weekday. Back to study!")
#
#
# age = int(input("Enter your age: "))
#
# if age >= 13 and age <= 19:
#     print("You are a teenager.")
# else:
#     print("You are not a teenager.")


# a = input('A: ')
# b = input('B: ')
#
# if a == b:
#     print('tie')
# elif a == 'rock' and b == 'scissors':
#     print('a wins')
# elif a == 'scissors' and b == 'paper':
#     print('a wins')
# elif a == 'paper' and b == 'rock':
#     print('a wins')
# else:
#     print('a loses')
#
# a = input('A: ')
# b = input('B: ')
#
# if a == b:
#     print('tie')
# elif (a == 'rock' and b == 'scissors') or (a == 'scissors' and b == 'paper') or (a == 'paper' and b == 'rock'):
#     print('a win')
# else:
#     print('a lose')

# a = print(1)
# print(type(a))


# a = input('input a: ')
# print(a, type(a))
# a = int(a)
#
# b = input('input b: ')
# print(b)
# b = int(b)
#
# print(a + b)


# a = 10
# b = 11
#
# if not a > b:
#     print('11')
# else:
#     print('22')


# for i in range(5):
#     print(i)
#
# a = range(5)
# for i in a:
#     print(i)


# a = input('a: ')
# a = int(a)


n = int(input('n: '))
total = 0
counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
        counter += 1
print(counter, total)

n = int(input('n: '))
total = 1
for i in range(1, n + 1):
    total *= i
print(total)


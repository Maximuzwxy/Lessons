# print all the factors of a number
# num = int(input('n: '))
# i = 1
#
# while i <= num:
#     if num % i == 0:
#         print(i, end=' ')
#     i += 1

# Harmonic series(调和级数)
# Calculate the sum of a sequence in the form: 1, 1/2, 1/3, ..., 1/n
# Continuously increase the value of n until the sum of the sequence exceeds 5
# n = 0
# sums = 0
# while sums <= 5:
#     n += 1
#     sums += 1/n
# print(n, sums)


# Output all perfect square numbers up to n
# n = int(input('n: '))
#
# i = 1
# while i * i <= n:
#     print(i ** 2, end=' ')
#     i += 1


# the mount everest problem
# height = 1
# count = 0
#
# while height <= 8848000:
#     height *= 2
#     count += 1
# print(count, height)


# the falling ball problem
# height = 100
# n = 0
#
# while height >= 0.5:
#     height /= 2
#     n += 1
# print(n, height)


# number reversal
# origin = int(input('n: '))
# reversed_num = 0
#
# while origin > 0:
#     last_digit = origin % 10
#     reversed_num = reversed_num * 10 + last_digit
#     origin = origin // 10
# print(reversed_num)


# juice dilution
# count = 0
# cur = 100
# target = int(input('target: '))
#
# while cur > target:
#     count += 1
#     cur *= 0.9
#
# print(count, cur)


# cow eating grass problem
# grass = 100
# consume = 12
# grow = 5
# day = 0
#
# while True:
#     grass -= consume
#     if grass < 0:
#         break
#     grass += grow
#     day += 1
# print(day, grass + consume)




















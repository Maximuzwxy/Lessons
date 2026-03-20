# s = {'a', 'b', 'c'}
# print(s, type(s))
#
# s = {}
# print(s, type(s))
#
# t = ('a', 'b', 'c')
# s1 = set(t)
# print(s1)
# s2 = set('edf')
# print(s2)
# # print(s2[1])

# t1 = (1, 2, 3)
# t2 = ([1], [2])
# print(set(t1))
# print(set(t2))

# s = {1, 2, 1, 3}
# print(s)

# s = {'a', 'b', 'c'}
# for i in s:
#     print(i)

# set(1, 2)
# print({(1, 2, 3)})
# print({[1, 2, 3]})

# s = {'apple', 'banana', 'cherry'}
# s.add('orange')
# print(s)
#
# tropical = {'pineapple', 'mango', 'papaya'}
# s.update(tropical)
# print(s)
#
# # s.remove('aaa')
# s.discard('aaa')

# input_lst_chr = input().split()
# print(input_lst_chr)
#
# nums = list(map(int, input_lst_chr))
# print(nums)
#
# sorted_lst = sorted(list(set(nums)))
# print(sorted_lst)
#
# print(len(sorted_lst))
# print(' '.join(map(str, sorted_lst)))

# n = int(input())
# s = set()
# for i in range(n):
#     t = s.add(tuple(sorted(input())))
# print(len(s))


# s = input()
# print(s)
#
# ss = s.split()
# print(ss, type(ss))
#
# m = map(int, ss)
# print(m, type(m))
#
# # for i in m:
# #     print(i, type(i))
#
# lst = list(m)
# print(lst)

# l = ['a', 'b', 'c']
# s = ' '.join(l)
# print(s)

# n = int(input())
#
# types = set()
# for _ in range(n):
#     s = sorted(input())  # Return the sorted list
#     types.add(''.join(s))
#
# print(len(types))


# 1. Problem Description
# A school recorded the names of students who ate lunch in the cafeteria on two separate days.
# Duplicate names mean the same student ate multiple times.
#
# Do the following tasks:
# Find the unique students who ate on Day 1 and Day 2 separately
# Find students who ate on both days using only loops and in checks
# Sort these students alphabetically and print them
# Count how many students ate only on Day 1
#
# sample data
# day1 = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
# day2 = ["Bob", "David", "Eve", "Charlie", "Eve", "Frank"]
#
# output:
# Unique students on Day 1: ['Alice', 'Bob', 'Charlie', 'David']
# Unique students on Day 2: ['Bob', 'Charlie', 'David', 'Eve', 'Frank']
# Students who ate both days: ['Bob', 'Charlie', 'David']
# Number of students only on Day 1: 1

day1 = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
day2 = ["Bob", "David", "Eve", "Charlie", "Eve", "Frank"]

s1 = set(day1)
s2 = set(day2)
lst1 = []
lst2 = []

print(f'Unique on day 1: {list(s1)}')
print(f'Unique on day 2: {list(s2)}')

for i in s1:
    if i in s2:
        lst1.append(i)
print(f'both day: {lst1}')

for i in s1:
    if i not in s2:
        lst2.append(i)
print(f'only day1: {lst2} {len(lst2)}')

s3 = set(day1 + day2)
print('sort:', sorted(s3))


# 2. Problem Description
# Generate a list of 20 random integers (range: 1 to 9).
# Output the numbers that appear at least 2 times and their corresponding occurrence counts.
#
# sample random integers:
# [3, 5, 2, 3, 7, 8, 5, 9, 1, 3, 5, 7, 4, 8, 2, 5, 6, 7, 8, 8]
#
# output:
# 3 appears 3 times
# 5 appears 4 times
# 7 appears 3 times
# 8 appears 4 times
# 2 appears 2 times

import random
lst = [random.randint(1, 9) for _ in range(20)]
# lst = [3, 5, 2, 3, 7, 8, 5, 9, 1, 3, 5, 7, 4, 8, 2, 5, 6, 7, 8, 8]

print(lst)

s = set(lst)
for i in s:
    if lst.count(i) > 1:
        print(f'{i} appears {lst.count(i)} times')



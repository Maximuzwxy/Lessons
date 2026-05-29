import random

# a = 1
# print(id(a))
#
# a += 1
# print(id(a))

# def change(a):
#     print(id(a))
#
# a = 1
# print(id(a))
# change(a)

# def change_int(a):
#     a = 10
# a = 1
# change_int(a)
# print(a)
#
# def change_list(lst):
#     lst.append(5)
#
# lst = [1, 2, 3, 4]
# change_list(lst)
# print(lst)


# def change1(lst):
#     lst.append(0)
#     # lst = [10, 20, 30]
# l1 = [1, 2, 3]
# change1(l1)
# print(l1)
#
# def change2():
#     l1.append(5)
# change2()
# print(l1)

# total = 0
# def my_sum(a, b):
#     total = a + b
#     print('local variable is', total)
#     return total
# print(my_sum(2, 3))
# print('global variable is', total)

# total = 10
# def my_sum(a, b):
#     global total
#     total += a + b
#     # print('global variable is', total)
#     return total
# print(my_sum(2, 3))
# print('global variable is', total)

# total = 0
# def add(a):
#     global total
#     total += a
# add(12)
# print(total)

# def my_func(lst):
#     for i in lst:
#         print(i)
#
# fruit = ['apple', 'banana', 'cherry']
# my_func(fruit)

def my_min(array, start, end):
    min_index = start

    for i in range(start + 1, end):
        if array[i] < array[min_index]:
            min_index = i

    return min_index

lst = [random.randint(1, 100) for _ in range(10)]
print(lst)
print(my_min(lst, 0, len(lst)))

# selection sort
lst = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
print(lst)

for i in range(len(lst) - 1):
    min_index = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
print(lst)

for i in range(len(lst) - 1):
    min_index = my_min(lst, i, len(lst))
    lst[i], lst[min_index] = lst[min_index], lst[i]
print(lst)

# 在2个列表中找到第一个一样的数
l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8, 10, 5]

# use flag
# flag = False
# for i in l1:
#     for j in l2:
#         if i == j:
#             print(i)
#             flag = True
#             break
#     if flag:
#         break

# for-else
for i in l1:
    for j in l2:
        if i == j:
            print(i)
            break
    else:
        continue
    break

def find_match(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return i
    return None

print(find_match(l1, l2))


# total = 0  # Defined outside the function, this is a global variable
#
# # Create Function sum
# def sum(arg1, arg2):  # Parameters arg1 and arg2 are local variables.
#     # The function assigns a value to the variable 'total',
#     # where 'total' is a local variable.
#     total = arg1 + arg2
#     print("local variables : ", total)
#     return total
#
#
# # Call the sum function
# sum(10, 20)
# print("global variables : ", total)











































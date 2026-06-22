# nested for loop
# for i in range(3):
#     for j in range(3):
#         print(i, j)


# selection sort
# solution 1
# unsorted_list = [9, 3, 7, 6, 1, 10, 0]
# sorted_list = []
#
# for i in range(len(unsorted_list)):
#     min_index = 0
#     for j in range(i + 1, len(unsorted_list)):
#         if unsorted_list[j] < unsorted_list[min_index]:
#             min_index = j
#     sorted_list.append(unsorted_list.pop(min_index))
# print(sorted_list)

# solution 2
# lst = [9, 3, 7, 6, 1, 10, 0]
#
# n = len(lst)
# for i in range(n - 1):
#     min_index = i
#     for j in range(i + 1, n):
#         if lst[j] < lst[min_index]:
#             min_index = j
#     lst[i], lst[min_index] = lst[min_index], lst[i]
# print(lst)

# bubble sort
# lst = [9, 3, 7, 6, 1, 10, 0]
# for i in range(len(lst) - 1):
#     for j in range(len(lst) - 1 - i):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
# print(lst)




# homework
lst1 = [3, 6, 9, 10, 20]
lst2 = [2, 3, 6, 6, 8, 9, 10, 16, 18, 19, 20, 21, 25]
lst = []
print(len(lst1), len(lst2))



# solution 1
while lst1 and lst2:
    if lst1[0] < lst2[0]:
        lst.append(lst1.pop(0))
    else:
        lst.append(lst2.pop(0))
lst.extend(lst1)
lst.extend(lst2)

# solution 2
a, b = 0, 0
while a < len(lst1) and b < len(lst2):
    if lst1[a] < lst2[b]:
        lst.append(lst1[a])
        a += 1
    else:
        lst.append(lst2[b])
        b += 1
lst.extend(lst1[a:])
lst.extend(lst2[b:])
#
# print(lst)
# print(len(lst))

# lst = [[1, 2, 3],
#        [4, 5, 6]]
# print(lst)

# lst = []
# for i in range(2):
#     row = []
#     for j in range(3):
#        row.append(i * 3 + j + 1)
#     lst.append(row)
# print(lst)

# lst = [i for i in range(3)]
# lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
# print(lst)

# lst = [[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]]

# lst = []
# for i in range(5):
#     lst.append([0, 0, 0, 0, 0])

# lst = [0] + [0] + [0] + [0] + [0]
# lst = [0] * 5

# lst = []
# for i in range(5):
#     lst.append([0] * 5)

# lst = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(0)
#     lst.append(row)

# lst = [[0 for j in range(5)] for i in range(5)]
# lst = [[0] * 5 for i in range(5)]

# print(lst)

# lst = [[0] * 5] * 5
# print(lst)
# lst[0][0] = 99
# print(lst)
#
# for i in lst:
#     print(i, id(i))

# lst = []
# inner = [0] * 5
# for i in range(5):
#     lst.append(inner)
# lst[0][0] = 99
# print(lst)
#
# for i in range(5):
#     print(id(lst[i]))

# lst = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(i + 1)
#     lst.append(row)
# print(lst)

# lst = [[i + 1 for j in range(5)] for i in range(5)]
# print(lst)

# lst = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(j + 1)
#     lst.append(row)
# print(lst)

# lst = [[j + 1 for j in range(5)] for i in range(5)]
# print(lst)

# lst = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(j + i)
#     lst.append(row)
# print(lst)

# lst = [[i + j for j in range(5)] for i in range(5)]
# print(lst)

lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
print(lst)

# for row in lst:
#     print(row)
#     for element in row:
#         print(element, end=' ')
#     print()

# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j], end=' ')
#     print()

# for j in range(len(lst[0])):
#     for i in range(len(lst)):
#         print(lst[i][j], end=' ')
#     print()

# for i in range(len(lst) - 1, -1, -1):
#     for j in range(len(lst[i]) - 1, -1, -1):
#         print(lst[i][j], end=' ')

for i in lst[::-1]:
    for j in i[::-1]:
        print(j, end=' ')

# lst = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
# print(lst)
#
# for i in range(len(lst)):
#     if i % 2 == 0:
#         for j in range(len(lst[i])):
#             print(lst[i][j], end=' ')
#     else:
#         for j in range(len(lst[i]) - 1, -1, -1):
#             print(lst[i][j], end=' ')

# lst = [[1, 0, 1],
#        [0, 1, 1],
#        [1, 0, 1]]
# total = 0
# for i in lst:
#     for j in i:
#         total += j
# if total % 2 == 0:
#     print('even')
# else:
#     print('odd')

# lst = [[1, 0, 1],
#        [0, 1, 1],
#        [1, 1, 1]]
#
# for i in lst:
#     total = 0
#     for j in i:
#         total += j
#     if total % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# lst = [[1, 1, 1],
#        [1, 1, 0],
#        [1, 1, 1]]
#
# for j in range(len(lst[0])):
#     total = 0
#     for i in range(len(lst)):
#         total += lst[i][j]
#     if total % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# lst = [[2, 6, 5],
#        [1, 3, 7],
#        [5, 3, 5],
#        [1, 7, 12]]
#
# min_value = lst[0][0]
# max_value = lst[0][0]

# for i in lst:
#     for j in i:
#         if j > max_value:
#             max_value = j
#         elif j < min_value:
#             min_value = j
# print(max_value - min_value)

lst = [[1, 2, 3, 4],
       [5, 6, 5, 8],
       [9, 1, 11, 10],
       [13, 4, 5, 16]]
# for i in range(1, len(lst) - 1):
#     for j in range(1, len(lst[i]) - 1):
#         if lst[i][j] > lst[i - 1][j] \
#             and lst[i][j] > lst[i + 1][j] \
#             and lst[i][j] > lst[i][j - 1] \
#             and lst[i][j] > lst[i][j + 1]:
#             print(lst[i][j])

# lst = [1, 2]
# lst1 = lst
# lst1[0]  = 0
#
# print(lst)
# print(lst1)
# print(id(lst), id(lst1))



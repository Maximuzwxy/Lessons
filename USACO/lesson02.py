# lst = [[1, 2, 3], [4, 5, 6]]
# print(lst)
#
# lst = []
# for i in range(2):
#     row = []
#     for j in range(3):
#         row.append(i * 3 + j + 1)
#     lst.append(row)
# print(lst)
#
# lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
# print(lst)

# lst = [[1, 2, 3],
#        [4, 5, 6]]

# lst = [[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]]

# lst = []
# for _ in range(5):
#     row = []
#     for _ in range(5):
#         row.append(0)
#     lst.append(row)
# print(lst)
#
# lst = []
# for _ in range(5):
#     lst.append([0] * 5)
# print(lst)
#
# lst = [[0 for _ in range(5)] for _ in range(5)]
# print(lst)
#
# lst = [[0] * 5 for _ in range(5)]
# lst[0][0] = 99
# print(lst)

# lst = [[0] * 5] * 5
# lst[0][0] = 99
# print(lst)
#
# lst = []
# inner = [0] * 5
# for _ in range(5):
#     lst.append(inner)
# lst[0][0] = 99
# print(lst)

# lst = [[1, 2, 3], [4, 5, 6]]
# for row in lst[::-1]:
#     for element in row[::-1]:
#         print(element, end=' ')
# print()
#
# for i in range(len(lst) - 1, -1, -1):
#     for j in range(len(lst[i]) - 1, -1, -1):
#         print(lst[i][j], end=' ')

lst = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
# print(lst)

for i in range(5):
    for j in range(i, 5):
        print(lst[i][j], end=' ')
    print()

# for i in range(5):
#     for j in range(5):


#
# for i in range(5):
#     for j in range(i + 1):
#         print(lst[i][j], end=' ')
#     print()

# def reverse_matrix(matrix):
#     rows = matrix[::-1]
#     for i in range(len(rows)):
#         rows[i] = rows[i][::-1]
#     return rows

# def reverse_matrix(matrix):
#     return [row[::-1] for row in matrix[::-1]]

# def reverse_matrix(matrix):
#     rows = matrix[::-1]
#     for row in rows:
#         row.reverse()
#     return rows

# def reverse_matrix(matrix):
#     rows = matrix[::-1]
#     for row in rows:
#         for i in range(len(row) // 2):
#             row[i], row[len(row) - 1 - i] = row[len(row) - 1 - i], row[i]
#     return rows
#
#
# matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
# print(matrix)
# print(reverse_matrix(matrix))

# def rotate(matrix):
#     n = len(matrix)
#     ret = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             ret[j][n - 1 - i] = matrix[i][j]
#     return ret

# def rotate(matrix):
#     n = len(matrix)
#     for i in range(n // 2):
#         for j in range(i, n - 1 - i):
#             tmp = matrix[i][j]
#             matrix[i][j] = matrix[n - 1 - j][i]
#             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
#             matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
#             matrix[j][n - 1 - i] = tmp
#     return matrix

# def rotate(matrix):
#     n = len(matrix)
#     ret = matrix[::-1]
#     for i in range(n):
#         for j in range(i, n):
#             ret[i][j], ret[j][i] = ret[j][i], ret[i][j]
#     return ret

# def rotate(matrix):
#     n = len(matrix)
#
#     for i in range(n // 2):
#         matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
#
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     return matrix
#
#
# def print_rotate(matrix):
#     for i in matrix:
#         print(i)
#
# dim = 5
# matrix = [[i * dim + j + 1 for j in range(dim)] for i in range(dim)]
# print_rotate(rotate(matrix))

# for i in [0, 1, 2]:
#     print(i)
#
# for i in range([0,1,2]):
#     print(i)

# a = range(3)
# print(type(a), a)

# for i in a:
#     print(i)

# for i in range(3):
#     print(i)

# lst1 = [1, 2, 3]
# lst2 = lst1
# lst2[0] = 99
# print(lst1)
# print(lst2)

# a = [1, 2, [3, 4, 5]]
# print(a[1])

# for i in a:
#     print(i)

# n = len(a)
# print(n)
# for i in range(len(a)):
#     # print(i)
#     print(a[i])

# print(a[6])



# lst = [[1, 2, 3], [4, 5, 6]]
# for row in lst:
#     for item in row:
#         print(item)



# lst=[]
# for i in range(5):
#     rows=[]
#     for j in range(5):
#         rows.append(i*5+j+1)
#     lst.append(rows)
# print(lst)
#
# def rotatematrix(matrix):
#     n=len(matrix)
#     matrix1=[[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             matrix1[j][n-i-1]=matrix[i][j]
#     return matrix1
# print(rotatematrix(lst))


lst = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(i * 5 + j + 1)
    lst.append(row)
print(lst)

l = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
print(l)














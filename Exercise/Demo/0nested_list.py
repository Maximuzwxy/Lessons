# a = [1, 2, 3], [4, 5, 6]
# print(a)

# lst = []
# num = 0
# for i in range(2):
#     row = []
#     for j in range(3):
#         num += 1
#         row.append(num)
#     lst.append(row)
# print(lst)

# lst = []
# for i in range(2):
#     row = []
#     for j in range(3):
#         row.append(i * 3 + j + 1)
#     lst.append(row)
# print(lst)

# 列表推导式
# lst = [[(i * 3 + j + 1) for j in range(3)] for i in range(2)]
# print(lst)
#
# for i in range(2):
#     for j in range(3):
#         lst[i][j] += 1
#         print(lst[i][j])

# lst = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(0)
#     lst.append(row)
# print(lst)

# lst = []
# for i in range(5):
#     lst.append([0] * 5)
# print(lst)

# lst = [[0 for j in range(5)] for i in range(5)]
# print(lst)

# lst = [[0] * 5 for i in range(5)]
# print(lst)

# a = [0] * 5
# print(a)
# a[0] = 1
# print(a)
# # 这样写得到的是一个25个元素的列表，而非二维列表
# # b = a * 5
# # 应该这样写：
# b = [a] * 5
# print(b)
# a[0] = 2
# print(b)
#
# # 这样写也不行
# c = [a for _ in range(5)]
# print(c)
# c[0][0] = 3
# print(c)
#
# # 这样才可以
# d = [[0] * 5 for _ in range(5)]
# print(d)
# d[0][0] = 4
# print(d)

# # 这样也是错的
# a = []
# b = [0] * 5
# for _ in range(5):
#     a.append(b)
# a[0][0] = 2
# print(a)

# 遍历
# lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
# print(lst)

# for i in lst:
#     for j in i:
#         print(j)
#
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j])

# for i in range(len(lst) - 1, -1, -1):
#     for j in range(len(lst[i]) - 1, -1, -1):
#         print(lst[i][j])
#
# for i in range(len(lst))[::-1]:
#     for j in range(len(lst[i]))[::-1]:
#         print(lst[i][j])

# 生成一个5*5的列表，从1~25
lst = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
print(lst)

cursor = 0
for i in lst:
    for j in i[cursor:]:
        print(j, end=' ')
    cursor += 1
    print()

for i in range(len(lst)):
    for j in range(i, len(lst[i])):
        print(lst[i][j], end=' ')
    print()

for i in range(len(lst)):
    for j in range(0, i + 1):
        print(lst[i][j], end=' ')
    print()


def rotate_matrix(n):
    matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    print(matrix)

    # 方法一：位置映射，通过临时二维列表来实现
    # ret = [[0] * n for _ in range(n)]
    #
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         ret[j][len(matrix) - i - 1] = matrix[i][j]
    #
    # for x in ret:
    #     print(x)

    # # 方法二：环形旋转
    # for i in range(len(matrix) // 2):
    #     m = len(matrix[i])
    #     for j in range(i, m - 1 - i):
    #         tmp = matrix[i][j]
    #         matrix[i][j] = matrix[m - j - 1][i]
    #         matrix[m - j - 1][i] = matrix[m - i - 1][m - j - 1]
    #         matrix[m - i - 1][m - j - 1] = matrix[j][m - i - 1]
    #         matrix[j][m - i - 1] = tmp
    #
    # for x in matrix:
    #     print(x)

    # 先倒序，再转置
    m = len(matrix)

    # 1. 切片倒置
    # matrix = matrix[::-1]

    # 2.原地倒置
    for i in range(m // 2):
        matrix[i], matrix[m - 1 - i] = matrix[m - 1 - i], matrix[i]

    # for i in range()
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for x in matrix:
        print(x)

# rotate_matrix(5)

# 按列遍历二维列表
def list_list():
    lst = [[i * 3 + j + 1 for j in range(3)] for i in range(2)]
    print(lst)

    # for j in range(len(lst[0])):
    #     for i in range(len(lst)):
    #         print(lst[i][j])

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j])

    print()

    # 逆序
    for i in range(len(lst) - 1, -1, -1):
        for j in range(len(lst[0]) - 1, -1, -1):
            print(lst[i][j])


list_list()



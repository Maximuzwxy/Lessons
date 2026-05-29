# n = 9
# data = [[0, 1], [0, 2], [0, 8],
#         [1, 2], [2, 4], [2, 5],
#         [3, 4], [3, 7], [3, 8],
#         [4, 7], [5, 6]]
#
# matrix = [[0 for _ in range(n)] for _ in range(n)]
#
# for i, j in data:
#     matrix[i][j] = 1
#     matrix[j][i] = 1
#
# for _ in matrix:
#     print(_)

# n = 6
# data = [[0, 4], [1, 0], [1, 2],
#         [1, 3], [2, 1], [3, 4],
#         [4, 1], [4, 5], [5, 4]]
#
# matrix = [[0 for _ in range(n)] for _ in range(n)]
#
# for i, j in data:
#     matrix[i][j] = 1
#
# for _ in matrix:
#     print(_)

# {0: [1, 2, 8], 1: [0, 2], 2: [0, 1, 4, 5], 3: [4, 7, 8], 4: [2, 3, 7], 5: [2, 6], 6: [5], 7: [3, 4], 8: [0, 3]}

# n = 9
# data = [[0, 1], [0, 2], [0, 8],
#         [1, 2], [2, 4], [2, 5],
#         [3, 4], [3, 7], [3, 8],
#         [4, 7], [5, 6]]
#
# d = {i:[] for i in range(n)}
#
# for i, j in data:
#     d[i].append(j)
#     d[j].append(i)
#
# for k, v in d.items():
#     print(k, v)

# n = 6
# data = [[0, 4], [1, 0], [1, 2],
#         [1, 3], [2, 1], [3, 4],
#         [4, 1], [4, 5], [5, 4]]
#
# d = {i:[] for i in range(n)}
#
# for i, j in data:
#     d[i].append(j)
#
# for k, v in d.items():
#     print(k, v)




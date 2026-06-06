# data = [[0, 1], [0, 3], [1, 2],
#         [3, 4], [3, 6], [4, 5],
#         [4, 8], [6, 7], [8, 9]]
#
# path = []
# flag = False
#
# def find_path(p):
#     global flag
#     print(p)
#     path.append(p)
#
#     if p[1] == 5:
#         print(path)
#         flag = True
#         return
#     else:
#         for d in data:
#             if p[1] == d[0]:
#                 find_path(d)
#                 if flag:
#                     return
#         else:
#             path.pop()
#
# for pp in data:
#     if pp[0] == 0:
#         find_path(pp)
#
# f = []
# for x in path:
#     if x[0] not in f:
#         f.append(x[0])
#     if x[1] not in f:
#         f.append(x[1])
# print(f)

n = 10
data = [[0, 1], [0, 3], [1, 2],
        [3, 4], [3, 6], [4, 5],
        [4, 8], [6, 7], [8, 9]]

d = {i:[] for i in range(10)}

for i, j in data:
    d[i].append(j)
    d[j].append(i)
print(d)

visited = [0] * n
path = []

def find_path(graph, start, end):
    path.append(start)

    if start == end:
        return True

    visited[start] = 1

    for neighbour in graph[start]:
        if visited[neighbour] == 0:
            if find_path(graph, neighbour, end):
                return True

    path.pop()
    return False

find_path(d, 0, 9)
print(path)
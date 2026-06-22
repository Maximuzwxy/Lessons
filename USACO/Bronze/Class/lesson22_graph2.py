# DFS
# n = 10
# data = [[0, 1], [0, 3], [1, 2],
#         [3, 4], [3, 6], [4, 5],
#         [4, 8], [6, 7], [8, 9]]
#
# d = {i:[] for i in range(10)}
#
# for i, j in data:
#     d[i].append(j)
#     d[j].append(i)
# print(d)
#
# visited = [0] * n
# path = []
#
# def find_path(graph, start, end):
#     path.append(start)
#
#     if start == end:
#         return True
#
#     visited[start] = 1
#
#     for neighbour in graph[start]:
#         if visited[neighbour] == 0:
#             if find_path(graph, neighbour, end):
#                 return True
#
#     path.pop()
#     return False

# find_path(d, 0, 9)
# print(path)

# connet = True
# for i in range(1, n):
#     visited = [0] * n
#     path = []
#     if not find_path(d, 0, i):
#         connet = False
#         print(i)
#         break
#
# print(connet)


# BFS
# n = 10
# data = [[0, 1], [0, 3], [1, 2],
#         [3, 4], [3, 6], [4, 5],
#         [4, 8], [6, 7], [8, 9]]
#
# d = {i:[] for i in range(10)}
#
# for i, j in data:
#     d[i].append(j)
#     d[j].append(i)
# print(d)
#
# visited = [0] * n
# path = []
#
# def bfs(g, start):
#     queue = [start]
#     visited[start] = 1
#     cnt = 1
#     while queue:
#         head = queue.pop(0)
#         path.append(head)
#
#         for neighbour in g[head]:
#             if visited[neighbour] == 0:
#                 visited[neighbour] = 1
#                 queue.append(neighbour)
#                 # print(neighbour)
#                 # print(queue)
#                 cnt += 1
#
#     # print(cnt)
#     return cnt == n

# if bfs(d, 0):
#     print(True)
#     print(path)

# 用bfs判断连通分量
# n = 10
# data1 = [[0, 1], [0, 3], [1, 2],
#          [4, 5], [4, 8], [6, 7],
#          [8, 9]]
#
# dd = {i:[] for i in range(10)}
#
# for i, j in data1:
#     dd[i].append(j)
#     dd[j].append(i)
# print(dd)
#
# v = [0] * n
# connect = 0
# path.clear()
#
# for i in range(n):
#     if i not in path:
#         connect += 1
#         bfs(dd, i)
#
# print(connect)


n = 10
data = [[0, 1], [0, 3], [1, 2],
         [4, 5], [4, 8], [6, 7],
         [8, 9]]

d = {i:[] for i in range(10)}

for i, j in data:
    d[i].append(j)
    d[j].append(i)
print(d)

def connect(g, v, start):
    v[start] = 1

    for neighbour in g[start]:
        if v[neighbour] == 0:
            connect(g, v, neighbour)

cnt = 0
v = [0] * n
for i in range(n):
    if v[i] == 0:
        cnt += 1
        connect(d, v, i)
print(cnt)

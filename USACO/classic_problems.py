# Triangle
# n = 8
# triangle = []
#
# for i in range(n):
#     row = [1]
#     for j in range(1, i):
#         row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
#     if i != 0:
#         row.append(1)
#
#     triangle.append(row)
#
# for k in triangle:
#     print(k)
#
# for x in range(len(triangle)):
#     for y in range(n - 1 - x):
#         print(' ', end='')
#     print(' '.join(map(str, triangle[x])))
from typing import List


# Maze
# maze = [[0 for j in range(3)] for i in range(3)]
# maze[1][1] = 1
# print(maze)
#
# path = []
# total = []
# m = len(maze)
# n = len(maze[0])
#
# def dfs(g, start, end):
#     path.append(start)
#     flag = False
#     # print(path)
#
#
#
#     if start == end:
#         total.append(path.copy())
#         return True
#
#     down = (start[0] + 1, start[1])
#     if down[0] < m and maze[down[0]][down[1]] != 1:
#         if dfs(g, down, end):
#             flag = True
#             path.pop()
#
#     right = (start[0], start[1] + 1)
#     if right[1] < n and maze[right[0]][right[1]] != 1:
#         if dfs(g, right, end):
#             flag = True
#             path.pop()
#
#     if flag:
#         return True
#     else:
#         path.pop()
#         return False
#
# dfs(maze, (0, 0), (m - 1, n - 1))
#
# print()
# for i in total:
#     print(i)
#
# maze = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
# maze = [[0 for j in range(3)] for i in range(3)]
# maze[1][1] = 1
# m = len(maze)
# n = len(maze[0])
# record = [[0 for j in range(n)] for i in range(m)]
#
# def dfs(g, r, c):
#     if r >= m or c >= n or g[r][c] == 1:
#         return 0
#
#     if r == m - 1 and c == n - 1:
#         return 1
#
#     if record[r][c] >= 1:
#         return record[r][c]
#
#     record[r][c] = dfs(g, r + 1, c) + dfs(g, r, c + 1)
#
#     return record[r][c]
#
# print(dfs(maze, 0, 0))
# for i in record:
#     print(i)

# 8 Queens
# import copy
# board = [['.'] * 8 for _ in range(8)]
# res = []
#
# def valid(r, c):
#     for i in range(8):
#         if board[r][i] == 'Q':
#             return False
#
#     for j in range(8):
#         if board[j][c] == 'Q':
#             return False
#
#     x = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
#
#     for a, b in x:
#         rr = r
#         cc = c
#         rr += a
#         cc += b
#         while 0 <= rr < 8 and 0 <= cc < 8:
#             if board[rr][cc] == 'Q':
#                 return False
#             rr += a
#             cc += b
#
#     return True
#
#
# def dfs(row):
#     if row == 8:
#         res.append(copy.deepcopy(board))
#         # print(board)
#         return
#
#     for column in range(8):
#         if valid(row, column):
#             board[row][column] = 'Q'
#             dfs(row + 1)
#             board[row][column] = '.'
#
# dfs(0)
# print(len(res))
# for s in res[4]:
#     print(s)

# 8 queens & compress 2d list to 1d list
# def valid(b, r, c):
#     for i in range(r):
#         if b[i] == c:
#             return False
#
#         if abs(r - i) == abs(c - b[i]):
#             return False
#
#     return True
#
# def gen_res(b, n):
#     lst = []
#     for i in range(n):
#         s = ''
#         for j in range(n):
#             if j == b[i]:
#                 s += 'Q'
#             else:
#                 s += '.'
#         lst.append(s)
#
#     return lst
#
# def dfs(l, b, n, r):
#     if r == n:
#         l.append(gen_res(b, n))
#         return 1
#
#     cnt = 0
#
#     for c in range(n):
#         if valid(b, r, c):
#             b[r] = c
#             cnt += dfs(l, b, n, r + 1)
#
#     return cnt
#
# N = 4
# board = [0] * N
# res = []
# m = dfs(res, board, N, 0)
# print(m)
# print(res)












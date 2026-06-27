import sys

# sys.stdin = open('hoofball.in', 'r')
# sys.stdout = open('hoofball.out', 'w')

n = int(input())
line = list(map(int, input().split()))
line.sort()
print(line)
hold = [0] * n

res = []

def kick(l, start, path):
    p = start
    ll = [line[p]]

    while True:
        l[p] = 1

        if p == 0:
            if l[1] == 1:
                break
            else:
                p += 1
        elif p == n - 1:
            if l[p - 1] == 1:
                break
            else:
                p -= 1
        else:
            if l[p + 1] - l[p] < l[p] - l[p - 1]:
                p += 1
            else:
                p -= 1

            if l[p] == 1:
                break
        ll.append(line[p])
        path.append(ll)

def dfs(h, l):
    print(h)
    if sum(h) == n:
        res.append(l.copy())
        return

    for j in h:
        kick(h, j, l)
        dfs(h.copy(), l)

dfs(hold, [])
print(res)




# aaa = []
# for i in range(n - 1):
#     aaa.append(line[i + 1] - line[i])
# print(aaa)

# cnt = n
# for i in res:
#     cnt = min(cnt, len(i))
# print(cnt)

# def forth(lst, start, end):
#     ll = [line[start]]
#     while start < end:
#         if start == 0:
#             start += 1
#             ll.append(line[start])
#         # elif start == end:
#         #     # if ll[-1] != start:
#         #     #     ll.append(start)
#         #     break
#         elif line[start] - line[start - 1] > line[start + 1] - line[start]:
#             start += 1
#             ll.append(line[start])
#         else:
#             break
#
#     lst.append(ll)
#     return start
#
# def back(lst, start, end):
#     ll = [line[end]]
#     while start < end:
#         if end == n - 1:
#             end -= 1
#             ll.append(line[end])
#         # elif end == start:
#         #     # if ll[0] != end:
#         #     #     ll.append(end)
#         #     break
#         elif line[end] - line[end - 1] < line[end + 1] - line[end]:
#             end -= 1
#             ll.append(line[end])
#         else:
#             break
#
#     lst.append(ll)
#     return end
#
# def dfs(l, s, e):
#     if s > e:
#         res.append(l.copy())
#         # print(res[-1])
#         # print()
#         return
#     # print('forth', s, e)
#     a = forth(l, s, e)
#     dfs(l, a + 1, e)
#     l.pop()
#
#     if a != e:
#         # print('back', s, e)
#         b = back(l, s, e)
#         dfs(l, s, b - 1)
#         l.pop()
#
# dfs([], 0, n - 1)
# # for _ in res:
# #     print(_)
#
# aaa = []
# for i in range(n - 1):
#     aaa.append(line[i + 1] - line[i])
# print(aaa)
#
# cnt = n
# for i in res:
#     cnt = min(cnt, len(i))
# print(cnt)




# while start > end:
#     if hold[start] == 0:
#         hold[start] = 1
#
#         if start == 0:
#             start += 1
#         elif start == n - 1:
#             cnt += 1
#             break
#         else:
#             if line[start + 1] - line[start] < line[start] - line[start - 1]:
#                 start += 1
#             else:
#                 cnt += 1
#
#     if hold[end] == 0:
#         hold[end] = 1
#
#         if end == n - 1:
#             end -= 1
#         else:




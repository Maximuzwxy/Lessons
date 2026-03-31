# USACO 2018 US Open Contest, Bronze
# Problem 1. Team Tic Tac Toe
# https://usaco.org/index.php?page=viewproblem2&cpid=831

# solution 1
# def win1(ch):
#     for i in range(3):
#         if ch == m[0][i] and ch == m[1][i] and ch == m[2][i]:
#             return 1
#
#     for i in range(3):
#         if ch == m[i][0] and ch == m[i][1] and ch == m[i][2]:
#             return 1
#
#     if ch == m[0][0] and ch == m[1][1] and ch == m[2][2]:
#         return 1
#
#     if ch == m[0][2] and ch == m[1][1] and ch == m[2][0]:
#         return 1
#
#     return 0
#
# def win_team(ch1, ch2):
#     set2 = set(ch1 + ch2)
#
#     for i in range(3):
#         set1 = set(m[i][0] + m[i][1] + m[i][2])
#         if set1 == set2:
#             return 1
#
#     for i in range(3):
#         set1 = set(m[0][i] + m[1][i] + m[2][i])
#         if set1 == set2:
#             return 1
#
#     set1 = set(m[0][0] + m[1][1] + m[2][2])
#     if set1 == set2:
#         return 1
#
#     set1 = set(m[0][2] + m[1][1] + m[2][0])
#     if set1 == set2:
#         return 1
#
#     return 0
#
# m = []
# chars = [chr(ord('A') + i) for i in range(26)]
#
# try:
#     with open('tttt.in', 'r') as f:
#         for _ in range(3):
#             m.append(list(f.readline().strip()))
# except FileNotFoundError:
#     for _ in range(3):
#         m.append(list(input().strip()))
#
# # print(m)
# # print(chars)
#
# w_1 = 0
# w_t = 0
#
# for x in chars:
#     w_1 += win1(x)
#
# for i in range(len(chars) - 1):
#     for j in range(i + 1, len(chars)):
#         w_t += win_team(chars[i], chars[j])
#
# with open('tttt.out', 'w') as f:
#     f.write(f'{w_1}\n{w_t}')
# print(f'{w_1}\n{w_t}')


# solution 2
def win1():
    s = set()
    for i in range(3):
        if m[0][i] == m[1][i] == m[2][i]:
            s.add(m[0][i])

    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2]:
            s.add(m[i][0])

    if m[0][0] == m[1][1] == m[2][2]:
        s.add(m[1][1])

    if m[0][2] == m[1][1] == m[2][0]:
        s.add(m[1][1])

    return len(s)

def win_team():
    s_t = set()
    for i in range(3):
        s = set(m[i][0] + m[i][1] + m[i][2])
        if len(s) == 2:
            s_t.add(''.join(sorted(s)))

    for i in range(3):
        s = set(sorted(m[0][i] + m[1][i] + m[2][i]))
        if len(s) == 2:
            s_t.add(''.join(sorted(s)))

    s = set(sorted(m[0][0] + m[1][1] + m[2][2]))
    if len(s) == 2:
        s_t.add(''.join(sorted(s)))

    s = set(sorted(m[2][0] + m[1][1] + m[0][2]))
    if len(s) == 2:
        s_t.add(''.join(sorted(s)))

    return len(s_t)

m = []
chars = [chr(ord('A') + i) for i in range(26)]

try:
    with open('tttt.in', 'r') as f:
        for _ in range(3):
            m.append(list(f.readline().strip()))
except FileNotFoundError:
    for _ in range(3):
        m.append(list(input().strip()))

# print(m)
# print(chars)

with open('tttt.out', 'w') as f:
    f.write(f'{win1()}\n{win_team()}')
print(f'{win1()}\n{win_team()}')


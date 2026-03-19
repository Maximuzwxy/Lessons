# s = {'a', 'b', 'c'}
# print(s, type(s))
#
# s = {}
# print(s, type(s))
#
# t = ('a', 'b', 'c')
# s1 = set(t)
# print(s1)
# s2 = set('edf')
# print(s2)
# # print(s2[1])

# t1 = (1, 2, 3)
# t2 = ([1], [2])
# print(set(t1))
# print(set(t2))

# s = {1, 2, 1, 3}
# print(s)

# s = {'a', 'b', 'c'}
# for i in s:
#     print(i)

# set(1, 2)
# print({(1, 2, 3)})
# print({[1, 2, 3]})

# s = {'apple', 'banana', 'cherry'}
# s.add('orange')
# print(s)
#
# tropical = {'pineapple', 'mango', 'papaya'}
# s.update(tropical)
# print(s)
#
# # s.remove('aaa')
# s.discard('aaa')

# input_lst_chr = input().split()
# print(input_lst_chr)
#
# nums = list(map(int, input_lst_chr))
# print(nums)
#
# sorted_lst = sorted(list(set(nums)))
# print(sorted_lst)
#
# print(len(sorted_lst))
# print(' '.join(map(str, sorted_lst)))

# n = int(input())
# s = set()
# for i in range(n):
#     t = s.add(tuple(sorted(input())))
# print(len(s))

# union
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A | B)
# print(A.union(B))
# print(B.union(A))

# intersection
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A & B)
# print(A.intersection(B))
# print(B.intersection(A))

# difference
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A - B)
# print(A.difference(B))
#
# print(B - A)
# print(B.difference(A))

# symmetric_difference
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A ^ B)
# print(A.symmetric_difference(B))
# print(B.symmetric_difference(A))


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

def union(A, B):
    R = set(A)
    for e in B:
        R.add(e)
    return R

def intersection(A, B):
    R = set()
    for e in A:
        if e in B:
            R.add(e)
    return R

def difference(A, B):
    R = set(A)
    for e in B:
        if e in A:
            R.remove(e)
    return R

def symmetric_difference(A, B):
    R = set()
    for e in A:
        if e not in B:
            R.add(e)

    for e in B:
        if e not in A:
            R.add(e)

    return R

# print(union(A, B))
# print(intersection(A, B))
# print(difference(A, B))
# print(symmetric_difference(A, B))

# s = input()
# print(s)
#
# ss = s.split()
# print(ss, type(ss))
#
# m = map(int, ss)
# print(m, type(m))
#
# # for i in m:
# #     print(i, type(i))
#
# lst = list(m)
# print(lst)

# l = ['a', 'b', 'c']
# s = ' '.join(l)
# print(s)

n = int(input())

types = set()
for _ in range(n):
    s = sorted(input())  # Return the sorted list
    types.add(''.join(s))

print(len(types))



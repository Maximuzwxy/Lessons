# 1. Input any number of digits in one line via input(), separated by spaces.
# 2. Store these digits in a list.
# 3. Multiply each digit in the list by 2.
# 4. Output the digits in the list in one line, separated by spaces.

l1 = input().split()
print(l1)

# for i in range(len(l1)):
#     l1[i] = int(l1[i])
# print(l1)

l2 = []
for i in l1:
    l2.append(int(i))
print(l2)

# s = input('input integers: ')
# lst = s.split()
# print(lst)
# lst1 = []
# for i in lst:
#     lst1.append(int(i) * 2)
# print(lst1)
#
# for i in range(len(lst1)):
#     lst1[i] = str(lst1[i])
# print(lst1)
#
# sep = ' '
# s1 = sep.join(lst1)
# print(s1)

#####################

lst = list(map(int, input('input integers: ').split()))
print(lst)
lst1 = [str(i * 2) for i in lst]
print('_'.join(lst1))



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


# solution 1
# def win1(ch, m):
#     pass
#
# def win_team(ch1, ch2, m):
#     pass
#
# # m = [['' for _ in range(3)] for _ in range(3)]
# m = []
#
# for i in range(3):
#     m.append(list(input()))
#
# print(m)

# s = set('AB')
# print(''.join(s))
#
# s = 'ABBA'
# print(sorted(s))

# s = {'A', 'B'}
# print(str(s))

# lst = [1.8, 2, 3]
# a = list(map(str, lst))
# print(list(a))

# a = 'Austin'
# a = {1, 2, 3}
# b = list(a)
# print(b)


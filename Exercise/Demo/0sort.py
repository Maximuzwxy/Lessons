import random

# 选择排序
unsorted_list = random.sample(range(10), 10)
# print(unsorted_list)
n = len(unsorted_list)

def fun1():
    sorted_list = []
    for i in range(n):
        min_index = 0
        for j in range(1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        sorted_list.append(unsorted_list.pop(min_index))

    print(sorted_list)

def fun2():
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

    print(unsorted_list)


# fun1()
# fun2()

# Bubble sort
def fun3():
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

    print(unsorted_list)

# fun3()

# unsorted_list.sort()
# unsorted_list.sort(reverse=True)
# print(unsorted_list)
# print(sorted(unsorted_list))
# print(sorted(unsorted_list, reverse=True))

# 归并排序merge
def merge_sorted_list():
    lst1 = random.sample(range(20), 5)
    lst2 = random.sample(range(20), 10)
    lst1.sort()
    lst2.sort()
    print(lst1)
    print(lst2)
    print(lst1 + lst2)

    len1 = len(lst1)
    len2 = len(lst2)

    total_len = len1 + len2
    a, b = 0, 0

    ret = []

    for i in range(total_len):
        if lst1[a] <= lst2[b]:
            ret.append(lst1[a])
            a += 1
        else:
            ret.append(lst2[b])
            b += 1

        if a == len1:
            ret.extend(lst2[b:])
            break

        if b == len2:
            ret.extend(lst1[a:])
            break

    print(ret)

# merge_sorted_list()

def merge_sorted_list2():
    lst1 = random.sample(range(20), 5)
    lst2 = random.sample(range(20), 10)
    lst1.sort()
    lst2.sort()
    print(lst1)
    print(lst2)
    print(lst1 + lst2)

    len1 = len(lst1)
    len2 = len(lst2)

    a, b = 0, 0

    ret = []

    while a < len1 and b < len2:
        if lst1[a] <= lst2[b]:
            ret.append(lst1[a])
            a += 1
        else:
            ret.append(lst2[b])
            b += 1

    ret.extend(lst1[a:])
    ret.extend(lst2[b:])

    print(ret)

merge_sorted_list2()






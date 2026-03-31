############################################
# Selection Sort
nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
print(nums)
n = len(nums)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
print(nums)

############################################

# Buble Sort
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

for i in range(n - 1):
    flag = True
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            flag = False
    if flag:
        break
print(nums)

############################################

# Insertion Sort
for i in range(1, n):
    target = nums[i]
    j = i - 1

    while j >= 0 and target < nums[j]:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = target
print(nums)


# 给定2个已经排好序的列表：
# lst1 = [3, 6, 9, 10, 20]
# lst2 = [2, 3, 6, 6, 8, 9, 10, 16, 18, 19, 20, 21, 25]
# 使用while循环，将2个列表中的元素放到一个新的列表lst中并且排序







# for i in range(n - 1):
#     min_index = i
#     for j in range(i + 1, n):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     nums[i], nums[min_index] = nums[min_index], nums[i]
# print(nums)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

# for i in range(n - 1):
#     flag = True
#     for j in range(n - 1 - i):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             flag = False
#
#     if flag:
#         break
#
# print(nums)

for i in range(1, n):
    target = nums[i]
    j = i - 1

    while j >= 0 and target < nums[j]:
        nums[j + 1] = nums[j]
        j -= 1

    j += 1

    nums[j] = target

print(nums)














# for i in range(1, n):
#     target = nums[i]
#     flag = False
#     index = 0
#     for j in range(i - 1, -1, -1):
#         if target < nums[j]:
#             nums[j + 1] = nums[j]
#             flag = True
#             index = j
#     if flag:
#         nums[index] = target
#
# print(nums)


################################################
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
# n = len(nums)
#
# for i in range(n - 1):
#     flag = True
#     for j in range(n - 1 - i):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             flag = False
#     if flag:
#         break
# print(nums)

# insert sort
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
# n = len(nums)
#
# for i in range(1, n):
#     to_insert = nums[i]
#     j = i - 1
#
#     while j >= 0 and to_insert < nums[j]:
#         nums[j + 1] = nums[j]
#         j -= 1
#     nums[j + 1] = to_insert
#
# print(nums)


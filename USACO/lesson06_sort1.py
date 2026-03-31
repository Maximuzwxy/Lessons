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
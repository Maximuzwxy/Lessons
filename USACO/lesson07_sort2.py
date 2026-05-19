import random

# counting sort
# def counting_sort(nums):
#     # find the max item value
#     max_v = nums[0]
#     for i in nums:
#         if i > max_v:
#             max_v = i
#     print(max_v, max(nums))
#
#     cnt_lst = [0] * (max_v + 1)
#     for i in nums:
#         cnt_lst[i] += 1
#
#     print(cnt_lst)
#
#     sorted_lst = []
#     for i in range(len(cnt_lst)):
#         if cnt_lst[i] == 0:
#             continue
#         for j in range(cnt_lst[i]):
#             sorted_lst.append(i)
#
#     return sorted_lst
#
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
#
# print(counting_sort(nums))



# merge sort
# def merge_sort(arr):
#     global number
#     number += 1
#     print(number, arr)
#
#     mid = len(arr) // 2
#     if mid >= 1:
#         left = arr[:mid]
#         right = arr[mid:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         merge(arr, left, right)
#
# def merge(arr, left, right):
#     i = j = k = 0
#
#     while i <= len(left) - 1 and j <= len(right) - 1:
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#
#     while i <= len(left) - 1:
#         arr[k] = left[i]
#         i += 1
#         k += 1
#
#     while j <= len(right) - 1:
#         arr[k] = right[j]
#         j += 1
#         k += 1
#
#
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
# number = 0
# merge_sort(nums)
# print(nums)


# quick sort
# def quick_sort(arr, low, high):
#     if high > low:
#         index = partition(arr, low, high)
#         print(low, high, index)
#         print(arr)
#         quick_sort(arr, low, index - 1)
#         quick_sort(arr, index + 1, high)
#
# def partition(arr, low, high):
#     pivot = arr[high]
#     pos = low
#
#     for i in range(low, high):
#         if arr[i] < pivot:
#             arr[i], arr[pos] = arr[pos], arr[i]
#             pos += 1
#     arr[pos], arr[high] = arr[high], arr[pos]
#
#     return pos
#
# nums = [8, 3, 5, 6, 0, 9, 2, 7, 1, 4]
# # number = 0
# quick_sort(nums, 0, len(nums) - 1)
# print(nums)




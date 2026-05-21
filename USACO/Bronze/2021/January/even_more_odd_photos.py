# USACO 2021 January Contest, Bronze
# Problem 2. Even More Odd Photos
# https://usaco.org/index.php?page=viewproblem2&cpid=1084

# solution 1
# n = int(input())
# origin = list(map(int, input().split()))
# even = []
# odd = []
#
# for num in origin:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
#
# while True:
#     e = len(even)
#     o = len(odd)
#     if e == o or e == o + 1:
#         break
#
#     if o > e:
#         if o - e > 1:
#             even.append((odd.pop(), odd.pop()))
#         else:
#             odd.append((odd.pop(), odd.pop(), odd.pop()))
#
#     if e > o + 1:
#         odd.append((even.pop(), odd.pop()))
#
# print(len(even) + len(odd))

# solution 2
n = int(input())
origin = list(map(int, input().split()))

odd = even = 0

for num in origin:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

if even >= odd:
    print(odd * 2 + 1)
else:
    diff = odd - even
    x = 0
    if diff % 3 == 1:
        x = -1
    elif diff % 3 == 2:
        x += 1

    t = even * 2 + (diff // 3) * 2 + x
    print(t)


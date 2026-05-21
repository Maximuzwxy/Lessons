coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 520

cur = []

while sum(cur) < target:
    max_v = coins.pop()
    while sum(cur) + max_v <= target:
        cur.append(max_v)

print(cur)

# USACO 2020 February Contest, Bronze
# Problem 2. Mad Scientist
# https://usaco.org/index.php?page=viewproblem2&cpid=1012

# USACO 2021 January Contest, Bronze
# Problem 2. Even More Odd Photos
# https://usaco.org/index.php?page=viewproblem2&cpid=1084

# USACO 2022 December Contest, Bronze
# Problem 1. Cow College
# https://usaco.org/index.php?page=viewproblem2&cpid=1251
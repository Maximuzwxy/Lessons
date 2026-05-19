# USACO 2020 December Contest, Bronze
# Problem 2. Daisy Chains
# https://usaco.org/index.php?page=viewproblem2&cpid=1060


n = int(input())
p = list(map(int, input().split()))

num = 0

for i in range(n):
    for j in range(i, n):
        flowers = p[i:j + 1]
        if sum(flowers) % (j - i + 1) == 0:
            average = sum(p[i:j + 1]) // (j - i + 1)
            if average in flowers:
                num += 1

print(num)


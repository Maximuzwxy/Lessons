get_on = [2, 5, 8, 10, 6, 0]
get_off = [1, 6, 5, 7, 10, 2]
people_number = 20

for i in range(len(get_on)):
    people_number += get_on[i]
    people_number -= get_off[i]
print(people_number)

print(sum(get_on))
print(sum(get_off))

# USACO 2019 January Contest, Bronze
# Problem 1. Shell Game
# https://usaco.org/index.php?page=viewproblem2&cpid=891


# USACO 2016 December Contest, Bronze
# Problem 3. The Cow-Signal
# https://usaco.org/index.php?page=viewproblem2&cpid=665





# USACO 2019 February Contest, Bronze
# Problem 3. Measuring Traffic
# https://usaco.org/index.php?page=viewproblem2&cpid=917
# inequality interval constraint

# Problem Interpretation
# 1. There are N road segments, each 1 mile long.
#    A sensor is placed in every segment to collect traffic information.
# 2. Each sensor provides a closed range of traffic flow values,
#    such as [10, 14], including both endpoints.
# 3. Sensors are divided into three types:
#    - "on": measures traffic entering the highway from an on-ramp
#    - "off": measures traffic leaving the highway from an off-ramp
#    - "none": directly measures traffic on the main highway
# 4. Using all sensor data, compute:
#    - traffic range before the 1st mile
#    - traffic range after the Nth mile

# Problem Solution Idea
# 1. The essence of this problem is inequality interval constraint.
#    It uses inequality intersection, addition and subtraction
#    to narrow down the valid range step by step.
#    Example 1: Inequality intersection
#    If 10 <= a <= 14 and 11 <= a <= 15 hold at the same time,
#    the actual valid range becomes 11 <= a <= 14.
#
#    Example 2: Inequality addition
#    Given 11 <= a <= 14 and 2 <= b <= 3,
#    we get 13 <= a + b <= 17.
#
#    Example 3: Inequality subtraction
#    Given 11 <= a <= 14 and 2 <= b <= 3,
#    convert b to -3 <= -b <= -2,
#    then combine to get 8 <= a - b <= 12.
# 2. We use all sensor constraints to narrow the interval
#    and get the most accurate valid traffic range.
# 3. "on"/"off" only measure ramp traffic, not the main highway flow.
#    They cannot be used as the main reference.
#    We must find the first "none" segment as the baseline.
# 4. Using the first "none" as the starting range,
#    traverse forward and apply "on"/"off" constraints
#    to compute the range after the Nth mile.
# 5. Forward traversal to calculate traffic range after the Nth mile
#    Base range of the first none: 11 <= none <= 14
#    Encounter on: 1 <= on <= 3
#    none + on results in: 12 <= none + on <= 17
#    Encounter off: 1 <= off <= 3
#    none - off results in: 8 <= none - off <= 13
#    Rule: If the lower bound is less than 0, set it to 0
# 6. Using the same "none" baseline,
#    traverse backward and apply inverse constraints
#    to compute the range before the 1st mile.
# 7. Reverse traversal to calculate traffic range before the 1st mile
#    Base range of the first none: 11 <= none <= 14
#    Encounter on: 1 <= on <= 3
#    none - on results in: 8 <= none - on <= 13
#    Encounter off: 1 <= off <= 3
#    none + off results in: 12 <= none + off <= 17
#    Rule: If the lower bound is less than 0, set it to 0


import sys

sys.stdin = open('traffic.in', 'r')
sys.stdout = open('traffic.out', 'w')

n = int(input())
lst = []

for i in range(n):
    s = input().split()
    lst.append([s[0], int(s[1]), int(s[2])])

end = [0, 0]
not_found = True

for t, low, high in lst:
    if not_found :
        if t == 'none':
            end = [low, high]
            not_found = False
        continue

    if t == 'none':
        end[0] = max(end[0], low)
        end[1] = min(end[1], high)
    elif t == 'off':
        end[0] = max(end[0] - high, 0)
        end[1] = max(end[1] - low, 0)
    else:
        end[0] += low
        end[1] += high

begin = [0, 0]
not_found = True

for t, low, high in lst[::-1]:
    if not_found :
        if t == 'none':
            begin = [low, high]
            not_found = False
        continue

    if t == 'none':
        begin[0] = max(begin[0], low)
        begin[1] = min(begin[1], high)
    elif t == 'on':
        begin[0] = max(begin[0] - high, 0)
        begin[1] = max(begin[1] - low, 0)
    else:
        begin[0] += low
        begin[1] += high

print(begin[0], begin[1])
print(end[0], end[1])


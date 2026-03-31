# solution 1 list
def count_cross(lines):
    cow_cur = [-1] * 11
    count = 0

    for row in lines:
        cow_id, side = list(map(int, row.split()))
        if cow_cur[cow_id] == -1:
            cow_cur[cow_id] = side
        else:
            if cow_cur[cow_id] != side:
                count += 1
                cow_cur[cow_id] = side

    return count

num = 0
lst = []
ret = 0
try:
    with open('crossroad.in', 'r') as f:
        num = int(f.readline().strip())
        for i in range(num):
            lst.append(f.readline().strip())
        ret = count_cross(lst)

except FileNotFoundError:
    num = int(input().strip())
    for i in range(num):
        lst.append(input().strip())
    ret = count_cross(lst)

with open('crossroad.out', 'w') as f:
    f.write(str(ret))
print(ret)

# solution 2 dict
def count_cross(lst):
    d = {}
    cnt = 0
    for cow_id, side in lst:
        if cow_id not in d:
            d[cow_id] = side
        elif d[cow_id] != side:
            cnt += 1
            d[cow_id] = side
    return cnt

cow_lst = []
num = 0
count = 0

try:
    with open('crossroad.in', 'r') as f:
        num = int(f.readline().strip())
        for i in range(num):
            cow_lst.append(list(map(int, f.readline().strip().split())))
        count = count_cross(cow_lst)
except FileNotFoundError:
    num = int(input().strip())
    for i in range(num):
        cow_lst.append(list(map(int, input().strip().split())))
    count = count_cross(cow_lst)

with open('crossroad.out', 'w') as f:
    f.write(str(count))
print(count)














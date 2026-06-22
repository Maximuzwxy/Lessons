import sys
# sys.stdin = open('promote.in', 'r')
# sys.stdout = open('promote.out', 'w')

bronze = list(map(int, input().split()))
silver = list(map(int, input().split()))
gold = list(map(int, input().split()))
platinum = list(map(int, input().split()))

new_participants = bronze[1] + silver[1] + gold[1] + platinum[1] \
    - bronze[0] - silver[0] - gold[0] - platinum[0]

# print(new_participants)

b_s = bronze[0] - (bronze[1] - new_participants)
s_g = silver[0] - (silver[1] - b_s)
g_p = gold[0] - (gold[1] - s_g)

print(b_s)
print(s_g)
print(g_p)

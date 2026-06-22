import random
for i in range(10):
    # print(round(random.random(), 2))
    print(random.randint(1, 10))

a = ['111', '222', '333', '444', '555']
for i in range(5):
    print(random.choice(a))

# 1~100的10个随机整数
a = random.sample(range(1, 100), 10)
print(a)
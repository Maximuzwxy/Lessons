o = 4500
r = 0

while o > 0:
    l = o % 10
    r = r * 10 + l
    o //= 10
print(r)



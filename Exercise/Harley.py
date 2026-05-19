import itertools

digits = ['1', '2', '3', '4', '5', '6']
result = set()  # 用集合自动去重

# 1. 生成整数：用 1~6 个数字排列
for k in range(1, 7):
    for p in itertools.permutations(digits, k):
        num_str = ''.join(p)
        result.add(num_str)

# 2. 生成小数：用 2~6 个数字，中间插小数点
for k in range(2, 7):
    for p in itertools.permutations(digits, k):
        s = ''.join(p)
        # 插小数点：左边至少1位，右边至少1位
        for i in range(1, len(s)):
            decimal = s[:i] + '.' + s[i:]
            result.add(decimal)

# 转成列表并排序（好看一点）
final = sorted(result, key=lambda x: (len(x), x))

# 打印所有
for n in final:
    print(n)

# 输出总数
print("\n总共有：", len(final), "个")

# 如何退出while
# 打印1~10的数字
# i = 0
# while i <= 10:
#     i += 1
#     print(i, end=' ')

# 打印1~10的偶数
# i = 0
# while i <= 10:
#     i += 1
#     if i % 2 == 0:
#         print(i)

# i = 0
# while i <= 10:
#     i += 1
#     if i % 2 != 0:
#         continue
#     print(i)




# 求和1~100
# total = 0
# num = 1
#
# while num <= 100:
#     total += num
#     num += 1
#
# print(total)

# 输入什么，输出什么
# while True:
#     a = input('input: ')
#     print(a)
#
#     if a == 'exit':
#         print('exit!')
#         break

# i = 1
# total = 0
# while True:
#     total += i
#     i += 1
#     if i > 100:
#         break
# print(total)




# import random
# total = 0
# while True:
#     a = random.randint(1, 100)
#     print(a)
#     total += 1
#     if a % 7 == 0:
#         break
# print(total)

# while True:
#     number = input('input: ')
#     if int(number) < 0:
#         break
#     print(int(number) ** 2)


# import random
# a = random.randint(1, 100)
# total = 0
# # print(a)
# while True:
#     b = input('input a number: ')
#     c = int(b)
#     total += 1
#
#     if c == a:
#         print('you are right! exit')
#         print('total is ', total)
#         break
#     elif c < a:
#         print('please try a larger one')
#     else:
#         print('please try a smaller one')








# from PIL import Image, ImageDraw, ImageFont
# import random
#
# # 生成四位随机数字
# random_numbers = [random.randint(0, 9) for _ in range(4)]
# print("随机生成的数字：", random_numbers)
#
# # 图片尺寸
# width = 300
# height = 100
#
# # 创建新的图像对象
# image = Image.new("RGB", (width, height), "white")
# draw = ImageDraw.Draw(image)
#
# # 设置字体和字体大小
# font_size = 36
# try:
#     # 尝试使用Arial字体
#     font = ImageFont.truetype("arial.ttf", font_size)
# except IOError:
#     # 如果找不到Arial，使用默认字体
#     font = ImageFont.load_default()
#     print("警告：未找到Arial字体，使用默认字体")
#
# # 在随机位置绘制数字
# x_positions = [random.randint(10, width - 40) for _ in range(4)]
# y_position = height // 2 - font_size // 2
#
# for i in range(4):
#     draw.text((x_positions[i], y_position), str(random_numbers[i]), fill="black", font=font)
#     x_positions[i] += font_size + random.randint(5, 15)  # 这个操作似乎没有实际用途
#
# # 添加干扰线
# for _ in range(5):
#     x1 = random.randint(0, width)
#     y1 = random.randint(0, height)
#     x2 = random.randint(0, width)
#     y2 = random.randint(0, height)
#     draw.line((x1, y1, x2, y2), fill="black", width=2)
#
# # 添加干扰点
# for _ in range(100):
#     x = random.randint(0, width)
#     y = random.randint(0, height)
#     draw.point((x, y), fill="black")
#
# # 保存并显示图像
# image.save("random_numbers_image.png")
# print("验证码图片已保存为 random_numbers_image.png")
# image.show()  # 显示图像（可选）
import random

# a = int(input('input numer: '))
# cnt = 0
#
# while True:
#     if a == 1:
#         print('cnt:', cnt)
#         break
#
#     if a % 2 == 0:
#         a //= 2
#     else:
#         a = a * 3 + 1
#
#     cnt += 1
#     print(a)











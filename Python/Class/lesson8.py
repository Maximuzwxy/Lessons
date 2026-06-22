# 打印所有因数
# a = input('input: ')
# b = int(a)
# # b = int(input('input: '))
# i = 1
# while i <= b:
#     if b % i == 0:
#         print(i)
#     i += 1

import random
# 计算数列的和，调和级数，计算n的值在几的时候会大于某个数，比如5
# total = 0
# n = 0
# while total <= 1:
#     # total += 1/n
#     total = total + 1/n
# print(total)
# print(n)

# 输出n以内的完全平方数
# n = int(input('n:'))
# i = 1
# while i*i <= n:
#     print(i ** 2)
#     i += 1

# 折纸问题
# num = 0
# height = 1
#
# while height <= 8844000:
#     height *= 2
#     num += 1
# print(height)
# print(num)

# 小球掉落问题
# height = 100
# num = 0
# while height >= 0.5:
#     height /= 2
#     num += 1
# print(height)
# print(num)

import tkinter as tk
import time
import random
import tkinter.messagebox

# 倒计时
# window = tk.Tk()
# window.title('Countdown Timer')
# window.geometry('300x300')
#
# label = tk.Label(window, text='')
# label.pack()
#
# counter = 5
# while counter >= 0:
#     label.config(text='Time left: ' + str(counter))
#     time.sleep(1)
#     counter -= 1
#     label.update()
#
# label.config(text='Time is up!!!')
# label.update()
#
# window.mainloop()

# 速算
# window = tk.Tk()
# window.title('Random number generator')
# window.geometry('300x300')
#
# label1 = tk.Label(window, text='')
# label1.pack()
#
# label2 = tk.Label(window, text='Enter the result:')
# label2.pack()
#
# entry = tk.Entry(window)
# entry.pack()
#
# total = 1
#
# def on_click():
#     num = int(entry.get())
#     if num == total:
#         tk.messagebox.showinfo('Result confirmation', 'Correct!')
#     else:
#         tk.messagebox.showerror('Result confirmation', 'Incorrect! Please try again')
#
# button = tk.Button(window, text='Check', command=on_click)
# button.pack()
#
# counter = 1
# while total <= 100:
#     n = random.randint(1, 5)
#     label1.config(text='Random number' + str(counter) + ': ' + str(n))
#     label1.update()
#     time.sleep(1)
#     total *= n
#     counter += 1
#
# time.sleep(5)
# print(total)
#
# window.mainloop()

# 移动小球
import tkinter as tk
import time
import random

window = tk.Tk()
window.title('Moving ball')

# 初始化canvas
size = 300
canvas = tk.Canvas(window, width=size, height=size)
canvas.pack()

# 初始化小球参数
radius = 30 # 球半径
dx = 2 # x轴每次移动的像素
dy = 2 # y轴每次移动的像素
tag = 'circle' # 每次创建球体的时候的标签，用于下一次进入循环的时候删除上一次创建的球体

# 初始位置随机
x = random.randint(10, size - 50)
y = random.randint(10, size - 50)

while True:
    canvas.delete(tag)

    # x += dx
    # y += dy
    #
    # if x + radius >= size or x <= 0:
    #     dx = -dx
    # if y + radius >= size or y <= 0:
    #     dy = -dy

    # x = x+dx
    # y = y+dy
    # if x >= 270:
    #     dx = -2
    # if y >= 270:
    #     dy = -2
    # if x <= 0:
    #     dx = 2
    # if y <= 0:
    #     dy = 2
    #

    oval = canvas.create_oval(x, y, x + radius, y + radius, fill='blue', tags=tag)

    window.update()
    time.sleep(0.02)

# window.mainloop()








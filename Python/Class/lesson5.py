import random
import time
import tkinter as tk

# window = tk.Tk()
# window.title('my tkinter window')
# window.geometry('300x300')

# window = None
# for i in range(10):
#     window = tk.Tk()
#     window.title('No. ' + str(i))
#     window.update()
#     time.sleep(0.5)
# window.mainloop()

# window = tk.Tk()
# label = tk.Label(window, text='Hello World!', font=('Times', 100))
# label.pack()
# window.mainloop()

# scrollbar需要结合canvas
# window = tk.Tk()
# for i in range(1, 11):
    # label = tk.Label(window, text='Label ' + str(i), font=('Times', 50))
    # label.pack()

    # label = tk.Label(window, text='Label ' + str(i), font=('Times', i))
    # label.pack()

    # label = tk.Label(window, text='Label ' + str(i), font=('Times', 10 * i))
    # label.pack()

# for i in range(10, 101, 10):
#     label = tk.Label(window, text='Label ' + str(i), font=('Times', i))
#     label.pack()
#
# window.mainloop()

# canvas
# window = tk.Tk()
# canvas = tk.Canvas(window, width=300, height=300, background='#ddccbb')
# canvas.create_line(10, 10, 100, 100)
#
# canvas.create_line(100, 100, 200, 100)
# canvas.create_line(200, 100, 200, 200)
# canvas.create_line(200, 200, 100, 200)
# canvas.create_line(100, 200, 100, 100)
#
# canvas.pack()
#
# window.mainloop()

# window = tk.Tk()
# window.title('Canvas Example')
# canvas = tk.Canvas(window, width=400, height=300)
# canvas.pack()

# for i in range(100):
#     canvas.create_line(i, 10, i, 100)
#     canvas.update()
#     time.sleep(0.1)

# for i in range(0, 100, 5):
#     canvas.create_line(i, 10, i, 100)
#     canvas.update()
#     time.sleep(0.1)

# for i in range(0, 150, 3):
#     canvas.create_line(i, 100, i + 100, 200)
#     canvas.update()
#     time.sleep(0.1)

# for i in range(100, 250, 3):
#     canvas.create_line(i, 100, i + 100, 200)
#     canvas.update()
#     time.sleep(0.1)
#
# for i in range(250, 100, -3):
#     canvas.create_line(i, 100, i - 100, 200)
#     canvas.update()
#     time.sleep(0.1)
#
#
# window.mainloop()


# rectangle
# window = tk.Tk()
# window.title('Canvas Rectangle')
#
# canvas = tk.Canvas(window, width=800, height=600, bg='#ccddee')
# canvas.pack()

# canvas.create_rectangle(100, 100, 150, 150, fill='red')
# # canvas.create_rectangle(100, 100, 200, 200, fill='#ff0000')
# canvas.update()

# for i in range(10, 200, 10):
#     canvas.create_rectangle(i, i, i + 10, i + 10, fill='red')
#     canvas.update()
#     time.sleep(0.2)

# j = 1
# for i in range(1, 200, 5):
#     canvas.create_rectangle(i, i, j, j, fill='red')
#     canvas.update()
#     time.sleep(0.2)
#     j += 10

# 起点(i, i)，终点(j, j)
# j = 300
# for i in range(300, 150, -5):
#     canvas.create_rectangle(i, i, j, j)
#     canvas.update()
#     time.sleep(0.2)
#     j += 5
# #
# window.mainloop()

# oval 椭圆&圆
# window = tk.Tk()
# window.title('Canvas Oral')
#
# canvas = tk.Canvas(window, width=800, height=600, bg='#ccddee')
# canvas.pack()

# canvas.create_oval(50, 50, 200, 200, fill='blue')
# canvas.update()

# canvas.create_oval(50, 50, 300, 200, fill='blue')
# canvas.update()

# for i in range(10, 100, 3):
#     canvas.create_oval(i, i, i + 100, i + 100, fill='chocolate')
#     canvas.update()
#     time.sleep(0.2)
#
# window.mainloop()

# window = tk.Tk()
# window.title('Counting stars')
#
# size = 500
#
# canvas = tk.Canvas(window, width=size, height=size, bg='black')
# canvas.pack()

# for i in range(100):
#     x = random.randint(0, size)
#     y = random.randint(0, size)
#     canvas.create_oval(x, y, x + 5, y + 5, fill='white')
#     canvas.update()
#     time.sleep(0.2)
#
# canvas.create_line(0, 200, size, 200)
# canvas.update()

# count = 0
# for i in range(100):
#     x = random.randint(0, size)
#     y = random.randint(0, size)
#     canvas.create_oval(x, y, x + 5, y + 5, fill='white')
#     canvas.update()
#     time.sleep(0.2)
#
#     if y > 200:
#         count += 1
#
# print('Counting stars: ', count)
# #
# window.mainloop()

# button
# def on_click():
#     print('click me!')
#
# window = tk.Tk()
# window.title('Button Example')
# window.geometry('300x300')
#
# button = tk.Button(window, text='click me', command=on_click)
# button.pack()
# # button.pack(side='left')
#
# for i in range(5):
#     btn = tk.Button(window, text=str(i+1), command=on_click)
#     btn.pack()
#
# window.mainloop()

# Entry
# window = tk.Tk()
# window.geometry('300x300')
#
# entry = tk.Entry(window)
# entry.pack()
# window.update()
#
# label = tk.Label(window, text='', bg='#bbccdd')
# label.pack()
#
# def show_text():
#     text = entry.get()
#     label.config(text=text)
#
# btn = tk.Button(window, text='click me', command=show_text)
# btn.pack()
#
# window.mainloop()

# list
# window = tk.Tk()
# window.geometry('300x300')
# window.title('List example')
#
# names = ['Harry', 'GeorgeZ', 'GeorgeF', 'Wang', 'Stephen Curry']
#
# for i in names:
#     label = tk.Label(window, bg='#bbccdd', text=i)
#     label.pack()
#
# window.mainloop()

# Counter
# window = tk.Tk()
# window.geometry('300x300')
# window.title('Counter')
#
# counter = 0
# label = tk.Label(window, bg='#bbccdd', text='0')
# label.pack()
#
# def on_click():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#
# btn = tk.Button(window, text='click', command=on_click)
# btn.pack()
#
# window.mainloop()

# calculator
# window = tk.Tk()
# window.geometry('300x300')
# window.title('Calculator')
#
# entry1 = tk.Entry(window)
# entry1.pack()
#
# entry2 = tk.Entry(window)
# entry2.pack()
#
# label = tk.Label(window, bg='#bbccdd')
# label.pack()
#
# def is_int(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False

# def on_click():
#     total = int(entry1.get()) + int(entry2.get())
#     label.config(text=str(total))
#     label.update()
#
# def on_click():
#     if is_int(entry1.get()) and is_int(entry2.get()):
#         total = int(entry1.get()) + int(entry2.get())
#         label.config(text=str(total))
#         label.update()
#     else:
#         label.config(text='Invalid input!')
# #
# btn = tk.Button(window, text='click', command=on_click)
# btn.pack()
#
# window.update()
#
# window.mainloop()

# color list
# window = tk.Tk()
# window.geometry('300x300')
# window.title('Color list')
#
# # 16个标准色，不区分大小写
# # color_names = [
# #     'white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta',
# #     'gray', 'grey', 'brown', 'orange', 'pink', 'purple', 'violet', 'turquoise'
# # ]
#
# colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
#
# for i in colors:
#     label = tk.Label(window, text=i, bg=i)
#     label.pack()
#
# window.mainloop()

# from datetime import datetime
# now = datetime.now()
# print(type(now), now)
#
# window = tk.Tk()
# window.geometry('300x300')
# window.title('Time')
#
# # label = tk.Label(window, text=str(now), bg='#bbccdd')
# label = tk.Label(window, text=str(now)[:19], bg='#bbccdd')
# label.pack()
#
# def on_click():
#     now1 = datetime.now()
#     label.config(text=str(now1)[:19])
#
# # def update_time():
# #     now1 = datetime.now()
# #     label.config(text=str(now1)[:19])
# #     window.after(1000, update_time)
#
# btn = tk.Button(window, text='show time', command=on_click)
# btn.pack()
#
# # update_time()
#
# window.mainloop()

# window = tk.Tk()
# window.geometry('300x300')
# window.title('List example')
#
# names = ['Harry', 'GeorgeZ', 'GeorgeF', 'Wang', 'Stephen Curry']
# colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
#
# for i in range(5):
#     label = tk.Label(window, bg=colors[i], text=names[i])
#     label.pack()
#
# window.mainloop()



# Homework
# window = tk.Tk()
# window.title('My tkinter window')
# window.geometry('400x400')
#
# canvas = tk.Canvas(window, width=400, height=400, bg='#ccddee')
# canvas.pack()
#
# j = 300
# for i in range(100, 200, 5):
#     canvas.create_line(i, i, j, i)
#     canvas.update()
#
#     print(i, j)
#     time.sleep(0.2)
#     j -= 5
#
# # 此处补全代码
#
# j = 200
# for i in range(200, 99, -5):
#     canvas.create_line(i, j, j, j)
#     canvas.update()
#
#     print(i, j)
#     time.sleep(0.2)
#     j += 5
#
# window.mainloop()





# random color
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return f'#{r:02x}{g:02x}{b:02x}'


# import tkinter as tk
#
# root = tk.Tk()
# root.title("Tkinter Demo")
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()
# root.mainloop()
#
# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((300, 200))
# pygame.display.set_caption("Pygame Demo")
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 120, 255))
#     pygame.display.flip()
# pygame.quit()
#
#
# import turtle
#
# t = turtle.Turtle()
# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# turtle.done()



# HZ
# import time
# import tkinter as tk
#
# window = tk.Tk()
# window.title('My tkinter window')
# window.geometry('400x400')
#
# canvas = tk.Canvas(window, width=400, height=400, bg='#ccddee')
# canvas.pack()
#
# j = 300
# for i in range(100, 200, 5):
#     canvas.create_line(i, i, j, i)
#     canvas.update()
#     print(i, j)
#     time.sleep(0.2)
#     j -= 5
# j = 300
# for i in range(100, 200, 5):
#     canvas.create_line(i, j, i, j)
#     canvas.update()
#     print(i, j)
#     time.sleep(0.2)
#     j -= 5
# window.mainloop()


# Harry
# import time
# import tkinter as tk
#
# window = tk.Tk()
# window.title('My tkinter window')
# window.geometry('400x400')
#
# canvas = tk.Canvas(window, width=400, height=400, bg='#ccddee')
# canvas.pack()
# canvas.create_line(140, 300, 260, 300)
# canvas.create_line(140, 300, 200, 200)
# canvas.create_line(200, 200, 260, 300)
#
# j = 300
# for i in range(100, 200, 5):
#     canvas.create_line(i, i, j, i)
#     canvas.update()
#     print(i, j)
#     time.sleep(0.2)
#     j -= 5
# window.mainloop()

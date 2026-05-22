# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple

import random
import turtle as t
from freegames import square, vector

# 1. square
# t.hideturtle()
# t.tracer(False)
# square(0, 0, 10, 'green')
# t.update()
# t.done()

# 2. snake
# t.hideturtle()
# t.tracer(False)
# square(0, 0, 10, 'green')
# square(-10, 0, 10, 'green')
# square(-20, 0, 10, 'green')
# t.update()
# t.done()

# 3. snake list and vector
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#     snake.append(vector(-BLOCK, 0))
#     snake.append(vector(-BLOCK * 2, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# init_snake()
#
# t.update()
# t.done()

# 4. snake move
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#     snake.append(vector(-BLOCK, 0))
#     snake.append(vector(-BLOCK * 2, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# def move():
#     head = vector(snake[0].x + BLOCK, snake[0].y)
#     snake.insert(0, head)
#     snake.pop()
#
#     t.clear()
#     draw_snake()
#     t.update()
#
#     t.ontimer(move, 200)
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# init_snake()
# move()
#
# t.update()
# t.done()

# 5. key event
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#     snake.append(vector(-BLOCK, 0))
#     snake.append(vector(-BLOCK * 2, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# def move():
#     head = vector(snake[0].x + BLOCK, snake[0].y)
#     snake.insert(0, head)
#     snake.pop()
#
#     t.clear()
#     draw_snake()
#     t.update()
#
#     t.ontimer(move, 200)
#
# def on_change(key):
#     print(key)
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# t.listen()
# t.onkey(lambda: on_change('Up'), 'Up')
# t.onkey(lambda: on_change('Down'), 'Down')
# t.onkey(lambda: on_change('Left'), 'Left')
# t.onkey(lambda: on_change('Right'), 'Right')
#
# init_snake()
# move()
#
# t.update()
# t.done()

# 6. control snake
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
# aim = vector(0, 0)
# begin = False
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#     snake.append(vector(-BLOCK, 0))
#     snake.append(vector(-BLOCK * 2, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# def move():
#     if begin:
#         t.clear()
#
#         head = vector(snake[0].x + aim.x, snake[0].y + aim.y)
#         snake.insert(0, head)
#         snake.pop()
#
#         draw_snake()
#         t.update()
#
#         t.ontimer(move, 200)
#
# def on_change(x, y):
#     global begin
#     if aim.x != -x or aim.y != -y:
#         aim.x = x
#         aim.y = y
#
#     if not begin:
#         begin = True
#         move()
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# t.listen()
# t.onkey(lambda: on_change(0, BLOCK), 'Up')
# t.onkey(lambda: on_change(0, -BLOCK), 'Down')
# t.onkey(lambda: on_change(-BLOCK, 0), 'Left')
# t.onkey(lambda: on_change(BLOCK, 0), 'Right')
#
# init_snake()
#
# t.update()
# t.done()

# 7. draw food
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
# aim = vector(0, 0)
# begin = False
# food = []
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# def move():
#     if begin:
#         t.clear()
#
#         head = vector(snake[0].x + aim.x, snake[0].y + aim.y)
#         snake.insert(0, head)
#         snake.pop()
#
#         draw_snake()
#         draw_food()
#         t.update()
#
#         t.ontimer(move, 200)
#
# def on_change(x, y):
#     global begin
#     if aim.x != -x or aim.y != -y:
#         aim.x = x
#         aim.y = y
#
#     if not begin:
#         begin = True
#         move()
#
# def draw_food():
#     for i in range(10 - len(food)):
#         lst = random.sample(range(-RADIUS, RADIUS - BLOCK, BLOCK), 2)
#         food.append(vector(lst[0], lst[1]))
#     for j in food:
#         square(j.x, j.y, BLOCK - 2, 'blue')
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# t.listen()
# t.onkey(lambda: on_change(0, BLOCK), 'Up')
# t.onkey(lambda: on_change(0, -BLOCK), 'Down')
# t.onkey(lambda: on_change(-BLOCK, 0), 'Left')
# t.onkey(lambda: on_change(BLOCK, 0), 'Right')
#
# init_snake()
# draw_food()
#
# t.update()
# t.done()

# 8. eat food
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
# aim = vector(0, 0)
# begin = False
# food = []
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# def move():
#     if begin:
#         t.clear()
#
#         head = vector(snake[0].x + aim.x, snake[0].y + aim.y)
#         snake.insert(0, head)
#
#         # if head in food, don't pop last one
#         if head in food:
#             food.remove(head)
#         else:
#             snake.pop()
#
#         draw_snake()
#         draw_food()
#
#         t.update()
#         t.ontimer(move, 300 // len(snake))
#
# def on_change(x, y):
#     global begin
#     if aim.x != -x or aim.y != -y:
#         aim.x = x
#         aim.y = y
#
#     if not begin:
#         begin = True
#         move()
#
# def draw_food():
#     for i in range(10 - len(food)):
#         lst = random.sample(range(-RADIUS, RADIUS - BLOCK, BLOCK), 2)
#         food.append(vector(lst[0], lst[1]))
#     for j in food:
#         square(j.x, j.y, BLOCK - 2, 'blue')
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# t.listen()
# t.onkey(lambda: on_change(0, BLOCK), 'Up')
# t.onkey(lambda: on_change(0, -BLOCK), 'Down')
# t.onkey(lambda: on_change(-BLOCK, 0), 'Left')
# t.onkey(lambda: on_change(BLOCK, 0), 'Right')
#
# init_snake()
# draw_food()
#
# t.update()
# t.done()

# 9. game over
snake = []
BLOCK = 12
RADIUS = BLOCK * 25
aim = vector(0, 0)
begin = False
food = []

def init_snake():
    snake.clear()
    snake.append(vector(0, 0))

    draw_snake()

def draw_snake():
    for i in snake:
        square(i.x, i.y, BLOCK - 2, 'green')

def move():
    if begin:
        t.clear()

        head = vector(snake[0].x + aim.x, snake[0].y + aim.y)
        snake.insert(0, head)

        # if head in food, don't pop last one
        if head in food:
            food.remove(head)
        elif head.x < -RADIUS or head.x > RADIUS - BLOCK or head.y < -RADIUS or head.y > RADIUS - BLOCK:
            game_over()
        else:
            snake.pop()

        draw_snake()
        draw_food()

        t.update()
        t.ontimer(move, 300 // len(snake))

def on_change(x, y):
    global begin
    if aim.x != -x or aim.y != -y:
        aim.x = x
        aim.y = y

    if not begin:
        begin = True
        move()

def draw_food():
    for i in range(10 - len(food)):
        lst = random.sample(range(-RADIUS, RADIUS - BLOCK, BLOCK), 2)
        x = vector(lst[0], lst[1])
        if x not in snake:
            food.append(x)
    for j in food:
        square(j.x, j.y, BLOCK - 2, 'blue')

def game_over():
    global begin
    aim.x, aim.y = 0, 0
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pencolor('red')
    t.write('Game Over!', align='center', font=('Arial', 24, 'normal'))
    begin = False

t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
t.hideturtle()
t.tracer(False)

t.listen()
t.onkey(lambda: on_change(0, BLOCK), 'Up')
t.onkey(lambda: on_change(0, -BLOCK), 'Down')
t.onkey(lambda: on_change(-BLOCK, 0), 'Left')
t.onkey(lambda: on_change(BLOCK, 0), 'Right')

init_snake()
draw_food()

t.update()
t.done()

# 10. restart game
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
# aim = vector(0, 0)
# begin = False
# food = []
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# def move():
#     if begin:
#         t.clear()
#
#         head = vector(snake[0].x + aim.x, snake[0].y + aim.y)
#         snake.insert(0, head)
#
#         # if head in food, don't pop last one
#         if head in food:
#             food.remove(head)
#         elif head.x < -RADIUS or head.x > RADIUS - BLOCK or head.y < -RADIUS or head.y > RADIUS - BLOCK:
#             game_over()
#         else:
#             snake.pop()
#
#         draw_snake()
#         draw_food()
#
#         t.update()
#         t.ontimer(move, 300 // len(snake))
#
# def on_change(x, y):
#     global begin
#     if aim.x != -x or aim.y != -y:
#         aim.x = x
#         aim.y = y
#
#     if not begin:
#         begin = True
#         move()
#
# def draw_food():
#     for i in range(10 - len(food)):
#         lst = random.sample(range(-RADIUS, RADIUS - BLOCK, BLOCK), 2)
#         x = vector(lst[0], lst[1])
#         if x not in snake:
#             food.append(x)
#     for j in food:
#         square(j.x, j.y, BLOCK - 2, 'blue')
#
# def game_over():
#     global begin
#     aim.x, aim.y = 0, 0
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.pencolor('red')
#     t.write('Game Over!', align='center', font=('Arial', 24, 'normal'))
#     begin = False
#
# def restart():
#     t.clear()
#     init_snake()
#     food.clear()
#     draw_food()
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# t.listen()
# t.onkey(lambda: on_change(0, BLOCK), 'Up')
# t.onkey(lambda: on_change(0, -BLOCK), 'Down')
# t.onkey(lambda: on_change(-BLOCK, 0), 'Left')
# t.onkey(lambda: on_change(BLOCK, 0), 'Right')
# t.onkey(restart, 'r')
#
# init_snake()
# draw_food()
#
# t.update()
# t.done()

# 11. score
# snake = []
# BLOCK = 12
# RADIUS = BLOCK * 25
# aim = vector(0, 0)
# begin = False
# food = []
#
# def init_snake():
#     snake.clear()
#     snake.append(vector(0, 0))
#
#     draw_snake()
#
# def draw_snake():
#     for i in snake:
#         square(i.x, i.y, BLOCK - 2, 'green')
#
# def move():
#     if begin:
#         t.clear()
#
#         head = vector(snake[0].x + aim.x, snake[0].y + aim.y)
#         snake.insert(0, head)
#
#         # if head in food, don't pop last one
#         if head in food:
#             food.remove(head)
#         elif head.x < -RADIUS or head.x > RADIUS - BLOCK or head.y < -RADIUS or head.y > RADIUS - BLOCK:
#             game_over()
#             snake.pop()
#         else:
#             snake.pop()
#
#         draw_snake()
#         draw_food()
#         show_score()
#
#         t.update()
#         t.ontimer(move, 300 // len(snake))
#
# def on_change(x, y):
#     global begin
#     if aim.x != -x or aim.y != -y:
#         aim.x = x
#         aim.y = y
#
#     if not begin:
#         begin = True
#         move()
#
# def draw_food():
#     for i in range(10 - len(food)):
#         lst = random.sample(range(-RADIUS, RADIUS - BLOCK, BLOCK), 2)
#         x = vector(lst[0], lst[1])
#         if x not in snake:
#             food.append(x)
#     for j in food:
#         square(j.x, j.y, BLOCK - 2, 'blue')
#
# def game_over():
#     global begin
#     aim.x, aim.y = 0, 0
#     t.penup()
#     t.goto(0, 0)
#     t.pencolor('red')
#     t.write('Game Over!', align='center', font=('Arial', 24, 'normal'))
#     begin = False
#
# def restart():
#     t.clear()
#     init_snake()
#     food.clear()
#     draw_food()
#
# def show_score():
#     t.penup()
#     t.goto(RADIUS - 75, RADIUS - 30)  # 根据画布大小调整位置
#     t.pendown()
#     t.pencolor('orange')
#     t.write(f'Score: {len(snake) - 1}', font=('Arial', 10, 'normal'))
#
#
# t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
# t.hideturtle()
# t.tracer(False)
#
# t.listen()
# t.onkey(lambda: on_change(0, BLOCK), 'Up')
# t.onkey(lambda: on_change(0, -BLOCK), 'Down')
# t.onkey(lambda: on_change(-BLOCK, 0), 'Left')
# t.onkey(lambda: on_change(BLOCK, 0), 'Right')
# t.onkey(restart, 'r')
#
# init_snake()
# draw_food()
# show_score()
#
# t.update()
# t.done()







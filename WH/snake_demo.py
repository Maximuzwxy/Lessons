# pip install freegames

import random
import turtle as t
from freegames import square, vector

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
        show_score()

        t.update()
        t.ontimer(move, 300 // len(snake))

def on_change(x, y):
    global begin
    if begin:
        if aim.x != -x or aim.y != -y:
            aim.x = x
            aim.y = y

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

def restart():
    global begin
    begin = True
    t.clear()
    init_snake()
    food.clear()
    draw_food()
    move()

def show_score():
    t.penup()
    t.goto(RADIUS - 75, RADIUS - 30)  # locate by the size of canvas
    t.pendown()
    t.pencolor('orange')
    t.write(f'Score: {len(snake) - 1}', font=('Arial', 10, 'normal'))

t.setup(RADIUS * 2, RADIUS * 2, 0, 0)
t.hideturtle()
t.tracer(False)

t.listen()
t.onkey(lambda: on_change(0, BLOCK), 'Up')
t.onkey(lambda: on_change(0, -BLOCK), 'Down')
t.onkey(lambda: on_change(-BLOCK, 0), 'Left')
t.onkey(lambda: on_change(BLOCK, 0), 'Right')
t.onkey(restart, 'r')

t.update()
t.done()

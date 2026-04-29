import turtle as t
import time

# 1. draw a line
# t.speed(1)
# t.goto(0, 0)
# t.pendown()
# t.forward(100)
# t.penup()
# t.done()

# 2. draw horizontal lines
# cell = 30
#
# def draw_board():
#     for i in range(5):
#         t.speed(0)
#         t.goto(0, 0 + cell * i)
#         t.pendown()
#         t.forward(100)
#         t.penup()
# draw_board()
# t.done()

# 3. draw vertical lines
# cell = 30
#
# def draw_board():
#     t.right(90)
#     for i in range(5):
#         t.speed(0)
#         t.goto(0 + cell * i, 0)
#         t.pendown()
#         t.forward(100)
#         t.penup()
# draw_board()
# t.done()

# 4. draw board
board_size = 14
half_size = board_size // 2
cell = 30

def draw_board():
    t.speed(0)
    t.penup()
    for i in range(board_size + 1):
        t.goto(-cell * half_size, cell * half_size - i * cell)
        t.pendown()
        t.forward(cell * board_size)
        t.penup()

    t.right(90)
    for i in range(board_size + 1):
        t.goto(-cell * half_size + i * cell, cell * half_size)
        t.pendown()
        t.forward(cell * board_size)
        t.penup()
    t.left(90)

draw_board()
t.done()

# 5. draw circle
# def draw_piece():
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.fillcolor('white')
#     t.begin_fill()
#     t.circle(13)
#     t.end_fill()
#     t.penup()
#
# t.setup(600,600)
# draw_piece()
# t.done()

# 6. draw pieces
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
#
# def draw_board():
#     t.speed(0)
#     t.penup()
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size, cell * half_size - i * cell)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#
#     t.right(90)
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size + i * cell, cell * half_size)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#     t.left(90)
#
# def draw_piece(x, y, color):
#     t.speed(1)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
#     t.penup()
#
# t.setup(600, 600)
#
# draw_board()
# draw_piece(0, -cell // 2, 'white')
# draw_piece(0, -cell // 2 + cell, 'white')
# draw_piece(0, -cell // 2 + 2 * cell, 'white')
#
# t.done()

# 7. click event
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
#
# def draw_board():
#     t.speed(0)
#     t.penup()
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size, cell * half_size - i * cell)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#
#     t.right(90)
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size + i * cell, cell * half_size)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#     t.left(90)
#
# def draw_piece(x, y, color):
#     t.speed(1)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
#     t.penup()
#
# def on_click(x, y):
#     print(x, y)
#     column = round(x / cell)
#     row = round(y / cell)
#     print(column, row)
#
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
# draw_piece(0, -cell // 2, 'white')
#
# t.onscreenclick(on_click)
# t.done()

# 8. put down piece
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
#
# def draw_board():
#     t.speed(0)
#     t.penup()
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size, cell * half_size - i * cell)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#
#     t.right(90)
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size + i * cell, cell * half_size)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#     t.left(90)
#
# def draw_piece(x, y, color):
#     t.speed(1)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
#     t.penup()
#
# def on_click(x, y):
#     print(x, y)
#     dx = round(x / cell)
#     dy = round(y / cell)
#     print(dx, dy)
#
#     draw_piece(dx * cell, -cell // 2 + dy * cell, 'white')
#
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
#
# t.onscreenclick(on_click)
# t.done()

# 9. turn white or black
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
# turn = 0
#
# def draw_board():
#     t.speed(0)
#     t.penup()
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size, cell * half_size - i * cell)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#
#     t.right(90)
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size + i * cell, cell * half_size)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#     t.left(90)
#
# def draw_piece(x, y, color):
#     t.speed(1)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
#     t.penup()
#
# def on_click(x, y):
#     print(x, y)
#     dx = round(x / cell)
#     dy = round(y / cell)
#     print(dx, dy)
#
#     global turn
#
#     if turn == 0:
#         color = 'white'
#         turn = 1
#     else:
#         color = 'black'
#         turn = 0
#
#     draw_piece(dx * cell, -cell // 2 + dy * cell, color)
#
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
#
# t.onscreenclick(on_click)
# t.done()

# 10. positions of the pieces
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
# turn = 0
#
# board = [[-1 for _ in range(board_size + 1)] for _ in range(board_size + 1)]
#
# def draw_board():
#     t.speed(0)
#     t.penup()
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size, cell * half_size - i * cell)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#
#     t.right(90)
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size + i * cell, cell * half_size)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#     t.left(90)
#
# def draw_piece(x, y, color):
#     t.speed(1)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
#     t.penup()
#
# def on_click(x, y):
#     print(x, y)
#     dx = round(x / cell)
#     dy = round(y / cell)
#     print(dx, dy)
#
#     global turn
#
#     if turn == 0:
#         color = 'white'
#         turn = 1
#     else:
#         color = 'black'
#         turn = 0
#
#     column = dx + half_size
#     row = dy - half_size
#     if -half_size <= dx <= half_size and -half_size <= dx <= half_size and board[column][row] == -1:
#         draw_piece(dx * cell, -cell // 2 + dy * cell, color)
#         board[column][row] = 1
#         print(column, row)
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
#
# t.onscreenclick(on_click)
# t.done()

# 11. check winner
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
# turn = 0
#
# board = [[-1 for _ in range(board_size + 1)] for _ in range(board_size + 1)]
#
# def draw_board():
#     t.speed(0)
#     t.penup()
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size, cell * half_size - i * cell)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#
#     t.right(90)
#     for i in range(board_size + 1):
#         t.goto(-cell * half_size + i * cell, cell * half_size)
#         t.pendown()
#         t.forward(cell * board_size)
#         t.penup()
#     t.left(90)
#
# def draw_piece(x, y, color):
#     t.speed(1)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
#     t.penup()
#
# def on_click(x, y):
#     dx = round(x / cell)
#     dy = round(y / cell)
#
#     global turn
#
#     if turn == 0:
#         color = 'white'
#     else:
#         color = 'black'
#
#     column = dx + half_size
#     row = half_size - dy
#     if -half_size <= dx <= half_size and -half_size <= dx <= half_size and board[column][row] == -1:
#         draw_piece(dx * cell, -cell // 2 + dy * cell, color)
#         board[column][row] = turn
#
#         if is_win(column, row, turn):
#
#         if turn == 0:
#             turn = 1
#         else:
#             turn = 0
#
#
# def is_win(x, y, player):
#     # 4 directions
#     dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]
#
#     cnt = 1
#     for dx, dy in dirs:
#         # forward direction
#         tx = x + dx
#         ty = y + dy
#
#         while 0 <= tx <= board_size and 0 <= ty <= board_size and board[tx][ty] == player:
#             cnt += 1
#             tx += dx
#             ty += dy
#
#         # backward direction
#         tx = x - dx
#         ty = y - dy
#         while 0 <= tx <= board_size and 0 <= ty <= board_size and board[tx][ty] == player:
#             cnt += 1
#             tx -= dx
#             ty -= dy
#
#         if cnt >= 5:
#             return True
#
#     return False
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
#
# t.onscreenclick(on_click)
# t.done()

# 11. game over and reset
board_size = 14
half_size = board_size // 2
cell = 30
radius = int(cell * 0.9 // 2)
turn = 0
over = False

board = [[-1 for _ in range(board_size + 1)] for _ in range(board_size + 1)]

def draw_board():
    t.speed(0)
    t.penup()
    for i in range(board_size + 1):
        t.goto(-cell * half_size, cell * half_size - i * cell)
        t.pendown()
        t.forward(cell * board_size)
        t.penup()

    t.right(90)
    for i in range(board_size + 1):
        t.goto(-cell * half_size + i * cell, cell * half_size)
        t.pendown()
        t.forward(cell * board_size)
        t.penup()
    t.left(90)

def draw_piece(x, y, color):
    t.speed(1)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

def on_click(x, y):
    if over:
        restart()
        return

    dx = round(x / cell)
    dy = round(y / cell)

    global turn

    if turn == 0:
        color = 'white'
    else:
        color = 'black'

    column = dx + half_size
    row = half_size - dy
    if -half_size <= dx <= half_size and -half_size <= dy <= half_size and board[column][row] == -1:
        draw_piece(dx * cell, -cell // 2 + dy * cell, color)
        board[column][row] = turn

        if is_win(column, row, turn):
            game_over()

        if turn == 0:
            turn = 1
        else:
            turn = 0


def is_win(x, y, player):
    # 4 directions
    dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]

    cnt = 1
    for dx, dy in dirs:
        # forward direction
        tx = x + dx
        ty = y + dy

        while 0 <= tx <= board_size and 0 <= ty <= board_size and board[tx][ty] == player:
            cnt += 1
            tx += dx
            ty += dy

        # backward direction
        tx = x - dx
        ty = y - dy
        while 0 <= tx <= board_size and 0 <= ty <= board_size and board[tx][ty] == player:
            cnt += 1
            tx -= dx
            ty -= dy

        if cnt >= 5:
            return True

    return False

def game_over():
    global over

    t.penup()
    t.goto(0, 250)
    t.write(f"{'black' if turn == 1 else 'white'} wins!", font=("Arial", 24, "bold"), align="center")
    over = True
    return

def restart():
    global over, turn
    over = False
    turn = 0

    t.reset()
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = -1

    draw_board()

t.setup(600, 600)
t.hideturtle()
t.tracer(0)

draw_board()

t.onscreenclick(on_click)
t.done()


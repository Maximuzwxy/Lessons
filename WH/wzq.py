import turtle

# ====================== 配置 ======================
BOARD_SIZE = 15        # 15x15 棋盘
CELL = 30              # 每个格子大小
RADIUS = 13            # 棋子半径

# 二维列表：0=空 1=黑棋 2=白棋
board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

turn = 1  # 1黑 2白
game_over = False

# ====================== 画棋盘 ======================
def draw_board():
    turtle.speed(0)
    turtle.penup()
    for i in range(BOARD_SIZE):
        turtle.goto(-CELL*7, CELL*7 - i*CELL)
        turtle.pendown()
        turtle.forward(CELL*14)
        turtle.penup()
    turtle.right(90)
    for i in range(BOARD_SIZE):
        turtle.goto(-CELL*7 + i*CELL, CELL*7)
        turtle.pendown()
        turtle.forward(CELL*14)
        turtle.penup()
    turtle.left(90)

# ====================== 画棋子 ======================
def draw_piece(x, y, color):
    turtle.penup()
    turtle.goto(x, y - RADIUS)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(RADIUS)
    turtle.end_fill()

# ====================== 判断胜负 ======================
def is_win(x, y, player):
    # 横、竖、左斜、右斜
    dirs = [(1,0),(0,1),(1,1),(1,-1)]
    for dx, dy in dirs:
        cnt = 1
        # 正方向
        tx, ty = x+dx, y+dy
        while 0<=tx<BOARD_SIZE and 0<=ty<BOARD_SIZE and board[tx][ty]==player:
            cnt +=1
            tx += dx
            ty += dy
        # 反方向
        tx, ty = x-dx, y-dy
        while 0<=tx<BOARD_SIZE and 0<=ty<BOARD_SIZE and board[tx][ty]==player:
            cnt +=1
            tx -= dx
            ty -= dy
        if cnt >=5:
            return True
    return False

# ====================== 点击落子 ======================
def click(x, y):
    global turn, game_over
    if game_over: return

    # 坐标转棋盘行列
    col = round(x / CELL) + 7
    row = 7 - round(y / CELL)

    if 0<=col<BOARD_SIZE and 0<=row<BOARD_SIZE and board[col][row]==0:
        board[col][row] = turn
        cx = (col -7)*CELL
        cy = (7 - row)*CELL
        draw_piece(cx, cy, "black" if turn==1 else "white")

        if is_win(col, row, turn):
            turtle.penup()
            turtle.goto(0, 250)
            turtle.write(f"{'黑棋' if turn==1 else '白棋'}胜利！", font=("Arial",24,"bold"), align="center")
            game_over = True
            return

        turn = 2 if turn==1 else 1

# ====================== 启动 ======================
turtle.setup(600,600)
turtle.hideturtle()
turtle.tracer(0)
draw_board()
turtle.onscreenclick(click)
turtle.done()
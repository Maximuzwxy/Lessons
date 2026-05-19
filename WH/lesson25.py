import turtle as t
import time

# ============================================================
# Step 1: Draw a single line
# Goal: Learn basic turtle movement and drawing commands
# ============================================================
# t.speed(1)
# t.goto(0, 0)
# t.pendown()
# t.forward(100)
# t.penup()
# t.done()

# ============================================================
# Step 2: Draw horizontal lines using a loop
# Goal: Use a for-loop to draw multiple parallel horizontal lines
# ============================================================
# cell = 30                              # NEW: spacing variable for line distance
#
# def draw_board():                      # NEW: wrap code in a function
#     for i in range(5):                 # NEW: loop to draw 5 horizontal lines
#         t.speed(0)
#         t.goto(0, 0 + cell * i)
#         t.pendown()
#         t.forward(100)
#         t.penup()
# draw_board()
# t.done()

# ============================================================
# Step 3: Draw vertical lines
# Goal: Rotate the turtle and draw vertical lines to form a grid
# ============================================================
# cell = 30
#
# def draw_board():
#     t.right(90)                        # NEW: rotate turtle 90 degrees for vertical direction
#     for i in range(5):
#         t.speed(0)
#         t.goto(0 + cell * i, 0)        # CHANGED: x-offset instead of y-offset
#         t.pendown()
#         t.forward(100)
#         t.penup()
# draw_board()
# t.done()

# ============================================================
# Step 4: Draw a complete centered board
# Goal: Combine horizontal and vertical lines into a full centered grid
# ============================================================
# board_size = 14                        # NEW: dynamic board size variable
# half_size = board_size // 2            # NEW: half size for centering
# cell = 30
#
# def draw_board():
#     t.speed(0)
#     t.penup()                          # NEW: ensure pen is up before positioning
#     for i in range(board_size + 1):    # CHANGED: loop count based on board_size
#         t.goto(-cell * half_size, cell * half_size - i * cell)   # CHANGED: centered coordinates
#         t.pendown()
#         t.forward(cell * board_size)   # CHANGED: line length based on board_size
#         t.penup()
#
#     t.right(90)                        # NEW: rotate for vertical lines
#     for i in range(board_size + 1):    # NEW: vertical line loop
#         t.goto(-cell * half_size + i * cell, cell * half_size)   # NEW: vertical line positioning
#         t.pendown()
#         t.forward(cell * board_size)   # NEW: draw vertical line
#         t.penup()
#     t.left(90)                         # NEW: rotate back to original direction
#
# draw_board()
# t.done()

# ============================================================
# Step 5: Draw a single piece (circle)
# Goal: Learn how to draw a filled circle as a game piece
# ============================================================
# board_size = 14                        # from Step 4
# half_size = board_size // 2            # from Step 4
# cell = 30                              # from Step 4
#
# def draw_board():                      # from Step 4
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
# def draw_piece():                      # NEW: function to draw a piece
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.fillcolor('white')               # NEW: set fill color
#     t.begin_fill()                     # NEW: start filling
#     t.circle(13)                       # NEW: draw circle
#     t.end_fill()                       # NEW: end filling
#     t.penup()
#
# t.setup(600,600)                       # NEW: set window size
# draw_board()
# draw_piece()                           # NEW: draw the piece
# t.done()

# ============================================================
# Step 6: Draw multiple pieces on the board
# Goal: Place several pieces on the grid to test positioning
# ============================================================
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)          # NEW: dynamic radius based on cell size
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
# def draw_piece(x, y, color):           # CHANGED: now takes x, y, color parameters
#     t.speed(1)
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.fillcolor(color)                 # CHANGED: use color parameter instead of hardcoded 'white'
#     t.begin_fill()
#     t.circle(radius)                   # CHANGED: use radius variable instead of hardcoded 13
#     t.end_fill()
#     t.penup()
#
# t.setup(600, 600)
#
# draw_board()
# draw_piece(0, -cell // 2, 'white')     # NEW: place test piece at grid position (0, 0)
# draw_piece(0, -cell // 2 + cell, 'white')      # NEW: place test piece at grid position (0, 1)
# draw_piece(0, -cell // 2 + 2 * cell, 'white')  # NEW: place test piece at grid position (0, 2)
#
# t.done()

# ============================================================
# Step 7: Add click event handling
# Goal: Detect mouse clicks and convert screen coordinates to grid coordinates
# ============================================================
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
# def on_click(x, y):                    # NEW: click event handler function
#     print(x, y)
#     column = round(x / cell)           # NEW: convert screen x to grid column
#     row = round(y / cell)              # NEW: convert screen y to grid row
#     print(column, row)
#
#
# t.setup(600, 600)
# t.hideturtle()                         # NEW: hide turtle for performance
# t.tracer(0)                            # NEW: disable animation for instant drawing
#
# draw_board()
# draw_piece(0, -cell // 2, 'white')     # CHANGED: kept only one test piece
#
# t.onscreenclick(on_click)              # NEW: register click event handler
# t.done()

# ============================================================
# Step 8: Place a piece on click
# Goal: Draw a piece at the clicked grid position
# ============================================================
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
#     dx = round(x / cell)               # CHANGED: renamed from column to dx
#     dy = round(y / cell)               # CHANGED: renamed from row to dy
#     print(dx, dy)
#
#     draw_piece(dx * cell, -cell // 2 + dy * cell, 'white')   # NEW: draw piece at clicked grid position
#
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
#                                          # CHANGED: removed hardcoded test piece
#
# t.onscreenclick(on_click)
# t.done()

# ============================================================
# Step 9: Alternate turns between white and black
# Goal: Switch piece color after each valid click
# ============================================================
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
# turn = 0                               # NEW: global turn variable (0=white, 1=black)
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
#     global turn                        # NEW: declare global to modify turn
#
#     if turn == 0:                      # NEW: check whose turn it is
#         color = 'white'                # NEW: white's turn
#         turn = 1                       # NEW: switch to black
#     else:                              # NEW: black's turn
#         color = 'black'                # NEW: set black color
#         turn = 0                       # NEW: switch to white
#
#     draw_piece(dx * cell, -cell // 2 + dy * cell, color)   # CHANGED: use dynamic color instead of 'white'
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

# ============================================================
# Step 10: Track piece positions with a 2D board array
# Goal: Store piece positions to prevent overwriting and enable win checking later
# ============================================================
# board_size = 14
# half_size = board_size // 2
# cell = 30
# radius = int(cell * 0.9 // 2)
# turn = 0
#
# board = [[-1 for _ in range(board_size + 1)] for _ in range(board_size + 1)]   # NEW: 2D array to track pieces
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
#     else:
#         color = 'black'
#
#     column = dx + half_size            # NEW: calculate array column index
#     row = half_size - dy               # NEW: calculate array row index
#     if -half_size <= dx <= half_size and -half_size <= dy <= half_size and board[column][row] == -1:   # NEW: boundary and occupancy check
#         draw_piece(dx * cell, -cell // 2 + dy * cell, color)
#         board[column][row] = 1         # NEW: mark position as occupied
#         print(column, row)
#
#         if turn == 0:                  # CHANGED: moved turn toggle inside valid move block
#             turn = 1
#         else:
#             turn = 0
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
#
# t.onscreenclick(on_click)
# t.done()

# ============================================================
# Step 11: Check for a winner after each move
# Goal: Detect 5 consecutive pieces in a row, column, or diagonal
# ============================================================
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
#     if -half_size <= dx <= half_size and -half_size <= dy <= half_size and board[column][row] == -1:
#         draw_piece(dx * cell, -cell // 2 + dy * cell, color)
#         board[column][row] = turn      # CHANGED: store turn value (0 or 1) instead of always 1
#
#         if is_win(column, row, turn):  # NEW: check for winner after placing piece
#             pass                       # NEW: placeholder for win handling (implemented in Step 12)
#
#         if turn == 0:                  # CHANGED: moved turn toggle AFTER win check
#             turn = 1
#         else:
#             turn = 0
#
#
# def is_win(x, y, player):              # NEW: function to check winning condition
#     # 4 directions
#     dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]   # NEW: direction vectors for 4 lines
#
#     for dx, dy in dirs:                # NEW: check each of 4 directions
#         cnt = 1
#         # forward direction
#         tx = x + dx                    # NEW: start from neighbor in forward direction
#         ty = y + dy
#
#         while 0 <= tx <= board_size and 0 <= ty <= board_size and board[tx][ty] == player:   # NEW: count consecutive pieces forward
#             cnt += 1
#             tx += dx
#             ty += dy
#
#         # backward direction
#         tx = x - dx                    # NEW: start from neighbor in backward direction
#         ty = y - dy
#         while 0 <= tx <= board_size and 0 <= ty <= board_size and board[tx][ty] == player:   # NEW: count consecutive pieces backward
#             cnt += 1
#             tx -= dx
#             ty -= dy
#
#         if cnt >= 5:                   # NEW: check if 5 or more in a row
#             print(turn, 'win')
#             return True
#
#     return False                       # NEW: no winner found
#
# t.setup(600, 600)
# t.hideturtle()
# t.tracer(0)
#
# draw_board()
#
# t.onscreenclick(on_click)
# t.done()

# ============================================================
# Step 12 (Final): Game over detection and restart
# Goal: Display winner message and allow clicking to restart the game
# ============================================================
board_size = 14
half_size = board_size // 2
cell = 30
radius = int(cell * 0.9 // 2)
turn = 0
over = False                           # NEW: game over state flag

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
    if over:                           # NEW: check if game is over
        restart()                      # NEW: click to restart
        return                         # NEW: exit early

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
            game_over()                # NEW: call game_over when someone wins

        if turn == 0:
            turn = 1
        else:
            turn = 0


def is_win(x, y, player):
    # 4 directions
    dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for dx, dy in dirs:
        cnt = 1
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

def game_over():                       # NEW: function to handle game over
    global over                        # NEW: declare global to modify over

    t.penup()
    t.goto(0, 250)                     # NEW: position for winner text
    t.write(f"{'black' if turn == 1 else 'white'} wins!", font=("Arial", 24, "bold"), align="center")   # NEW: display winner
    over = True                        # NEW: set game over flag
    return

def restart():                         # NEW: function to restart the game
    global over, turn                  # NEW: declare globals to reset
    over = False                       # NEW: reset game over flag
    turn = 0                           # NEW: reset to white's turn

    t.reset()                          # NEW: clear turtle canvas
    for i in range(len(board)):        # NEW: loop to clear board array
        for j in range(len(board)):    # NEW: inner loop for columns
            board[i][j] = -1           # NEW: reset cell to empty

    draw_board()                       # NEW: redraw the board

t.setup(600, 600)
t.hideturtle()
t.tracer(0)

draw_board()

t.onscreenclick(on_click)
t.done()

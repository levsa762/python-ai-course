import turtle as t
ROW=150

def draw_game(size=3):
    t.hideturtle()
    t.speed(0)
    cell_size = (ROW * 2) / size
    for i in range(1, size):
        t.penup()
        t.goto(-ROW + i * cell_size, ROW)
        t.pendown()
        t.goto(-ROW + i * cell_size, -ROW)
        t.penup()
        t.goto(-ROW, ROW - i * cell_size)
        t.pendown()
        t.goto(ROW, ROW - i * cell_size)

def draw_move(row, col, player, size=3):
    cell_size = (ROW * 2) / size
    x = -ROW + (col - 1) * cell_size + (cell_size / 2)
    y = ROW - (row - 1) * cell_size - (cell_size / 1.5)
    t.penup()
    t.goto(x, y)
    t.write(player, align="center", font=("Arial", int(120/size), "bold"))

def draw_win(frmx, frmy, dstx, dsty, size=3):
    cell_size = (ROW * 2) / size
    x = -ROW + (frmy - 1) * cell_size + (cell_size / 2)
    y = ROW - (frmx - 1) * cell_size - (cell_size / 2)
    dst_x = -ROW + (dsty - 1) * cell_size + (cell_size / 2)
    dst_y = ROW - (dstx - 1) * cell_size - (cell_size / 2)
    t.penup()
    t.goto(x, y)
    t.pensize(3)
    t.pendown()
    t.goto(dst_x, dst_y)
import turtle 
ROW=150

def draw_game(size=3):
    turtle.hideturtle()
    turtle.speed(0)
    cell_size = (ROW * 2) / size
    for i in range(1, size):
        turtle.penup()
        turtle.goto(-ROW + i * cell_size, ROW)
        turtle.pendown()
        turtle.goto(-ROW + i * cell_size, -ROW)
        turtle.penup()
        turtle.goto(-ROW, ROW - i * cell_size)
        turtle.pendown()
        turtle.goto(ROW, ROW - i * cell_size)

def draw_move(row, col, player, size=3):
    cell_size = (ROW * 2) / size
    x = -ROW + (col - 1) * cell_size + (cell_size / 2)
    y = ROW - (row - 1) * cell_size - (cell_size / 1.5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(player, align="center", font=("Arial", int(120/size), "bold"))

def draw_win(frmx, frmy, dstx, dsty, size=3):
    cell_size = (ROW * 2) / size
    x = -ROW + (frmy - 1) * cell_size + (cell_size / 2)
    y = ROW - (frmx - 1) * cell_size - (cell_size / 2)
    dst_x = -ROW + (dsty - 1) * cell_size + (cell_size / 2)
    dst_y = ROW - (dstx - 1) * cell_size - (cell_size / 2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(3)
    turtle.pendown()
    turtle.goto(dst_x, dst_y)
import random as rt
import to_check as ch
import draw 
import load_save as l
import turtle as t


def game_human(list_record,size=3):
    draw.draw_game(size)
    # אם הלוח כבר חצי מלא (מטעינה), נצייר את המהלכים הקיימים
    for r in range(3):
        for c in range(3):
            if list_record[r][c] != " ":
                draw.draw_move(r + 1, c + 1, list_record[r][c],size)

    p1 = t.textinput("Name", "Name for Player X:")
    p2 = t.textinput("Name", "Name for Player O:")

    while ch.full(list_record):
        turn = ch.get_turn(list_record)
        current_player = p1 if turn == "X" else p2

        check = False
        while not check:
            point = t.textinput(f"Turn: {turn}", f"{current_player}, enter row,col (or 'yes' to save):")

            if point and point.lower().strip() == "yes":
                l.save_game(list_record, "h", turn)
                continue  # ממשיך את הלולאה, לא יוצא מהמשחק!

            try:
                x, y = map(int, point.split(","))
                if 1 <= x <= size and 1 <= y <= size:
                    if ch.check_point(list_record, x - 1, y - 1):
                        list_record[x - 1][y - 1] = turn
                        draw.draw_move(x, y, turn,size)
                        check = True
                    else:
                        print("Place occupied!")
                else: print("enter num between 1-sise of game")
            except:
                print("Invalid input please enter 1-3 in patter.")

        if ch.check_win(list_record, turn, current_player,size):
            l.history(f"{current_player} won", p2 if turn == "X" else p1)
            break


def game_computer_strategy(list_record, size=3):
    draw.draw_game(size)
    for r in range(size):
        for c in range(size):
            if list_record[r][c] != " ":
                d.draw_move(r + 1, c + 1, list_record[r][c], size)
    player = t.textinput("name", "please enter your name")
    win = False
    while not win:
      if(ch.full(list_record)==False):
         win=True
      else:
        turn = ch.get_turn(list_record)
        if turn == "X":
            move_found = False
            for shape in ["X", "O"]:
                if not move_found:
                    for r in range(size):
                        for c in range(size):
                            if not move_found and ch.check_point(list_record, r, c):
                                list_record[r][c] = shape
                                if ch.check_win(list_record, shape, "Computer", size, True):
                                    list_record[r][c] = "X"
                                    d.draw_move(r + 1, c + 1, "X", size)
                                    move_found = True
                                    if shape == "X":
                                        win = ch.check_win(list_record, "X", "Computer", size)
                                        l.history("The computer win", player)
                                else: list_record[r][c] = " "
            if not move_found:
                check_r = False
                while not check_r:
                    rx, ry = rt.randint(0, size-1), rt.randint(0, size-1)
                    if ch.check_point(list_record, rx, ry):
                        list_record[rx][ry] = "X"
                        d.draw_move(rx + 1, ry + 1, "X", size)
                        check_r = True
                        if ch.check_win(list_record, "X", "Computer", size):
                            win = True
                            l.history("The computer win", player)
        else:
            check_p = False
            while not check_p:
                point = t.textinput(f"Your turn - {turn}", f"enter 1,{size} or 'yes' to save")
                if point is None: continue
                if point.lower().strip() == "yes":
                    l.save_game(list_record, "a", "O")
                    continue
                try:
                    x, y = map(int, point.split(","))
                    if 1 <= x <= size and 1 <= y <= size:
                        if ch.check_point(list_record, x - 1, y - 1):
                            list_record[x - 1][y - 1] = "O"
                            d.draw_move(x, y, "O", size)
                            check_p = True
                            if ch.check_win(list_record, "O", player, size):
                                win = True
                                l.history(player + " won", "computer")
                        else: print("The place is occupied")
                    else: print(f"the num must be between 1 and {size}")
                except: print("the place is not good enter again")

def game_computer_random(list_record, size=3):
    d.draw_game(size)
    # אם הלוח כבר חצי מלא (מטעינה), נצייר את המהלכים הקיימים
    for r in range(3):
        for c in range(3):
            if list_record[r][c] != " ":
                d.draw_move(r + 1, c + 1, list_record[r][c], size)
    player = t.textinput("name", "please enter your name")
    win = False
    while not win:
      if(ch.full(list_record)==False):
          win=True
      else:
        turn = ch.get_turn(list_record)
        if turn == "X":
            check_r = False
            while not check_r:
                rx, ry = rt.randint(0, size-1), rt.randint(0, size-1)
                if ch.check_point(list_record, rx, ry):
                    list_record[rx][ry] = "X"
                    d.draw_move(rx + 1, ry + 1, "X", size)
                    check_r = True
                    if ch.check_win(list_record, "X", "Computer", size):
                        win = True
                        l.history("The computer win", player)
        else:
            check_p = False
            while not check_p:
                point = t.textinput(f"Your turn - {turn}", f"enter 1,{size} or 'yes' to save")
                if point is None: continue
                if point.lower().strip() == "yes":
                    l.save_game(list_record, "r", "O")
                    continue
                try:
                    x, y = map(int, point.split(","))
                    if 1 <= x <= size and 1 <= y <= size:
                        if ch.check_point(list_record, x - 1, y - 1):
                            list_record[x - 1][y - 1] = "O"
                            d.draw_move(x, y, "O", size)
                            check_p = True
                            if ch.check_win(list_record, "O", player, size):
                                win = True
                                l.history(player + " won", "computer")
                        else: print("The place is occupied")
                    else: print(f"the num must be between 1 and {size}")
                except: print("the place is not good enter again")
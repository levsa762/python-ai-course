import random 
import to_check
import draw 
import load_save
import turtle

# Constants
YES_NO = ["yes", "no"]
MODES = ["h", "c"]
TYPES = ["a", "r"]
SIZES = ["3", "4"]

def game_human(list_record,size):
    draw.draw_game(size)
    # אם הלוח כבר חצי מלא (מטעינה), נצייר את המהלכים הקיימים
    for r in range(size):
        for c in range(size):
            if list_record[r][c] != " ":
                draw.draw_move(r + 1, c + 1, list_record[r][c],size)

    p1 = turtle.textinput("Name", "Name for Player X:")
    p2 = turtle.textinput("Name", "Name for Player O:")

    while to_check.full(list_record):
        turn = to_check.get_turn(list_record)
        current_player = p1 if turn == "X" else p2

        check = False
        while not check:
            point = turtle.textinput(f"Turn: {turn}", f"{current_player}, enter row,col (or 'yes' to save):")

            if point and point.lower().strip() == "yes":
                load_save.save_game(list_record, "h")
                continue  # ממשיך את הלולאה, לא יוצא מהמשחק!

            try:
                x, y = map(int, point.split(","))
                if 1 <= x <= size and 1 <= y <= size:
                    if to_check.check_point(list_record, x - 1, y - 1):
                        list_record[x - 1][y - 1] = turn
                        draw.draw_move(x, y, turn,size)
                        check = True
                    else:
                        print("Place occupied!")
                else: print("enter num between 1-sise of game")
            except:
                print("Invalid input please enter 1-3 in patter.")

        if to_check.check_win(list_record, turn, current_player,size):
            load_save.history(f"{current_player} won", p2 if turn == "X" else p1)
            break


def game_computer_strategy(list_record, size=3):
    draw.draw_game(size)
    for r in range(size):
        for c in range(size):
            if list_record[r][c] != " ":
                draw.draw_move(r + 1, c + 1, list_record[r][c], size)
    player = turtle.textinput("name", "please enter your name")
    win = False
    while not win:
      if(to_check.full(list_record)==False):
         win=True
      else:
        turn = to_check.get_turn(list_record)
        if turn == "X":
            move_found = False
            for shape in ["X", "O"]:
                if not move_found:
                    for r in range(size):
                        for c in range(size):
                            if not move_found and to_check.check_point(list_record, r, c):
                                list_record[r][c] = shape
                                if to_check.check_win(list_record, shape, "Computer", size, True):
                                    list_record[r][c] = "X"
                                    draw.draw_move(r + 1, c + 1, "X", size)
                                    move_found = True
                                    if shape == "X":
                                        win = to_check.check_win(list_record, "X", "Computer", size)
                                    load_save.history("The computer won", player)
                                else: list_record[r][c] = " "
            if not move_found:
                check_r = False
                while not check_r:
                    rx, ry = random.randint(0, size-1), random.randint(0, size-1)
                    if to_check.check_point(list_record, rx, ry):
                        list_record[rx][ry] = "X"
                        draw.draw_move(rx + 1, ry + 1, "X", size)
                        check_r = True
                        if to_check.check_win(list_record, "X", "Computer", size):
                            win = True
                            load_save.history("The computer won", player)
        else:
            check_p = False
            while not check_p:
                point = turtle.textinput(f"Your turn - {turn}", f"enter 1,{size} or 'yes' to save")
                if point is None: continue
                if point.lower().strip() == "yes":
                    load_save.save_game(list_record, "a")
                    continue
                try:
                    x, y = map(int, point.split(","))
                    if 1 <= x <= size and 1 <= y <= size:
                        if to_check.check_point(list_record, x - 1, y - 1):
                            list_record[x - 1][y - 1] = "O"
                            draw.draw_move(x, y, "O", size)
                            check_p = True
                            if to_check.check_win(list_record, "O", player, size):
                                win = True
                                load_save.history(player + " won", "computer")
                        else: print("The place is occupied")
                    else: print(f"the num must be between 1 and {size}")
                except: print("the place is not good enter again")

def game_computer_random(list_record, size):
    draw.draw_game(size)
    # אם הלוח כבר חצי מלא (מטעינה), נצייר את המהלכים הקיימים
    for r in range(size):
        for c in range(size):
            if list_record[r][c] != " ":
                draw.draw_move(r + 1, c + 1, list_record[r][c], size)
    player = turtle.textinput("name", "please enter your name")
    win = False
    while not win:
      if(to_check.full(list_record)==False):
          win=True
      else:
        turn = to_check.get_turn(list_record)
        if turn == "X":
            check_r = False
            while not check_r:
                rx, ry = random.randint(0, size-1), random.randint(0, size-1)
                if to_check.check_point(list_record, rx, ry):
                    list_record[rx][ry] = "X"
                    draw.draw_move(rx + 1, ry + 1, "X", size)
                    check_r = True
                    if to_check.check_win(list_record, "X", "Computer", size):
                        win = True
                        load_save.history("The computer won", player)
        else:
            check_p = False
            while not check_p:
                point = turtle.textinput(f"Your turn - {turn}", f"enter 1,{size} or 'yes' to save")
                if point is None: continue
                if point.lower().strip() == "yes":
                    load_save.save_game(list_record, "r")
                    continue
                try:
                    x, y = map(int, point.split(","))
                    if 1 <= x <= size and 1 <= y <= size:
                        if to_check.check_point(list_record, x - 1, y - 1):
                            list_record[x - 1][y - 1] = "O"
                            draw.draw_move(x, y, "O", size)
                            check_p = True
                            if to_check.check_win(list_record, "O", player, size):
                                win = True
                                load_save.history(player + " won", "computer")
                        else: print("The place is occupied")
                    else: print(f"the num must be between 1 and {size}")
                except: print("the place is not good enter again")


def get_input(title, prompt, valid_options):
    """Get and validate user input."""
    while True:
        answer = turtle.textinput(title, prompt)
        if answer and answer.lower().strip() in valid_options:
            return answer.lower().strip()
        print(f"Invalid input. Please enter: {', '.join(valid_options)}")

def start_game(board, size, mode):
    """Start game with specified mode."""
    game_map = {
        "h": game_human,
        "a": game_computer_strategy,
        "r": game_computer_random
    }
    game_map[mode](board, size)

def handle_load_game():
    """Handle loading a saved game."""
    try:
        list_record, flag = load_save.load()
        size = len(list_record)
        start_game(list_record, size, flag)
        return True
    except Exception as e:
        print(f"Failed to load game: {e}")
        return False

def handle_new_game():
    """Handle starting a new game."""
    # Show history
    if get_input("History", "Show game history? (yes/no)", YES_NO) == "yes":
        load_save.show_history()
    
    # Get board size
    size = int(get_input("Size", "Choose board size - 3 for 3x3, 4 for 4x4:", SIZES))
    
    # Initialize board
    board = [[" " for _ in range(size)] for _ in range(size)]
    
    # Get game mode
    mode = get_input("Mode", "Select mode - h: Human vs Human, c: vs Computer", MODES)
    
    if mode == "h":
        start_game(board, size, "h")
    else:
        game_type = get_input("Computer Type", "a: Strategic AI, r: Random AI", TYPES)
        start_game(board, size, game_type)
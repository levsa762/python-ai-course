import games 
import load_save 
import turtle 


def main():
    # --- שלב 1: קודם כל שואלים על טעינה ---
    check_load = False
    load = ""
    while not check_load:
        ans = turtle.textinput("Load", "Do you want to load last game? (yes/no)")
        if ans and ans.lower().strip() in ["yes", "no"]:
            load = ans.lower().strip()
            check_load = True
        else:
            print("Please enter yes or no")

    # --- שלב 2: ניתוב לפי בחירת הטעינה ---
    if load == "yes":
        list_record, flag, turn = load_save.load()
        size = len(list_record)  # מזהה אוטומטית אם זה 3 או 4 מהקובץ

        if flag == "h":
            games.game_human(list_record, size)
        elif flag == "a":
            games.game_computer_strategy(list_record, size)
        elif flag == "r":
            games.game_computer_random(list_record, size)

    else:
        # אם בחר NO - שואלים את שאר השאלות בסדר הנכון
        check_h = False
        while not check_h:
            h_input = turtle.textinput("History", "Show history? (yes/no)")
            if h_input and h_input.lower().strip() in ["yes", "no"]:
                if h_input.lower().strip() == "yes": load_save.show_history()
                check_h = True
            else:
                print("Please enter yes or no")

        check_s = False
        size = 3
        while not check_s:
            try:
                s_input = turtle.textinput("Size", "for 3x3-3, for 4x4-4:")
                if s_input in ["3", "4"]:
                    size = int(s_input)
                    check_s = True
                else:
                    print("Please enter 3 or 4")
            except:
                print("Invalid input")

        list_record = [[" " for _ in range(size)] for _ in range(size)]

        check_m = False
        while not check_m:
            m = turtle.textinput("Mode", "h-Human, c-Computer")
            if m and m.lower().strip() in ["h", "c"]:
                mode = m.lower().strip()
                check_m = True
            else:
                print("Please enter h or c")

        if mode == "h":
            games.game_human(list_record, size)
        else:
            check_t = False
            while not check_t:
                ty = turtle.textinput("Type", "a-strategy, r-random")
                if ty and ty.lower().strip() in ["a", "r"]:
                    if ty.lower().strip() == "a":
                        games.game_computer_strategy(list_record, size)
                    else:
                        games.game_computer_random(list_record, size)
                    check_t = True
                else:
                    print("Please enter a or r")
    turtle.done()


if __name__ == "__main__":
    main()
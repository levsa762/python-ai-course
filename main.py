import games 
import load_save 
import turtle 


def main():
    # --- שלב 1: קודם כל שואלים על טעינה ---
    check_load = False
    load = ""
    while not check_load:
        answer = turtle.textinput("Load", "Do you want to load last game? (yes/no)")
        if answer and answer.lower().strip() in ["yes", "no"]:
            load = answer.lower().strip()
            check_load = True
        else:
            print("Please enter yes or no")

    # --- שלב 2: ניתוב לפי בחירת הטעינה ---
    if load == "yes":
        list_record, flag, _ = load_save.load()
        size = len(list_record)  # מזהה אוטומטית אם זה 3 או 4 מהקובץ

        if flag == "h":
            games.game_human(list_record, size)
        elif flag == "a":
            games.game_computer_strategy(list_record, size)
        elif flag == "r":
            games.game_computer_random(list_record, size)

    else:
        # אם בחר NO - שואלים את שאר השאלות בסדר הנכון
        check_human = False
        while not check_human:
            h_input = turtle.textinput("History", "Show history? (yes/no)")
            if h_input and h_input.lower().strip() in ["yes", "no"]:
                if h_input.lower().strip() == "yes": load_save.show_history()
                check_human = True
            else:
                print("Please enter yes or no")

        check_size = False
        size = 3
        while not check_size:
            try:
                s_input = turtle.textinput("Size", "for 3x3-3, for 4x4-4:")
                if s_input in ["3", "4"]:
                    size = int(s_input)
                    check_size = True
                else:
                    print("Please enter 3 or 4")
            except:
                print("Invalid input")

        list_record = [[" " for _ in range(size)] for _ in range(size)]

        check_mode = False
        while not check_mode:
            m = turtle.textinput("Mode", "h-Human, c-Computer")
            if m and m.lower().strip() in ["h", "c"]:
                mode = m.lower().strip()
                check_mode = True
            else:
                print("Please enter h or c")

        if mode == "h":
            games.game_human(list_record, size)
        else:
            check_type = False
            while not check_type:
                type_input = turtle.textinput("Type", "a-strategy, r-random")
                if type_input and type_input.lower().strip() in ["a", "r"]:
                    if type_input.lower().strip() == "a":
                        games.game_computer_strategy(list_record, size)
                    else:
                        games.game_computer_random(list_record, size)
                    check_type = True
                else:
                    print("Please enter a or r")
    turtle.done()


if __name__ == "__main__":
    main()
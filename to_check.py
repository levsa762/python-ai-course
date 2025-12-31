import draw 


def get_turn(list_record):
    count = 0
    for row in list_record:
        for cell in row:
            if cell != " ": count += 1
    return "X" if count % 2 == 0 else "O"

def check_win(list_record, char, name, size=3, is_sim=False):
    # בדיקת שורות
    for i in range(size):
        # הפקודה all בודקת אם כל התאים בשורה i הם ה-char המבוקש
        if all(list_record[i][j] == char for j in range(size)):
            if not is_sim:
                draw.draw_win(i+1, 1, i+1, size, size)
                print(f"{name} won!")
            return True

    # בדיקת עמודות
    for j in range(size):
        # בודק אם כל התאים בעמודה j הם ה-char המבוקש
        if all(list_record[i][j] == char for i in range(size)):
            if not is_sim:
                draw.draw_win(1, j+1, size, j+1, size)
                print(f"{name} won!")
            return True

    # בדיקת אלכסון ראשי (מלמעלה שמאל למטה ימין)
    if all(list_record[i][i] == char for i in range(size)) and char != " ":
        if not is_sim:
            draw.draw_win(1, 1, size, size, size)
            print(f"{name} won!")
        return True

    # בדיקת אלכסון משני (מלמעלה ימין למטה שמאל)
    if all(list_record[i][size - 1 - i] == char for i in range(size)) and char != " ":
        if not is_sim:
            draw.draw_win(1, size, size, 1, size)
            print(f"{name} won!")
        return True

    return False

def full(list_record):
    for row in list_record:
        if " " in row: return True
    print("Tie!")
    return False

def check_point(list_record, x, y):
    return list_record[x][y] == " "
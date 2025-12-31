import pickle

def save_game(list_record, flag):
    try:
        with open("list.dat", 'wb') as file:
            # שמירה של הלוח, סוג המשחק והתור הנוכחי
            pickle.dump((list_record, flag), file)
        print("--- The game was saved successfully! ---")
    except:
        print("Error: Could not save the game.")

def load():
    try:
        with open("list.dat", 'rb') as file:
            # טעינה באותו סדר בדיוק
            list_record, flag = pickle.load(file)
            print("--- Game loaded successfully! ---")
            return list_record, flag
    except:
        print("No saved game found. Starting a new board.")
        list_record = [[" " for _ in range(3)] for _ in range(3)]
        return list_record, "h", "X"

def history(winner_msg, opponent):
    try:
        with open("history.txt", 'a') as file:
            file.write(f"Result: {winner_msg}, Opponent: {opponent}\n")
    except:
        print("Error saving history.")
def show_history():
    try:
        with open("history.txt", 'r') as file:
            print("--- Games History ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No history found.")
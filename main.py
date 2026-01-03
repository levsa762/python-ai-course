# Student1 name: Nachman Zilberman Id: 322255738
# Student2 name: Lev sakaju Id: 209266667

import games
import load_save 
import turtle



def main():
    """Main game entry point."""
    load_choice = games.get_input("Load Game", "Load saved game? (yes/no)", games.YES_NO)
    
    if load_choice == "yes":
        if not games.handle_load_game():
            print("Starting new game instead...")
            games.handle_new_game()
    else:
        games.handle_new_game()

    turtle.done()

if __name__ == "__main__":
    main()
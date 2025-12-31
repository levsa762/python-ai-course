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
SAVE_KEYWORD = "yes"


# ============================================
# Board State Functions
# ============================================

def is_board_full(board):
    """Check if board has available moves."""
    return to_check.full(board)


def get_current_turn(board):
    """Get whose turn it is (X or O)."""
    return to_check.get_turn(board)


def is_valid_move(board, row, col, size):
    """Check if a move is valid."""
    return (0 <= row < size and 
            0 <= col < size and 
            to_check.check_point(board, row, col))


def make_move(board, row, col, symbol, size):
    """Make a move on the board and draw it."""
    if is_valid_move(board, row, col, size):
        board[row][col] = symbol
        draw.draw_move(row + 1, col + 1, symbol, size)
        return True
    return False


def check_winner(board, symbol, player_name, size, silent=False):
    """Check if the current move wins the game."""
    return to_check.check_win(board, symbol, player_name, size, silent)


# ============================================
# Game Initialization Functions
# ============================================

def initialize_game(size):
    """Initialize and draw the game board."""
    draw.draw_game(size)


def redraw_existing_moves(board, size):
    """Redraw moves from a loaded game."""
    for r in range(size):
        for c in range(size):
            if board[r][c] != " ":
                draw.draw_move(r + 1, c + 1, board[r][c], size)


# ============================================
# Input Functions
# ============================================

def get_player_input(board, size, player_name, symbol, save_flag):
    """
    Get and validate player input for a move.
    Returns: (row, col) tuple or None if invalid.
    """
    while True:
        prompt = f"{player_name}, enter row,col (1-{size}) or '{SAVE_KEYWORD}' to save:"
        point = turtle.textinput(f"Turn: {symbol}", prompt)
        
        if point is None:
            continue
        
        point = point.strip().lower()
        
        # Check for save request
        if point == SAVE_KEYWORD:
            load_save.save_game(board, save_flag)
            print("Game saved!")
            continue
        
        # Parse move input
        try:
            x, y = map(int, point.split(","))
            row, col = x - 1, y - 1  # Convert to 0-indexed
            
            if not (1 <= x <= size and 1 <= y <= size):
                print(f"Numbers must be between 1 and {size}")
                continue
            
            if not is_valid_move(board, row, col, size):
                print("That position is already occupied!")
                continue
            
            return row, col
            
        except ValueError:
            print(f"Invalid format. Please enter as: row,col (e.g., 1,2)")
        except Exception as e:
            print(f"Error processing input: {e}")


# ============================================
# Computer AI Functions
# ============================================

def get_computer_strategic_move(board, size):
    """
    Get strategic move for computer (X).
    Strategy: 
    1. Check if computer can win
    2. Check if need to block opponent
    3. Random move as fallback
    """
    # First try to win, then try to block
    for target_symbol in ["X", "O"]:
        for r in range(size):
            for c in range(size):
                if is_valid_move(board, r, c, size):
                    # Simulate move
                    board[r][c] = target_symbol
                    
                    # Check if this wins
                    if check_winner(board, target_symbol, "Computer", size, silent=True):
                        board[r][c] = " "  # Undo simulation
                        return r, c  # This is the winning/blocking move
                    
                    board[r][c] = " "  # Undo simulation
    
    # No strategic move found - use random move
    return get_computer_random_move(board, size)


def get_computer_random_move(board, size):
    """Get random valid move for computer."""
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if is_valid_move(board, row, col, size):
            return row, col


# ============================================
# Turn Playing Functions
# ============================================

def play_human_turn(board, size, player_name, symbol, save_flag):
    """
    Play a human player's turn.
    Returns: True if move was made successfully.
    """
    move = get_player_input(board, size, player_name, symbol, save_flag)
    if move:
        row, col = move
        return make_move(board, row, col, symbol, size)
    return False


def play_computer_turn(board, size, symbol, use_strategy):
    """
    Play a computer's turn.
    Returns: True if move was made successfully.
    """
    if use_strategy:
        row, col = get_computer_strategic_move(board, size)
    else:
        row, col = get_computer_random_move(board, size)
    
    return make_move(board, row, col, symbol, size)


# ============================================
# Main Game Functions
# ============================================

def game_human(list_record, size):
    """Human vs Human game."""
    initialize_game(size)
    redraw_existing_moves(list_record, size)
    
    # Get player names
    p1 = turtle.textinput("Player 1", "Name for Player X:") or "Player 1"
    p2 = turtle.textinput("Player 2", "Name for Player O:") or "Player 2"
    
    # Main game loop
    game_over = False
    while not game_over and is_board_full(list_record):
        symbol = get_current_turn(list_record)
        current_player = p1 if symbol == "X" else p2
        opponent = p2 if symbol == "X" else p1
        
        # Get player move
        play_human_turn(list_record, size, current_player, symbol, "h")
        
        # Check for winner
        if check_winner(list_record, symbol, current_player, size):
            load_save.history(f"{current_player} won", opponent)
            game_over = True
    
    # Check for tie
    if not game_over and not is_board_full(list_record):
        print("Game Over - It's a tie!")


def game_computer_strategy(list_record, size):
    """Human vs Strategic Computer game."""
    initialize_game(size)
    redraw_existing_moves(list_record, size)
    
    # Get player name
    player = turtle.textinput("Player Name", "Please enter your name:") or "Player"
    
    # Main game loop
    game_over = False
    while not game_over and is_board_full(list_record):
        symbol = get_current_turn(list_record)
        
        if symbol == "X":
            # Computer's turn (strategic)
            play_computer_turn(list_record, size, symbol, use_strategy=True)
            
            # Check if computer won
            if check_winner(list_record, symbol, "Computer", size):
                load_save.history("The computer won", player)
                game_over = True
        else:
            # Player's turn
            play_human_turn(list_record, size, player, symbol, "a")
            
            # Check if player won
            if check_winner(list_record, symbol, player, size):
                load_save.history(f"{player} won", "Computer")
                game_over = True
    
    # Check for tie
    if not game_over and not is_board_full(list_record):
        print("Game Over - It's a tie!")


def game_computer_random(list_record, size):
    """Human vs Random Computer game."""
    initialize_game(size)
    redraw_existing_moves(list_record, size)
    
    # Get player name
    player = turtle.textinput("Player Name", "Please enter your name:") or "Player"
    
    # Main game loop
    game_over = False
    while not game_over and is_board_full(list_record):
        symbol = get_current_turn(list_record)
        
        if symbol == "X":
            # Computer's turn (random)
            play_computer_turn(list_record, size, symbol, use_strategy=False)
            
            # Check if computer won
            if check_winner(list_record, symbol, "Computer", size):
                load_save.history("The computer won", player)
                game_over = True
        else:
            # Player's turn
            play_human_turn(list_record, size, player, symbol, "r")
            
            # Check if player won
            if check_winner(list_record, symbol, player, size):
                load_save.history(f"{player} won", "Computer")
                game_over = True
    
    # Check for tie
    if not game_over and not is_board_full(list_record):
        print("Game Over - It's a tie!")


# ============================================
# Helper functions for main.py
# ============================================

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
    if mode in game_map:
        game_map[mode](board, size)
    else:
        print(f"Unknown game mode: {mode}")


def handle_load_game():
    """Handle loading a saved game."""
    try:
        list_record, flag = load_save.load()
        size = len(list_record)
        start_game(list_record, size, flag)
        return True
    except FileNotFoundError:
        print("No saved game found.")
        return False
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
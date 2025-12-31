# test_games.py
import games

# -------------------------
# Fake / mock dependencies
# -------------------------

def fake_full(board):
    # Board is full if no spaces remain
    return any(" " in row for row in board)

def fake_get_turn(board):
    # X starts, alternate by count
    count_x = sum(row.count("X") for row in board)
    count_o = sum(row.count("O") for row in board)
    return "X" if count_x == count_o else "O"

def fake_check_point(board, row, col):
    return board[row][col] == " "

def fake_check_win(board, symbol, player_name, size, silent=False):
    # Simple row-based win check (enough for unit testing)
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    return False

def fake_draw_move(*args, **kwargs):
    pass

def fake_draw_game(*args, **kwargs):
    pass


# Inject mocks
games.to_check.full = fake_full
games.to_check.get_turn = fake_get_turn
games.to_check.check_point = fake_check_point
games.to_check.check_win = fake_check_win
games.draw.draw_move = fake_draw_move
games.draw.draw_game = fake_draw_game


# -------------------------
# Tests: Board state
# -------------------------

def test_is_board_full_true():
    board = [["X", "O"], ["O", "X"]]
    assert games.is_board_full(board) is False

def test_is_board_full_false():
    board = [["X", " "], ["O", "X"]]
    assert games.is_board_full(board) is True

def test_get_current_turn_x():
    board = [[" ", " "], [" ", " "]]
    assert games.get_current_turn(board) == "X"

def test_get_current_turn_o():
    board = [["X", " "], [" ", " "]]
    assert games.get_current_turn(board) == "O"


# -------------------------
# Tests: Moves
# -------------------------

def test_is_valid_move_true():
    board = [[" ", " "], [" ", " "]]
    assert games.is_valid_move(board, 0, 0, 2) is True

def test_is_valid_move_false_out_of_bounds():
    board = [[" ", " "], [" ", " "]]
    assert games.is_valid_move(board, 3, 0, 2) is False

def test_is_valid_move_false_occupied():
    board = [["X", " "], [" ", " "]]
    assert games.is_valid_move(board, 0, 0, 2) is False

def test_make_move_success():
    board = [[" ", " "], [" ", " "]]
    result = games.make_move(board, 0, 1, "X", 2)
    assert result is True
    assert board[0][1] == "X"

def test_make_move_fail():
    board = [["X", " "], [" ", " "]]
    result = games.make_move(board, 0, 0, "O", 2)
    assert result is False


# -------------------------
# Tests: Winner
# -------------------------

def test_check_winner_true():
    board = [["X", "X"], ["O", "O"]]
    assert games.check_winner(board, "X", "Player", 2) is True

def test_check_winner_false():
    board = [["X", " "], ["O", " "]]
    assert games.check_winner(board, "X", "Player", 2) is False


# -------------------------
# Tests: Computer moves
# -------------------------

def test_computer_random_move_valid():
    board = [["X", " "], ["O", " "]]
    row, col = games.get_computer_random_move(board, 2)
    assert board[row][col] == " "

def test_computer_strategic_move_blocks():
    board = [
        ["O", "O", " "],
        ["X", " ", " "],
        [" ", " ", "X"]
    ]
    row, col = games.get_computer_strategic_move(board, 3)
    assert (row, col) == (0, 2)

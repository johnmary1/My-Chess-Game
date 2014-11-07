from chess_board import *
from chess_turn import *
from chess_pieces import *
from movement import *
# I'm indiscriminately importing for now for ease of getting the program up and running

def __main__():
    board = create_board()
    white_pieces = create_white_pieces(board)
    black_pieces = create_black_pieces(board)
    # Insert some sort of start up message
    # Insert question, do you want to play a new game
    row_from, column_from = get_from_space()
    row_to, column_to = get_to_space()

__main__()







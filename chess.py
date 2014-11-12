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
    perform_move(board, row_from, row_to, column_from, column_to)

def perform_move(board, row_from, row_to, column_from, column_to):
    from_space = board[row_from][column_from]    
    to_space = board[row_to][column_to]
    moving_piece = from_space.occupying_piece
    taken_piece = to_space.occupying_piece
    available_moves = moving_piece.threatening(board)
    if to_space in available_moves:
        from_space.occupying_piece = None
        to_space.occupy_piece = moving_piece
        if taken_piece != None:
            # Don't know how to remove piece from pieces list yet.
            # Might need to change pieces list from a simple list
            # To it's own class.
        else:
            pass
    else:
        print "That is not a valid move!"
               
   

__main__()







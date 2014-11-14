from chess_board import *
from chess_turn import *
from chess_pieces import *
from movement import *
# I'm indiscriminately importing for now for ease of getting the program up and running

def __main__():
    board = create_board()
    white = set_of_pieces("white")
    black = set_of_pieces("black")
    white.pieces = white.create_pieces(board)
    black.pieces = black.create_pieces(board) 
    # Insert some sort of start up message
    # Insert question, do you want to play a new game
    loop_turn(board)


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
            pass
        else:
            pass
    else:
        print "That is not a valid move!"

def check_test(color, board):
    pass           

def threatening_space_check(board, row_from, row_to, column_from, column_to):   
    from_space = board[row_from][column_from]    
    to_space = board[row_to][column_to]
    moving_piece = from_space.occupying_piece
    taken_piece = to_space.occupying_piece
    available_moves = moving_piece.threatening(board)
    print available_moves

    # threatening_space_check(board, row_from, row_to, column_from, column_to)

def loop_turn(board):
    continue_to_play = True
    while continue_to_play == True:
        row_from, column_from = get_from_space()
        row_to, column_to = get_to_space()
        perform_move(board, row_from, row_to, column_from, column_to)
        ask_quit = raw_input("If you wish to quit, press q now. Otherwise the game will continue.")
        if ask_quit == "q":
            continue_to_play == False
        else:
            pass

__main__()







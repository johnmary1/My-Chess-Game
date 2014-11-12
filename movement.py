"""
This file contains the various movement classes which are instantiated in the pieces
file.
"""


class Movement(object):
    def __init__(self):
        pass

class HorizontalMove(Movement):
    def __init__(self):
        pass

    def __str__(self):
        return "horizontal"
    
    # Returns a list of squares threatened. Does not determine if king is threatened. 
    def squares_threatening(self, unchanging_row, start_column, board):
        threatened_squares = []        
        for column in range(start_column + 1, 8):
            if column == 8:
                break 
            elif board[unchanging_row][column].occupying_piece == None:
                threatened_squares.append(board[unchanging_row][column])
            elif board[unchanging_row][column].occupying_piece.color \
            != board[unchanging_row][start_column].occupying_piece.color:
                threatened_squares.append(board[unchanging_row][column])
                break
            else:
                break
        for column in range(start_column -1, -1, -1):
            if column == -1:
                break
            elif board[unchanging_row][column].occupying_piece == None:
                threatened_squares.append(board[unchanging_row][column])
            elif board[unchanging_row][column].occupying_piece.color \
            != board[unchanging_row][start_column].occupying_piece.color:
                threatened_squares.append(board[unchanging_row][column])
                break
            else:
                break
        return threatened_squares        

class VerticalMove(Movement):
    def __init__(self):
        pass
    
    def __str__(self):
        return "vertical"

    # Returns a list of squares threatened. Does not determine if king is threatened. 
    def squares_threatening(self, start_row, unchanging_column, board):
        threatened_squares = []        
        for row in range(start_row + 1, 8):
            if row == 8:
                break 
            elif board[row][unchanging_column].occupying_piece == None:
                threatened_squares.append(board[row][unchanging_column])
            elif board[row][unchanging_column].occupying_piece.color \
            != board[start_row][unchanging_column].occupying_piece.color:
                threatened_squares.append(board[row][unchanging_column])
                break
            else:
                break
        for column in range(start_row -1, -1, -1):
            if row == -1:
                break
            elif board[row][unchanging_column].occupying_piece == None:
                threatened_squares.append(board[row][unchanging_column])
            elif board[row][unchanging_column].occupying_piece.color \
            != board[start_row][unchanging_column].occupying_piece.color:
                threatened_squares.append(board[row][unchanging_column])
                break
            else:
                break
        return threatened_squares  

class DiagonalMove(Movement):
    def __init__(self):
        pass    

    def __str__(self):
        return "diagonal"
    
    def squares_threatening(self, start_row, start_column, board):
        threatened_squares = []
        # This is a little different because as I do it now, I need to include two separate
        # if statements under my single for loop but if I do this then I can't use breaks
        # like I do in my horizontal and vertical movement classes.
        # How do I deal with the king that can only move diagonal one space
        threatened_squares = []
        for each_row in range(start_row + 1, 8):
        i = 1
            if board[start_column + i][each_row].occupying_piece == None:
                squares_threatened.append(board[start_column + i][each_row]
            if board[start_column - i][each_row].occupying_piece == None:
                squares_threatened.append(board[start_column - i][each_row]
            i +=1
        return threatened_squares  

class KingMove(Movement):
    def __init__(self):
        pass

    def __str__(self):
        return "king move"
   
    def squares_threatening(self, start_row, start_column, board):
        threatened_squares = []
        for row in range(start_row - 1, start_row + 2):
            for column in range(start_column - 1, start_column + 2):
                if column == -1 or row == -1 or column == 8 or row == 8:
                    pass
                elif row == start_row and column = start_column:
                    pass
                # Check if the first part of this elif is necessary
                elif board[row][column].occupying_piece != None and \
                board[row][column].occupying_piece.color == \
                board[start_row][start_column].occupying_piece.color:
                    pass
                # Problem to fix... what if opposite king is within a space
                # Same problem if move puts king in check...
                # Am going to need to run each of these squares through opposite
                # colors threatened squares and remove any that are threatened
                # Problem to return to at end of threatened_square total solution
                else:
                    threatened_squares.append(board[row][colum])                               
        return threatened_squares    

class PawnMove(Movement):
    # This will not currently build in en passant functionality
    def __init__(self):
        pass

    def __str__(self):
        return "pawn move"
  
    def squares_threatening(self, start_column, start_row, board):
        threatened_squares = []
            if board[start_row][start_column].occupying_piece.moved_yet == False \
            and board[start_row + 1][start_column].occupying_piece == None and \
            board[start_row + 2][start_column].occupying_piece == None:
                threatened_squares.append(board[start_row + 1][start_column])
                threatened_squares.append(board[start_row + 2][start_column])
            elif board[start_row + 1][start_column] == None:
                threatened_squares.append(board[start_row + 1][start_column])
            else:
                pass

            if start_column - 1 >= 0:
                if board[start_row + 1][start_column - 1].occupying_piece != None \
                board[start_row + 1][start_column - 1].occupying_piece.color \
                != board[start_row][start_column].occupying_piece.color:
                    threatened_squares.append(board[start_row + 1][start_column - 1]
                else:
                    pass
            else:
                pass

            if start_column + 1 <= 7:
                if board[start_row + 1][start_column - 1].occupying_piece != None \
                board[start_row + 1][start_column + 1].occupying_piece.color \
                != board[start_row][start_column].occupying_piece.color:
                    threatened_squares.append(board[start_row + 1][start_column + 1]
                else:
                    pass
            else:
                pass                            
        return threatened_squares


class Capture(Movement):
    def __init__(self):
        pass
    
    def perform(self):
        pass

class Castle(Movement):
    def __init__(self):
        pass
    
    def perform(self):
        pass

class Promotion(Movement):
    def __init__(self):
        pass
    
    def perform(self):
        pass

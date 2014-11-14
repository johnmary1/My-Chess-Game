""" This file creates the pieces. 
"""
from movement import *

# Create a general class for pieces
class Piece(object):  
    def __init__(self):
        # I need to figure out why this doesn't pass to all children classes...
        # Thought it would... Having trouble with this property generally       
        self.moved_yet = False    

class Pawn(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        self.moved_yet = False
        board[self.row][self.column].occupying_piece = self
    
    def __repr__(self):
        return "pawn"    

    def threatening(self, board):
        # Problem, this doesn't register diagonal captures as possible moves if there
        # isn't a piece there... this could be trouble for determining check
        # Other problem... I only thought about this function with respect to white...
        # Black the numbers need to go in the other direction..
        move_one = PawnMove()
        threatened_squares = move_one.squares_threatening(self.row, self.column, board)
        return threatened_squares

class Rook(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self
    
    def __repr__(self):
        return "rook" 
              
    def threatening(self, board):
        move_one = HorizontalMove()
        move_two = VerticalMove()
        threatened_squares_one = move_one.squares_threatening(self.row, self.column, board)
        threatened_squares_two = move_two.squares_threatening(self.row, self.column, board)
        threatened_squares = threatened_squares_one + threatened_squares_two
        return threatened_squares

class Knight(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.column = column
        self.row = row
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self  
    
    def __repr__(self):
        return "knight" 

class Bishop(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self  
    
    def __repr__(self):
        return "bishop" 

    def threatening(self, board):
        move_one = DiagonalMove()
        threatened_squares = move_one.squares_threatening(self.row, self.column, board)
        return threatened_squares

class Queen(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self  
    
    def __repr__(self):
        return "queen" 

    def threatening(self, board):
        move_one = HorizontalMove()
        move_two = VerticalMove()
        move_three = DiagonalMove()
        threatened_one = move_one.squares_threatening(self.row, self.column, board)
        threatened_two = move_two.squares_threatening(self.row, self.column, board)
        threatened_three = move_three.squares_threatening(self.row, self.column, board)
        threatened_squares = threatened_one + threatened_two + threatened_three
        return threatened_squares

class King(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self  
    
    def __repr__(self):
        return "king" 

    def threatening(self, board):
        move_one = KingMove()
        threatened_squares = move_one.squares_threatening(self.row, self.column, board)
        return threatened_squares

# Creates all the starting white pieces

class set_of_pieces(object):  
        
    def __init__(self, color):
        self.color = color
        self.pieces = []
    
    def create_pieces(self, board):
        new_pieces = []        
        if self.color == "white":        
            new_pieces.append(Pawn("white", 1, 0, board))
            new_pieces.append(Pawn("white", 1, 1, board))
            new_pieces.append(Pawn("white", 1, 2, board))
            new_pieces.append(Pawn("white", 1, 3, board))
            new_pieces.append(Pawn("white", 1, 4, board))
            new_pieces.append(Pawn("white", 1, 5, board))
            new_pieces.append(Pawn("white", 1, 6, board))
            new_pieces.append(Pawn("white", 1, 7, board))
            new_pieces.append(Rook("white", 0, 0, board))
            new_pieces.append(Knight("white", 0, 1, board))
            new_pieces.append(Bishop("white", 0, 2, board))
            new_pieces.append(Queen("white", 0, 3, board))
            new_pieces.append(King("white", 0, 4, board))
            new_pieces.append(Bishop("white", 0, 5, board))
            new_pieces.append(Knight("white", 0, 6, board))
            new_pieces.append(Rook("white", 0, 7, board))
        else:
            new_pieces.append(Pawn("black", 6, 0, board))
            new_pieces.append(Pawn("black", 6, 1, board))
            new_pieces.append(Pawn("black", 6, 2, board))
            new_pieces.append(Pawn("black", 6, 3, board))
            new_pieces.append(Pawn("black", 6, 4, board))
            new_pieces.append(Pawn("black", 6, 5, board))
            new_pieces.append(Pawn("black", 6, 6, board))
            new_pieces.append(Pawn("black", 6, 7, board))
            new_pieces.append(Rook("black", 7, 0, board))
            new_pieces.append(Knight("black", 7, 1, board))
            new_pieces.append(Bishop("black", 7, 2, board))
            new_pieces.append(Queen("black", 7, 3, board))
            new_pieces.append(King("black", 7, 4, board))
            new_pieces.append(Bishop("black", 7, 5, board))
            new_pieces.append(Knight("black", 7, 6, board))
            new_pieces.append(Rook("black", 7, 7, board))
        return new_pieces                


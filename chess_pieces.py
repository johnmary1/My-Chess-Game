""" This file creates the pieces. 
"""

# Create a general class for pieces
class Piece(object):
    moved_yet = False  
    def __init__(self):
        pass    

class Pawn(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self
    
    def __str__(self):
        return "pawn"    

    def threatening(self, board):
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
    
    def __str__(self):
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
    
    def __str__(self):
        return "knight" 

class Bishop(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self  
    
    def __str__(self):
        return "bishop" 

class Queen(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self  
    
    def __str__(self):
        return "queen" 

class King(Piece):
    def __init__(self, color, row, column, board):
        self.color = color
        self.row = row
        self.column = column
        self.occupied_space = board[self.row][self.column]
        board[self.row][self.column].occupying_piece = self  
    
    def __str__(self):
        return "king" 

    def threatening(self, board):
        move_one = KingMove()
        threatened_squares = move_one.squares_threatening(self.row, self.column, board)
        return threatened_squares

# Creates all the starting white pieces
def create_white_pieces(board):
    white_pieces = []
    A2Pawn = Pawn("white", 1, 0, board)
    white_pieces.append(A2Pawn)
    B2Pawn = Pawn("white", 1, 1, board)
    white_pieces.append(B2Pawn)
    C2Pawn = Pawn("white", 1, 2, board)
    white_pieces.append(C2Pawn)
    D2Pawn = Pawn("white", 1, 3, board)
    white_pieces.append(D2Pawn)
    E2Pawn = Pawn("white", 1, 4, board)
    white_pieces.append(E2Pawn)
    F2Pawn = Pawn("white", 1, 5, board)
    white_pieces.append(F2Pawn)
    G2Pawn = Pawn("white", 1, 6, board)
    white_pieces.append(G2Pawn)
    H2Pawn = Pawn("white", 1, 7, board)
    white_pieces.append(H2Pawn)
    WQRook = Rook("white", 0, 0, board)
    white_pieces.append(WQRook)
    WQKnight = Knight("white", 0, 1, board)
    white_pieces.append(WQKnight)
    WQBishop = Bishop("white", 0, 2, board)
    white_pieces.append(WQBishop)
    WQueen = Queen("white", 0, 3, board)
    white_pieces.append(WQueen)
    WKing = King("white", 0, 4, board)
    white_pieces.append(WKing)
    WKBishop = Bishop("white", 0, 5, board)
    white_pieces.append(WKBishop)
    WKKnight = Knight("white", 0, 6, board)
    white_pieces.append(WKKnight)
    WKRook = Rook("white", 0, 7, board)
    white_pieces.append(WKRook)    
    return white_pieces

# Creates all the starting black pieces
def create_black_pieces(board):
    black_pieces = []
    A7Pawn = Pawn("black", 6, 0, board)
    black_pieces.append(A7Pawn)
    B7Pawn = Pawn("black", 6, 1, board)
    black_pieces.append(B7Pawn)
    C7Pawn = Pawn("black", 6, 2, board)
    black_pieces.append(C7Pawn)
    D7Pawn = Pawn("black", 6, 3, board)
    black_pieces.append(D7Pawn)
    E7Pawn = Pawn("black", 6, 4, board)
    black_pieces.append(E7Pawn)
    F7Pawn = Pawn("black", 6, 5, board)
    black_pieces.append(F7Pawn)
    G7Pawn = Pawn("black", 6, 6, board)
    black_pieces.append(G7Pawn)
    H7Pawn = Pawn("black", 6, 7, board)
    black_pieces.append(H7Pawn)
    BQRook = Rook("black", 7, 0, board)
    black_pieces.append(BQRook)
    BQKnight = Knight("black", 7, 1, board)
    black_pieces.append(BQKnight)
    BQBishop = Bishop("black", 7, 2, board)
    black_pieces.append(BQBishop)
    BQueen = Queen("black", 7, 3, board)
    black_pieces.append(BQueen)
    BKing = King("black", 7, 4, board)
    black_pieces.append(BKing)
    BKBishop = Bishop("black", 7, 5, board)
    black_pieces.append(BKBishop)
    BKKnight = Knight("black", 7, 6, board)
    black_pieces.append(BKKnight)
    BKRook = Rook("black", 7, 7, board)
    black_pieces.append(BKRook)
    return black_pieces





# Create parent class Movement.
# The perform movement will make the relevant Board changes for the type of move.

class Movement(object):
    def __init__(self):
        pass

class Move(Movement):
    def __init__(self):
        pass
    def perform(self):
        pass

# Do I want this to return an updated board?
class horizontal_move(Move):
    def __init__(self):
        self.start_column = None
        self.end_column = None
        self.unchanging_row = None
    def perform_move(self, start_column, end_column, unchanging_row, board):
        self.start_column = start_column
        self.end_column = end_column
        self.unchanging_row = unchanging_row
        # This is what tuples were created for. Exchange with a tuple when you figure out how.        
        temp_piece = board[unchanging_row][start_column].occupying_piece
        board[unchanging_row][start_column].occupying_piece = None
        board[unchanging_row][end_column].occupying_piece = temp_piece
        

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

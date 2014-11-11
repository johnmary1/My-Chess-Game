# Create parent class Movement.
# The perform movement will make the relevant Board changes for the type of move.

class Movement(object):
    def __init__(self):
        pass

class HorizontalMove(Movement):
    def __init__(self):
        self.start_column = None
        self.end_column = None
        self.unchanging_row = None

    def __str__(self):
        return "horizontal"
    
    # Returns a list of squares threatened. Does not determine if king is threatened. 
    def squares_threatening(self, start_column, unchanging_row, board):
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
    
    def perform_move(self, start_column, end_column, unchanging_row, board):
        # This method is not correct and needs to be redone. This is a placeholder.        
        self.start_column = start_column
        self.end_column = end_column
        self.unchanging_row = unchanging_row
        # This is what tuples were created for. Exchange with a tuple when you figure out how.        
        temp_piece = board[unchanging_row][start_column].occupying_piece
        board[unchanging_row][start_column].occupying_piece = None
        board[unchanging_row][end_column].occupying_piece = temp_piece
        

class VerticalMove(Movement):
    def __init__(self):
        self.start_column = None
        self.end_column = None
        self.unchanging_row = None
    
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
    
    def perform_move(self, start_row, end_row, unchanging_column, board):
        # This method is not correct and needs to be scrapped.. this is a placeholder        
        self.start_row = start_row
        self.end_row = end_row
        self.unchanging_column = unchanging_column
        # This is what tuples were created for. Exchange with a tuple when you figure out how.        
        temp_piece = board[start_row][unchanging_column].occupying_piece
        board[start_row][unchanging_column].occupying_piece = None
        board[end_row][unchanging_column].occupying_piece = temp_piece

class DiagonalMove(Movement):
    def __init__(self):
        self.start_column = None
        self.end_column = None
        self.start_row = None
        self.end_row = None
    
    def squares_threatening(self, start_row, start_column, end_row, end_column, board):
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

    def perform_move(self, start_row, start_column, end_row, end_column, board):

    

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

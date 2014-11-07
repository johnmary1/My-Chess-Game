"""This creates the board consisting of all the various squares.

"""

# Each square on the board is going to be its own object
class Square(object):
    # I will need to create the board before placing pieces
    # Otherwise the squares will be set to empty
    occupying_piece = None    
    def __init__(self):
        pass

# Creates a row with the correct color spaces...
# color_first = the color of the first square in the row
def create_row():
    row = []     
    for column_value in range(0, 8):
        row.append(Square)     
    return row

# Creates an 8x8 board with each square being occupied by a Square object
# The returned board is accessed board[row][column]
def create_board():
    board = []        
    for row_value in range(0,8):
        row = create_row()
        board.append(row)
    return board
    # Need to call with board = create_board()

"""
Idea for what an ASCII Board might look like

      ######      ######      ######      ######
  Br  # Bn #  Bb  # BQ #  BK  # Bb #  Bn  # Br #
      ######      ######      ######      ######
      ######      ######      ######      ######
######      ######      ######      ######      
# Bp #  Bp  # Bp #  Bp  # Bp #  Bp  # Bp #  Bp  
######      ######      ######      ######      
######      ######      ######      ######      
      ######      ######      ######      ######
      ######      ######      ######      ######
      ######      ######      ######      ######
      ######      ######      ######      ######
######      ######      ######      ######      
######      ######      ######      ######      
######      ######      ######      ######      
######      ######      ######      ######      
      ######      ######      ######      ######
      ######      ######      ######      ######
      ######      ######      ######      ######
      ######      ######      ######      ######
######      ######      ######      ######      
######      ######      ######      ######      
######      ######      ######      ######      
######      ######      ######      ######      
      ######      ######      ######      ######
  Wp  # Wp #  Wp  # Wp #  Wp  # Wp #  Wp  # Wp #
      ######      ######      ######      ######
      ######      ######      ######      ######
######      ######      ######      ######      
# Wr #  Wn  # Wb #  WQ  # WK #  Wb  # Wn #  Wr  
######      ######      ######      ######      
######      ######      ######      ######      

"""


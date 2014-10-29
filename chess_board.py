"""This creates the board consisting of all the various squares.

"""

# Each square on the board is going to be its own object
class Square(object):
    #I will need to create the board before placing pieces
    #Otherwise the squares will be set to empty
    occupying_piece = None    
    def __init__(self, color):
        self.color = color

#Creates a row with the correct color spaces...
#color_first = the color of the first square in the row
def create_row(color_first):
    row = []     
    for column_value in range(0, 8):
        if color_first == "white":
            color_second = "black"
        else:
            color_second = "white"    
        if column_value % 2 == 0:
            square_color = color_first
        else:
            square_color = color_second
        row.append(Square(square_color))     
    return row

# Creates an 8x8 board with each square being occupied by a Square object
# The returned board is accessed board[row][column]
def create_board():
    board = []        
    for number in range(0,8):
        if number % 2 == 0:
            first_square_color = "black"
        else:
            first_square_color = "white"
        row = create_row(first_square_color)
        board.append(row)
    return board
    #Need to call with board = create_board()

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


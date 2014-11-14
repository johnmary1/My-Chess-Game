"""This creates the board consisting of all the various squares.

"""

# Each square on the board is going to be its own object
class Square(object):
    # I will need to create the board before placing pieces
    # Otherwise the squares will be set to empty
    occupying_piece = None    
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        column_conversion_num_let = {
            '0': 'A',
            '1': 'B',
            '2': 'C',
            '3': 'D',
            '4': 'E',
            '5': 'F',
            '6': 'G',
            '7': 'H'
            }
        return column_conversion_num_let[str(self.column)] + str(self.row + 1)

# Creates a row with the correct color spaces...
# color_first = the color of the first square in the row
def create_row(row_value):
    row = []     
    for column_value in range(0, 8):
        row.append(Square(row_value, column_value))     
    return row

# Creates an 8x8 board with each square being occupied by a Square object
# The returned board is accessed board[row][column]
def create_board():
    board = []        
    for row_value in range(0,8):
        row = create_row(row_value)
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


"""This file contains an individual turn. In general it asks a user for input,
tests if that input is valid, and then (if so) makes the move.
"""

# These dictionaries are to aid in the conversion from column numbers
# to chess Algebraic notation (i.e. A1, H8)

column_conversion_let_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

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

#To prompt the user for the space containing the piece they'd like to move
def get_from_space():  
    ask_piece_from = raw_input("On what space is the piece you'd like to move? (e.g. A1, C2, H8)")
    # Need to add some kind of error check here.    
    row_from = int(ask_piece_from[1]) - 1  
    column_from = column_conversion_let_num[ask_piece_from[0]]
    return row_from, column_from

#To prompt the user for the space they'd like to move the moving piece.
def get_to_space(): 
    new_space = raw_input("To which space would you like to move this piece? (e.g. A1, C2, H8)")    
    # Need to add some kind of error check here.
    row_to = int(new_space[1]) - 1
    column_to = column_conversion_let_num[new_space[0]]
    return row_to, column_to    

#Tests if a piece moves in a manner/direction it is able to move.
def test_valid_direction(row_from, column_from, row_to, column_to):
    piece_to_move = board[row_from][column_from]    
    #Tests if piece is moving horizontally    
    if row_from - row_to == 0 and column_from - column_to != 0:
        #Tests if piece is allowed to move horizontally        
        if piece_to_move.movement_type[0] == True:
            movement = "horizontal"            
            validity = True
            spaces_moved = abs(column_from - column_to)
        else:
            validity = False
    #Tests if piece is moving vertically    
    elif row_from - row_to != 0 and column_from - column_to == 0:
        #Tests if the piece is allowed to move vertically
        if piece_to_move.movement_type[1] == True:
            movement = "vertical"            
            validity = True
            spaces_moved = abs(row_from - row_to)
        else:
            validity = False
    #Tests if piece is moving diagonally    
    elif abs(row_from - row_to) == abs(column_from - column_to):
        #Tests if the piece is allowed to move diagonally
        if piece_to_move.movement_type[2] == True:
            movement = "diagonal"            
            validity = True
            spaces_moved = abs(row_from - row_to)
        else:
            validity = False
    #Tests if piece moves like a knight    
    elif (abs(row_from - row_to) == 1 and abs(column_from - column_to) == 2) \
        or (abs (row_from - row_to) == 2 and abs(column_from - column_to) == 1):
        #Tests if piece is allowed to move like a knight
        if piece_to_move.movement_type[3] == True:
            movement = "knight"            
            validity = True
            spaces_moved = 3
        else: validity = False
    else:
        validity = False
    if spaces_moved > piece_to_move.spaces_can_move:
        validity = False
    else:
        validity = True   
    if spaces_moved == 1
        no_spaces_between = True
    else:
        no_spaces_between = False    
    return validity, movement, no_spaces_between

# Checks to make sure there are no pieces in the spaces between it's starting and ending spot
# Need to only run this check if no_spaces_between == False
# Need to get rid of all these nested ifs...
def check_spaces_between(movement, row_from, column_from, row_to, column_to):
    pieces_between = 0    
    row_values = [row_from, row_to]
    row_values.sort()
    column_values = [column_from, column_to]
    column.values.sort()
    if movement = "horizontal":       
        for space_between in range(column_values[0] + 1, column_values[1]):
            if board[row_from][space_between].occupying_piece != None:
                    pieces_between += 1
            else:
                pass
    elif movement = "vertical":
        for space_between in range(row_values[0], row_values[1]):
            if board[space_between][column_from].occupying_piece != None:
                    pieces_between +=1
            else:
                pass
    elif movement = "diagonal":
        pass
        ###obviously need to figure this out...
    elif movement = "knight":
        pass
        #This is ok. Knights can skip over other pieces.
    else:
        pass
    if pieces_between > 0:
        #Here using the same variable name as other function. Think this is ok...        
        validity = False
        return validity
    
        
#Need to create another test to see if the space being moved to is occupied or not (and by what color piece).
#If the space is occupied by an opposing piece that is not the king *AND* the moving piece is not a pawn
#Will take piece. Need to control for opposing king, color
def test_piece_capture():
    pass
    
#Generic move function which actually moves the piece and registers the new state of affairs with the piece object
#and the square object. This is currently incomplete.    
def piece_move(row_from, column_from, row_to, column_to):
    board[row_from][column_from].occupying_piece.occupied_space = board[row_to][column_to]
    board[row_from][column_from].occupying_piece = None
    ##Need to change new space to be occupied by piece... need to be able to call the piece itself
    ##as opposed to a method of original space.    












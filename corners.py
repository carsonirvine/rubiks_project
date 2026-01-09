import magiccube
import dictionaries as dict

# Finds the corner sequence
def solve_corners(cube):
    solved = False
    unsolved_pieces_present = False
    # initialize position, piece, and significant side
    starting_x = 0
    starting_y = 2
    starting_z = 0
    current_position = (starting_x, starting_y, starting_z)
    current_piece = cube.get_piece(current_position)
    significant_pos = "horizontal"
    return_letters = []

    return_letters.append(convert_piece_to_letter(current_piece, significant_pos))

    # while not solved keep looking
    while not solved:
        '''
        if unsolved_pieces_present:
            unsolved_position = find_unsolved_piece(cube)

            current_position = unsolved_position
            significant_pos = find_significant_pos(current_piece, significant_pos)
            current_piece = cube.get_piece(current_position)
            return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
            unsolved_pieces_present = False
        '''
        #else:
        # get next piece location, piece, and significant side data
        if unsolved_pieces_present:
            current_position = find_unsolved_piece(cube)
        else:
            current_position = find_next_position(current_piece)
        significant_pos = find_significant_pos(current_piece, significant_pos)
        current_piece = cube.get_piece(current_position)
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos))

        # check if done or unsolved pieces present
        if return_letters[-1] in ("E"):
            solved = True
            #print("\nSUCCESS\n")
            # delete last 'E' letter
            del return_letters[-1]
            break
            '''
            unsolved_position_return = find_unsolved_piece(cube)
            
            if unsolved_position_return is None:
                break
            else:
                unsolved_pieces_present
            '''

        # unsolved pieces present
        elif return_letters[-1] in ("A", "R"):
            unsolved_pieces_present = True
            # TEMPORARY SO THE PROGRAM TERMINATES
            #solved = True

            #print("UNSOLVED PIECE PRESENT")

    return return_letters

# significant_pos can be "vertical" for top and bottom, "horizontal" for left and right
# and "through" for front and back

# Takes in a piece and side and finds its matching letter
def convert_piece_to_letter(piece, significant_pos):
    # take in piece colors by side
    x_color = str(piece)[0]
    y_color = str(piece)[1]
    z_color = str(piece)[2]

    piece_colors = ""

    if significant_pos == "vertical":
        piece_colors+=y_color
        piece_colors+=x_color
        piece_colors+=z_color
        
    elif significant_pos == "horizontal":
        piece_colors+=x_color
        piece_colors+=y_color
        piece_colors+=z_color
    
    elif significant_pos == "through":
        piece_colors+=z_color
        piece_colors+=x_color
        piece_colors+=y_color

    # search dict for matching letter
    letter = dict.corner_piece_to_letter[piece_colors]
    return letter

# returns the position for the next piece
def find_next_position(current_piece):
    home_position = dict.corner_piece_to_position[str(current_piece)]
    return home_position

# checks based on the colour of the piece and significant side
# what the next significant side will be
def find_significant_pos(current_piece, significant_pos):
    next_pos = ""
    color = ""
    # find relevant color
    if significant_pos == "vertical":
        color = str(current_piece)[1]
    elif significant_pos == "horizontal":
        color = str(current_piece)[0]
    elif significant_pos == "through":
        color = str(current_piece)[2]

    # find side from color
    if color == "R" or color == "O":
        next_pos = "horizontal"
    elif color == "W" or color == "Y":
        next_pos = "vertical"
    elif color == "B" or color == "G":
        next_pos = "through"
    return next_pos

def find_unsolved_piece(cube):
    unsolved_piece_found = False
    unsolved_piece_position = ''
    x,y,z = 0,0,0
    current_position = (x, y, z)
    current_piece = cube.get_piece(current_position)
    while not unsolved_piece_found:
        # get where the piece should be
        desired_position = dict.corner_piece_to_position[str(current_piece)]
        # if not in spot piece is unsolved
        if desired_position != current_position:
            unsolved_piece_found = True
            unsolved_piece_position = current_position
            break
        # else go to next position
        current_position = next_corner_position(current_position)
        if current_position == None:
            return None

    if unsolved_piece_found:
        return unsolved_piece_position
    else:
        return None


# finds next position to check through each corner
def next_corner_position(current_position):
    x,y,z = 0,0,0
    if current_position[2] == 0:
        z = 2
    elif current_position[1] == 0 and current_position[2] == 2:
        y = 2
        z = 0
    elif current_position[0] == 0 and current_position[1] == 2 and current_position[2] == 2: 
        x = 2
        y = 0
        z = 0
    elif current_position[0] == 2 and current_position[1] == 2 and current_position[2] == 2:
        return None
    return (x,y,z)

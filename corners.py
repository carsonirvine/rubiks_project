import magiccube
import dictionaries as dict

# Finds the corner sequence
def solve_corners(cube):
    solved = False
    #unsolved_pieces_present = False
    # initialize position, piece, and significant side
    starting_x = 0
    starting_y = 2
    starting_z = 0
    current_position = (starting_x, starting_y, starting_z)
    current_piece = cube.get_piece(current_position)
    significant_pos = "horizontal"
    # list of answer letters
    return_letters = []
    visited_positions = []
    return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
    visited_positions.append(current_position)

    # while not solved keep looking
    while not solved:

        # get next piece location, piece, and significant side data
        current_position = find_next_position(current_piece)
        significant_pos = find_significant_pos(current_piece, significant_pos)
        current_piece = cube.get_piece(current_position)
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
        visited_positions.append(current_position)

        # check if done or unsolved pieces present
        if return_letters[-1] in ("E"):
            solved = True
            # delete last 'E' letter
            del return_letters[-1]
            break

        # unsolved pieces present
        elif return_letters[-1] in ("A", "R"):
            #unsolved_pieces_present = True
            unsolved_piece_position = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece_position is not None:
                print("\n\nUNSOLVED PIECE POSITION IS NOT NONE\n\n")
                current_piece = cube.get_piece(unsolved_piece_position)
                significant_pos = "horizontal"
                current_position = unsolved_piece_position
                return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
                visited_positions.append(current_position)
                continue
            else:
                print("\n\nUNSOLVED PIECE POSITION IS NONE\n\n")
                solved = True
                break
                
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

def find_unsolved_piece(cube, visited_positions):
    unsolved_piece_found = False
    checked_all_corners = False
    unsolved_piece_position = None
    # Start in bottom left, 0,0,0
    current_position = (0, 0, 0)
    current_piece = cube.get_piece(current_position)
    # loop until found unsolved piece or checked every point
    while not unsolved_piece_found and not checked_all_corners:
        # get where the piece should be
        if current_position in visited_positions:
            current_position = next_corner_position(current_position)
            current_piece = cube.get_piece(current_position)
            continue
        # FOR SOME REASON CURRENT PIECE CAN BE ENTIRE CUBE, FIX THIS
        if isinstance(str(current_piece),list):
            current_piece = str(current_piece)[-1]
        desired_position = dict.corner_piece_to_position[str(current_piece)]
        # if not in spot piece is unsolved
        if desired_position != current_position:
            unsolved_piece_found = True
            unsolved_piece_position = current_position
            return unsolved_piece_position
            break
        # else go to next position
        current_position = next_corner_position(current_position)
        if current_position == None:
            checked_all_corners = True
        current_piece = cube.get_piece(current_position)
    # None unless unsolved piece found, then its position
    return unsolved_piece_position


# finds next position to check through each corner
def next_corner_position(current_position):
    x,y,z = current_position
    if z == 0:
        z = 2
    elif y == 0 and z == 2:
        y = 2
        z = 0
    elif x == 0 and y == 2 and z == 2: 
        x = 2
        y = 0
        z = 0
    elif x == 2 and y == 2 and z == 2:
        return None
    return (x,y,z)

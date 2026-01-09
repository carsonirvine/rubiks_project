import magiccube
import dictionaries as dict

# Finds the corner sequence
def solve_edges(cube):
    solved = False
    unsolved_pieces_present = False
    # initialize position, piece, and significant side
    current_x = 2
    current_y = 2
    current_z = 1
    current_position = (current_x, current_y, current_z)
    current_piece = cube.get_piece(current_position)
    significant_pos = "vertical"
    return_letters = []

    return_letters.append(convert_piece_to_letter(current_piece, significant_pos))

    # while not solved keep looking
    while not solved:
        # get next piece location, piece, and significant side data
        current_position = find_next_position(current_piece)
        significant_pos = find_significant_pos(current_piece, significant_pos)
        current_piece = cube.get_piece(current_position)
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos))

        # check if done or unsolved pieces present
        if return_letters[-1] in ("B"):
            solved = True
            #print("\nSUCCESS\n")
            # delete last 'E' letter
            del return_letters[-1]
            break
        # unsolved pieces present
        elif return_letters[-1] in ("M"):
            unsolved_pieces_present = True

            # TEMPORARY SO THE PROGRAM TERMINATES
            solved = True

            #print("UNSOLVED PIECE PRESENT")
            break

    return return_letters

# significant_pos can be "vertical" for top and bottom, "horizontal" for left and right
# and "through" for front and back

# Takes in a piece and side and finds its matching letter
def convert_piece_to_letter(piece, significant_pos):
    # take in piece colors by side
    color_1 = str(piece)[0]
    color_2 = str(piece)[1]

    no_x = True
    # if first letter is not O or R then it is a middle line edge
    if color_1 in ("O", "R"):
        no_x = False

    piece_colors = ""

    if significant_pos == "vertical":
        # if theres no x then the vertical letter is first
        if no_x:
            piece_colors+=color_1
            piece_colors+=color_2
        # if there is an X vertical letter is last
        else:
            piece_colors+=color_2
            piece_colors+=color_1
        
    elif significant_pos == "horizontal":
        # Horizontal letter is always first
        piece_colors+=color_1
        piece_colors+=color_2

    elif significant_pos == "through":
        # Through letter is always last
        piece_colors+=color_2
        piece_colors+=color_1

    # search dict for matching letter
    letter = dict.edge_piece_to_letter[piece_colors]
    return letter

# returns the position for the next piece
def find_next_position(current_piece):
    home_position = dict.edge_piece_to_position[str(current_piece)]
    return home_position

# checks based on the colour of the piece and significant side
# what the next significant side will be
def find_significant_pos(current_piece, significant_pos):

    color_1 = str(current_piece)[0]
    color_2 = str(current_piece)[1]
    no_x = True
    # if first color is O or R then there is an x side colour
    if color_1 in ("O", "R"):
        no_x = False
    
    next_pos = ""
    color = ""
    # find relevant color
    if significant_pos == "vertical":
        # if no R or O then W or Y will be first letter
        if no_x:
            color = str(current_piece)[0]
        else:
            color = str(current_piece)[1]
    elif significant_pos == "horizontal":
        # Always first letter
        color = str(current_piece)[0]
    elif significant_pos == "through":
        # Always last letter
        color = str(current_piece)[1]

    # find side from color
    if color == "R" or color == "O":
        next_pos = "horizontal"
    elif color == "W" or color == "Y":
        next_pos = "vertical"
    elif color == "B" or color == "G":
        next_pos = "through"
    return next_pos

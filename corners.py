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
    visited_positions = set()
    return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
    visited_positions.add(current_position)

    seen_states = set()

    # while not solved keep looking
    while not solved:
        
        # get next piece location, piece, and significant side data
        current_position = find_next_position(current_piece)
        significant_pos = find_significant_pos(current_piece, significant_pos)
        current_piece = cube.get_piece(current_position)
        print(f"Current piece line 30: {current_piece}")
        current_letter = convert_piece_to_letter(current_piece, significant_pos)
        return_letters.append(current_letter)

        if current_position in visited_positions:
            del return_letters[-1]
            unsolved_piece_position = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece_position is None:
                buffer_piece = cube.get_piece((starting_x, starting_y, starting_z))
                if str(buffer_piece) == "OYB":
                    solved = True
                    break
                else:
                    print("FLIP PRESENT SOMEWHERE")
                    break
            current_piece = cube.get_piece(unsolved_piece_position)
            print(f"Current piece line 43: {current_piece}")
            significant_pos = "horizontal"
            current_position = unsolved_piece_position

        visited_positions.add(current_position)

        state = (current_position, significant_pos, str(current_piece))
        if state in seen_states:
            raise RuntimeError(f"Infinite loop detected, current string {return_letters}")
        seen_states.add(state)
        # check if done or unsolved pieces present
        if return_letters[-1] == "E":
            solved = True
            # delete last 'E' letter
            del return_letters[-1]
            break

        # unsolved pieces present
        
        elif return_letters[-1] in ("A", "R"):
            #unsolved_pieces_present = True
            unsolved_piece_position = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece_position is not None:
                current_piece = cube.get_piece(unsolved_piece_position)
                print(f"Current piece line 67: {current_piece}")
                significant_pos = "horizontal"
                current_position = unsolved_piece_position
                return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
                visited_positions.add(current_position)
                continue
            else:
                solved = True
                print("No unsolved piece location found")
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
    #unsolved_piece_found = False
    unseen_corners = [x for x in dict.corner_position_list if x not in visited_positions]
    for corner in unseen_corners:
        current_position = corner
        current_piece = cube.get_piece(current_position)
        if current_piece is None:
            continue
        desired_position = dict.corner_piece_to_position[str(current_piece)]
        if current_position != desired_position:
            #unsolved_piece_found = True
            unsolved_piece_position = current_position
            return unsolved_piece_position
    return None    
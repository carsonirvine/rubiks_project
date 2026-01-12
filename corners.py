import dictionaries as dict

# Finds the corner sequence
def solve_corners(cube):
    # list of answer letters
    return_letters = []
    visited_positions = {}
    solved = False
    something_done = False
    # initialize position, piece, and significant side
    current_position = dict.corner_starting_position
    significant_pos = "horizontal"


    # while not solved keep looking
    #while not solved:
    while not solved:
        current_piece = cube.get_piece(current_position)
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
        visit(visited_positions, current_position)
        
        # if current piece is A or R then corner is twisted
        if convert_piece_to_letter(current_piece, significant_pos) in ("A", "R"):
            del return_letters[-1]
            unsolved_piece = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece is None:
                solved = True
                break
            else: 
                current_position = unsolved_piece
                significant_pos = find_significant_pos(current_piece, "horizontal")
                something_done = True
        # If last letter is E then check if theres unsolved pieces
        elif convert_piece_to_letter(current_piece, significant_pos) == "E":
            # delete last 'E' letter
            del return_letters[-1]
            unsolved_piece = find_unsolved_piece(cube, visited_positions)
            if unsolved_piece is None:
                solved = True
                break
            else: 
                current_position = unsolved_piece
                significant_pos = find_significant_pos(current_piece, "horizontal")
                something_done = True
        # get next piece location, piece, and significant side data
        try:
            if visited_positions[current_position] == 2 and current_position != dict.corner_starting_position:
                unsolved_piece = find_unsolved_piece(cube, visited_positions)
                #print(f"Visited positions is 2, unsolved piece is {unsolved_piece}")
                if unsolved_piece is None:
                    #print("Visited positions is 2 and unsolved piece is none")
                    solved = True
                    break
                else:
                    current_position = unsolved_piece
                    significant_pos = find_significant_pos(current_piece, "horizontal")
                    something_done = True
                solved = False
        except:
            pass
        if not something_done:
            current_position = find_next_position(current_piece)
            significant_pos = find_significant_pos(current_piece, significant_pos)
            
        something_done = False

        
    return return_letters

# visit the provided position in the visited dictionary
def visit(visited, position):
    if position in visited:
        visited[position] += 1
    else:
        visited[position] = 1


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

# Finds the position of the next unsolved piece, returns none if no unsolved piece
def find_unsolved_piece(cube, visited_positions):
    # select all corners not visited from the position list
    unseen_corners = [pos for pos in dict.corner_position_list if pos not in visited_positions]
    for corner in unseen_corners:
        # set current corner position
        current_position = corner
        # get piece
        current_piece = cube.get_piece(current_position)
        # if none then skip
        if current_piece is None:
            continue
        desired_position = dict.corner_piece_to_position[str(current_piece)]
        # if not in desired location then piece is unsolved
        if current_position != desired_position:
            unsolved_piece_position = current_position
            return unsolved_piece_position
        # else if letters in this order piece must be flipped but in correct location
        elif str(current_piece)[0] not in ("R", "O") or str(current_piece)[1] not in ("Y", "W") or str(current_piece)[2] not in ("B", "G"):
            unsolved_piece_position = current_position
            return unsolved_piece_position
    # if no unsolved pieces return none
    return None    
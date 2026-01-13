import Data.constants as dict

# Finds the corner sequence
def solve_corners(cube):
    # list of answer letters
    return_letters = []
    # dict of visited positions with value = number of visits
    visited_positions = {}
    # Is cube solved
    solved = False
    # Was an unsolved piece found
    unsolved_piece_found = False

    # Start from starting position
    current_position = dict.corner_starting_position
    # First starting side is left
    significant_pos = "horizontal"


    # while not solved keep looking
    while not solved:
        # get piece from current position
        current_piece = cube.get_piece(current_position)
        # add piece converted to letter
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos))
        # Visit position after appending letter
        visit(visited_positions, current_position)
        
        # If letter was A or R then buffer piece is in spot flipped
        if convert_piece_to_letter(current_piece, significant_pos) in ("A", "R"):
            # delete the A or R
            del return_letters[-1]
            # find an unsolved piece
            unsolved_pos = find_unsolved_piece(cube, visited_positions)
            # if none returned corners must be solved
            if unsolved_pos is None:
                solved = True
                break
            # else take unsolved position and start from horizontal side
            else: 
                current_position = unsolved_pos
                significant_pos = find_significant_pos(current_piece, "horizontal")
                unsolved_piece_found = True
        # If letter is E, correct for buffer to be right
        elif convert_piece_to_letter(current_piece, significant_pos) == "E":
            # delete last 'E' letter
            del return_letters[-1]
            # search for an unsolved piece
            unsolved_pos = find_unsolved_piece(cube, visited_positions)
            # if no unsolved piece edges are done
            if unsolved_pos is None:
                solved = True
                break
            # else get unsolved position and find its significant side
            else: 
                current_position = unsolved_pos
                significant_pos = find_significant_pos(current_piece, "horizontal")
                unsolved_piece_found = True
        # Try, because might search key not in dict. if so means unvisited position so just pass
        try:
            # check if position has been visited twice and also not starting position, and no unsolved piece already found
            if visited_positions[current_position] == 2 and current_position != dict.corner_starting_position:
                # search for an unsolved piece
                unsolved_pos = find_unsolved_piece(cube, visited_positions)
                # if no unsolved piece edges are done
                if unsolved_pos is None:
                    solved = True
                    break
                # else get unsolved position and find its significant side
                else:
                    current_position = unsolved_pos
                    significant_pos = find_significant_pos(current_piece, "horizontal")
                    unsolved_piece_found = True
                # If here then cube must be unsolved
                solved = False
        except:
            # Pass, as only error could be searching for unvisited position
            pass
        # if we havent found an unsolved piece to go to simply go to next in chain
        if not unsolved_piece_found:
            current_position = find_next_position(current_piece)
            significant_pos = find_significant_pos(current_piece, significant_pos)
        # reset whether we have found an unsolved piece
        unsolved_piece_found = False
    # after loop return sequence
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

    # create correct colour order for dictionary
    if significant_pos == "vertical":
        piece_colors+=y_color
        piece_colors+=x_color
        piece_colors+=z_color
        
    # create correct colour order for dictionary
    elif significant_pos == "horizontal":
        piece_colors+=x_color
        piece_colors+=y_color
        piece_colors+=z_color
    
    # create correct colour order for dictionary
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
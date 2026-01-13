import Data.constants as dict

# Finds the corner sequence
def solve_edges(cube):
    # is cube solved
    solved = False
    # Was an unsolved piece found
    unsolved_piece_found = False
    # sequence of edge letters
    return_letters = []
    # dictionary of visited positions as keys and number of visits as values
    visited_positions = {}

    # Start at the starting position
    current_position = dict.edge_starting_position
    # first significant side is top
    significant_pos = "vertical"

    

    # while not solved keep looking
    while not solved:
        # get piece from current position
        current_piece = cube.get_piece(current_position)
        # add piece converted to letter
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos, current_position))
        # Visit position after appending letter
        visit(visited_positions, current_position)

        # If letter was M then buffer piece is in spot flipped
        if convert_piece_to_letter(current_piece, significant_pos, current_position) == "M":
            # delete last 'M' letter
            del return_letters[-1]
            # find an unsolved piece
            unsolved_pos = find_unsolved_piece(cube, visited_positions)
            # temporary position for finding next significant pos after getting unsolved position
            temp_sig_pos = "horizontal"
            # if none returned corners must be solved
            if unsolved_pos is None:
                solved = True
                break
            # else get unsolved position and find its significant side
            else: 
                current_position = unsolved_pos
                significant_pos = find_significant_pos(current_piece, temp_sig_pos, current_position)
                unsolved_piece_found = True
        # If letter is B, correct for buffer to be right
        elif convert_piece_to_letter(current_piece, significant_pos, current_position) == "B":
            # delete last 'E' letter
            del return_letters[-1]
            # search for an unsolved piece
            unsolved_pos = find_unsolved_piece(cube, visited_positions)
            temp_sig_pos = "horizontal"
            # if no unsolved piece edges are done
            if unsolved_pos is None:
                solved = True
                break
            # else get unsolved position and find its significant side
            else: 
                current_position = unsolved_pos
                significant_pos = find_significant_pos(current_piece, "horizontal", current_position)
                unsolved_piece_found = True
        # Try, because might search key not in dict. if so means unvisited position so just pass
        try:
            # check if position has been visited twice and also not starting position, and no unsolved piece already found
            if visited_positions[current_position] == 2 and current_position != dict.edge_starting_position and not unsolved_piece_found:
                # search for an unsolved piece
                unsolved_pos = find_unsolved_piece(cube, visited_positions)
                temp_sig_pos = "horizontal"
                # if no unsolved piece edges are done
                if unsolved_pos is None:
                    solved = True
                    break
                # else get unsolved position and find its significant side
                else:
                    current_position = unsolved_pos
                    significant_pos = find_significant_pos(current_piece, "horizontal", current_position)
                    unsolved_piece_found = True
                # If here then cube must be unsolved
                solved = False
        except:
            # Pass, as only error could be searching for unvisited position
            pass
        # if we havent found an unsolved piece to go to simply go to next in chain
        if not unsolved_piece_found:
            significant_pos = find_significant_pos(current_piece, significant_pos, current_position)
            current_position = find_next_position(current_piece)
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
def convert_piece_to_letter(piece, significant_pos, position):
    # take in piece colors by position
    color_1 = str(piece)[0]
    color_2 = str(piece)[1]

    piece_colors = ""

    if significant_pos == "vertical":
        # if theres no x then the vertical letter is first
        if position[0] not in (0,2):
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
def find_significant_pos(current_piece, significant_pos, position):

    next_pos = ""
    color = ""
    # find relevant color
    if significant_pos == "vertical":
        # if no R or O then W or Y will be first letter
        if position[0] not in (0,2):
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

# Finds the position of the next unsolved piece, returns none if no unsolved piece
def find_unsolved_piece(cube, visited_positions):
    # select all edges not visited from the position list
    unseen_edges = [pos for pos in dict.edge_position_list if pos not in visited_positions]
    # loop through unseen edges
    for edge in unseen_edges:
        # set current edge position
        current_position = edge
        # get piece
        current_piece = cube.get_piece(current_position)
        # if none then skip
        if current_piece is None:
            continue
        # find the desired location of the piece
        desired_position = dict.edge_piece_to_position[str(current_piece)]
        # if not in desired location then piece is unsolved
        if current_position != desired_position:
            unsolved_piece_position = current_position
            return unsolved_piece_position
        # else if letters in this order piece must be flipped but in correct location
        elif str(current_piece)[0] in ("G", "B") or str(current_piece)[1] in ("O", "R"):
            unsolved_piece_position = current_position
            return unsolved_piece_position
    # if no unsolved pieces return none
    return None    
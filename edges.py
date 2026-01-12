import magiccube
import dictionaries as dict

# Finds the corner sequence
def solve_edges(cube):
    solved = False
    something_done = False
    return_letters = []
    visited_positions = {}
    # initialize position, piece, and significant side
    starting_position = (2,2,1)
    current_position = starting_position
    significant_pos = "vertical"

    

    # while not solved keep looking
    while not solved:
        # get  piece and add to list
        current_piece = cube.get_piece(current_position)
        print(f"COONVERTING TO LETTER: Piece: {current_piece}, sig_pos: {significant_pos}, current position: {current_position}, letter: {convert_piece_to_letter(current_piece, significant_pos, current_position)}")
        return_letters.append(convert_piece_to_letter(current_piece, significant_pos, current_position))
        # Visit position after appending letter
        visit(visited_positions, current_position)

        if convert_piece_to_letter(current_piece, significant_pos, current_position) == "M":
            # delete last 'E' letter
            del return_letters[-1]
            unsolved_pos = find_unsolved_piece(cube, visited_positions)
            temp_sig_pos = "horizontal"
            
            if unsolved_pos is None:
                solved = True
                break
            else: 
                current_position = unsolved_pos
                significant_pos = find_significant_pos(current_piece, temp_sig_pos, current_position)
                something_done = True
        elif convert_piece_to_letter(current_piece, significant_pos, current_position) == "B":
            # delete last 'E' letter
            del return_letters[-1]
            unsolved_pos = find_unsolved_piece(cube, visited_positions)
            temp_sig_pos = "horizontal"
            if unsolved_pos is None:
                solved = True
                
                break
            else: 
                current_position = unsolved_pos
                significant_pos = find_significant_pos(current_piece, "horizontal", current_position)
                something_done = True
        
        try:
            if visited_positions[current_position] == 2 and current_position != starting_position and not something_done:
                unsolved_pos = find_unsolved_piece(cube, visited_positions)
                temp_sig_pos = "horizontal"
                if unsolved_pos is None:
                    solved = True
                    break
                else:
                    current_position = unsolved_pos
                    significant_pos = find_significant_pos(current_piece, "horizontal", current_position)
                    something_done = True
                solved = False
        except:
            print("")
        if not something_done:
            
            print(f"Sig pos: {significant_pos}, piece: {current_piece}, pos: {current_position}")
            significant_pos = find_significant_pos(current_piece, significant_pos, current_position)
            current_position = find_next_position(current_piece)
            print(f"Sig pos: {significant_pos}")
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
    unseen_edges = [pos for pos in dict.edge_position_list if pos not in visited_positions]
    for edge in unseen_edges:
        current_position = edge
        current_piece = cube.get_piece(current_position)
        if current_piece is None:
            continue
        desired_position = dict.edge_piece_to_position[str(current_piece)]
        if current_position != desired_position:
            unsolved_piece_position = current_position
            return unsolved_piece_position
        elif str(current_piece)[0] in ("G", "B") or str(current_piece)[1] in ("O", "R"):
            unsolved_piece_position = current_position
            return unsolved_piece_position

    return None    
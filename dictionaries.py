# dictionary of 3 letter corner piece colours to blind letter
corner_piece_to_letter = {
    # O Y B
    "OYB": "H",
    "OBY": "H",
    "YBO": "X",
    "YOB": "X",
    "BOY": "S",
    "BYO": "S",

    # O Y G
    "OYG": "G",
    "OGY": "G",
    "YGO": "U",
    "YOG": "U",
    "GOY": "L",
    "GYO": "L",

    # O W B
    "OWB": "E",
    "OBW": "E",
    "WBO": "A",
    "WOB": "A",
    "BOW": "R",
    "BWO": "R",

    # O W G
    "OWG": "F",
    "OGW": "F",
    "WGO": "D",
    "WOG": "D",
    "GOW": "I",
    "GWO": "I",

    # R Y B
    "RYB": "O",
    "RBY": "O",
    "YBR": "W",
    "YRB": "W",
    "BRY": "T",
    "BYR": "T",

    # R Y G
    "RYG": "P",
    "RGY": "P",
    "YGR": "V",
    "YRG": "V",
    "GRY": "K",
    "GYR": "K",

    # R W B
    "RWB": "N",
    "RBW": "N",
    "WBR": "B",
    "WRB": "B",
    "BRW": "Q",
    "BWR": "Q",

    # R W G
    "RWG": "M",
    "RGW": "M",
    "WGR": "C",
    "WRG": "C",
    "GRW": "J",
    "GWR": "J"
}

# search for original corner position by piece colours
corner_piece_to_position = {
    # Corner at (0,0,0): OYB
    "OYB": (0,0,0), "OBY": (0,0,0), "YOB": (0,0,0), "YBO": (0,0,0), "BOY": (0,0,0), "BYO": (0,0,0),

    # Corner at (0,0,2): OYG
    "OYG": (0,0,2), "OGY": (0,0,2), "YOG": (0,0,2), "YGO": (0,0,2), "GOY": (0,0,2), "GYO": (0,0,2),

    # Corner at (0,2,0): OWB
    "OWB": (0,2,0), "OBW": (0,2,0), "WOB": (0,2,0), "WBO": (0,2,0), "BOW": (0,2,0), "BWO": (0,2,0),

    # Corner at (0,2,2): OWG
    "OWG": (0,2,2), "OGW": (0,2,2), "WOG": (0,2,2), "WGO": (0,2,2), "GOW": (0,2,2), "GWO": (0,2,2),

    # Corner at (2,0,0): RYB
    "RYB": (2,0,0), "RBY": (2,0,0), "YRB": (2,0,0), "YBR": (2,0,0), "BRY": (2,0,0), "BYR": (2,0,0),

    # Corner at (2,0,2): RYG
    "RYG": (2,0,2), "RGY": (2,0,2), "YRG": (2,0,2), "YGR": (2,0,2), "GRY": (2,0,2), "GYR": (2,0,2),

    # Corner at (2,2,0): RWB
    "RWB": (2,2,0), "RBW": (2,2,0), "WRB": (2,2,0), "WBR": (2,2,0), "BRW": (2,2,0), "BWR": (2,2,0),

    # Corner at (2,2,2): RWG
    "RWG": (2,2,2), "RGW": (2,2,2), "WRG": (2,2,2), "WGR": (2,2,2), "GRW": (2,2,2), "GWR": (2,2,2)
}

# dictionary of 2 letter edge piece colours to blind letter
edge_piece_to_letter = {
    #OY
    "OY": "G",
    "YO": "X",

    #OB
    "OB": "H",
    "BO": "R",

    # OG
    "OG": "F",
    "GO": "L",

    # OW
    "OW": "E",
    "WO": "D",

    # YB
    "YB": "W",
    "BY": "S",

    # YG
    "YG": "U",
    "GY": "K",

    # WB
    "WB": "A",
    "BW": "Q",

    # WG
    "WG": "C",
    "GW": "I",

    # RY
    "RY": "O",
    "YR": "V",

    # RB
    "RB": "N",
    "BR": "T",

    # RG
    "RG": "P",
    "GR": "J",

    # RW
    "RW": "M",
    "WR": "B"
}

# search for original edge position by piece colours
edge_piece_to_position = {
    # Edge at (0,0,1): OY
    "OY": (0,0,1), "YO": (0,0,1),

    # Edge at (0,1,0): OB
    "OB": (0,1,0), "BO": (0,1,0),

    # Edge at (0,1,2): OG
    "OG": (0,1,2), "GO": (0,1,2),

    # Edge at (0,2,1): OW
    "OW": (0,2,1), "WO": (0,2,1),

    # Edge at (1,0,0): YB
    "YB": (1,0,0), "BY": (1,0,0),

    # Edge at (1,0,2): YG
    "YG": (1,0,2), "GY": (1,0,2),

    # Edge at (1,2,0): WB
    "WB": (1,2,0), "BW": (1,2,0),

    # Edge at (1,2,2): WG
    "WG": (1,2,2), "GW": (1,2,2),

    # Edge at (2,0,1): RY
    "RY": (2,0,1), "YR": (2,0,1),

    # Edge at (2,1,0): RB
    "RB": (2,1,0), "BR": (2,1,0),

    # Edge at (2,1,2): RG
    "RG": (2,1,2), "GR": (2,1,2),

    # Edge at (2,2,1): RW
    "RW": (2,2,1), "WR": (2,2,1)
}

# List of all corner position coordinates
corner_position_list = [(0,0,0),(0,0,2),(0,2,0),(0,2,2),(2,0,0),(2,0,2),(2,2,0),(2,2,2)]

# List of all edge position coordinates
edge_position_list = [(0,0,1),(0,1,0),(0,1,2),(0,2,1),(1,0,0),(1,0,2),(1,2,0),
                      (1,2,2),(2,0,1),(2,1,0),(2,1,2),(2,2,1)]

# Alphabet of moves
moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'",
         "D2","F","F'","F2","B","B'","B2"]

# Edge starting position
edge_starting_position = (2,2,1)

# Corner starting position
corner_starting_position = (0,2,0)

# all setup moves for corner pieces
corner_setup_moves = {
    "B": "R2",
    "C":"F2 D",
    "D": "F2",
    "F": "F' D",
    "G": "F'",
    "H": "D' R",
    "I": "F R'",
    "J": "R'",
    "K": "F' R'",
    "L": "F2 R'",
    "M": "F",
    "N": "R' F",
    "O": "R2 F",
    "P": "R F",
    "Q": "R D'",
    "S": "D F'",
    "T": "R",
    "U": "D",
    "V": "",
    "W": "D'",
    "X": "D2"
}

# dictionary of all algorithms this method requires
algorithms = {
    "edge_swap": "R U R' U' R' F R2 U' R' U' R U R' F'",
    "corner_swap": "R U' R' U' R U R' F' R U R' U' R' F R",
    "parity": "R U' R' U' R U R D R' U' R D' R' U2 R' U'"
}
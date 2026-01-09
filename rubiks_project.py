import magiccube
from magiccube import BasicSolver
import random
from scramble import Scramble


corner_piece_to_letter = {
    "OYB": "H",
    "YBO": "X",
    "BOY": "S",

    "OYG": "G",
    "YGO": "U",
    "GOY": "L",

    "OWB": "E",
    "WBO": "A",
    "BOW": "R",

    "OWG": "F",
    "WGO": "D",
    "GOW": "I",

    "RYB": "O",
    "YBR": "W",
    "BRY": "T",

    "RYG": "P",
    "YGR": "V",
    "GRY": "K",

    "RWB": "N",
    "WBR": "B",
    "BRW": "Q",

    "RWG": "M",
    "WGR": "C",
    "GRW": "J"
}

corner_letter_to_piece = {v: k for k, v in corner_piece_to_letter.items()}

edge_piece_locations = {
    "OY": "G",
    "YO": "X"
}


moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]

def print_all_pieces():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(i,",",j,",",k,": ", cube.get_piece((i,j,k)), "\n")

'''


'''


cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")

solver = BasicSolver(cube)

scramble = Scramble(20, moves)
print(scramble.scramble)




print(cube)
for n in range(3):
    for i in range(3):
        for k in range(3):
            print(f"piece {n},{i},{k}: ", cube.get_piece((n,i,k)))


cube.rotate(scramble.scramble)
print("\nSCRAMBLING\n")
print(cube)
for n in range(3):
    for i in range(3):
        for k in range(3):
            print(f"piece {n},{i},{k}: ", cube.get_piece((n,i,k)))

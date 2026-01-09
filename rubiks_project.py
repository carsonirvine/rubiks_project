import magiccube
from magiccube import BasicSolver
import random
from scramble import Scramble
import printing
import dictionaries as dict
import corners
import edges

moves = ["R","R'","R2","L","L'","L2","U","U'","U2","D","D'","D2","F","F'","F2","B","B'","B2"]

cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")

solver = BasicSolver(cube)

printing.print_all_pieces(cube)
scramble = Scramble(20, moves)
print(f"Scramble: {scramble.scramble}")


cube.rotate(scramble.scramble)
print(cube)


corner_sequence = corners.solve_corners(cube)

print(f"\n\nCORNER SEQUENCE\n\n {corner_sequence}")

#edge_sequence = edges.solve_edges(cube)

#print(f"\n\nEDGE SEQUENCE\n\n {edge_sequence}")

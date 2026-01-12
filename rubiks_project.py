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

#printing.print_all_pieces(cube)
scramble = Scramble(20, moves)
#print(f"Scramble: {scramble.scramble}")
#cube.rotate(scramble.scramble)


print(f"Scramble: B L2 U2 R B L F' U L F2 U L D L' U2 L' F U2 R' B")
cube.rotate("B L2 U2 R B L F' U L F2 U L D L' U2 L' F U2 R' B")


print(cube)

edge_sequence = edges.solve_edges(cube)
corner_sequence = corners.solve_corners(cube)

print(f"\nEDGE SEQUENCE:\n {edge_sequence}")
if len(edge_sequence) % 2 != 0:
    print("\nPARITY Ra PERM REQUIRED")
print(f"\nCORNER SEQUENCE:\n {corner_sequence}")

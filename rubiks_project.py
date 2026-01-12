import magiccube
from scramble import Scramble
import dictionaries as dict
import corners
import edges

# Solved cube state for solve comparison
solved_cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
successfully_solved = False

# 3x3 Cube with normal colour scheme and white top green front
cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")

# generate a scramble object from the move alphabet and  normal length
scramble = Scramble(20, dict.moves)
# print the scramble
print(f"Scramble: {scramble.scramble}")
# scramble the cube
cube.rotate(scramble.scramble)
# print the current state of the cube for reference
print(cube)

# calculate the edge sequence
edge_sequence = edges.solve_edges(cube)
# calculate the corner sequence
corner_sequence = corners.solve_corners(cube)
# Is the parity algorithm required
parity = False

# output results
print(f"EDGE SEQUENCE:\n {edge_sequence}")
if len(edge_sequence) % 2 != 0:
    parity = True
    print("\nPARITY Ra PERM REQUIRED")
print(f"\nCORNER SEQUENCE:\n {corner_sequence}")

# Solves the edges
for edge in edge_sequence:
    cube.rotate(dict.edge_setup_moves[edge])
    cube.rotate(dict.algorithms["edge_swap"])
    cube.rotate(dict.edge_unsetup_moves[edge])

# if the parity algorithm is required
if parity:
    cube.rotate(dict.algorithms["parity"])

# Solves the corners
for corner in corner_sequence:
    cube.rotate(dict.corner_setup_moves[corner])
    cube.rotate(dict.algorithms["corner_swap"])
    cube.rotate(dict.corner_unsetup_moves[corner])

# if cube is back to solved state print and update var
if str(cube) == str(solved_cube):
    successfully_solved = True
    print("\n SUCCESS")
else:
    print("\nUNSUCCESSFUL")
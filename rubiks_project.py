import magiccube
from scramble import Scramble
import dictionaries as dict
import corners
import edges

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

# output results
print(f"EDGE SEQUENCE:\n {edge_sequence}")
if len(edge_sequence) % 2 != 0:
    print("\nPARITY Ra PERM REQUIRED")
print(f"\nCORNER SEQUENCE:\n {corner_sequence}")
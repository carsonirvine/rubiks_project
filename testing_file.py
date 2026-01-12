import magiccube
from scramble import Scramble
import dictionaries as dict
import corners
import edges

# Solved cube state for solve comparison
solved_cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
unsuccessfully_solved = False
successes = 0
cubes_to_test = 1000
number_of_parities = 0
number_of_corners = 0
number_of_edges = 0

for i in range (0, cubes_to_test):
    # 3x3 Cube with normal colour scheme and white top green front
    cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
    # generate a scramble object from the move alphabet and  normal length
    scramble = Scramble(20, dict.moves)
    # print the scramble
    #print(f"Scramble: {scramble.scramble}")
    # scramble the cube
    cube.rotate(scramble.scramble)
    # print the current state of the cube for reference
    #print(cube)

    # calculate the edge sequence
    edge_sequence = edges.solve_edges(cube)
    # add edge count to average
    number_of_edges += len(edge_sequence)

    # calculate the corner sequence
    corner_sequence = corners.solve_corners(cube)
    # add edge count to average
    number_of_corners += len(corner_sequence)

    # Is the parity algorithm required
    parity = False

    # output results
    #print(f"EDGE SEQUENCE:\n {edge_sequence}")
    if len(edge_sequence) % 2 != 0:
        parity = True
        #print("\nPARITY Ra PERM REQUIRED")
    #print(f"\nCORNER SEQUENCE:\n {corner_sequence}")

    # Solves the edges
    for edge in edge_sequence:
        cube.rotate(dict.edge_setup_moves[edge])
        cube.rotate(dict.algorithms["edge_swap"])
        cube.rotate(dict.edge_unsetup_moves[edge])

    # if the parity algorithm is required
    if parity:
        cube.rotate(dict.algorithms["parity"])
        number_of_parities += 1

    # Solves the corners
    for corner in corner_sequence:
        cube.rotate(dict.corner_setup_moves[corner])
        cube.rotate(dict.algorithms["corner_swap"])
        cube.rotate(dict.corner_unsetup_moves[corner])

    # if cube is back to solved state print and update var
    if str(cube) == str(solved_cube):
        successes += 1
        print(f"SUCCESS #{successes}")
    else:
        unsuccessfully_solved = True
        print("UNSUCCESSFUL")

print(f"Number of successes: {successes}/{cubes_to_test}")
print(f"Number of parities: {number_of_parities}/{cubes_to_test}")
print(f"Average number of edge swaps: {number_of_edges/cubes_to_test}")
print(f"Average number of corner swaps: {number_of_corners/cubes_to_test}")
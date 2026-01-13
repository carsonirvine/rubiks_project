import magiccube
from magiccube.cube_base import Face
from Scramble.scramble import Scramble
import Data.constants as dict
import Solving.corners as corners
import Solving.edges as edges
class Blind_Solver():
    def __init__(self, mode, scramble=""):
        self.mode = mode
        self.output = ""
        self.scramble = scramble
        if self.scramble == "":
            self.random_scramble = True
        else:
            self.random_scramble = False
    
    def solve(self):
        cube = magiccube.Cube(3,"WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
        # generate a scramble object from the move alphabet and  normal length
        scramble = Scramble(20, dict.moves)
        # print the scramble
        if self.random_scramble:
            self.output += (f"Random Scramble: {scramble.scramble}")
            # scramble the cube
            cube.rotate(scramble.scramble)
        else:
            self.output += (f"Inputted Scramble: {self.scramble}")
            # scramble the cube
            cube.rotate(self.scramble)
            
        # print the current state of the cube for reference
        self.output += self.cube_to_html(cube)
        # calculate the edge sequence
        edge_sequence = edges.solve_edges(cube)
        # calculate the corner sequence
        corner_sequence = corners.solve_corners(cube)
        # Is the parity algorithm required
        parity = False

        # output results
        if self.mode == "edges" or self.mode == "both":
            self.output += '\n'+(f"EDGE SEQUENCE:\n {edge_sequence}")
            # if odd number of edge and corner moves the parity algorithm is required
            if len(edge_sequence) % 2 != 0 and self.mode == "both":
                parity = True
                self.output += '\n'+("\nPARITY Ra PERM REQUIRED")
        if self.mode == "corners" or self.mode == "both":
            self.output += '\n'+(f"\nCORNER SEQUENCE:\n {corner_sequence}")

        # Solves the edges
        if self.mode == "edges" or self.mode == "both":
            for edge in edge_sequence:
                cube.rotate(dict.edge_setup_moves[edge])
                cube.rotate(dict.algorithms["edge_swap"])
                cube.rotate(dict.edge_unsetup_moves[edge])

        # if the parity algorithm is required
        if self.mode == "both":
            if parity:
                cube.rotate(dict.algorithms["parity"])

        # Solves the corners
        if self.mode == "corners" or self.mode == "both":
            for corner in corner_sequence:
                cube.rotate(dict.corner_setup_moves[corner])
                cube.rotate(dict.algorithms["corner_swap"])
                cube.rotate(dict.corner_unsetup_moves[corner])
        
        return self.output
    
    def cube_to_html(self, cube):
        faces = cube.get_all_faces()

        # Map face to position in the 3x12 grid (row, col_start)
        face_positions = {
            Face.U: (0, 3),   # top row, starting at col 3
            Face.L: (3, 0),   # middle row, starting col 0
            Face.F: (3, 3),   # middle row, starting col 3
            Face.R: (3, 6),   # middle row, starting col 6
            Face.B: (3, 9),   # middle row, starting col 9
            Face.D: (6, 3),   # bottom row, starting col 3
        }

        # Create a 9-row x 12-col grid to hold all squares
        html = '<div style="display:grid; grid-template-columns: repeat(12, 20px); grid-auto-rows: 20px; gap:4px;">'

        # Initialize empty grid
        grid = [[None for _ in range(12)] for _ in range(9)]

        # Fill grid with face colors
        for face, (row_start, col_start) in face_positions.items():
            face_2d = faces[face]
            for i, row_cells in enumerate(face_2d):
                for j, color_obj in enumerate(row_cells):
                    grid[row_start + i][col_start + j] = dict.color_map[color_obj.name]

        # Render grid
        for row in grid:
            for color in row:
                if color:
                    html += f'<span style="width:20px; height:20px; display:inline-block; background-color:{color}; border:1px solid black;"></span>'
                else:
                    html += '<span style="width:20px; height:20px; display:inline-block;"></span>'
        html += '</div>'
        return html
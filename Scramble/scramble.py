import random

# Scramble class that takes a length and move list
# and generates a scramble
# CURRENTLY HARDCODED FOR 3x3 MOVES ONLY
class Scramble:

    # Initialize the length and list of possible moves
    def __init__(self, length, moves):
        self.length = length
        self.moves = moves
        # set the self scramble
        self.scramble = self.generate_scramble()
    
    # generates and returns a scramble
    def generate_scramble(self): 
        scramble_string= ""
        # get first move
        move = random.randrange(0,17)
        # add move to scramble string
        scramble_string = scramble_string + " " + self.moves[move]
        # loop length-1 times to get that many moves
        for x in range(self.length-1):
            # get move
            next_move = self.pick_move_num(move)
            # Add it to string
            scramble_string = scramble_string + " " + self.moves[next_move]
            # set move to previous move
            move = next_move
        return scramble_string

    # based on last move chooses next move. 
    # Cant have two same side moves in a row
    def pick_move_num(self, previous_move): 
        # if move was above 2/3 cant be again
        if previous_move > 11:
            return random.randrange(0,11)
        # if move was middle third cant be again
        elif previous_move > 5:
            # random to determine if above or bellow middle
            temp_random = random.randrange(0,1)
            if temp_random == 1:
                return random.randrange(12, 17)
            else:
                return random.randrange(0,5)
        # must be from first third, choose from last two
        else:
            return random.randrange(6,17)

    
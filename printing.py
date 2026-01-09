def print_all_pieces(cube):
    for n in range(3):
        for i in range(3):
            for k in range(3):
                print(f"piece {n},{i},{k}: ", cube.get_piece((n,i,k)))
from random import randint 
from tictactoe_without_class import empty_board

def random_player(x_or_o, x_positions, o_positions):
    move = (0, 0)
    while move in x_positions + o_positions:
        x = randint(0, 2)
        y = randint(0, 2)
        move = (x, y)
    return move 

def smart_player(x_or_o, x_positions, o_positions):
    no_lose_board=[[(0,0), (1,0), (2,0)],
                  [(0,0), (0,1), (0,2)],
                  [(0,0), (1,1), (2,2)],
                  [(1,0), (1,1), (1,2)],
                  [(2,0), (1,1), (0,2)],
                  [(2,0), (2,1), (2,2)],
                  [(2,1), (1,1), (0,1)],
                  [(1,1), (0,1), (2,1)],
                  [(1,1), (1,0), (1,2)],
                  [(1,2), (0,2), (2,2)],
                  [(1,2), (1,1), (1,0)],
                  [(2,2), (2,1), (2,0)],
                  [(2,2), (2,1), (0,2)],
                ]

    possible_moves = []
    for pattern in no_lose_board:
        client_cell = None
        for cell in pattern:
            if cell not in x_positions and cell not in o_positions:
                if client_cell == None:
                    client_cell = cell
                else : 
                    client_cell = None
                    break

    if client_cell :
        possible_moves.append(client_cell)
    
    if possible_moves:
        return possible_moves[randint(0, len(possible_moves)-1)]
    else :
        return random_player(x_or_o, x_positions, o_positions)


                
"""
    ---------- ---------- ----------
        |          |          |          |
        |  (0,0)   |  (1,0)   |  (2,0)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,1)   |  (1,1)   |  (2,1)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,2)   |  (1,2)   |  (2,2)   |
        |          |          |          |
         ---------- ---------- ----------
"""
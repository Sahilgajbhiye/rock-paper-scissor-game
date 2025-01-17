from RPS_game import play
from RPS import player

def quincy(prev_play, opponent_history=[]):
    moves = ["R", "P", "S"]
    return moves[len(opponent_history) % 3]
 


play(player, quincy, 10, verbose=True)



import random

def play(player1, player2, num_games=1000, verbose=False):
    results = {"Player 1": 0, "Player 2": 0, "Ties": 0}

    for _ in range(num_games):
        move1 = player1("")
        move2 = player2("")
        if move1 == move2:
            results["Ties"] += 1
        elif (move1 == "R" and move2 == "S") or (move1 == "P" and move2 == "R") or (move1 == "S" and move2 == "P"):
            results["Player 1"] += 1
        else:
            results["Player 2"] += 1

        if verbose:
            print(f"Player 1: {move1} | Player 2: {move2}")
    
    print(results)
    return results

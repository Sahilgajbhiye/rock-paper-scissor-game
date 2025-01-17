import random

def player(prev_play, opponent_history=[]):
    # If it's the first move, play randomly
    if prev_play == '':
        return random.choice(['R', 'P', 'S'])
    
    # Track the opponent's previous moves
    opponent_history.append(prev_play)
    
    # Let's try to predict the opponent's next move based on the history
    # For simplicity, let's assume the opponent repeats their previous move
    predicted_move = opponent_history[-1]
    
    # Counter the predicted move
    if predicted_move == 'R':
        return 'P'  # Paper beats Rock
    elif predicted_move == 'P':
        return 'S'  # Scissors beats Paper
    elif predicted_move == 'S':
        return 'R'  # Rock beats Scissors
    
    # Default to random if something goes wrong
    return random.choice(['R', 'P', 'S'])

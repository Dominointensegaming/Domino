import random

def generate_dominoes():
    dominoes = [(i, j) for i in range(7) for j in range(i, 7)]
    random.shuffle(dominoes)
    return dominoes
def deal_hands():
    hands = {f"player_{i}": dominoes[i*7:(i+1) * 7] for i in range(num_players)}
    remaining = dominoes[num_players * 7:]
    return hands, remaining

def valid_move(piece, board):
    if not board:
        return True
    left, right = board=[0][0], board[-1][-1]
    return piece[0] == left or piece[1] == left or piece[0] == right or piece[1] == right
import sys
import os

# Adiciona o diretório 'app' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora o import deve funcionar
from game_logic import generate_dominoes, deal_hands, valid_move
def test_generate_dominoes():
    dominoes = generate_dominoes()
    assert len(dominoes) == 28, "deve haver 28 peças"
    assert len(set(dominoes)) == 28, "peças devem ser únicas"
    print("teste1 passou")

def test_deal_hands():
    dominoes = generate_dominoes()
    hands, remaining = deal_hands(dominoes, num_players=2)
    assert len(hands["player_0"]) == 7, "cada jogador deve ter 7 peças"
    assert len(hands["player_1"]) == 7, "cada jogador deve ter 7 peças"
    assert len(remaining) == 28 - (2 * 7), "deve sobrar peça"
    print("teste 2 passou")

def test_valid_move():
    board = [(6, 5), (5, 3)]
    valid_piece = (3, 4)
    invalid_piece = (1, 2)

    assert valid_move((2, 3), []), "primeira jogada valida"
    assert valid_move(valid_piece, board), "deve ser movimento valido"
    assert not valid_move(invalid_piece, board), "deve ser movimento invalido"
    print("teste3 passou")

if __name__ == "__main__":
    test_generate_dominoes()
    test_deal_hands()
    test_valid_move()

import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.
EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]



def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    move = minimax_move(state, 5, evaluate_custom)
    
    if move is None:
        legal = state.legal_moves()
        if legal:
            return random.choice(list(legal))
        else:
            return None

    return move


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    opponent = Board.opponent(player)

    if state.is_terminal():
        winner = state.winner()
        if winner == player:
            return float("inf")
        elif winner == opponent:
            return float("-inf")
        else:
            return 0.0

    board = state.get_board()
    player_pieces = board.num_pieces(player)
    opponent_pieces = board.num_pieces(opponent)
    total_pieces = player_pieces + opponent_pieces
    phase = total_pieces / 64.0

    piece_diff = player_pieces - opponent_pieces

    corners = [(0,0), (0,7), (7,0), (7,7)]
    player_corners = sum(1 for x, y in corners if board.tiles[y][x] == player)
    opponent_corners = sum(1 for x, y in corners if board.tiles[y][x] == opponent)
    corner_diff = player_corners - opponent_corners

    edges = [(x, y) for x in range(8) for y in range(8) if x in {0,7} or y in {0,7}]
    player_edges = sum(1 for x, y in edges if board.tiles[y][x] == player)
    opponent_edges = sum(1 for x, y in edges if board.tiles[y][x] == opponent)
    edge_diff = player_edges - opponent_edges

    player_moves = len(state.legal_moves())
    opponent_moves = len(state.board._legal_moves.get(opponent, set()))
    if player_moves + opponent_moves > 0:
        mobility = 100 * (player_moves - opponent_moves) / (player_moves + opponent_moves)
    else:
        mobility = 0

    player_positional = sum(
        EVAL_TEMPLATE[y][x] for x in range(8) for y in range(8) if board.tiles[y][x] == player
    )
    opponent_positional = sum(
        EVAL_TEMPLATE[y][x] for x in range(8) for y in range(8) if board.tiles[y][x] == opponent
    )
    positional_diff = player_positional - opponent_positional

    danger_positions = [(0,1), (1,0), (1,1), (0,6), (1,6), (1,7),
                        (6,0), (6,1), (7,1), (6,6), (6,7), (7,6)]
    player_danger = sum(1 for x, y in danger_positions if board.tiles[y][x] == player)
    opponent_danger = sum(1 for x, y in danger_positions if board.tiles[y][x] == opponent)
    danger_penalty = player_danger - opponent_danger

    def is_stable(x, y):
        return (x == 0 or x == 7) and (y == 0 or y == 7)

    player_stable = sum(1 for x, y in corners if board.tiles[y][x] == player)
    opponent_stable = sum(1 for x, y in corners if board.tiles[y][x] == opponent)
    stability = player_stable - opponent_stable

    early_score = (
        10 * mobility +
        25 * corner_diff +
        5 * edge_diff +
        10 * positional_diff -
        20 * danger_penalty
    )
    late_score = (
        40 * piece_diff +
        50 * corner_diff +
        5 * edge_diff +
        15 * positional_diff +
        30 * stability
    )

    score = (1 - phase) * early_score + phase * late_score

    return float(score)

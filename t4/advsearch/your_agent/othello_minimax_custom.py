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

    return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player.
    If the state is terminal, returns its utility.
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    adversary = Board.opponent(player)

    if state.is_terminal():
        winning_player = state.winner()
        if winning_player == player:
            return float("inf")
        elif winning_player == adversary:
            return float("-inf")
        else:
            return 0

    current_board = state.get_board()

    player_count = current_board.num_pieces(player)
    adversary_count = current_board.num_pieces(adversary)

    piece_difference = player_count - adversary_count

    corner_coords = [(0, 0), (0, 7), (7, 0), (7, 7)]
    player_corner_count = sum(1 for cx, cy in corner_coords if current_board.tiles[cy][cx] == player)
    adversary_corner_count = sum(1 for cx, cy in corner_coords if current_board.tiles[cy][cx] == adversary)

    corner_difference = player_corner_count - adversary_corner_count

    edge_coords = [(x, y) for x in range(8) for y in range(8) if x in [0, 7] or y in [0, 7]]
    player_edge_count = sum(1 for ex, ey in edge_coords if current_board.tiles[ey][ex] == player)
    adversary_edge_count = sum(1 for ex, ey in edge_coords if current_board.tiles[ey][ex] == adversary)

    edge_difference = player_edge_count - adversary_edge_count

    player_move_options = len(state.legal_moves())
    adversary_move_options = len(GameState(current_board, adversary).legal_moves())

    mobility_difference = player_move_options - adversary_move_options

    player_position_value = sum(
        EVAL_TEMPLATE[x][y] for x in range(8) for y in range(8) if current_board.tiles[y][x] == player
    )
    adversary_position_value = sum(
        EVAL_TEMPLATE[x][y] for x in range(8) for y in range(8) if current_board.tiles[y][x] == adversary
    )

    position_difference = player_position_value - adversary_position_value

    total_count = player_count + adversary_count

    if total_count < 20:
        score = (
            8 * mobility_difference +
            25 * corner_difference +
            2 * edge_difference +
            10 * position_difference
        )
    elif total_count < 44:
        score = (
            7 * mobility_difference +
            40 * corner_difference +
            3 * edge_difference +
            20 * position_difference +
            3 * piece_difference
        )
    else:
        score = (
            20 * piece_difference +
            50 * corner_difference +
            5 * edge_difference +
            10 * position_difference
        )

    return score

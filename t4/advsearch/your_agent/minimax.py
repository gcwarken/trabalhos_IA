import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    score, chosen_move = maximize_score(state, state.player, max_depth, eval_func, depth = 0)
    return chosen_move

def maximize_score(state, player, max_depth: int, eval_func: Callable, depth: int = 0, alpha=float('-inf'), beta=float('inf')):
    if state.is_terminal() or depth == max_depth:
        return eval_func(state, player), None

    legal_moves = state.legal_moves()
    if not legal_moves:
        return eval_func(state, player), None

    highest_score = float('-inf')
    best_move = None

    for action in legal_moves:
        resulting_state = state.next_state(action)
        evaluated_score, _ = minimize_score(resulting_state, player, max_depth, eval_func, depth + 1, alpha, beta)

        if evaluated_score > highest_score:
            highest_score = evaluated_score
            best_move = action

        alpha = max(alpha, highest_score)
        if alpha >= beta:
            break

    return highest_score, best_move


def minimize_score(state, player, max_depth: int, eval_func: Callable, depth: int = 0, alpha=float('-inf'), beta=float('inf')):
    if state.is_terminal() or depth == max_depth:
        return eval_func(state, player), None

    legal_moves = state.legal_moves()
    if not legal_moves:
        return eval_func(state, player), None

    lowest_score = float('inf')
    best_move = None

    for action in legal_moves:
        resulting_state = state.next_state(action)
        evaluated_score, _ = maximize_score(resulting_state, player, max_depth, eval_func, depth + 1, alpha, beta)

        if evaluated_score < lowest_score:
            lowest_score = evaluated_score
            best_move = action

        beta = min(beta, lowest_score)
        if beta <= alpha:
            break

    return lowest_score, best_move

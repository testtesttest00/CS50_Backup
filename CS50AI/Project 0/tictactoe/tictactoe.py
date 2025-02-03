"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    first = X
    second = O
    xminuso = 0
    for row in board:
        for value in row:
            if value == X:
                xminuso += 1
            elif value == O:
                xminuso -= 1
    if xminuso == 0:
        return first
    return second


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] not in range(3) or action[1] not in range(3):
        raise Exception("Invalid action")
    nextstate = copy.deepcopy(board)
    if not nextstate[action[0]][action[1]]:
        nextstate[action[0]][action[1]] = player(nextstate)
    else:
        raise Exception("Already filled")
    return nextstate


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = None
    for e in X, O:
        # check diagonal
        if e == board[0][0] == board[1][1] == board[2][2] or e == board[0][2] == board[1][1] == board[2][0]:
            win = e
            break
        # check horizontal
        for row in board:
            if e == row[0] == row[1] == row[2]:
                win = e
                break
        if win:
            break
        # check vertical
        for i in range(3):
            if e == board[0][i] == board[1][i] == board[2][i]:
                win = e
                break
        if win:
            break
    return win


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # terminal @ win/lose
    if winner(board):
        return True
    # terminal @ draw
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def maxplay(state, recordlow): # x's thought process
        if terminal(state):
            return utility(state)
        value = float("-inf")
        for action in actions(state):
            value = max(value, minplay(result(state, action), value))
            if value > recordlow:
                return value
        return value

    def minplay(state, recordhigh): # o's thought process
        if terminal(state):
            return utility(state)
        value = float("inf")
        for action in actions(state):
            value = min(value, maxplay(result(state, action), value))
            if value < recordhigh:
                return value
        return value

    if player(board) == X:
        v = maxplay(board, float("inf"))
        for action in actions(board):
            if minplay(result(board, action), float("-inf")) == v:
                return action

    if player(board) == O:
        v = minplay(board, float("-inf"))
        for action in actions(board):
            if maxplay(result(board, action), float("inf")) == v:
                return action

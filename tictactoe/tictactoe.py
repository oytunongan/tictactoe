"""
Tic Tac Toe Player
"""

import math
import copy

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
    table = []
    for i in range(len(board[0])):
        for j in range(len(board)):
            table.append(board[i][j])
    if X not in table and O not in table:
        return X
    elif table.count(X) > table.count(O):
        return O
    else:
        return X

    #raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves

    #raise NotImplementedError

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action in actions(board):
        raise Exception("Not a valid action!")

    new_board = copy.deepcopy(board)

    if player(board) == X and board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = X
    elif player(board) == O and board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = O

    return new_board

    #raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    if winner == None:
        for i in range(len(board)):
            check = []
            for j in range(len(board)):
                check.append(board[i][j])
            if (check[1:] == check[:-1]) and check[i] != None:
                winner = check[i]
                return winner

        for b in range(len(board)):
            check = []
            for a in range(len(board)):
                check.append(board[a][b])
            if (check[1:] == check[:-1]) and check[i] != None:
                winner = check[b]
                return winner

        for k in range(len(board)):
            check[k] = board[k][k]
        if (check[1:] == check[:-1]):
            winner = check[k]
            return winner

        for l in range(len(board)):
            check[l] = board[l][len(board) - 1 - l]
        if (check[1:] == check[:-1]):
            winner = check[l]
            return winner
    else:
        return None

    #raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    check = []
    for row in board:
        for cell in row:
            check.append(cell)
    if not EMPTY in check:
        return True

    return False

    #raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

    #raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        chances = []
        for action in actions(board):
            chances.append([Min_Value(result(board, action)), action])
        return sorted(chances, reverse=True)[0][1]
    elif player(board) == O:
        chances = []
        for action in actions(board):
            chances.append([Max_Value(result(board, action)), action])
        return sorted(chances)[0][1]
    else:
        return None

    #raise NotImplementedError

def Max_Value(board):
    if terminal(board):
        return utility(board)
    v = float(-math.inf)
    for action in actions(board):
        v = max(v, Min_Value(result(board, action)))
    return v

def Min_Value(board):
    if terminal(board):
        return utility(board)
    v = float(math.inf)
    for action in actions(board):
        v = min(v, Max_Value(result(board, action)))
    return v

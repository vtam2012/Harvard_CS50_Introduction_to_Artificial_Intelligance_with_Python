"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    next_player = X
    if next_player == X:
        return next_player
    else:
        next_player = O
    return next_player

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row_index, row in enumerate(board):
        for column_index, object in enumerate(row):
            if object == None:
                possible_actions.add((row_index, column_index))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if len(action) != 2:
        raise Exception("incorrect action")
    else:
        i, j = action
    new_board = deepcopy(board)
    if board[i][j] != None:
        raise Exception("provided action already taken")
    else:
       new_board[i][j] = player(board)
   

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
     
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != EMPTY:
            return board[1][1]

    return None
        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there is a winner return True
    if winner(board) != None:
        return True
    
    # iterate rows, if there is an empty spot, moves are still possible and no winner is detected
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    elif winning_player == 0:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

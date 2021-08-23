"""
# Horizontal winning condition
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
        # Vertical Winning Condition
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
        # Diagonal Winning Condition
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
        # Match Tie or Draw Condition
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running

"""
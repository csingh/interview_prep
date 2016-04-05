def select_cell(board, row, col):
    board = board[:]
    board[col] = row
    return board

def block_row(blocked_rows, row):
    blocked_rows = blocked_rows[:]
    blocked_rows[row] = True
    return blocked_rows

def diags_clear(board, current_col, row):
    up = row
    down = row
    for col in reversed(range(current_col)):
        up -= 1
        down += 1
        if up >= 0 and board[col] == up: return False
        if down < len(board) and board[col] == down: return False

    return True

def eight_queens():
    solutions = []

    def pick(board, blocked_rows, col):
        if col == len(board):
            solutions.append(board)
            return

        for row in range(len(board)):
            if not blocked_rows[row] and diags_clear(board,col,row):
                new_board = select_cell(board, row, col)
                new_blocked_rows = block_row(blocked_rows, row)
                pick(new_board, new_blocked_rows, col+1)

        return

    pick([None]*8, [False]*8, 0)

    return solutions

if __name__ == '__main__':
    soln = eight_queens()
    print("Should be 92:", len(soln))
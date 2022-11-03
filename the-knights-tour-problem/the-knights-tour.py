n = 8


def is_safe(x, y, board):
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False


def solve_knight_tour(n):
    board = [[-1 for i in range(n)] for i in range(n)]
    move_x = [2, 1, 2, 1, -2, -1, -2, -1]
    move_y = [1, 2, -1, -2, 1, 2, -1, -2]

    board[0][0] = 0
    pos = 1

    if (not solve(n, board, 0, 0, move_x, move_y, pos)):
        print("No solution exists")
    else:
        print_solution(n, board)


def print_solution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solve(n, board, curr_x, curr_y, move_x, move_y, pos):
    if (pos == n**2):
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = pos
            # print_solution(n, board)
            if solve(n, board, new_x, new_y, move_x, move_y, pos + 1):
                return True
            board[new_x][new_y] = -1
    return False


if __name__ == '__main__':
    solve_knight_tour(n)

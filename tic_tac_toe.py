def row_winner (board):
    for row  in board:
        all_equal = True
        piece = row[0]
        for entry in row:
            if entry ==' ' or piece != entry:
                all_equal = False
                break
        if all_equal:
            return True
    return False

def column_winner(board):
    for col in range(len(board[0])):
        all_equal = True
        piece = board[0][col]
        for row in board:
            if row[col] == ' ' or row[col] != piece:
                all_equal = False
                break
        if all_equal:
            return True
    return False

def diagonal_winner(board):
    all_equal1 = True
    all_equal2 = True
    topleft = board[0][0]
    topright = board[0][-1]
    for i in range(len(board)):
        if board[i][i] == ' ' or board [i][i] != topleft:
            all_equal1 = False
        if board[i][-i -1] == ' ' or board [i][-i-1] != topright:
            all_equal2 = False

    return all_equal1 or all_equal2

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def format_board(board):
    joined_rows = []
    for row in board:
        joined_rows.append("|".join(row))
    lines=[]
    for _ in board[0]:
        lines.append("-")
    line = f'\n{"+".join(lines)}\n'
    return line.join(joined_rows)

def play_move(board, player):
    print(f'{player} to play:')
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            if row < 0 or row > 2:
                print('Invalid row')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')

    while True:
        try:
            col = int(input("Enter column (1-3): ")) - 1
            if col < 0 or col > 2:
                print('Invalid column')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')


    if board[row][col] == ' ':
        board[row][col] = player
        print(format_board(board))
    else:
        print("That spot is already taken!")
        play_move(board, player)


def make_board():
    row = []
    for _ in range(3):
        row.append(' ')
    board = []
    for _ in range(3):
        board.append(row.copy())
    return board

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def play_game( player1, player2):
    board = make_board()
    print(format_board(board))
    player = player1
    for _ in range(9):
        play_move(board, player)

        if winner(board):
            print_winner(player)
            return

        if player == player1:
            player = player2
        else:
            player = player1

    print_draw()

play_game( 'X', 'O')
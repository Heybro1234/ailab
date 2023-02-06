board = [' ' for _ in range(9)]

def draw_board():
    row = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    print(row)
    print('---------')
    row = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    print(row)
    print('---------')
    row = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    print(row)

def get_move(player):
    move = -1
    while move < 0 or move > 8:
        try:
            move = int(input('{}, enter your move (0-8): '.format(player)))
            if board[move] != ' ':
                print('That space is already occupied')
                move = -1
        except ValueError:
            print('Please enter a valid number')
    return move

def has_won(player):
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def main():
    while True:
        draw_board()
        player_x_move = get_move('X')
        board[player_x_move] = 'X'
        if has_won('X'):
            draw_board()
            print('X has won!')
            break
        draw_board()
        player_o_move = get_move('O')
        board[player_o_move] = 'O'
        if has_won('O'):
            draw_board()
            print('O has won!')
            break

main()

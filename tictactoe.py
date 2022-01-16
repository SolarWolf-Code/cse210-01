'''
Tic-Tac-Toe
Author: Bradley Strange
'''


import colorama
from colorama import Fore


def create_board():
    board = []
    for slot in range(9):
        board.append(slot + 1)
    return board


def print_board(board):
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('- - - - -')
    print(board[3], '|', board[4], '|', board[5])
    print('- - - - -')
    print(board[6], '|', board[7], '|', board[8])
    print()


def player_turn(turn):
    if turn % 2 == 0:
        return (Fore.RED + 'X' + Fore.RESET)
    else:
        return (Fore.BLUE + 'O' + Fore.RESET)

# player input
# player chooses a number between 1 and 9
# chosen number is where the player wants to place their mark
# if the chosen number is already taken, player chooses again
# if the chosen number is not taken, the player places their mark there


def player_input(board, turn):
    move = int(
        input(f"It's {player_turn(turn)}'s turn. Choose a position (1-9): "))
    # if move is not between 1 and 9, player chooses again
    while move not in range(1, 10):
        move = int(
            input('You chose a number that is not between 1 and 9. Try again: '))
    # if move is already "X" or "O", player chooses again
    while board[move - 1] == (Fore.RED + 'X' + Fore.RESET) or board[move - 1] == (Fore.BLUE + 'O' + Fore.RESET):
        move = int(
            input('You chose a spot that is already taken from another player. Try again: '))
    # if move is not taken, the player places their mark there
    return move

# update board with player input


def update(board, player, turn):
    board[player_input(board, turn) - 1] = player
    print_board(board)


def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


# check if board is full and there are no winners

def cat_fight(board):
    count = 0
    for square in board:
        if square == (Fore.RED + 'X' + Fore.RESET) or square == (Fore.BLUE + 'O' + Fore.RESET):
            count += 1
        else:
            return False
    if count == 9:
        return True


def game_over(board):
    if has_winner(board):
        return True
    else:
        return False


# def main
def main():
    board = create_board()
    print_board(board)
    turn = 0
    while not game_over(board):
        turn += 1
        player = player_turn(turn)
        update(board, player, turn)
        if cat_fight(board) == True:
            print('Cat Fight!')
    else:
        print(f'{player} is the winner!')


if __name__ == "__main__":
    main()

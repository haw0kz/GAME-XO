

board = list(range(1,10))

def display_board(board):
    for i in range(3):
            print("|", board[1+i*3], "|", board[2+i*3], "|", board[3+i*3], "|")
            print("-" * 13)

def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Игрок 1 - выберите x или o:').upper()
    if marker == 'X':
        return ('X','O')       
    else:
        return ('O','X')
    
def place_marker(board,marker,position):
    board[position] = marker      

def win_check(board,mark):  
    # проверка строк
    if board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark:
         return True
    # проверка столбцов
    if board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark:
        return True
    # проверка диагоналей
    if board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark:
        return True
    return False
    
import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Игрок 1'
    else:
        return 'Игрок 2'

def board_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if board_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not board_check(board,position):
        position = int(input('Укажите поле:(1-9)'))
    return position

def replay():
    check = input('Хотите сыграть снова?: Y/N: ')
    return check == 'Y'


print('Добро пожаловать в игру КРЕСТИКИ-НОЛИКИ! Приятной игры!')

while True:
    the_board = [' ']*10
    display_board(the_board)
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' ходит первым!')
    play_game = input('Вы готовы играть? YES or NO: ')

    if play_game == 'YES':
        game_on = True
    else:
        game_on = False
    while game_on:

        if turn == 'Игрок 1':
            display_board(the_board)
            pos1 = player_choice(the_board)
            place_marker(the_board,player1_marker,pos1)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Выйграл игрок номер 1')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('У ВАС НИЧЬЯ!')
                    game_on = False
            turn = 'Игрок 2'
        else:
            if turn == 'Игрок 2':
                display_board(the_board)
                pos1 = player_choice(the_board)
                place_marker(the_board,player2_marker,pos1)
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print('Выйграл игрок номер 1')
                    game_on = False
                else: 
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('У ВАС НИЧЬЯ!')
                        game_on = False
                    else:
                        turn = 'Игрок 1'

    if not replay():
        break







 




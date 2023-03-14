import time

def field_create():
    global field
    field = [['-'] * 3 for i in range(3)]

def salute():
    print('................................Welcome|')
    time.sleep(1)
    print('................To the classic X-0 game|')
    time.sleep(1)
    print('..........You can play with your friend|')
    time.sleep(1)
    print('................Or enjoy it by yourself|')
    time.sleep(1)
    print('...Enter two coordinates to make a move|')
    time.sleep(1)
    print('..........................Choose wisely|')
    time.sleep(1)

def good_buy():
    print('...................Thanks for your time|')
    time.sleep(1)
    print('...You can play again whenever you want|')
    time.sleep(1)
    print('........................Have a good day|')

def field_view():
    global field
    print('  | 1 | 2 | 3 |')
    print('---------------')
    for i in range(3):
        print(i+1, '|', ' | '.join(field[i]), '|')
        print('---------------')

def make_move():
    while True:
        move = input('Make your move: ').split()

        if len(move) != 2:
            print('Your move must contain 2 coordinates.')
            continue

        x, y = move

        if not(x.isdigit() and y.isdigit()):
            print('Your move must contain numbers.')
            continue

        x, y = int(x), int(y)

        if 1 > x or x > 3 or 1 > y or y > 3:
            print('Numbers must be in the range from 1 to 3.')
            continue

        x, y = x-1, y-1

        if field[x][y] != '-':
            print('Choose another cell, this one is already filled.')
            continue

        return x, y

def win_check():

    for i in range(3):
        numbers = []
        for j in range(3):
            numbers.append(field[i][j])
        if numbers[0] == numbers[1] == numbers[2] and numbers[0] != '-':
            field_view()
            print(f'The game is over. {numbers[0]} wins.')
            return True

    for i in range(3):
        numbers = []
        for j in range(3):
            numbers.append(field[j][i])
        if numbers[0] == numbers[1] == numbers[2] and numbers[0] != '-':
            field_view()
            print(f'The game is over. {numbers[0]} wins.')
            return True

    numbers = []
    for i in range(3):
        numbers.append(field[i][i])
    if numbers[0] == numbers[1] == numbers[2] and numbers[0] != '-':
        field_view()
        print(f'The game is over. {numbers[0]} wins.')
        return True

    numbers = []
    for i in range(3):
        numbers.append(field[i][2-i])
    if numbers[0] == numbers[1] == numbers[2] and numbers[0] != '-':
        field_view()
        print(f'The game is over. {numbers[0]} wins.')
        return True

def play_again():
    print('Do you want to play again?')
    answer = input("Enter 'Y' for 'Yes' or anything else for 'No': ")
    if str.lower(answer) == 'y':
        main_game()

def main_game():
    field_create()
    turn = 0
    while True:
        field_view()

        if turn % 2 == 0:
            print("X's turn")
        else:
            print("0's turn")

        x, y = make_move()

        if turn % 2 == 0:
            field[x][y] = 'X'
        else:
            field[x][y] = '0'

        if win_check():
            play_again()
            break

        if turn == 8:
            field_view()
            play_again()
            break

        turn += 1

salute()
main_game()
good_buy()
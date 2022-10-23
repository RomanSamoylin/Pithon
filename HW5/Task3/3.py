# Создайте программу для игры в ""Крестики-нолики""
import random

clear_board = [i for i in range (1,10)]
tic = 'X'
tac = 'O'

def DrawBoard(b):
    print('-' * 15)
    k=1
    for i in range(len(b)):
        print(f'| {b[i]} |', end='')
        if k%3==0:
            print('\n'+'-'*15)
        k+=1

# DrawBoard(clear_board)

def RunGame(tic, tac, b):
    play_board = b
    player_doko= lambda x, a, b: a if x else b
    coin_toss = bool(random.randint(0,2))
    pos = int(input('В какую клетку ходим? '))
    k=0
    while k<10:
        # while (not 0<pos<10) or (pos not in b):
        #     print('Такой клетки нет или занята... Попробуйте ещё раз.')
        #     pos = int(input('В какую клетку ходим? '))
        for i in range(len(b)):
            if pos == b[i]:
                b[i] = player_doko(coin_toss, tic, tac)
        DrawBoard(b)
        coin_toss= not coin_toss
        k+=1

DrawBoard(clear_board)
RunGame(tic, tac, clear_board)
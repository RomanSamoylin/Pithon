import random


def RunGame_player (ps, pm, hl, tc):
    coin_toss = True
    while tc>0:
        turn = pm(coin_toss)
        while turn>hl:
            print(f'А вот жульничать не надо! Максимум {hl} за раз. \nПопробуйте ещё раз.')
            turn=pm(coin_toss)
        tc-=turn
        coin_toss = not coin_toss
        print(f'Осталось {tc} конфет')
    else:
        coin_toss = not coin_toss
        print(f'Игрок{ps(coin_toss)} победил. Поздравляем!')

def RunGame_bot (ps, pm, hl, tc):
    coin_toss = True
    while tc>0:
        if coin_toss == False:
            print('Ходит бот...')
            if tc<hl:
                tc=0
            else:
                tc-=random.randint(1,hl+1)
        else:
            turn = pm(coin_toss)
            while turn>hl:
                print(f'А вот жульничать не надо! Максимум {hl} за раз. \nПопробуйте ещё раз.')
                turn=pm(coin_toss)
            tc-=turn
        coin_toss = not coin_toss
        print(f'Осталось {tc} конфет')
    else:
        coin_toss = not coin_toss
        if coin_toss:
            print(f'Игрок{ps(coin_toss)} победил. Поздравляем!')
        else:
            print('Победил БОТ. Удачи в другой раз.')

def RunGame_AI (ps, pm, hl, tc):
    coin_toss = True
    while tc>0:
        if coin_toss == False:
            print('Ходит ИИ...')
            if tc<=hl:
                tc=0
            elif 0<tc<2*hl+1:
                if tc%29 == 0:
                    tc-=1
                else:
                    tc-=(tc%29)
            else:
                tc-=random.randint(1,hl+1)
        else:
            turn = pm(coin_toss)
            while turn>hl:
                print(f'А вот жульничать не надо! Максимум {hl} за раз. \nПопробуйте ещё раз.')
                turn=pm(coin_toss)
            tc-=turn
        coin_toss = not coin_toss
        print(f'Осталось {tc} конфет')
    else:
        coin_toss = not coin_toss
        if coin_toss:
            print(f'Игрок{ps(coin_toss)} победил. Поздравляем!')
        else:
            print('Победил ИИ. Удачи в другой раз.')

def Help():
    print('1v1 - Игра с другим игроком')
    print('1vsBot - Игра с ботом')
    print('1vsAI - Игра с  ИИ')
    print('exit или quit - закрыть программу')


player_switch = lambda x: 1 if x else 2
player_move = lambda b: int(input('Игрок {}, ваш ход: '.format(player_switch(b))))
hard_limit = 28
total_candies = 201
is_running= True
command=''

while is_running:
    command=input('Введите команду или help: ')
    if command == '1v1':
        RunGame_player (player_switch, player_move, hard_limit,total_candies)
    elif command == '1vsAI':
        RunGame_AI(player_switch, player_move, hard_limit,total_candies)
    elif command=='1vsBot':
        RunGame_bot(player_switch, player_move, hard_limit,total_candies)
    elif command == 'exit' or command == 'quit':
        is_running=False
        print('Завершение работы...')
    elif command == 'help':
        Help()
    else:
        print('Некорректный ввод. Попробуйте ещё раз...')
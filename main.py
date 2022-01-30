import os

from red_black import RedBlack
from game_interface import GameInterface
from user import User


print('Добро пожаловать в игру!')
while True:
    user_name = input('Введите Ваш ник: ')
    if f"{user_name.replace('@', '')}.json" in os.listdir('data'):
        user = User(user_name)
        password = input('Введите пароль: ')
        if password == user.password:
            print('Авторизация прошла успешно.')
            print(f'Ваш банк -- {user.money}')

            choice = int(input('Хотите пополнить деньги?\nНажмите 1, если да.\nНажмите 2, если нет.\n> '))
            if choice == 1:
                money = int(input('Сколько денег хотите добавить на счёт?\n> '))
                user.update_user_bank(money)
                print('Успешно добавлено!')
                print(f'Ваш банк -- {user.money}')
            break
        else:
            print('Ошибка! Пароль не верный!')
            continue
    else:
        print('Регистрация.')
        password = input('Введите пароль: ')
        user_bank = int(input('Введите Ваш банк: '))
        user = User(user_name, user_bank)
        if user.registration_new_user(password): 
            print('Регистрация прошла успешно!')
            print(f'Ваш банк -- {user.money}')
            break

while True:
    user_bet = int(input('Введите Вашу ставку: '))
    user_color_choice = int(input('Введите цвет (цифрой).\n0. Зелёное\n1. Красное\n2. Чёрное\n> '))
    user_number_choice = int(input('Введите число: '))

    game = RedBlack(user_color_choice, user_number_choice, user_bet)
    game.start_game()
    prize = game.get_prize_color_bet(user.money) + game.get_prize_number_bet()

    console = GameInterface(game)
    console.game_result_information()
    console.checking_winning(user.money, )

    user.update_statistic(console.game_color, game.game_number, game.color, game.user_number, user_bet, prize)
    user.update_user_bank(prize)
    print(f'Ваш банк -- {user.money}')

    if not game.checking_user_bank(user.money):
        print('У Вас больше нет денег в банке!')
        break

    choice = int(input('Нажмите 1, если хотите продолжить.\nНажмите 2, если хотите выйти.\n> '))
    if choice == 2:
        break

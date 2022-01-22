import os

from red_black import RedBlack
from game_interface import GameInterface
from user import User
from statistic import Statistic



print('Добро пожаловать в игру!')
user_name = input('Введите Ваш ник: ')
if f"{user_name.replace('@', '')}.json" in os.listdir('data'):
    user = User(user_name)
    password = input('Введите пароль: ')
    if user.verification_password(password):
        print('Авторизация прошла успешно.')
        print(f'Ваш банк -- {user.get_info_of_bank_from_json_file()}')

        choice = int(input('Хотите пополнить деньги?\nНажмите 1, если да.\nНажмите 2, если нет.\n> '))
        if choice == 1:
            money = int(input('Сколько денег хотите добавить на счёт?\n> '))
            user.update_user_bank(money)
            print('Успешно добавлено!')
            print(f'Ваш банк -- {user.get_info_of_bank_from_json_file()}')
    else:
        print('Ошибка! Пароль не верный!')
else:
    print('Регистрация.')
    password = input('Введите пароль: ')
    user_bank = int(input('Введите Ваш банк: '))
    user = User(user_name)
    user.create_json_file(password, user_bank)
    print('Регистрация прошла успешно!')
    print(f'Ваш банк -- {user.get_info_of_bank_from_json_file()}')

while True:
    user_bet = int(input('Введите Вашу ставку: '))
    if user.get_info_of_bank_from_json_file() < user_bet or user_bet > 300:
        print('Ставка не может превышать сумму в банке и не может быть больше 300.')
        continue

    user_color_choice = int(input('Введите цвет (цифрой).\n0. Зелёное\n1. Красное\n2. Чёрное\n> '))
    user_number_choice = int(input('Введите число: '))

    game = RedBlack(user_color_choice, user_number_choice, user_bet)
    game.start_game()
    prize = game.get_prize_color_bet()

    console = GameInterface(game)
    console.game_result_information()
    console.checking_winning()

    user.update_statistic(console.game_color, game.game_number, game.color, game.user_number, user_bet, prize)
    Statistic().update_statistic(console.game_color, game.game_number, game.color, game.user_number, user_bet, prize)
    user.update_user_bank(prize)
    print(f'Ваш банк -- {user.get_info_of_bank_from_json_file()}')

    if user.get_info_of_bank_from_json_file() <= 0:
        break

    choice = int(input('Нажмите 1, если хотите продолжить.\nНажмите 2, если хотите выйти.\n> '))
    if choice == 2:
        break

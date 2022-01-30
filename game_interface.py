import random
import time


class GameInterface:
    def __init__(self, game: object):
        self.game = game

    def drop_effect(function):
        def wrapper(self, *args, **kwargs):
            game_number_index = self.game.game_box.index(self.game.game_number)
            print_time = 20 + random.randint(0, 20)

            if game_number_index >= print_time:
                numbers = self.game.game_box[game_number_index - 20:game_number_index]
            else:
                numbers = self.game.game_box[game_number_index: game_number_index + 20]

            for index, number in enumerate(numbers, 1):
                print(f'{number}\n', end='')
                time.sleep(.1 + index/25)
            return function(self, *args, **kwargs)
        return wrapper

    @drop_effect
    def game_result_information(self):
        if self.game.game_number in self.game.red_numbers:
            self.game_color = 'Красное'
            print(f'Выпало красное число -- {self.game.game_number}')
        elif self.game.game_number in self.game.black_numbers:
            self.game_color = 'Чёрное'
            print(f'Выпало чёрное число -- {self.game.game_number}')
        else:
            self.game_color = 'Зелёное'
            print(f'Выпало зелёное число -- {self.game.game_number}')

    def checking_winning(self, money):
        game_result = self.game.get_prize_color_bet(money) + self.game.get_prize_number_bet()
        if game_result < 0:
            print('К сожалению, Вы проиграли!')
        else:
            print('Поздравляем с победой!')

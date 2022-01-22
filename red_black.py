import random

from exceptions import NotCorrectColorIndex


class RedBlack:
    def __init__(self,  user_color_index: int,
                        user_number: int,
                        bet: int):
        self.red_numbers = [number for number in range(1, 51)]
        self.black_numbers = [number for number in range(51, 101)]
        self.green_numbers = [0 for number in range(15)]

        self.game_box = self.red_numbers + self.black_numbers + self.green_numbers
        self.bet = bet
        self.user_color = self.__from_color_index_to_number(user_color_index)
        self.user_number = user_number

    def start_game(self):
        self.__shuffle_game_box()
        self.game_number = self.__generate_number()

    def get_prize_color_bet(self):
        if (self.game_number in self.red_numbers and \
            self.user_color in self.red_numbers) or \
            (self.game_number in self.black_numbers and \
            self.user_color in self.black_numbers):
            return self.bet * 2

        elif self.game_number in self.green_numbers and \
            self.user_color in self.green_numbers:
            return self.bet * 14

        if self.game_number == self.user_number:
            return self.bet * 30

        return -self.bet

    def check_correct_index_color(function):
        def wrapper(self, user_color_index, *args, **kwargs):
            if user_color_index not in range(0, 3):
                raise NotCorrectColorIndex("Введите корректный индекс цвета")
            return function(self, user_color_index, *args, **kwargs)
        return wrapper

    def __shuffle_game_box(self):
        return random.shuffle(self.game_box)

    def __generate_number(self):
        return random.sample(self.game_box, 1)[0]

    @check_correct_index_color
    def __from_color_index_to_number(self, user_color_index: int):
        if user_color_index == 1:
            self.color = 'Красное'
            return random.sample(self.red_numbers, 1)[0]

        elif user_color_index == 2:
            self.color = 'Чёрное'
            return random.sample(self.black_numbers, 1)[0]

        self.color = 'Зелёное'
        return 0

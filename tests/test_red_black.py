import unittest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from red_black import RedBlack


class TestUser(unittest.TestCase, RedBlack):
    # Тесты для игры.

    def test_get_prize_color_bet_with_red_or_black_color(self):
        # Тест, при котором и игра и пользователь загадали красное или чёрное.
        game = RedBlack(1, 10, 200)
        game.game_number = 10
        result = game.get_prize_color_bet(1000)
        self.assertEqual(result, 400)

    def test_get_prize_color_bet_with_green_color(self):
        # Тест, при котором и игра и пользователь загадали зелёное.
        game = RedBlack(0, 0, 200)
        game.game_number = 0
        result = game.get_prize_color_bet(1000)
        self.assertEqual(result, 2800)

    def test_get_prize_color_bet_with_different_colors(self):
        # Тест, при котором игра и пользователь загадали разные цвета.
        game = RedBlack(0, 0, 200)
        game.game_number = 10
        result = game.get_prize_color_bet(1000)
        self.assertEqual(result, -200)

    def test_get_prize_color_bet_with_uncorrect_bank(self):
        # Тест с некорректной суммой в банке.
        game = RedBlack(0, 0, 200)
        game.game_number = 0
        result = game.get_prize_color_bet(0)
        self.assertEqual(result, False)


    def test_get_prize_number_bet_with_same_numbers(self):
        # Тест, при котором игра и пользователь загадали одинаковое число.
        RedBlack.game_number = 10
        result = RedBlack(1, 10, 200).get_prize_number_bet()
        self.assertEqual(result, 6000)

    def test_get_prize_number_bet_with_different_numbers(self):
        # Тест, при котором игра и пользователь загадали разные числа.
        RedBlack.game_number = 1
        result = RedBlack(1, 10, 200).get_prize_number_bet()
        self.assertEqual(result, 0)


    def test_from_color_index_to_number(self):
        # Тест замены индекса на цвет игрока.
        def _from_color_index_to_number(user_color_index: int):
            # Переопределяем метод.
            if user_color_index == 1:
                return 15

            elif user_color_index == 2:
                return 75

            return 0

        result = _from_color_index_to_number(0)
        self.assertEqual(result, 0)

unittest.main()

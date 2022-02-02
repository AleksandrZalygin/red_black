import unittest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from user import User


class TestUser(unittest.TestCase):
    # Тесты для класса User
    """ 
    def test_create_json_file(self):
        # Тест создания нового json-файла.
        result = User('@nikolay', 1000).create_json_file('12345678')
        self.assertEqual(result, True)


    def test_registration_new_user_with_correct_data(self):
        # Тест регистрации нового пользователя. Все данные корректны.
        result = User('@nikolay', 100).registration_new_user('12345678')
        self.assertEqual(result, True)

    def test_registration_new_user_with_not_correct_name(self):
        # Тест регистрации нового пользователя. Имя некорректное.
        result = User('ivan', 100).registration_new_user('12345678') # or '@ivan123' or 'ivan123'
        self.assertEqual(result, False)   # raise NotCorrectNickName('Неккоректное имя пользователя!')

    def test_registration_new_user_with_not_correct_password(self):
        # Тест регистрации нового пользователя. Пароль некорректный.
        result = User('@ivan', 100).registration_new_user('123')
        self.assertEqual(result, False)  # raise NotCorrectPassword('Пароль не может быть меньше восьми символов!')
    

    def test_get_right_password_from_json(self):
        # Тест получения пароля пользователя из json-файла.
        result = User('@nikolay').get_right_password_from_json()
        self.assertEqual(result, '12345678')


    def test_get_info_of_bank_from_json_file(self):
        # Тест получения количество средств пользователя из json-файла.
        result = User('@nikolay')._get_info_of_bank_from_json_file()
        self.assertEqual(result, 1000)


    def test_update_user_bank(self):
        # Тест обновления банка пользователя.
        result = User('@nikolay').update_user_bank(200)
        result_true = User('@nikolay')._get_info_of_bank_from_json_file()
        self.assertEqual(result, result_true)
    """

    def test_update_user_bank_with_bonus(self):
        # Тест обновления банка пользователя.
        result = User('@nikolay').update_user_bank(1000)
        # result_true = User('@nikolay')._get_info_of_bank_from_json_file()
        self.assertEqual(result, 2700)

unittest.main()
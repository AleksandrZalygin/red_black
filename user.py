import json
import os

from exceptions import FileAlreadyExist, NotCorrectNickName, NotCorrectPassword

class User:
    def __init__(self, user_name: str, user_bank=0):
        self.user_name = user_name
        self.user_bank = user_bank

    def registration_new_user(self, password):
        if f"{self.user_name.replace('@', '')}.json" in os.listdir('../data/'):
            raise FileAlreadyExist('Такой пользователь уже существует!')
            return False

        for letter in self.user_name:
            if not self.user_name.startswith('@') or letter in r'[0-9]':
                raise NotCorrectNickName('Неккоректное имя пользователя!')
                return False

        if len(password) < 8:
            raise NotCorrectPassword('Пароль не может быть меньше восьми символов!')
            return False

        self.__create_json_file(password)
        return True

    def create_json_file(self, password):
        user_data = {
            "nickname": self.user_name,
            "password": password,
            "bank": self.user_bank,
            "statistic": {}
        }

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(user_data, json_file, ensure_ascii=False)
        return True

    def _get_right_password_from_json(self):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data['password']

    def _get_info_of_bank_from_json_file(self):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            self.money = data['bank']
        return self.money

    def add_bonus(function):
        def wrapper(self, money,  *args, **kwargs):
            if money >= 1000:
                money += 100
            return function(self, money, *args, **kwargs)
        return wrapper

    @add_bonus
    def update_user_bank(self, money: int):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        new_bank = data['bank'] + money
        data['bank'] = new_bank

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

        return new_bank

    def update_statistic(self,  game_color: str,
                                game_number: int,
                                user_color: str,
                                user_number: int,
                                bet: int,
                                result: str):

        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        data['statistic'][f'{len(data["statistic"]) + 1} game'] = {
                                        "game_color": game_color,
                                        "game_number": game_number,
                                        "user_color": user_color,
                                        "user_number": user_number,
                                        "bet": bet,
                                        "result": result
                                    }


        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)


        with open('data/statistic.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        data[f'{len(data) + 1} game'] = {
                                        "game_color": game_color,
                                        "game_number": game_number,
                                        "user_color": user_color,
                                        "user_number": user_number,
                                        "bet": bet,
                                        "result": result
                                    }


        with open('data/statistic.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

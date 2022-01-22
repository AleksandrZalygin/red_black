import json

from exceptions import NotCorrectNickName, NotCorrectPassword

class User:
    def __init__(self, user_name: str):
        self.user_name = user_name

    def check_correct_nickname(function):
        def wrapper(self, *args, **kwargs):
            for letter in self.user_name:
                if letter in '1234567890' or not self.user_name.startswith('@'):
                    raise NotCorrectNickName("Некорректный ник!")
            return function(self, *args, **kwargs)
        return wrapper

    def check_correct_password(function):
        def wrapper(self, password,  *args, **kwargs):
            if len(password) < 8:
                raise NotCorrectPassword('Пароль не может быть меньше восьми символов!')
            return function(self, password, *args, **kwargs)
        return wrapper

    @check_correct_nickname
    @check_correct_password
    def create_json_file(self, password: str, user_bank: int):
        user_data = {
            "nickname": self.user_name,
            "password": password,
            "bank": user_bank,
            "statistic": {}
        }

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(user_data, json_file, ensure_ascii=False)

    def verification_password(self, password):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        if data['password'] == password:
            return True
        return False

    def get_info_of_bank_from_json_file(self):
        with open(f'data/{self.user_name.replace("@", "")}.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data['bank']

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

        data['bank'] += money

        with open(f'data/{self.user_name.replace("@", "")}.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

        return data['bank']

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

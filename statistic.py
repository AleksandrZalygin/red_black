import json


class Statistic:
    def __init__(self):
        self.data_file = 'data/statistic.json'

    def update_statistic(self,  game_color: str,
                                game_number: int,
                                user_color: str,
                                user_number: int,
                                bet: int,
                                result: str):
                                
        with open(self.data_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        data[f'{len(data) + 1} game'] = {
                                        "game_color": game_color,
                                        "game_number": game_number,
                                        "user_color": user_color,
                                        "user_number": user_number,
                                        "bet": bet,
                                        "result": result
                                    }


        with open(self.data_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

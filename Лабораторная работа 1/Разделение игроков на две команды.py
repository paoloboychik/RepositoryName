list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

players_num = len(list_players)
size_of_team = players_num // 2

print(list_players[:size_of_team])
print(list_players[size_of_team:])
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

length = len(list_players)

team1 = list_players[:int(length / 2)]
team2 = list_players[int(length / 2):length]

print(team1)    # Первая команда
print(team2)    # Вторая команда

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статистикой посещений

dictionary = {
    "Общее количество": None,
    "Уникальные посещения": None
}

dictionary["Общее количество"] = len(users)
dictionary["Уникальные посещения"] = len(set(users))

print(dictionary)
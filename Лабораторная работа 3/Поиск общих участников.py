# TODO Напишите функцию find_common_participants
def find_common_participants(gr1, gr2, divider=','):
    res = list(set(gr1.split(divider)).intersection(set(gr2.split(divider))))
    res.sort()
    return res
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
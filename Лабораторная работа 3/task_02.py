# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, separator=","):
    str1 = set(str1.split(separator))
    str2 = set(str2.split(separator))

    common_list = list(str1.intersection(str2))
    # common_list = [x for x in str1 if x in str2] -  не понял как работает
    return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, "|"))

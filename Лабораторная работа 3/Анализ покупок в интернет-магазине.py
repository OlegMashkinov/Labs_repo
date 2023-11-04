# TODO Напишите функцию find_common_items

def find_common_items(last_week_purchases, current_week_purchases):
    # print(last_week_purchases, current_week_purchases)
    my_set1 = set(last_week_purchases)
    my_set2 = set(current_week_purchases)

    result = list(my_set1.intersection(my_set2))
    result.sort()
    # print(result)
    return result

last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары

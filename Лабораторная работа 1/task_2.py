# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44

volume_book = 100 * 50 * 25 * 4 / (1024**2)
numbers_book = int(volume / volume_book)

print("Количество книг, помещающихся на дискету:", numbers_book)

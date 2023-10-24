numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_missing = numbers.index(None)

average = sum(numbers[:index_missing] + numbers[index_missing + 1:]) / len(numbers)
numbers[index_missing] = average

print("Измененный список:", numbers)

# TODO Напишите функцию `is_palindrome`
def is_palindrome (str1):
    str1 = str1.lower()
    str1 = str1.split()
    str1 = "".join(str1)

    str2 = str1[::-1]

    if str1 == str2:
        return True
    else:
        return False

str1 = 'Кит на море не романтик'
print(is_palindrome(str1))

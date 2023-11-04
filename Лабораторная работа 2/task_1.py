money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
budjet = money_capital
count = 0
while budjet >= 0:
    budjet = budjet + salary - spend
    spend += spend * 0.05
    count += 1

if budjet < 0:
    count -= 1

print("Количество месяцев, которое можно протянуть без долгов:", count)

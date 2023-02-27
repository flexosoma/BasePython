#Задача 3
#Выполните следующие действия:
#   1. Изучите справку для модуля calendar с помощью функции help
#   2. Импортируйте модуль calendar
#   3. Найдите расположение файла модуля calendar и изучите его содержимое
#   4. Получите список доступных атрибутов модуля calendar
#   5. С помощью модуля calendar узнайте, является ли 2027 год високосным
#   6. С помощью модуля calendar узнайте, каким днем недели был день 25 июня 1995 года
#   7. Выведите в консоль календарь на 2023 год

import calendar

daysofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(calendar.isleap(2027))
print(daysofweek[calendar.weekday(1995, 6, 25)])

c = calendar.TextCalendar(calendar.MONDAY)

for i in range(1, 13):

    str = c.formatmonth(2023, i)
    print(str)
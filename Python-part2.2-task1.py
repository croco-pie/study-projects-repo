# Курс Python: основы и применение

# Задача 1, блок 2.2. Работа с кодом: модули и импорт

'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
'''

# Решение
import datetime

date_raw = list(map(int, input().split(' ')))
delta = datetime.timedelta(int(input()))
date_raw = datetime.date(*date_raw)
date = date_raw + delta
print(date.year, date.month, date.day)
# Курс Python: основы и применение

# Задача 1, блок 2.1. Ошибки и исключения
'''
Вашей программе будет доступна функция foo, которая может бросать исключения.
Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.
Пример решения, которое вы должны отправить на проверку.

try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
    
Подсказка: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''

# Решение
try:
    foo()
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')
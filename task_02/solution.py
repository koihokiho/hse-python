# Задание 2: Арифметические операции
# Реализуйте функции для выполнения основных арифметических операций


def add(a, b):
    """
    Сложение двух чисел
    """
    c = a + b
    pass


def subtract(a, b):
    """
    Вычитание b из a
    """
    c = a - b
    pass


def multiply(a, b):
    """
    Умножение двух чисел
    """
    c = a * b
    pass


def divide(a, b):
    """
    Деление a на b
    Должно вызывать исключение ZeroDivisionError при делении на ноль
    """
    c = a/b
    if b == 0:
        print("ZeroDivisionError")
    pass


def power(a, b):
    """
    Возведение числа a в степень b
    """
    c = a**b
    pass


def modulo(a, b):
    """
    Остаток от деления a на b
    """
    c = a % b
    pass


def floor_division(a, b):
    """
    Целочисленное деление a на b
    """
    c = a//b
    pass

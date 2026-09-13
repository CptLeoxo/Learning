# Week one

# Импортируем твою функцию из основного файла (допустим, он называется calculator.py)
# I have to import my code what I want to test
from calculator import calculator
from compare import compare

def test_int_addition():
    # Assert like what to put in, function(args) == "What I except to get"
    # Проверяем, что 2 + 2 = 4 (с форматированием, как в твоем коде)
    assert calculator("Int", "2", "2") == "Your result is 4"
    assert calculator("Int", "-5", "10") == "Your result is 5"

def test_invalid_type():
    # Assert like what to put in, function(args) == "What I except to get"
    # Проверяем, как код реагирует на неверный тип операции
    assert calculator("String", "5", "5") == "You have to choose Int / Float !"

def test_invalid_value():
    # Проверяем, как код реагирует на неверный параметр в операции
    # Assert like what to put in, function(args) == "What I except to get"
    assert calculator("Int", "5", "five") == "Error: Please enter only numbers."
    assert calculator("Float", "five", "6.7") == "Error: Please enter only numbers."

def test_greater():
    assert compare("5", "10") == "x is greater then y"
    assert compare("0", "-10") == "x is greater then y"


def test_less():
    assert compare("10", "5") == "x is less then y"
    assert compare("-10", "0") == "x is less then y"

def test_equal():
    assert compare("5", "5") == "x is equal to y"

def test_value_error():
    assert compare("five", "ten") == "Error Value!"
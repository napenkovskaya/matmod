# encoding: UTF-8

from __future__ import division # чтобы любое деление было гарантированно с плавающей точкой


# solves ODE using Euler method given the derivative function (right-hand side of the equation), interval, number of steps and start value
# решатель ОДУ методом эйлера. принимает (функцию!) производную, интервал (start_x ... end_x), размер сетки и начальное значение
def solve (derivative, start_x, end_x, grid_size, start_value):
    # массив для хранения решения. первое значение известно из аргументов.
    solution = [(start_x, start_value)]
    
    # вычисляем шаг сетки
    step = (end_x - start_x) / grid_size
    
    # текщие значения на текущем шаге сетки
    current_x = start_x
    current_value = start_value
    
    # идем по интервалу от начала до конца
    while current_x <= end_x:
        # собственно ФОРМУЛА для метода Эйлера
        current_value = current_value + step * derivative (current_x, current_value)
        
        current_x = current_x + step # передвигаем текущее значение по иксу на слеудющий шаг сетки
        solution.append ((current_x, current_value)) # добавляем в массим приближенных значений
        
    
    return solution # список кортежей (x, y)


# для удобства. вычисляет локальную погрешность из заданного приближенного решения и функции для вычисления точного
def local_error (approx, precise):
    # массив погрешностей
    errors = []
    
    # для каждого x и y приближенного решения...
    for x, y in approx:
        errors.append((x, abs(y - precise (x))))

    return errors

# для удобства. генерирует массив точных значений в том же формате что и .solve (нужно для построения графиков)
def generate_precise (precise_func, start, end, grid_size):
    step = (end-start)/grid_size
    current_x = start

    precise = []
    
    while current_x <= end:
        precise.append ((current_x, precise_func(current_x)))
        current_x = current_x + step
        
    return precise # list of tuples (x, y)
    





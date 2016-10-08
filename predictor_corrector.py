# encoding: UTF-8
from __future__ import division 


# предиктор-корректор. работает так же как метод эйлера, но с дополнительными итерациями (последний параметр)
def solve (derivative, start_x, end_x, grid_size, start_value, extra_iterations = 0):
    
    # сначала вычисляем первое приближенное решение по методу эйлера
    
    solution = [(start_x, start_value)]
    step = (end_x - start_x) / grid_size
    
    current_x = start_x
    current_value = start_value
    
    while current_x <= end_x:
        current_value = current_value + step * derivative (current_x, current_value)
        current_x = current_x + step
        solution.append ((current_x, current_value))


    # дополнительные итерации
    while extra_iterations > 0:
        extra_iterations = extra_iterations - 1 # декрементим счетчик оставшихся итераций
        
        new_solution = [] # исправленное решение для текущей итерации
        
        # первый элемент всех решений всегда одинаковый, т.к. он точный по определению метода
        # запоминаем x и y "прошлого" шага
        last_x, last_y = solution.pop(0)
        
        # и сразу добавляем в исправленное решение
        new_solution.append((last_x, last_y))
        
        # итерируем по оставшимся элементам "неисправленного" решения (из прошлого шага), для каждого значения вычисляем новое, уточненное и добавляем в массив уточненных значений
        
        for x, y in solution:
            # (x - last_x) всегда равен step, но для красоты вычислим его на месте, чтобы не полагаться на равномерность сетки
            
            # x и y - значения из предыдущей итерации. х, понятное дело, никогда не меняется - сетка-то та же самая
            # считаем новое значение:
            new_y = last_y + (x - last_x) * (derivative (last_x, last_y) + derivative (x, y)) / 2
            
            new_solution.append((x, new_y))
            
            last_x = x
            last_y = new_y
            
        solution = new_solution # уточненное решение становится исходным решением для следующей итерации
        
    # дополнительные итерации кончились тут.
    
    return solution 


 
def local_error (approx, precise):
    errors = []
    for x, y in approx:
        errors.append((x, abs(y - precise (x))))

    return errors


def generate_precise (precise_func, start, end, grid_size):
    step = (end-start)/grid_size
    current_x = start

    precise = []
    
    while current_x <= end:
        precise.append ((current_x, precise_func(current_x)))
        current_x = current_x + step
        
    return precise 
    





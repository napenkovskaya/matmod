# encoding: UTF-8
from __future__ import division, print_function
import predictor_corrector as pc

from math import sin, cos, log
import matplotlib.pyplot as plot



def precise (x):
    return sin (2 * x) + cos (x)

def derivative (x, y):
    k = 0.5 # extra error...
    return 2 * cos (2 * x) - sin (x)  + k * (y - precise (x))

start = 0
end = 7

start_N = 5

iterations = 4


errors = [] # тут будут глобальные ошибки для каждого размера сетки в виде [(размер сетки, ошибка), (размер сетки, ошибка), ... ]


# для сеток от 5 до дофига
for grid_multiplier in range(0, 12):
    grid_size = start_N * (2**grid_multiplier)
    
    # вычисляем приближенное решение
    approx = pc.solve (derivative = derivative, start_x = start, end_x = end, grid_size=grid_size, start_value=precise(start), extra_iterations = iterations)
    
    # только чтобы посчитать ошибки
    local_errors = pc.local_error (approx, precise)
    
    # и найти максимальную
    global_error = max ([x[1] for x in local_errors])
    
    # добавляем в массивчик
    errors.append((grid_size, global_error))
    
# рисуем по отработанной схеме
plot.figure ()

# по заданию обе оси должны быть логарифмическими. тогда получается симпатичный почти прямой график
plot.xscale('log')
plot.yscale('log')


x_val = [x[0] for x in errors] 
y_val = [x[1] for x in errors]

plot.plot (x_val, y_val, color="green", label="error", )

plot.savefig ("error_vs_grid_predictor.png")
    
    
    
    
    
# считаем критерии сходимости (или чо это там...)
    
p_asterisk = []
p_tilda = []

# копируем массив ошибок чобы не проебать
tmp_errors = errors

# предыдущие значения (изымаем первый элемент из массива ошибок)
prev_size, prev_err = tmp_errors.pop(0)

# шагаем по оставшимся значениям
for size, err in tmp_errors:
    # и считаем  для каждого значения циферки по формуле из задания 
    # log (x, 2) = логарифм второй степени из x
    p_asterisk.append( (size, log(prev_err/err, 2)) )
    prev_size = size # текущие ошибки становятся предыдущими
    prev_err = err
    


# то же самое, но нам уже нужны три значения - текущее, предыдущее и пред-предыдущее
tmp_errors = errors

prev_prev_size, prev_prev_err = tmp_errors.pop(0)
prev_size, prev_err = tmp_errors.pop(0)

for size, err in tmp_errors:
    # ну и формула другая..
    p_tilda.append ( (size, log((prev_prev_err - prev_err)/(prev_err - err), 2)) )
    prev_prev_size = prev_size
    prev_prev_err = prev_err
    prev_err = err
    prev_size = size
    



plot.figure ()

plot.xscale('log')
#plot.yscale('log') # у нас и так логарифм есть в подсчете, зачем нам еще один...

x_val = [x[0] for x in p_asterisk]
y_val = [x[1] for x in p_asterisk]

plot.plot (x_val, y_val, color="green", label="p_asterisk", )


x_val = [x[0] for x in p_tilda]
y_val = [x[1] for x in p_tilda]

plot.plot (x_val, y_val, color="red", label="p_tilda", )

plot.savefig ("p_asterisk_p_tilda_predictor.png")



f = open('p_asterisk_predictor.csv', 'w')
print ("size,p*", file=f)

for size, p in p_asterisk:
    print ("{0},{1}".format (size, p), file=f)

f.close()

f = open('p_tilda_predictor.csv', 'w')
print ("size,p~", file=f)

for size, p in p_tilda:
    print ("{0},{1}".format (size, p), file=f)

f.close()

        
    
    
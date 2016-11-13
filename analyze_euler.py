# encoding: UTF-8

from __future__ import division
from __future__ import print_function

import euler

from math import cos, sin
import matplotlib.pyplot as plot




def precise (x): # точное решение
    return sin (2 * x) + cos (x)

def derivative (x, y): # производная
    k = 0.5 # дополнительная ошибка
    return 2 * cos (2 * x) - sin (x)  + k * (y - precise (x))

start = 0
end = 7

N = 320

# возвращает массив кортежей вида [(x, y), (x, y), ...]
approx = euler.solve (derivative = derivative, start_x = start, end_x = end, grid_size=N, start_value=precise(start))

# подсчет локальной ошибки [(x, abs(y - precise(x)), ...]
errors = euler.local_error (approx, precise)

# для графика точного решения
precise_plot = euler.generate_precise (precise, start, end, N)


# создаем новую картинку
plot.figure ()


# приводим массив кортежей к понятному для pyplot формату
x_val = [x[0] for x in approx]
y_val = [x[1] for x in approx]

# рисуем график
plot.plot (x_val, y_val, color="blue", label="approx")

x_val = [x[0] for x in precise_plot]
y_val = [x[1] for x in precise_plot]

plot.plot (x_val, y_val, color="black", label="precise")




# подсчет глобальной ошибки
#x_val = [x[0] for x in errors]
y_val = [x[1] for x in errors]
global_error = max (y_val)

#plot.plot (x_val, y_val, color="red", label="errors")

# сохраняем картинку
plot.savefig ("plot_euler_{}.png".format(N))


print ("global error: {}".format(global_error))


# отгрузка циферок в файл
f = open('euler_{}.csv'.format(N), 'w')

print ("x,approx,precise,error", file=f)

for x, app in approx:
    print ("{0},{1},{2},{3}".format (x, app, precise(x),abs(app-precise(x))), file=f)

f.close()





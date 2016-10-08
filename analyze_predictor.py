# encoding: UTF-8

from __future__ import division
from __future__ import print_function

import predictor_corrector as pc

from math import cos, sin
import matplotlib.pyplot as plot




def precise (x):
    return sin (2 * x) + cos (x)

def derivative (x, y):
    k = 0.5 # extra error...
    return 2 * cos (2 * x) - sin (x)  + k * (y - precise (x))

start = 0
end = 7
N = 400

iterations = 10



approx = pc.solve (derivative = derivative, start_x = start, end_x = end, grid_size=N, start_value=precise(start), extra_iterations = iterations)


errors = pc.local_error (approx, precise)
precise_plot = pc.generate_precise (precise, start, end, N)

plot.figure ()


x_val = [x[0] for x in approx]
y_val = [x[1] for x in approx]
plot.plot (x_val, y_val, color="blue", label="approx")

x_val = [x[0] for x in precise_plot]
y_val = [x[1] for x in precise_plot]
plot.plot (x_val, y_val, color="black", label="precise")

x_val = [x[0] for x in errors]
y_val = [x[1] for x in errors]

global_error = max (y_val)

print ("global error: {}".format(global_error))

plot.plot (x_val, y_val, color="red", label="errors")

plot.savefig ("plot_predictor.pdf")


f = open('predictor.csv', 'w')
print ("x,approx,precise,error", file=f)

for x, app in approx:
    print ("{0},{1},{2},{3}".format (x, app, precise(x),abs(app-precise(x))), file=f)

f.close()






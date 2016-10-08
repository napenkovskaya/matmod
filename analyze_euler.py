from __future__ import division
from __future__ import print_function

import euler

from math import cos, sin
import matplotlib.pyplot as plot




def precise (x):
    return sin (2 * x) + cos (x)

def derivative (x, y):
    k = 0.5 # extra error...
    return 2 * cos (2 * x) - sin (x)  + k * (y - precise (x))

start = 0
end = 7
N = 4000


approx = euler.solve (derivative = derivative, start_x = start, end_x = end, grid_size=N, start_value=precise(start))


errors = euler.local_error (approx, precise)
precise_plot = euler.generate_precise (precise, start, end, N)

plot.figure ()


x_val = [x[0] for x in approx]
y_val = [x[1] for x in approx]
plot.plot (x_val, y_val, color="blue", label="approx")

x_val = [x[0] for x in precise_plot]
y_val = [x[1] for x in precise_plot]
plot.plot (x_val, y_val, color="black", label="precise")

#x_val = [x[0] for x in errors]
y_val = [x[1] for x in errors]

global_error = max (y_val)
print ("global error: {}".format(global_error))


f = open('euler.csv', 'w')
print ("x,approx,precise,error", file=f)

for x, app in approx:
    print ("{0},{1},{2}".format (x, app, abs(app-precise(x))), file=f)

f.close()

#plot.plot (x_val, y_val, color="red", label="errors")

plot.savefig ("plot_euler.pdf")



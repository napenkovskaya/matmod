import euler

from math import sin, cos
import matplotlib.pyplot as plot

def phi (x):
    return sin(2*x)+cos(x)

def phi_1 (x):
    return 2*cos(2*x)-sin(x)
    

errors = []
start_grid_size = 3
for grid_multiplier in range(0, 10):
    grid_size = start_grid_size * (2**grid_multiplier)
    
    approx = euler.solve_with_added_error (phi_1, 0, 7, grid_size, 1, precise = phi, k=5)
    local_errors = euler.local_error (approx, phi)
    
    global_error = max ([x[1] for x in local_errors])
    errors.append((grid_size, global_error))
    
plot.figure ()

plot.xscale('log')
plot.yscale('log')


x_val = [x[0] for x in errors]
y_val = [x[1] for x in errors]

plot.plot (x_val, y_val, color="green", label="error", )

plot.savefig ("error_vs_grid.pdf")
    
    
    
    
    
    
    
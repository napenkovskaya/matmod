import euler

from math import sin, cos, log
import matplotlib.pyplot as plot



def precise (x):
    return sin (2 * x) + cos (x)

def derivative (x, y):
    k = 0.5 # extra error...
    return 2 * cos (2 * x) - sin (x)  + k * (y - precise (x))

start = 0
end = 7

start_N = 10


errors = []


for grid_multiplier in range(0, 12):
    grid_size = start_N * (2**grid_multiplier)
    
    approx = euler.solve (derivative = derivative, start_x = start, end_x = end, grid_size=grid_size, start_value=precise(start))
    local_errors = euler.local_error (approx, precise)
    
    global_error = max ([x[1] for x in local_errors])
    errors.append((grid_size, global_error))
    
plot.figure ()

plot.xscale('log')
plot.yscale('log')


x_val = [x[0] for x in errors]
y_val = [x[1] for x in errors]

plot.plot (x_val, y_val, color="green", label="error", )

plot.savefig ("error_vs_grid_euler.pdf")
    
p_asterisk = []
p_tilda = []

tmp_errors = errors

prev_size, prev_err = tmp_errors.pop(0)

for size, err in tmp_errors:
    p_asterisk.append( (size, log(prev_err/err, 2)) )
    prev_size = size
    prev_err = err
    

tmp_errors = errors

prev_prev_size, prev_prev_err = tmp_errors.pop(0)
prev_size, prev_err = tmp_errors.pop(0)

for size, err in tmp_errors:
    p_tilda.append ( (size, log((prev_prev_err - prev_err)/(prev_err - err), 2)) )
    prev_prev_size = prev_size
    prev_prev_err = prev_err
    prev_err = err
    prev_size = size
    



plot.figure ()

plot.xscale('log')
#plot.yscale('log')

x_val = [x[0] for x in p_asterisk]
y_val = [x[1] for x in p_asterisk]

plot.plot (x_val, y_val, color="green", label="p_asterisk", )


x_val = [x[0] for x in p_tilda]
y_val = [x[1] for x in p_tilda]

plot.plot (x_val, y_val, color="red", label="p_tilda", )

plot.savefig ("p_asterisk_p_tilda_euler.pdf")

    
    
    
    
    
    
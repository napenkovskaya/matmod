import euler

from math import cos, sin
import matplotlib.pyplot as plot




precise = sin

derivative = cos

approx = euler.solve_with_added_error (derivative, 0, 12, 40, precise(0), precise=precise, k=3)


errors = euler.local_error (approx, precise)
precise = euler.generate_precise (precise, 0, 12, 100)

plot.figure ()


x_val = [x[0] for x in approx]
y_val = [x[1] for x in approx]
plot.plot (x_val, y_val, color="blue", label="approx")

x_val = [x[0] for x in precise]
y_val = [x[1] for x in precise]
plot.plot (x_val, y_val, color="black", label="precise")

x_val = [x[0] for x in errors]
y_val = [x[1] for x in errors]

global_error = max (y_val)
print "global error: ", global_error

#plot.plot (x_val, y_val, color="red", label="errors")


plot.savefig ("plot.pdf")






from __future__ import division # ensure every division is floating point by default



# solves ODE using Euler method given the derivative function (right-hand side of the equation), interval, number of steps and start value
def solve (derivative, start_x, end_x, grid_size, start_value):
    solution = [(start_x, start_value)]
    
    step = (end_x - start_x) / grid_size
    
    current_x = start_x
    current_value = start_value
    
    while current_x <= end_x:
        # current value is only required for artificially added error
        current_value = current_value + step * derivative (current_x, current_value)
        current_x = current_x + step
        solution.append ((current_x, current_value))
        
    
    return solution # list of tuples (x, y)



# solves ODE using Euler method given the derivative function (right-hand side of the equation), interval, number of steps and start value
def solve_with_added_error (derivative, start_x, end_x, grid_size, start_value, precise = None, k = 0):
    solution = [(start_x, start_value)]
    
    step = (end_x - start_x) / grid_size
    
    current_x = start_x
    current_value = start_value
    
    while current_x <= end_x:
        # current value is only required for artificially added error
        current_value = current_value + step * derivative (current_x)
        
        true_increment = precise(current_x + step) - precise (current_x)
        added_error = k * (step * derivative(current_x) - true_increment)
        
        current_value = current_value + added_error
        
        current_x = current_x + step
        solution.append ((current_x, current_value))
        
    
    return solution # list of tuples (x, y)





# calculates local error for approx (list of tuples) compared to the precise (function!)
def local_error (approx, precise):
    errors = []
    for x, y in approx:
        errors.append((x, abs(y - precise (x))))

    return errors

# generates list of values in the same form as returned from euler solver but for the precise solution (needed for plotting)
def generate_precise (precise_func, start, end, grid_size):
    step = (end-start)/grid_size
    current_x = start

    precise = []
    
    while current_x <= end:
        precise.append ((current_x, precise_func(current_x)))
        current_x = current_x + step
        
    return precise # list of tuples (x, y)
    





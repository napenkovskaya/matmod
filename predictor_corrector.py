from __future__ import division # ensure every division is floating point by default


# solves ODE using iterative predictor-corrector method given the derivative function (right-hand side of the equation), interval, grid size, 
# start value and number of additional iterations (equivalent to euler method for zero extra iterations)
def solve (derivative, start_x, end_x, grid_size, start_value, extra_iterations = 0):
    
    #first compute the initial solution 
    solution = [(start_x, start_value)]
    step = (end_x - start_x) / grid_size
    
    current_x = start_x
    current_value = start_value
    
    while current_x <= end_x:
        # current value is only required for artificially added error
        current_value = current_value + step * derivative (current_x, current_value)
        current_x = current_x + step
        solution.append ((current_x, current_value))


    # run additional iterations
    while extra_iterations > 0:
        extra_iterations = extra_iterations - 1
        new_solution = [] # corrected solution for the current iteration
        
        # remove the first element from the previsou solution and add it to the new one. (first element never changes!)
        last_x, last_y = solution.pop(0)
        new_solution.append((last_x, last_y))
        
        # iterate through remaining elements of the previous solution, calculate corrected values and add them to the new solution
        for x, y in solution:
            # (x - last_x) always equals step, but let's calculate it from x and last_x for clarity
            # x and y are values from th previous step. x from previous step happens to always be the same as in the current step
            new_y = last_y + (x - last_x) * (derivative (last_x, last_y) + derivative (x, y)) / 2
            
            new_solution.append((x, new_y))
            
            last_x = x
            last_y = new_y
            
        solution = new_solution # new solution is the next step's solution
        
    # end of extra iterations
    
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
    





from Blackbox_Problems_fixed import problem_1, problem_2, problem_3
import numpy as np

def random_search(function,input_args,seed):
    import numpy as np
    import random    
    n = 100
    best_fitness = 100    
    xmin, xmax = -10,10
    x = np.random.uniform(xmin,xmax,[input_args,n])
    r = 1    
    
    np.random.seed(seed)
    if input_args==2:
        fitness = function(x[0,:],x[1,:])
    else:
        fitness = function(x[0,:],x[1,:],x[2,:],x[3,:])
    
    stuck = 0
    iteration = 0
    
    while stuck<100:
        np.random.seed()
        xplus = np.random.uniform(-r,r,[input_args,n])    
        x_new = x.copy()
        x_new += xplus
        
        np.random.seed(seed)
        if input_args==2:
            fitness_new = function(x_new[0,:],x_new[1,:])
        else:
            fitness_new = function(x_new[0,:],x_new[1,:],x_new[2,:],x_new[3,:])
        
        if sum(fitness_new>fitness)==n:
            stuck += 1
        else:
            stuck = 0
        
        x = x * (fitness_new>fitness) + x_new * (fitness_new<fitness)
        fitness = fitness * (fitness_new>fitness) + fitness_new * (fitness_new<fitness)
        iteration += 1
    
    return x[:,fitness.argmin()],fitness.min(),iteration


seed = 5
x,fitness,iteration = random_search(problem_1,2,seed)
print('problem 1 random search result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
x,fitness,iteration = random_search(problem_2,2,seed)
print('problem 2 random search result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
x,fitness,iteration = random_search(problem_3,4,seed)
print('problem 3 random search result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
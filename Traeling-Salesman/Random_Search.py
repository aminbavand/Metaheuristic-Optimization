from Traveling_Salesman import traveling_salesman
import numpy as np
import matplotlib.pyplot as plt
import random
import time
start_time = time.time()



best_fitness = 10000
stuck = 0
iteration = 0
while stuck<500:

    salesman = traveling_salesman(num_cities=50)
    
    
    perm = np.random.permutation(range(50))
    
    N_old = perm[:6]
    
    N_rest = np.delete(perm,[0,1,2,3,4,5])
    
    best_fitness_new = 100000000
    
    
    r1 = random.randint(0,5)
    r2 = random.randint(0,43)
    N_new1 = N_old[0:r1]
    N_new2 = N_old[r1+1:6]
       
    N_new = np.concatenate((N_new1, [N_rest[r2]], N_new2))
    
    
    n=1
    while n<100:
        salesman.new_tour(tour = N_new)
        new_fitness = salesman.tour_length()
        if new_fitness<best_fitness_new:
            best_answer_new = N_new
            best_fitness_new = new_fitness         
            n=1
            N_rest[r2] = N_old[r1]
            N_old = N_new
        else:
            n+=1
        r1 = random.randint(0,5)
        r2 = random.randint(0,43)
        N_new1 = N_old[0:r1]
        N_new2 = N_old[r1+1:6]          
        N_new = np.concatenate((N_new1, [N_rest[r2]], N_new2))
    
    if best_fitness_new > best_fitness:
        stuck+=1
    else:
        stuck = 0
        best_answer = best_answer_new
        best_fitness = best_fitness_new    
    iteration+=1

print('best tour found is: ', best_answer)
print('length of this tour is: ', best_fitness)
print('iterations = ',iteration)
print("running time=",time.time() - start_time)
print('running time per iteration = ',(time.time() - start_time)/iteration)
salesman.new_tour(tour = best_answer)
salesman.plot()
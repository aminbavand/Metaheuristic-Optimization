from Traveling_Salesman import traveling_salesman
import numpy as np
import matplotlib.pyplot as plt
import random
import time
start_time = time.time()

import numpy as np

#selection
def selection(pop,fitness,mps):
    fitness1 = fitness.copy()
    fitness1 = fitness1.max()-fitness1
    fitness1+=50
    rel_fit = fitness1/fitness1.sum()
    rel_fit_cumm = np.cumsum(rel_fit)
    selected_ind = np.zeros((mps))
    for i in range(mps):
        selected_ind[i] = (rel_fit_cumm<random.uniform(0, 1)).sum()
        
    selected_ind = selected_ind.astype(int)
    selected_pop = pop[selected_ind,:]
    return selected_pop,selected_ind              
#mutation
def mutation(individual):
    individual_new = individual.copy()
    numbers = np.arange(50).tolist()
    for i in range(6):
        numbers.remove(individual_new[i])
    
    mut_ind = np.random.randint(6)
    replace_ind = np.random.randint(44)
    
    individual_new[mut_ind] = numbers[replace_ind]
    return individual_new
#crossover
def crossover(individual1,individual2,k):#k: the number of crossover points
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()
    
    all_points = np.random.permutation(range(5))    
    k_points = all_points[0:k] + 1
    k_points.sort()
    k_points = k_points.tolist()
    k_points = [0] + k_points
    for i in range(k):
        if i%2 ==1:
            individual1_new[k_points[i]:k_points[i+1]] = individual2[k_points[i]:k_points[i+1]]
            individual2_new[k_points[i]:k_points[i+1]] = individual1[k_points[i]:k_points[i+1]]
    i+=1
    if i%2==1:
        individual1_new[k_points[i]:] = individual2[k_points[i]:]
        individual2_new[k_points[i]:] = individual1[k_points[i]:] 
    return individual1_new, individual2_new



def rep_check(individual_new, individual_old):#checks if the new individual has repitition in it, replace it with its old values
    summ = 0
    for j in range(6):
        summ+= np.count_nonzero(individual_new-individual_new[j])
    if summ!=30:
        individual_new = individual_old
    return individual_new     






ps = 1000#population size
mps = 1000#mating pool size
miu = 0.4#probability of mutation
k = 1#crossover points
salesman = traveling_salesman(num_cities=50)


#generating and evaluating population
pop = np.zeros((ps,6))
fitness = np.zeros((ps))
for i in range(ps):
    perm = np.random.permutation(range(50))
    pop[i,:] = perm[0:6]
    

    

min_fitness = 10000
stuck = 0
iteration = 0
while stuck<300:
#for iteration in range(iterations):
    #compute fitness for all individuals
    for i in range(ps):
        salesman.new_tour(tour = pop[i,:])
        fitness[i] = salesman.tour_length()
    min_fitness_new = fitness.min()
    if min_fitness_new<min_fitness:
        stuck = 0
    else:
        stuck+=1
    #selection                
    selected_pop,selected_ind = selection(pop,fitness,mps)

    #mutation
    for i in range(mps):
        if random.uniform(0, 1) < miu:
            selected_pop[i,:] = mutation(selected_pop[i,:])
    #crossover
    selected_pop1 = selected_pop.copy()
    for i in range(int(mps/2)):
        selected_pop1[i*2,:],selected_pop1[i*2+1,:] = crossover(selected_pop1[i*2,:],selected_pop1[i*2+1,:],k)        
        #checking if there is a repitition a new arrays, then undo crossover
        selected_pop1[i*2,:] = rep_check(selected_pop1[i*2,:], selected_pop[i*2,:])
        selected_pop1[i*2+1,:] = rep_check(selected_pop1[i*2+1,:], selected_pop[i*2+1,:])        
    #replace new children in population
    minind = fitness.argmin()    
    min_fitness = fitness.min()
    elitism = pop[minind,:]
    #pop[selected_ind,:] = selected_pop1
    pop = selected_pop1
    maxind = fitness.argmax()
    pop[maxind,:] = elitism
    iteration+=1

for i in range(ps):
    salesman.new_tour(tour = pop[i,:])
    fitness[i] = salesman.tour_length()

print('best tour founded is: ',pop[fitness.argmin(),:])
print('length of this tour is: ',fitness.min())
print('iterations = ',iteration)
print("running time=",time.time() - start_time)
print('running time per iteration = ',(time.time() - start_time)/iteration)
salesman.new_tour(tour = pop[fitness.argmin(),:])
salesman.plot()
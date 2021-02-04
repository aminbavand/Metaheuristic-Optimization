from traveling_salesman import traveling_salesman
import numpy as np
import matplotlib.pyplot as plt
import random
import time


start_time = time.time()
def DE_mutation(pop,ind,F,ps):
    numbers = np.arange(ps).tolist()
    numbers.remove(ind)
    random.shuffle(numbers)
    individual2,individual3 = pop[numbers[0:2],:]
    individual = pop[ind,:] + F*(individual2-individual3)    
    individual = [ round(elem) for elem in individual]
    individual = np.array(individual)
    individual = individual%50
    return individual


def DE_crossover(pop,trial,parent_ind,pr):
    parent_individual = pop[parent_ind,:]
    
    bi_vec = np.random.choice(2,6,p=[1-pr, pr])#0:no change  1:change
    individual = np.zeros((6))
    for j in range(6):
        bi_vec_not = not(bi_vec[j])
        individual[j] = trial[j]*bi_vec[j] + parent_individual[j]*bi_vec_not
    return individual


def rep_check(individual_new, individual_old):#checks if the new individual has repitition in it, replace it with its old values
    summ = 0
    for j in range(6):
        summ+= np.count_nonzero(individual_new-individual_new[j])
    if summ!=30:
        individual_new = individual_old
    return individual_new     








import numpy as np
import random

ps = 200#population size
F = 0.5
pr = 0.3
salesman = traveling_salesman(num_cities=50)


#generating and evaluating population
pop = np.zeros((ps,6))
fitness = np.zeros((ps))
for i in range(ps):
    perm = np.random.permutation(range(50))
    pop[i,:] = perm[0:6]
    
pop1 = pop



min_fitness = 10000
stuck = 0
iteration = 0
while stuck<500:
#for i in range(iterations):
    pop = pop1
    pop1 = np.zeros((ps,6))#population at next step
    for ind in range(ps):
        salesman.new_tour(tour = pop[ind,:])
        fitness_old = salesman.tour_length()
        
        pop1[ind,:] = DE_mutation(pop,ind,F,ps)      
        pop1[ind,:] = DE_crossover(pop,pop1[ind,:],ind,pr)
     
        salesman.new_tour(tour = pop1[ind,:])   
        fitness_new = salesman.tour_length()
        
        if fitness_new > fitness_old:
            pop1[ind,:] = pop[ind,:]

        pop1[ind,:] = rep_check(pop1[ind,:],pop[ind,:])
    for i in range(ps):
        salesman.new_tour(tour = pop1[i,:])
        fitness[i] = salesman.tour_length()
    if fitness.min()>=min_fitness:
        stuck+=1
    else:    
        stuck = 0
        min_fitness = fitness.min()
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
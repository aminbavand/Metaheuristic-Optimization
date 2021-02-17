from Blackbox_Problems_fixed import problem_1, problem_2, problem_3
import numpy as np
import random


xmin, xmax = -10,10    

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


def mutation(individual):
    ind = np.random.randint(len(individual))
    individual[ind] = np.random.uniform(xmin,xmax,[1])
    return individual


def crossover(individual1,individual2,k):#k: the number of crossover points
    individual1_copy = individual1.copy()
    individual2_copy = individual2.copy()
    individual1[0:int(len(individual1)/2)] = individual2_copy[0:int(len(individual1)/2)]
    individual2[0:int(len(individual1)/2)] = individual1_copy[0:int(len(individual1)/2)]
    return individual1, individual2

def GA(function,input_args,seed):   
    ps = 100#population size
    miu = 0.2#probability of mutation    
    #initialization
    x = np.random.uniform(xmin,xmax,[input_args,ps])
    
    stuck = 0
    iteration = 0
    best_fitness = 100
    np.random.seed(seed)
    if input_args==2:
        fitness = function(x[0,:],x[1,:])
    else:
        fitness = function(x[0,:],x[1,:],x[2,:],x[3,:])
    
    
    while stuck<500:
        if fitness.min()<best_fitness:
            stuck = 0
        else:
            stuck += 1
        
        ind = fitness.argmin()
        best_individual = x[:,ind]
        best_fitness = fitness.min()
        
        #selection
        selected_pop,selected_ind = selection(x.T,fitness,ps)
        #mutation
        for i in range(ps):
            if random.uniform(0, 1) < miu:
                selected_pop[i,:] = mutation(selected_pop[i,:])
        #crossover        
        selected_pop1 = selected_pop.copy()
        for i in range(int(ps/2)):
            selected_pop[i*2,:],selected_pop[i*2+1,:] = crossover(selected_pop1[i*2,:],selected_pop1[i*2+1,:],2) 
        #updating the population and calculate fitness
        x = selected_pop.T
        np.random.seed(seed)
        if input_args==2:
            fitness = function(x[0,:],x[1,:])
        else:
            fitness = function(x[0,:],x[1,:],x[2,:],x[3,:])
        #elistism
        x[:,fitness.argmax()] = best_individual
        fitness[fitness.argmax()] = best_fitness    
        iteration += 1
    x = best_individual
    fitness = best_fitness
    return x,fitness,iteration
seed = 5
x,fitness,iteration = GA(problem_1,2,seed)
print('problem 1 GA result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
x,fitness,iteration = GA(problem_2,2,seed)
print('problem 2 GA result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
x,fitness,iteration = GA(problem_3,4,seed)
print('problem 3 GA result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
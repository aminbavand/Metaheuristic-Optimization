from traveling_salesman import traveling_salesman
import numpy as np
import matplotlib.pyplot as plt
import random
import time
start_time = time.time()


from sympy.utilities.iterables import multiset_permutations
#constructing all 60 permutations for a combination
count = 0
M = [1,2,3,4,5]
premutationn = np.zeros((60,6))
for a1 in range(4):
    for a5 in range(a1+1,5):
        M_copy = M.copy()
        del M_copy[a1]
        del M_copy[a5-1]
        for p in multiset_permutations(M_copy):
            premutationn[count,:] = [0]+[M[a1]]+p+[M[a5]]
            count+=1

salesman = traveling_salesman(num_cities=50)

N = [0,1,2,3,4,5,49,49,49,49]
old_fitness = 100000000

for n in range(15890700-1):#50!/(6!*44!)=15890700
     
    N[0] = (N[1]+N[2]+N[3]+N[4]+N[5]==45+46+47+48+49)+N[0]
    N[1] = ((N[2]+N[3]+N[4]+N[5]==46+47+48+49)+N[1])*(N[1]+N[2]+N[3]+N[4]+N[5]!=45+46+47+48+49) + (N[0]+1)*(N[1]+N[2]+N[3]+N[4]+N[5]==45+46+47+48+49)
    N[2] = ((N[3]+N[4]+N[5]==47+48+49)+N[2])*(N[2]+N[3]+N[4]+N[5]!=46+47+48+49) + (N[1]+1)*(N[2]+N[3]+N[4]+N[5]==46+47+48+49)
    N[3] = ((N[4]+N[5]==48+49)+N[3])*(N[3]+N[4]+N[5]!=47+48+49) + (N[2]+1)*(N[3]+N[4]+N[5]==47+48+49)
    N[4] = ((N[5]==49)+N[4])*(N[4]+N[5]!=48+49) + (N[3]+1)*(N[4]+N[5]==48+49)
    N[5] = ((N[5]+1)%50 + (N[4]+1)*(N[5]==49))%50#if this digit reach 50, start from the begining        
    
    N1 = N[0:6]
    for j in range(60):
        N2 =  [N1[int(premutationn[j,0])]]
        N2.append(N1[int(premutationn[j,1])])
        N2.append(N1[int(premutationn[j,2])])
        N2.append(N1[int(premutationn[j,3])])
        N2.append(N1[int(premutationn[j,4])])
        N2.append(N1[int(premutationn[j,5])])
        
        salesman.new_tour(tour = N2)
        new_fitness = salesman.tour_length()
        if new_fitness<old_fitness:
            best_answer = N2
            old_fitness = new_fitness                            

salesman.new_tour(tour = best_answer)
print('best tour is: ', best_answer)
print('length of best tour is: ', salesman.tour_length())
print("running time=",time.time() - start_time)
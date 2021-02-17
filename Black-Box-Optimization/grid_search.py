from Blackbox_Problems_fixed import problem_1, problem_2, problem_3
import numpy as np

def grid_search(function,seed):

    


    if function==problem_1:    
        #problem 1 grid search:
        steps = 2000
        x = 0.01*np.arange(-steps/2, steps/2)
        y = 0.01*np.arange(-steps/2, steps/2)
        X, Y= np.meshgrid(x, y)
        Z1= problem_1(X, Y)
        fitness = Z1.min()
        r1,c1 = np.where(Z1==Z1.min())
        x = [x[c1],y[r1]]
        
    #problem 2 grid search
    if function==problem_2:
        steps = 2000
        x = 0.01*np.arange(-steps/2, steps/2)
        y = 0.01*np.arange(-steps/2, steps/2)
        X, Y= np.meshgrid(x, y)
        np.random.seed(seed)
        Z2= problem_2(X, Y)
        fitness = Z2.min()
        r2,c2 = np.where(Z2==Z2.min())
        x = [X[r2,c2],Y[r2,c2]]


    #problem 3 grid search
    if function==problem_3:
        steps = 100
        x = 0.1*np.arange(-steps/2, steps/2)
        y = 0.1*np.arange(-steps/2, steps/2)
        w = 0.1*np.arange(-steps/2, steps/2)
        t = 0.1*np.arange(-steps/2, steps/2)
        X, Y, W, T = np.meshgrid(x, y, w, t)
        np.random.seed(seed)
        Z3= problem_3(X, Y, W, T)
        fitness = Z3.min()                
        r3,c3,f3,u3 = np.where(Z3==Z3.min())
        x = [X[r3,c3,f3,u3],Y[r3,c3,f3,u3],W[r3,c3,f3,u3],T[r3,c3,f3,u3]]        
    return x,fitness
seed = 5
x,fitness = grid_search(problem_1,seed)
print('problem 1 grid search result is:', fitness)
print('and this result is for point: ', x)
print('')
x,fitness = grid_search(problem_2,seed)
print('problem 2 grid search result is:', fitness)
print('and this result is for point: ', x)
print('')
x,fitness = grid_search(problem_3,seed)
print('problem 3 grid search result is:', fitness)
print('and this result is for point: ', x)
print('')
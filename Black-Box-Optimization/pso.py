from Blackbox_Problems_fixed import problem_1, problem_2, problem_3
import numpy as np

def PSO(function,input_args,seed):
    import numpy as np

    ns = 100

    xmin, xmax = -10,10


    x = np.random.uniform(xmin,xmax,[input_args,ns])
    np.random.seed(seed)
    if input_args==2:
        Zx = function(x[0,:], x[1,:])    
    else:
        Zx = function(x[0,:], x[1,:], x[2,:], x[3,:])


    y = x.copy()
    if input_args==2:
        Zy = function(y[0,:], y[1,:])    
    else:
        Zy = function(y[0,:], y[1,:], y[2,:], y[3,:])

    yhat = y[:,Zy.argmin()]
    Zyhat = Zy.min()


    v = np.zeros((input_args,ns))
    c1 = 0.01
    c2 = 0.1

    stuck = 0
    iteration = 0
    while stuck<500:#stopping criterion: if for 500 iterations, the best answer does not change
        iteration += 1
        np.random.seed()
        r1 = np.random.uniform(0,1,input_args)
        r2 = np.random.uniform(0,1,input_args)
        #for each particle if f(xi)<f(yi) then yi=xi 
        y[:,(Zx<Zy)] = x[:,(Zx<Zy)].copy()
        #set yhat equal to minimum y
        np.random.seed(seed)
        if input_args==2:
            Zy = function(y[0,:], y[1,:])    
        else:
            Zy = function(y[0,:], y[1,:], y[2,:], y[3,:])
        yhat = y[:,Zy.argmin()]
        #for each particle update velocity and position
        v += (c1*r1*(y-x).T + c2*r2*(yhat-x.T)).T
        x += v
        if input_args==2:
            Zx = function(x[0,:], x[1,:])    
        else:
            Zx = function(x[0,:], x[1,:], x[2,:], x[3,:])   

        Zyhatold = Zyhat.copy()
        Zyhat = Zy.min()
        if Zyhat<Zyhatold:
            stuck = 0
        else:
            stuck += 1
    if input_args==2:
        x = [y[0,Zy.argmin()], y[1,Zy.argmin()]]
    else:
        x = [y[0,Zy.argmin()], y[1,Zy.argmin()], y[2,Zy.argmin()], y[3,Zy.argmin()]]    
    fitness = Zyhat
    return x,fitness,iteration 

    
    
    
seed = 5
x,fitness,iteration = PSO(problem_1,2,seed)
print('problem 1 PSO result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
x,fitness,iteration = PSO(problem_2,2,seed)
print('problem 2 PSO result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
x,fitness,iteration = PSO(problem_3,4,seed)
print('problem 3 PSO result is:', fitness)
print('and this result is for point: ', x)
print('iteration numbers = ', iteration)
print('')
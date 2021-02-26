# Black-Box-Optimization

This project is comprised of 7 .py files as follows:

1. **Blackbox_Problems_fixed.py**:
Defines 3 Blackbox problems class

2. **Initialize.py**:
Shows one example for each blackbox problem: for a given input, it shows the respective output

3. **ga.py**:
Applies the genetic algorithm to find the minimum answer for each blackbox problem

4. **random_search.py**:
Applies random search algorithm to find the minimum answer for each blackbox problem

5. **grid_search.py**:
Applies grid search to find the minimum answer for each blackbox problem

6. **pso.py**:
Applies particle swarm optimization algorithm to find the minimum answer for each blackbox problem

7. **main.py**:
Applies all of the above functions on each of the 3 blackbox problems and compares them together



### Grid search

For grid search, I used meshgrid to construct every possible combination of input arguments. Then I used the constructed matrices (form meshgrid) as input arguments to problem_1,2, and 3. In the martix of results, the minimum element is the answer. With a few trial and error, we would find out that the best answers for all 3 problems are in range -5 to 5. For problem_1 and problem_2, we set the range of inputs to [-10,10] with step size 0.01. But since probem_3 has 4 input arguments, the meshgrid size would be very large and we will get a memory error. So for problem_3, the input ranges are from -5 to 5 and with step size 0.1.



### Random search

For Random search, I started from 100 random points in 4 dimensional space and update them inependently. In each step, I generate a random point in the neighborhood of each point and check if the objective function is improved, then change the point to the new point. If after 100 iterations, none of the points get improved, then the algorithm would be terminated.


### Particle Swarm Optimization

In particle swarm optimization, we start with a population of random answers in the search space and in eacn step, we move the populations toward better positions. The update is based on the memory of eacch particle itself and also the memory of all particles. The movement direction of each particle is a linear combination of the two directions. One is the direction toward the best point that this particle has ever reached, and the other is the direction toward the best point that all of particles have ever reached. This way,at each step all points would be updated and probably give us better results. After some number of iterations, if thereis no improvement in the best acheived point, we will terminate the algorithm.

The tendancies of the algorithm is moving toward those points that probably give us better objective values. The tunable parameters are the population size, and c1 and c2 coefficients (coeffinients that tell us how much is the effect of the local minimum and global minimum on the update). One flaw in the PSO algorithm is that there is no checking if the new points actually give us better results. So we can modify the algorithm so that if the objective function for the new point is not better, then do not update that point.

PSO is expected to work better than random search, because in random search there is no rational behind how we update the points. But in PSO, the points are moving toward the optimum points. Compared to grid search, it probably is much faster than that because it is not searching every point in the space. But this is the reason that the found answer by grid search is better, because PSO might miss some points in the search space. The only problem is that since the step size of our grid search cannot be selected to small (it takes much time to be executed), it is possible that the respond found by PSO would be better than grid search, but he probability is low. 


### Genetic algorithm

Genetic algorithm is a powerful tool for problems that are facing a alarge space of possible answers. First it generates a population of possible answers randomly. After that, it chooses some individuals of this popluation (individuals with better fitness have higher probability of being choosed) to be parents for the next generation. This is called selection. After that each of these parents mutate with a small probability. Mutation is a little change in the construction of an answer. Next step is crossover which two parents swap some genes between them. Now we have next generation. Note that also we transfer the best answer of each generation without any change to the next generation (elitism). This way, we can make sure that the best solution found so far, would not be destroyed. We repeat this process for multiple times until for 500 consecutive iterations, the best found tour would not be changed.

Genetic algorithm tends to produce better answers by combining better answers togetger and making small change to some of them. Tunable parameters are the probability of mutation, population size, mating pool size and the number of crossover points. We can modify the algorithm by changing these parameters and set them to those values which give us better results in terms of finding optimum value in a short time.

The performance of genetic algorithm is expected to be the same as PSO. Because both of these algorithms start with a random population and update the populations trying to improve the obective function for the population. In campare to random search, I expect the GA to works better because there is some logic behind updating points, but random search blindly generate new points in the vicinity of the points and update them if the new point sare better. In campare to grid search, it is the same comparison that I made between PSO and grid search in the previous part.


# Traveling-Salesman

This project is comprised of 6 .py files as follows:

1. **Traveling_Salesman.py**:
Defines the traveling-salesman class

2. **Initialization.py**:
Plots three random tours

3. **Exhaustive_Search.py**:
Applies an omptimum exhaustive search algorithm to find the best tour consisting of 6 cities.

4. **Random_Search.py**:
Applies the random search algorithm to find the best tour consisting of 6 cities.

5. **Genetic_Algorithm.py**:
Applies the genetic algorithm to find the best tour consisting of 6 cities.

6. **Differential_Evolution.py**:
Applies the differential evolution algorithm to find the best tour consisting of 6 cities.




### Exhaustive search
Exhasutive search is a search through every possible answer in the space. In traveling salesman problem defined above, we are facing with the problem of finding 6 cities among 50 different cities which the distance of traveling from the first city to the 6th city and going back to the first one, in a way that it passes all 4 other cities exactly once would be minimum. On other words, we want to choose 6 cities named a0, a1, a2, a3, a4, and a5 from 50 cities in which |a1-a0|+|a2-a1|+|a3-a2|+|a4-a3|+|a5-a4|+|a0-a5| would be minimum. There are a total 50!/(6!*44!) possible combinations of 6 cities out of 50 cities and each of them has 6!=720 permutations. But some permutations may represent the same tour. For example, all these permutations of a0, a1, a2, a3, a4, a5 are the same:

[a0, a1, a2, a3, a4, a5],[a0, a5, a4, a3, a2, a1]

[a5, a0, a1, a2, a3, a4],[a5, a4, a3, a2, a1, a0]

[a4, a5, a0, a1, a2, a3],[a4, a3, a2, a1, a0, a5]

[a3, a4, a5, a0, a1, a2],[a3, a2, a1, a0, a5, a4]

[a2, a3, a4, a5, a0, a1],[a2, a1, a0, a5, a4, a3]

[a1, a2, a3, a4, a5, a0],[a1, a0, a5, a4, a3, a2]

So, there are actually (6!/12)=60 permutations for each combination of 6 cities. Therefore, there are (50!/(6!44!))*60 possible tours that need to be evaluated, so the minimum length tour would be found.

Advantage of exhastive search in this problem is that we can find the optimum solution with certainty, but it takes so much time to search through all the possible solutions (disadvantage).

###### Implementation:
I used two for loops. The first loop finds every combination of 6 cities among 50 cities and the second loop finds all the 120 permuations for that combination. Before that, I constructed a 120*6 array that gives us all the 120 permutations for one combination and used this matrix in second loop every time (to avoid redundancy and save time). Every time, the code checks out whether or noty the current permutation is the best tour found so far and if it is, it preserves that tour until it finds another tour that its length is better than current best tour.








### Random search

Random search starts from one random possible answer and everytime tries to move into a new answer in the neighborhood of the current answer. At each step, it randomly chooses an answer in the neighborhood of the current answer and check if the objective function for this new answer is better than the current point; if it is, it then moves to the new point and otherwise it stays at its current position.

For this problem, the answers are string of length 6 (with order) out of 50 cities. I defined the "neighborhood" of each individual as follows: every string that differs with current one in exactly one place. In other words, the hamming distance between each two neighbors should be 1. Since this method has a high probability of getting stuck in a local minimum, I ran it multiple times (starting from different random initialization) and the best tour obtained in all runs will be reported as the final answer.

I ran this algorithm multilpe times. In each run, the terminated criterion was defined as follows: If for 100 consecutive updates, there was no replacement, which means the algorithm has got stuck in a local minimum. After each run, the answer will be saved and if for another run the answer gets better, the new answer will replace the old one. If for 500 consecutive runs, the best answer doesn't change, the algorithm would be terminated.

Advantage of using random search in traveling salesman problem is that it is very fast, but its disadvantage is that it might get stuck in a local minimum. Also, doesn't matter how much we run it, still we cannot be sure that the best solution that we have found so far, is actually the best answer to the problem.


### Genetic Algorithm


Genetic algorithm is a powerful tool for the problems that are facing a large volume of possible answers. First, it generates a population of possible answers randomly. After that, it chooses some individuals from this popluation (individuals with better fitness have higher probability of being chose) to be parents for the next generation. This is called selection. After that, each of these parents mutate with a small probability. Mutation is a little change in the construction of an answer. Next step is crossover which is swap of some genes between two parents. Now, the next generation is created (after performing mutation and crossover). Note that also we transfer the best answer of each generation without any change to the next generation. This way, we can make sure that the best solution found so far, would not be tossed away. We repeat this process for multiple times until for 500 consecutive iterations, the best obtained tour would not be changed. For solving traveling salesman problem with genetic algorithm, our populatoin's individuals are 6 length strings which their elements are 6 different cities of 50 possoble cities. There are 3 important parts that should be defined in this poroblem:

* Selectoin: We can assign a probability to each individual of population which is the probability of that individual being chose as a parent for the next generation. As said, this probability should be higher for those who have better fitness than the others. We know that the smaller the length of a tour, the better the tour is. So we can subtract each individual's length from the maximum length of individuals in the current poulation, and divide all of them by this maximum. The resulting numbers are relative fitnesses and sum of them is equal to 1 and they are suitable for being the selction probabilities. Note that we should add a constant value in order to avoid zero probability.
* Mutation: we use single point mutation. It means with a small probability (for example 0.2) each individual mutates (one of the elements of 6 length string will be changed to another random number).
* Crossover: generally, k point crossover between 2 parents means that we set k points in random places in the string and start from the beginning of the strings. Each string is now divided into k+1 substrings. Starting from the 1st area, we swap this area between two parents. In next area we don't do anything, but in the one after that and generally in all the areas that have even distance with first one, we swap the elements of that area between two parents. Note that crossover might produce some tours that have repeated cities inside them. What I did to overcome this probelm was that after each crossover, I checked that if it has repetition in it, then did not apply that crossover (undo crossover).

The parameters that can be tuned are the population size (ps), mutation probability (miu), crossover points (k). Note that I used a pooling mate size equal to population size. At first, I set ps=100 and the final answer was often good (always under 70 length which is in the top 1% of the answers), but it could reach 52 (length of minimum tour) only a few times. So, I decided to begin with a more populated one and I set ps=1000 and the results got much more improved. I also changed the numbers of crossover points and ran the algorithm few times for each, and 1 point crossover led to better results. Also mutation probability of 0.2 led to better results. Note that after setting population size to 1000, the speed of algorithm got decreased, so I changed stopping criterion such that it stops the algorithm if after 100 iterations the best obtained individual didn't improve (instead of 500 which was was my stopping criterion in other methods).



### Differential Evolution


Differential evolution algorithm works based on the difference of individuals in the population. It actually tries to get all individuals of the population close to each other (decreasing the difference between the individuas). So, the mutation and crossover should be defined based on the difference of individuals. Also, unlike genetic algorithm, it does not move to new answer after each mutation and crossover, because we don't want to move in a direction that the fitness is getting worse. Therefore, each time, we check whether or not the new fitness is better than the old one and if it is, we change the old individual to the new one. The reason behind this is that in genetic algorithm, all changes are random and it is ok if some of the individuals move to the direction of worse fitness, but in differential evolution, as we are moving all of our population toward the same direction, we have to be careful in which direction we are moving.

The algorithm works as follows: for all of the individuals in the population, it first applies mutation and then crossover on them and keeps the result for the next generation if the fitness is improved for the new constructed individual. It does this precodeure multiple time until for some consecutive runs, there won't be any change in the fitness of the best individual. So, the two important points in the implementation that we should mention are how to implement mutation and crossover for differential evolution.

* Mutation: it randomly chooses two other individuals and add their difference multiply by a coefficient btween zero and one (F) to the original individual (parent). For the traveling salesman problem, this addition might produce individuals that are not compatible with our notations. Because first, it might go over 50 or under 0 and second, because of multiplying by a floating point number, the result is probably not an integer. To overcome these problems in the implementation, we could do two simple things. First, rounding each produced number to the nearest integer and second, replacing each number by residual of that number divided by 50. This way, every new individual will remain in the intended set.

* Crossover: the crossover is between the parent and the new constructed individual after mutation. It follows a parameter Pr that detemines the probability of existence of each element in the current individual isnide the new individual. There are two distributions that we can use for Pr: binomial or exponentia. I used the binomial distribution in the implementation. By probability of Pr, elements are being chose from the new individual and by probability (1-Pr), they will be chose from the parent. And this selection happens for all elements seperately.



In DE, there are 3 important parameters that affect the final result: the population size, the scaling factor (F) and the recombination probability (Pr). After regulating these parameters, I found F=0.5 and Pr=0.3 better than the others. Also, it is obvious that as the population size is larger, the probability of finding the better solutions would also be higher. I ran these algorithm with F=0.5 and Pr =0.3 once with the population size 100 and another time with 200 (each multiple times). Popluation size 100 also reached an answer with the length below 60 most of the times. But with the population size 200, it always reached the best tour, but took much more time. I also made the algorithm stop if after 500 iterations there was no update in the best obtained individual. At first, I set it to 200, but I noticed sometimes even after 200 iterations of not updating, it could reach a better individual, so I decided to set it to a larger number. Although it affects the walltime, the probability of finding the optimum answer will increase which is a good thing.










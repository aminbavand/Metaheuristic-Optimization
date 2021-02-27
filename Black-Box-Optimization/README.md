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


After running grid_search.py:
```
problem 1 grid search result is: -23.60403513764952
and this result is for point:  [array([-3.14]), array([-3.14])]

problem 2 grid search result is: -149.96262442323604
and this result is for point:  [array([0.21]), array([-0.22])]

problem 3 grid search result is: -86.5677784678323
and this result is for point:  [array([-3.2]), array([-3.1]), array([-0.3]), array([0.])]
```



### Random search

For Random search, I started from 100 random points in 4 dimensional space and update them inependently. In each step, I generate a random point in the neighborhood of each point and check if the objective function is improved, then change the point to the new point. If after 100 iterations, none of the points get improved, then the algorithm would be terminated.

After running random_search.py:
```
problem 1 random search result is: -23.60425165558675
and this result is for point:  [-3.13956753 -3.1424089 ]
iteration numbers =  2538

problem 2 random search result is: -149.97743997660385
and this result is for point:  [-0.24641691  0.02572728]
iteration numbers =  2601

problem 3 random search result is: -86.51647456516926
and this result is for point:  [-3.03741142 -3.17745189  0.07120992 -1.1015367 ]
iteration numbers =  3659
```


### Particle Swarm Optimization

In particle swarm optimization, we start with a population of random answers in the search space and in eacn step, we move the populations toward better positions. The update is based on the memory of eacch particle itself and also the memory of all particles. The movement direction of each particle is a linear combination of the two directions. One is the direction toward the best point that this particle has ever reached, and the other is the direction toward the best point that all of particles have ever reached. This way,at each step all points would be updated and probably give us better results. After some number of iterations, if thereis no improvement in the best acheived point, we will terminate the algorithm.

The tendancies of the algorithm is moving toward those points that probably give us better objective values. The tunable parameters are the population size, and c1 and c2 coefficients (coeffinients that tell us how much is the effect of the local minimum and global minimum on the update). One flaw in the PSO algorithm is that there is no checking if the new points actually give us better results. So we can modify the algorithm so that if the objective function for the new point is not better, then do not update that point.

PSO is expected to work better than random search, because in random search there is no rational behind how we update the points. But in PSO, the points are moving toward the optimum points. Compared to grid search, it probably is much faster than that because it is not searching every point in the space. But this is the reason that the found answer by grid search is better, because PSO might miss some points in the search space. The only problem is that since the step size of our grid search cannot be selected to small (it takes much time to be executed), it is possible that the respond found by PSO would be better than grid search, but he probability is low. 



After running pso.py:
```
problem 1 PSO result is: -23.467476648039174
and this result is for point:  [-3.147464230072697, -3.186934200485236]
iteration numbers =  507

problem 2 PSO result is: -149.74549929755673
and this result is for point:  [-0.7705810714882136, 0.3784793734066594]
iteration numbers =  665

problem 3 PSO result is: -85.11636721788312
and this result is for point:  [-2.935670384556046, -2.991771851256867, 0.06804678306434253, -0.494362655483668]
iteration numbers =  533
```


### Genetic algorithm

Genetic algorithm is a powerful tool for problems that are facing a alarge space of possible answers. First it generates a population of possible answers randomly. After that, it chooses some individuals of this popluation (individuals with better fitness have higher probability of being choosed) to be parents for the next generation. This is called selection. After that each of these parents mutate with a small probability. Mutation is a little change in the construction of an answer. Next step is crossover which two parents swap some genes between them. Now we have next generation. Note that also we transfer the best answer of each generation without any change to the next generation (elitism). This way, we can make sure that the best solution found so far, would not be destroyed. We repeat this process for multiple times until for 500 consecutive iterations, the best found tour would not be changed.

Genetic algorithm tends to produce better answers by combining better answers togetger and making small change to some of them. Tunable parameters are the probability of mutation, population size, mating pool size and the number of crossover points. We can modify the algorithm by changing these parameters and set them to those values which give us better results in terms of finding optimum value in a short time.

The performance of genetic algorithm is expected to be the same as PSO. Because both of these algorithms start with a random population and update the populations trying to improve the obective function for the population. In campare to random search, I expect the GA to works better because there is some logic behind updating points, but random search blindly generate new points in the vicinity of the points and update them if the new point sare better. In campare to grid search, it is the same comparison that I made between PSO and grid search in the previous part.

After running ga.py:
```
problem 1 GA result is: -22.594094058564306
and this result is for point:  [-2.90842219 -2.91723914]
iteration numbers =  508

problem 2 GA result is: -149.91053334669166
and this result is for point:  [ 0.29475934 -1.26928893]
iteration numbers =  529

problem 3 GA result is: -85.38481078467264
and this result is for point:  [-2.47935964 -2.69427081 -0.10802375 -0.26370948]
iteration numbers =  957
```


## Comparison and discussion

After running main.py which applies all the above methods on all 3 problems:

```
for seed =  0

problem 1 grid search result is: -23.60403513764952
and this result is for point:  [array([-3.14]), array([-3.14])]

problem 2 grid search result is: -149.96786755692338
and this result is for point:  [array([-0.14]), array([0.33])]

problem 3 grid search result is: -86.55063857761692
and this result is for point:  [array([-3.2]), array([-3.1]), array([0.]), array([0.])]
running time= 19.8120698928833

problem 1 random search result is: -23.609865313814467
and this result is for point:  [-3.14125154 -3.14139044]
iteration numbers =  2695

problem 2 random search result is: -149.96859374943315
and this result is for point:  [-0.20326833 -0.66609717]
iteration numbers =  2105

problem 3 random search result is: -86.42459056200809
and this result is for point:  [-3.26520753 -3.12732703 -0.52414993  0.6222692 ]
iteration numbers =  2237
running time= 1.8770074844360352

problem 1 PSO result is: -23.560705268357086
and this result is for point:  [-3.1292170980842586, -3.1518042789049456]
iteration numbers =  729

problem 2 PSO result is: -149.72973974425562
and this result is for point:  [0.12960256689326566, 0.07661131303768326]
iteration numbers =  800

problem 3 PSO result is: -83.98262642405359
and this result is for point:  [-3.2582217201124037, -2.3340856016542304, 0.3595374841704926, 0.3071642406225057]
iteration numbers =  519
running time= 0.3490636348724365

problem 1 GA result is: -23.494336251224574
and this result is for point:  [-3.13216542 -3.10563745]
iteration numbers =  512

problem 2 GA result is: -149.63629784211165
and this result is for point:  [-0.77041275 -0.28744808]
iteration numbers =  517

problem 3 GA result is: -85.89903795150398
and this result is for point:  [-3.23682096 -3.05532964 -0.43259386  0.82761588]
iteration numbers =  577
running time= 1.00528883934021

for seed =  1

problem 1 grid search result is: -23.60403513764952
and this result is for point:  [array([-3.14]), array([-3.14])]

problem 2 grid search result is: -149.98583082116642
and this result is for point:  [array([-0.19]), array([0.04])]

problem 3 grid search result is: -86.586303259159
and this result is for point:  [array([-3.1]), array([-3.1]), array([0.5]), array([-0.2])]
running time= 17.62297010421753

problem 1 random search result is: -23.60417129323973
and this result is for point:  [-3.14237075 -3.13952521]
iteration numbers =  3603

problem 2 random search result is: -149.98611540190802
and this result is for point:  [-0.21269885 -0.32851385]
iteration numbers =  2311

problem 3 random search result is: -86.51268442816963
and this result is for point:  [-3.28820446 -3.08349507 -0.61910389  0.50378345]
iteration numbers =  2051
running time= 2.1362884044647217

problem 1 PSO result is: -23.567409672439165
and this result is for point:  [-3.1279152847367437, -3.1441292555146325]
iteration numbers =  513

problem 2 PSO result is: -149.9930136454838
and this result is for point:  [-0.4188966482870724, 0.0678563008291928]
iteration numbers =  522

problem 3 PSO result is: -85.65987304797147
and this result is for point:  [-3.6058399006763335, -3.1805012967957165, 0.3615417737333323, -0.2031125350736942]
iteration numbers =  508
running time= 0.29618120193481445

problem 1 GA result is: -22.921558398068957
and this result is for point:  [-2.92930275 -3.08602358]
iteration numbers =  502

problem 2 GA result is: -149.07007361185947
and this result is for point:  [0.63336213 0.35187979]
iteration numbers =  523

problem 3 GA result is: -84.11729598726393
and this result is for point:  [-1.783773   -3.1509176  -0.68580243  0.61394877]
iteration numbers =  529
running time= 1.0491952896118164

for seed =  2

problem 1 grid search result is: -23.60403513764952
and this result is for point:  [array([-3.14]), array([-3.14])]

problem 2 grid search result is: -149.92891628679732
and this result is for point:  [array([-0.53]), array([-0.99])]

problem 3 grid search result is: -86.5597157485541
and this result is for point:  [array([-3.2]), array([-3.2]), array([0.]), array([-0.5])]
running time= 17.843385696411133

problem 1 random search result is: -23.5958809106363
and this result is for point:  [-3.14617275 -3.1431817 ]
iteration numbers =  3152

problem 2 random search result is: -149.9814193964462
and this result is for point:  [-0.51924571 -0.9007918 ]
iteration numbers =  3739

problem 3 random search result is: -86.67973726692846
and this result is for point:  [-3.10616694 -3.12427823  1.33290927 -0.21063581]
iteration numbers =  3557
running time= 2.862321615219116

problem 1 PSO result is: -23.579282474471057
and this result is for point:  [-3.151620473788819, -3.140147845903287]
iteration numbers =  602

problem 2 PSO result is: -149.6627413064971
and this result is for point:  [0.3554264320906101, -0.7482960748982767]
iteration numbers =  571

problem 3 PSO result is: -84.93754137545973
and this result is for point:  [-2.588322733391684, -3.240859549692233, 0.5034291818079601, -0.25934206184108155]
iteration numbers =  682
running time= 0.33112287521362305

problem 1 GA result is: -23.02735287664089
and this result is for point:  [-3.32706846 -3.13083444]
iteration numbers =  504

problem 2 GA result is: -149.95917748339136
and this result is for point:  [ 1.01955811 -0.57180285]
iteration numbers =  516

problem 3 GA result is: -85.74008952814333
and this result is for point:  [-3.27414055 -3.5294297  -0.73380451 -0.44527294]
iteration numbers =  520
running time= 0.9524524211883545

for seed =  3

problem 1 grid search result is: -23.60403513764952
and this result is for point:  [array([-3.14]), array([-3.14])]

problem 2 grid search result is: -149.90693296784573
and this result is for point:  [array([0.22]), array([-0.78])]

problem 3 grid search result is: -86.50361790875286
and this result is for point:  [array([-3.1]), array([-3.1]), array([0.2]), array([0.9])]
running time= 18.578328847885132

problem 1 random search result is: -23.606909182601132
and this result is for point:  [-3.14292708 -3.14150176]
iteration numbers =  3687

problem 2 random search result is: -149.9646256576891
and this result is for point:  [0.2979366  0.07078249]
iteration numbers =  2212

problem 3 random search result is: -86.43683649229911
and this result is for point:  [-3.29306348 -3.26290897  0.29545375 -0.2130135 ]
iteration numbers =  2198
running time= 2.259045124053955

problem 1 PSO result is: -23.590900081795255
and this result is for point:  [-3.1353596075259462, -3.143185572774788]
iteration numbers =  676

problem 2 PSO result is: -149.61590743296944
and this result is for point:  [0.6295388512525764, 0.3287618196292632]
iteration numbers =  508

problem 3 PSO result is: -85.92042184537397
and this result is for point:  [-3.631639817223255, -2.9152569951705867, 0.37832943233860683, 0.32763154371936]
iteration numbers =  562
running time= 0.2971780300140381

problem 1 GA result is: -22.423249239983917
and this result is for point:  [-2.76870474 -3.08185404]
iteration numbers =  519

problem 2 GA result is: -149.55532906609997
and this result is for point:  [0.2165521  0.78893001]
iteration numbers =  519

problem 3 GA result is: -80.77981811286222
and this result is for point:  [-1.36149362 -3.89777226 -1.4879054  -1.11064871]
iteration numbers =  532
running time= 1.007307529449463

for seed =  4

problem 1 grid search result is: -23.60403513764952
and this result is for point:  [array([-3.14]), array([-3.14])]

problem 2 grid search result is: -149.91428523632356
and this result is for point:  [array([0.48]), array([-0.43])]

problem 3 grid search result is: -86.57471566847127
and this result is for point:  [array([-3.1]), array([-3.1]), array([0.]), array([-0.7])]
running time= 19.384230136871338

problem 1 random search result is: -23.603941329200982
and this result is for point:  [-3.13962775 -3.14043177]
iteration numbers =  2625

problem 2 random search result is: -149.9919702944923
and this result is for point:  [-0.00893099 -0.03450359]
iteration numbers =  2980

problem 3 random search result is: -86.4242640073348
and this result is for point:  [-3.11387899 -3.03565693 -0.20222337 -0.01938768]
iteration numbers =  2965
running time= 2.291872024536133

problem 1 PSO result is: -23.5844244329125
and this result is for point:  [-3.1428295753014983, -3.1331885581358945]
iteration numbers =  1067

problem 2 PSO result is: -148.78771015876185
and this result is for point:  [0.39337918531178206, -0.27564808093446563]
iteration numbers =  536

problem 3 PSO result is: -85.10942719148956
and this result is for point:  [-2.7424723960844903, -2.9448145349110355, -0.08941880396798917, -0.4266522642911419]
iteration numbers =  977
running time= 0.4797191619873047

problem 1 GA result is: -22.357372342089874
and this result is for point:  [-2.77007312 -3.28602254]
iteration numbers =  504

problem 2 GA result is: -149.45468137246405
and this result is for point:  [0.29307394 0.10000813]
iteration numbers =  529

problem 3 GA result is: -85.88797000708193
and this result is for point:  [-3.6114961  -2.88756698 -0.10928833 -0.24460107]
iteration numbers =  578
running time= 1.0462279319763184
```

In terms of runtime, grid search takes much more time than the other 3. After that random search takes more than GA and GA takes morethan PSO to run. In terms of iteration effiniency, PSO could reach the answers close to optimum answer very fast and in small number of iterations. Number of iterations in GA is also small, but a little bit more than PSO. The number of iterations in random search is much larger than PSO and GA.

In terms of convergence stability, as can be predicted, grid search is the most stable one, because there is no randomness in its search algorithm. But the other 3 algoritms use random to transfer between answers, so they cannot always reach the answer. However, it seems that PSO work better than the other two and for 5 seeds that we used, it got close to the optimal answers more than GA and random search.

Indeed, grid search is the easiest algorithm to implement, because the algorithm is straightforward and there is no ambiguity in it. After that random search is the easiest one, because the only complexity is defining the neighborhood and updating the points. But PSO and GA are more complex and harder to implement because they have some hyperparameters need to define, and also in GA we have define mutation and crossover and in PSO we have to write down the velocity equations. So, with the above explanations, we can infer that random search and grid search need less apriory knowledge, but PSO and GA need more (choosing hyperparameters, defining relative transformation, etc.).



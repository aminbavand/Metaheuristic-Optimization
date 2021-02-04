from Traveling_Salesman import traveling_salesman
import matplotlib.pyplot as plt
import numpy as np


salesman = traveling_salesman(num_cities=50) # initialize the TS's world with 50 cities

random_initial_tour = salesman.random_tour(num_stops=6) # create a random tour for the TS, plot and calculate length of tour
plt.figure()
salesman.plot()
print("length of first tour: ", salesman.tour_length())


salesman.new_tour(tour = np.arange(6).tolist()) # assign a new tour to the TS, plot and calculate length
plt.figure()
salesman.plot()
print("length of first tour: ", salesman.tour_length())

salesman.new_tour(tour = [1, 6, 7, 28, 42, 9]) # assign a new tour to the TS, plot and calculate length
plt.figure()
salesman.plot()
print("length of first tour: ", salesman.tour_length())

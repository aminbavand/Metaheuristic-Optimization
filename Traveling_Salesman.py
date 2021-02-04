import numpy as np
import matplotlib.pyplot as plt
import random
class traveling_salesman():
    def __init__(self, num_cities=50):
        # initialize the position of the cities
        random.seed(42)
        gridsize=100
        self.num_cities = num_cities
        self.cities = [random.sample(range(gridsize), 2) for x in range(self.num_cities)]

    def random_tour(self, num_stops=6):
        # take a random tour of a given length
        self.num_stops = num_stops
        self.tour = random.sample(range(self.num_cities), self.num_stops)
        return self.tour
        
    def new_tour(self, tour):
        # define a new tour
        tour = [int(_) for _ in tour]
        self.num_stops = len(tour)
        self.tour = tour
    
    def tour_length(self):
        # calculate tour length
        visited_cities = [self.cities[_] for _ in self.tour]
        for city in visited_cities:
            if city == visited_cities[0]:
                #start tour at the start
                traveled_distance = 0
                location = city
            else:
                # each travelled leg
                traveled_distance += np.sqrt((location[0] - city[0])**2 + (location[1] - city[1])**2)
                location = city
        # return to start
        traveled_distance += np.sqrt((visited_cities[0][0] - city[0])**2 + (visited_cities[0][1] - city[1])**2)
        return traveled_distance    

    def plot(self, tour=None):
        #plot the tour if you want to
        if tour is not None:
            self.tour = tour
        plt.plot([self.cities[_][0] for _ in range(self.num_cities)],
                 [self.cities[_][1] for _ in range(self.num_cities)],
                 linestyle='',
                 marker='*',
                markersize=11.0,
                color=[1,0,0])
        plt.plot([self.cities[self.tour[_ % self.num_stops]][0] for _ in range(self.num_cities)],
                 [self.cities[self.tour[_ % self.num_stops]][1] for _ in range(self.num_cities)],
                 'xb-')
        plt.show()
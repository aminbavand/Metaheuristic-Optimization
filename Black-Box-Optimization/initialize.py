from Blackbox_Problems_fixed import problem_1, problem_2, problem_3

# all three problems have 2 input dimensions
# the problems can be queried in tensors, matrices, vectors and single queries.
# internally, numpy does a lot of broadcasting, so querying with different dimensionalities is possible.
# but for safety reasons I would recommend making sure the two inputs have the same shape.
import numpy as np
# single values
x_one = np.array(1.0)
y_one = np.array(3.0)
z_one = problem_1(x_one, y_one)
print('Queried with two single values, returns a value of ', z_one, ' ,shape: ', z_one.shape)

# arrays, for populations maybe
x_arr = np.linspace(1,9, 20)
y_arr = np.linspace(1,9, 20)
z_arr = problem_2(x_arr, y_arr)
print('Queried with two arrays of shape', x_arr.shape, y_arr.shape, 'it returns an array of shape:', z_arr.shape)

# matrices ... like ... in a grid maybe
steps = 20
x = 0.01*np.arange(-steps/2, steps/2)
y = 0.01*np.arange(-steps/2, steps/2)
X, Y = np.meshgrid(x, y)
Z = problem_3(X, Y, X, Y)
print('Queried with 4 matrices of shape', X.shape, Y.shape, 'it returns a matrix of shape:', Z.shape)
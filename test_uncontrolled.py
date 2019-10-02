from random_variables import RandomVector, cBetaRandomVariable
import numpy as np
from stochastic_verification_functions import StochasticVerificationFunction
from kinematic_car import *
import time
import cProfile, pstats, io
from pstats import SortKey
"""
Test the uncontrolled car model.
"""

p = lambda x,y: x**2 + 0.1 * y**2 - 1
n_t = 3
alpha = 50
beta = 55
dt = 0.05
x0 = -1.1
y0 = 0.0
v0 = 0
theta0 = 0.0

wvs = [cBetaRandomVariable(alpha, beta, 2) for i in range(n_t)]
wthetas = [cBetaRandomVariable(alpha, beta, 0.01) for i in range(n_t)]
car_model = UncontrolledKinematicCar(n_t, dt)
cos_rvs, sin_rvs = car_model.construct_cos_sin_theta_rvs(0.0, wthetas)

ordered_random_variables = wvs + cos_rvs + sin_rvs

start_compile = time.time()
verification_function = StochasticVerificationFunction(p, car_model)
verification_function.compile_moment_functions_multinomial()
print("Time to compile: " + str(time.time() - start_compile))

input_variables = InputVariables(x0 = x0, y0 = y0, v0 = v0)
verification_function.set_random_vector(RandomVector(ordered_random_variables))
verification_function.compute_prob_bound_multimonial(input_variables)
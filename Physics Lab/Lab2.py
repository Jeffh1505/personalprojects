import math
import matplotlib.pyplot as plt 
import numpy as np
import scipy.optimize as opt

h1_prime = 123.0
h2_prime = 117.5

delta_h_prime = h1_prime - h2_prime

h1a = 132.6
h2a = 112
h3a = 104
Da = 40
La = 40.5
x_estimate = 72.99

x_distance_a = [4.8, 4.8, 4.8, 4.9, 4.9, 4.9, 5, 5.5, 5.5, 5.7, 5.8, 5.8, 5.9, 6, 6.1, 6.2, 6.3, 6.5, 6.5, 6.6, 7.3, 7.2, 7.2, 7.7, 7.8, 7.9, 8, 9, 9.4, 10.2]

z_distance_a = [-0.5, -0.3, -0.2, 0.1, 0, 0.2, 0.1, -0.6, 0.2, 1.3, -0.5, -0.8, 0, 0.1, -0.8, -0.2, 0.2, -0.7, -0.6, 0.1, -0.6, 0, 0.2, 0.3, 0.7, 2.9, 0.3, 0.4, 0.5, 0.1]

def unweighted_stats(a1:list) -> tuple:
    unweighted_average = sum(a1)/ len(a1)
    sum_for_sigma = sum((x - unweighted_average)**2 for x in a1)
    sigma = math.sqrt(sum_for_sigma / (len(a1) - 1))
    sigma_average = sigma / math.sqrt(len(a1))
    return unweighted_average, sigma_average

x_average, x_std = unweighted_stats(x_distance_a)

print(f"Motion along x-axis: {x_average} cm +- {x_std}")
import numpy as np
from scipy.optimize import fsolve

b = 1.1e6
r = 8
s = 16

def f(c, a):
    return (1 - a) * c + b * c**r * np.exp(-s * c)

def fixed_points(a):
    func = lambda c: f(c, a) - c
    guesses = np.linspace(0, 0.6, 20)
    points = []
    for g in guesses:
        p, = fsolve(func, g)
        if 0 <= p <= 0.6:
            points.append(p)
    # usuwa duplikaty numeryczne
    points = np.unique(np.round(points, 6))
    return points

def stability(c_star, a):
    f_prime = (1 - a) + b * np.exp(-s*c_star) * (r * c_star**(r-1) - s * c_star**r)
    return np.abs(f_prime) < 1

# a = 0.2
a = 0.2
points_a02 = fixed_points(a)
print("Punkty stałe dla a=0.2:")
for c in points_a02:
    print(f"c* = {c:.6f}, stabilny = {stability(c, a)}")

# a = 0.3
a = 0.3
points_a03 = fixed_points(a)
print("\nPunkty stałe dla a=0.3:")
for c in points_a03:
    print(f"c* = {c:.6f}, stabilny = {stability(c, a)}")

import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    sum = 0
    for i in range(x_vals.shape[0] - 1):
        sum += func(x_vals[i]) * (x_vals[i + 1] - x_vals[i])
    return sum

def trapezoid(x_vals: np.ndarray, func: np.ufunc):
    sum = 0
    for i in range(x_vals.shape[0] - 1):
        sum += ((func(x_vals[i]) + func(x_vals[i + 1])) / 2.0) * (x_vals[i + 1] - x_vals[i])
    return sum

def simpson(x_vals: np.ndarray, func: np.ufunc):
    # body


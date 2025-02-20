import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    lefts = x_vals[:-1]
    rights = x_vals[1:]
    rects = (rights - lefts) * func(lefts)
    return sum(rects)

def trapezoid(x_vals: np.ndarray, func: np.ufunc):
    left_x = x_vals[:-1]
    right_x = x_vals[1:]
    left_y = func(left_x)
    right_y = func(right_x)
    traps = (right_x - left_x) * ((left_y + right_y) / 2)
    return sum(traps)

def simpson(x_vals: np.ndarray, func: np.ufunc):
    return ((x_vals[-1] - x_vals[0]) / 6.0) * (func(x_vals[0]) + 4 * func((x_vals[0] + x_vals[-1]) / 2.0) + func(x_vals[-1]))
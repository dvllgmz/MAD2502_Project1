import numpy as np

# def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
#     lefts = x_vals[:-1]
#     rights = x_vals[1:]
#     rects = (rights - lefts) * func(lefts)
#     return sum(rects)

def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    """
    Calculates the Riemann sum of a function using the left endpoints from all the values in x_vals
    :int NumPy array x_vals: All the x values at which the Riemann sum is computed
    :param func: The function under which the Riemann sum is computed
    :return: The Riemann sum
    """
    a = x_vals[:-1]
    b = x_vals[1:]
    # Multiplies the base (right endpoint minus left endpoint) by the height (the function value at the left endpoint) for each rectangle
    rects = (b - a) * func(a)
    # Sums the rectangles
    return sum(rects)

def trapezoid(x_vals: np.ndarray, func: np.ufunc):
    """
    Calculates the Riemann sum of a function using the trapezoids formed by all the values in x_vals and their respective outputs from func
    :int NumPy array x_vals: All the x values at which the Riemann sum is computed
    :param func: The function under which the Riemann sum is computed
    :return: The Riemann sum
    """
    a = x_vals[:-1]
    b = x_vals[1:]
    # The function at the left/right endpoints
    left_y = func(a)
    right_y = func(b)
    # Multiplies the base (right endpoint minus left endpoint) by the mean of the left height and the right height for each trapezoid
    traps = (b - a) * ((left_y + right_y) / 2)
    # Sums the trapezoids
    return sum(traps)

def simpson(x_vals: np.ndarray, func: np.ufunc):
    """
    Estimates the integral of func from x_vals[0] to x_vals[-1] using Simpson's rule
    :int NumPy array x_vals: The x values for which we are estimating the integral
    :param func: The function for which we are estimating the integral
    :return: The estimated integral
    """
    a = x_vals[0]
    b = x_vals[-1]
    val = ((b-a)/6) * (func(a) + (4*func((a+b)/2)) + func(b))
    return val
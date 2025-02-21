import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc):
    """
    Calculates the Riemann sum of a function using the left endpoints from all the values in x_vals
    :int NumPy array x_vals: All the x values at which the Riemann sum is computed
    :param func: The function under which the Riemann sum is computed
    :return: The Riemann sum
    """
    # The left endpoints
    lefts = x_vals[:-1]
    # The right endpoints
    rights = x_vals[1:]
    # Multiplies the base (right endpoint minus left endpoint) by the height (the function value at the left endpoint) for each rectangle
    rects = (rights - lefts) * func(lefts)
    # Sums the rectangles
    return sum(rects)

def trapezoid(x_vals: np.ndarray, func: np.ufunc):
    """
    Calculates the Riemann sum of a function using the trapezoids formed by all the values in x_vals and their respective outputs from func
    :int NumPy array x_vals: All the x values at which the Riemann sum is computed
    :param func: The function under which the Riemann sum is computed
    :return: The Riemann sum
    """
    # The left endpoints
    left_x = x_vals[:-1]
    # The right endpoints
    right_x = x_vals[1:]
    # The function at the left endpoints
    left_y = func(left_x)
    # The function at the right endpoints
    right_y = func(right_x)
    # Multiplies the base (right endpoint minus left endpoint) by the mean of the left height and the right height for each trapezoid
    traps = (right_x - left_x) * ((left_y + right_y) / 2)
    # Sums the trapezoids
    return sum(traps)

def simpson(x_vals: np.ndarray, func: np.ufunc):
    """
    Estimates the integral of func from x_vals[0] to x_vals[-1] using Simpson's rule
    :int NumPy array x_vals: The x values for which we are estimating the integral
    :param func: The function for which we are estimating the integral
    :return: The estimated integral
    """
    # Plug all values into Simpson's rule, x_vals[0] is a and x_vals[-1] is b
    return ((x_vals[-1] - x_vals[0]) / 6.0) * (func(x_vals[0]) + 4 * func((x_vals[0] + x_vals[-1]) / 2.0) + func(x_vals[-1]))
#! usr/bin/env python3

from statistics import mean

def best_fit_slope_and_intercept(x_vals, y_vals):
    """Find slope and intercept for x and y vals"""
    # Find means
    x_mean = mean(x_vals)
    y_mean = mean(y_vals)
    xy_mean = mean(x_vals * y_vals)

    # (xavg*yavg - xyavg) / (xavg^2 - (x^2)avg)
    slope = ((x_mean * y_mean) - xy_mean) / (x_mean ** 2 - mean(x_vals ** 2))
    intercept = y_mean - slope * x_mean
    return slope, intercept


def squared_error(ys, ys_line):
    """Find squared error between lbf and the avg of the original 'y' values"""
    return sum((ys_line - ys) ** 2)


def coefficient_of_determination(ys, ys_line):
    y_mean = mean(ys)
    # Create a list of size ys that contains repeats of y_mean
    y_mean_line = [y_mean for y in ys]

    # Error of regression line
    squared_error_regr = squared_error(ys, ys_line)

    # Error of average of all ys
    squared_error_y_mean = squared_error(ys, y_mean_line)

    return 1 - (squared_error_regr / squared_error_y_mean)

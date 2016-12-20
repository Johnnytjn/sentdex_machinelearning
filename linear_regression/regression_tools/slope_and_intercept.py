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

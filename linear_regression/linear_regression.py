#! usr/bin/env python3

from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Convert CSV stuff into pandas dataframe
df = pd.read_csv("x_and_y_vals.csv", names=["x_vals", "y_vals"])

# Convert pandas dataframe into float64 np arrays
x_arr = df["x_vals"].astype("float64").values
y_arr = df["y_vals"].astype("float64").values

def best_fit_slope(x_vals, y_vals):
    # Lots of ()'s but is just (top) / (bot)
    slope = (((mean(x_vals) * mean(y_vals)) - mean(x_vals * y_vals)) /
             (mean(x_vals) ** 2 - mean(x_vals ** 2)))


m = best_fit_slope(x_arr, y_arr)

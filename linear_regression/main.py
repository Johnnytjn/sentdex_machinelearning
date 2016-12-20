#! usr/bin/env python3

import numpy as np
import pandas as pd
from regression_tools import best_fit_slope_and_intercept as m_and_b
from regression_tools import coefficient_of_determination
from regression_tools import make_graph


def main():
    # Convert CSV stuff into pandas dataframe
    df = pd.read_csv("data/x_and_y_vals.csv", names=["x", "y"])

    # Convert pandas dataframe into float64 numpy arrays
    x_vals = df["x"].astype("float64").values
    y_vals = df["y"].astype("float64").values

    # Tuple of m and b ----> (y=mx+b)
    m, b = m_and_b(x_vals, y_vals)

    # Make regression line
    regression_line = [(m * x + b) for x in x_vals]

    # Find coefficient of determination
    r_squared = coefficient_of_determination(y_vals, regression_line)
    print("Coefficient of Determination: ", r_squared, sep='')

    # Where to save the graph?
    vis_loc = "visuals/regression.png"

    # Graph it
    make_graph(x_vals, y_vals, m, b, regression_line, vis_loc)


if __name__ == '__main__':
    main()

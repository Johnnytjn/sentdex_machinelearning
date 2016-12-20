#! usr/bin/env python3

import numpy as np
import pandas as pd
from regression_tools import best_fit_slope_and_intercept as bfs_and_int
from regression_tools import make_graph


def main():
    # Convert CSV stuff into pandas dataframe
    df = pd.read_csv("data/x_and_y_vals.csv", names=["miles", "time"])

    # Convert pandas dataframe into float64 numpy arrays
    miles_driven = df["miles"].astype("float64").values
    time_taken = df["time"].astype("float64").values

    # Tuple of m and b ----> (y=mx+b)
    m, b = bfs_and_int(miles_driven, time_taken)

    # Graph it
    make_graph(miles_driven, time_taken, m, b)






if __name__ == '__main__':
    main()

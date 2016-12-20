#! usr/bin/env python3

import numpy as np
import random
from regression_tools import best_fit_slope_and_intercept as m_and_b
from regression_tools import coefficient_of_determination
from regression_tools import make_graph

def create_dataset(ds_size, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(ds_size):
        # No neg variance because can't have negative time
        y = val + random.randrange(variance)
        ys.append(y)
        # No neg correlation because can't have negative time
        if correlation == "pos":
            val += step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


def main():
    # Change these values for testing
    xs, ys = create_dataset(50, 15, 1, "pos")

    # Find (y=mx+b)
    m, b = m_and_b(xs, ys)

    # Make regression line
    regression_line = [(m * x + b) for x in xs]

    # Find coefficient of determination
    r_sq = coefficient_of_determination(ys, regression_line)
    print("TEST Coefficient of Determination: ", r_sq, sep='')

    # Where to save the graph?
    vis_loc = "visuals/test_regression.png"

    # Graph it
    make_graph(xs, ys, m, b, regression_line, vis_loc)


if __name__ == '__main__':
    main()

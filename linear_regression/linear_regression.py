#! usr/bin/env python3

from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


def main():
    # Convert CSV stuff into pandas dataframe
    df = pd.read_csv("x_and_y_vals.csv", names=["miles", "time"])

    # Convert pandas dataframe into float64 numpy arrays
    miles_driven = df["miles"].astype("float64").values
    time_taken = df["time"].astype("float64").values

    # Tuple of m and b ----> (y=mx+b)
    m, b = best_fit_slope_and_intercept(miles_driven, time_taken)
    regression_line_and_graph(miles_driven, time_taken, m, b)


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


def regression_line_and_graph(x_vals, y_vals, m, b):
    # y=mx+b
    regression_line = [(m * x + b) for x in x_vals]

    # average speed in mph
    avg_speed = m * 60

    # Make prediction
    predict_distance = 40
    predict_time = m * predict_distance + b

    # Style, Title & Axis Labels
    suptitle_text = "Avg. Speed: {num: .{dig}f} mph".format(num=avg_speed,
                                                            dig=1)
    title_text = "Predicted{num: .{dig}f} min to "\
                 "travel {dis} mi".format(num=predict_time, dig=1,
                                          dis=predict_distance)
    style.use("fivethirtyeight")
    plt.suptitle(suptitle_text, ha="center", fontsize=14)
    plt.title(title_text, ha="center", fontsize=10)
    plt.xlabel("Distance Driven (miles)")
    plt.ylabel("Time Taken (minutes)")

    # Plot
    plt.scatter(x_vals, y_vals, s=100)
    plt.scatter(predict_distance, predict_time, s=100, color='r')
    plt.plot(x_vals, regression_line)

    # Display
    # plt.show()
    # Save png
    plt.savefig("regression.png", bbox_inches="tight")


if __name__ == '__main__':
    main()

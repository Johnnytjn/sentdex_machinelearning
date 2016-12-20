#! usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import style

def make_graph(x_vals, y_vals, m, b):
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
    plt.savefig("visuals/regression.png", bbox_inches="tight")

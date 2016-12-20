#! usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import style

def make_graph(x_vals, y_vals, m, b, regression_line, vis_loc):

    # average speed in mph
    avg = m

    # Make prediction
    predict_x = 40
    predict_y = m * predict_x + b

    # Style, Title & Axis Labels
    suptitle_text = "Slope={num:.{dig}f}".format(num=avg, dig=1)
    title_text = "Predicted y={num:.{dig}f} from "\
                 "x={dis}".format(num=predict_y, dig=1, dis=predict_x)
    style.use("fivethirtyeight")
    plt.suptitle(suptitle_text, ha="center", fontsize=14)
    plt.title(title_text, ha="center", fontsize=10)
    plt.xlabel("x")
    plt.ylabel("y")

    # Plot
    plt.scatter(x_vals, y_vals, s=100)
    plt.scatter(predict_x, predict_y, s=100, color='r')
    plt.plot(x_vals, regression_line)

    # Display
    # plt.show()
    # Save png
    plt.savefig(vis_loc, bbox_inches="tight")

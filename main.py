#!/usr/bin/env python


"""
Main script.
Plot and analyse the data.
"""


# Import external libraries
import matplotlib.pyplot as plt

# Import default libraries

# Import own modules
from data import TurbineData

# Import variables


def plot_power(turbine):
    """
    :param turbine: Class which contains the turbine data and the power curve of the turbine.
    """
    plt.figure(figsize=(14, 8))
    plt.scatter(turbine.avg_data()["wsp"], turbine.avg_data()["pwr"], s=0.5, c="tab:blue", label="Turbine data")
    plt.plot(turbine.pwr_curve()["wsp"], turbine.pwr_curve()["pwr"], c="tab:orange", label="Theoretical power curve")
    plt.legend()
    plt.title("Power Curve")
    plt.xlabel("Wind speed in $m/s$")
    plt.ylabel("Power in $kW$")
    plt.show()


if __name__ == "__main__":
    # Plot the power curve
    plot_power(TurbineData())

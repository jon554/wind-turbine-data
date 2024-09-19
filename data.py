#!/usr/bin/env python


"""
Functions to read and process the data.
"""


# Import external libraries
import pandas as pd

# Import default libraries

# Import own modules

# Import variables
from config import PATH_AVG_DATA, PATH_DEV_DATA, PATH_PWR_CURVE


def convert_unix_to_datetime(df: pd.DataFrame, key: str, localtime: bool = True):
    """
    Converts the unix timestamp in seconds of a Dataframe column to a datetime format.
    :param df: Pandas DataFrame with a unix time column.
    :param key: Column name of the time column.
    :param localtime: If True the local time (Europe/Berlin) is used in the time column.
        If False the UTC time is used.
    """
    df[key] = pd.to_datetime(df[key], unit="s")
    if localtime:
        df[key] = df[key].dt.tz_localize('UTC').dt.tz_convert('Europe/Berlin')


def read_data(path: str, unix: bool = False, localtime: bool = True) -> pd.DataFrame:
    """
    :param path: Path of the CSV file that contains the data.
    :param unix: If True the time column of the DataFrame is in seconds starting from 1970-01-01.
        If False the time column is in Datetime format.
    :param localtime: If True the local time (Europe/Berlin) is used in the time column.
        If False the UTC time is used.
    :return: DataFrame with the average turbine data.
    """
    df = pd.read_csv(path, sep=",")
    if not unix:
        convert_unix_to_datetime(df=df, key="tstamp", localtime=localtime)
    return df


def read_power_curve(path):
    """
    Reads the CSV file that contains the turbine's theoretical power curve.
    :param path: Path of the CSV file that contains the data.
    :return: DataFrame with the turbine's power curve data.
    """
    return pd.read_csv(path, sep=",")


class TurbineData:
    def __init__(self, path_avg=PATH_AVG_DATA, path_dev=PATH_DEV_DATA, path_pwr_curve=PATH_PWR_CURVE):
        self.path_avg = path_avg
        self.path_dev = path_dev
        self.path_pwr_curve = path_pwr_curve

    def avg_data(self, unix=False, localtime=True):
        """
        Get the data of the turbine's average data.
        :param unix: If True the time column of the DataFrame is in seconds starting from 1970-01-01.
            If False the time column is in Datetime format.
        :param localtime: If True the local time (Europe/Berlin) is used in the time column.
            If False the UTC time is used.
        :return: DataFrame with the average turbine data.
        """
        return read_data(self.path_avg, unix=unix, localtime=localtime)

    def dev_data(self, unix=False, localtime=True):
        """
        Get the data of the turbine's deviation data.
        :param unix: If True the time column of the DataFrame is in seconds starting from 1970-01-01.
            If False the time column is in Datetime format.
        :param localtime: If True the local time (Europe/Berlin) is used in the time column.
            If False the UTC time is used.
        :return: DataFrame with the deviation turbine data.
        """
        return read_data(self.path_dev, unix=unix, localtime=localtime)

    def pwr_curve(self):
        """
        Get the data of the turbine's theoretical power curve.
        :return: DataFrame with the data of the turbine's power curve.
        """
        return read_power_curve(self.path_pwr_curve)


if __name__ == "__main__":
    # Call the object
    turbine = TurbineData()
    # Print the average values
    print(turbine.avg_data())

# prep_data.py
"""
This module cleans the dataframe in preparation for creating
visualisations with holoviews and bokeh packages.

Functions:
    read_data: read csv and return pandas dataframe
Classes:
    CleanData: remove/replace nans and fix data types.
"""
import pandas as pd


def read_data(data_path):
    """Read csv and return pandas dataframe."""
    return pd.read_csv(data_path)


class CleanData:
    """
    This class is used to clean a dataframe in preparation for creating
    a chord diagram.

    Attributes:
        df (df): dataframe containing raw data

    Methods:
         drop_nans: remove rows with nans in any specified column
         make_numeric: moke specified columns numeric type
         replace_nans: replace nans with 0
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def drop_nans(self, null_drop_list: list) -> pd.DataFrame:
        """Remove rows with nans in any colum in null_drop_list."""
        return self.df.dropna(subset=null_drop_list, how="any", inplace=True)

    def make_numeric(self, numeric_col_list: list) -> None:
        """Make columns in numerical_col_list numeric type."""
        self.df[numeric_col_list] = self.df[numeric_col_list].apply(
            pd.to_numeric, errors="coerce"
        )

    def replace_nans(self) -> pd.DataFrame:
        """Replace nans with 0."""
        return self.df.fillna(value=0, inplace=True)

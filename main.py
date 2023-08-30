# main.py
"""This module contains the main pipline for creating visualisations with
holoviews and bokeh packages. It requires the visualisation.py and
pre_data.py modules. """

from prep_data import read_data, CleanData
from visualisations import MakeChordDiagram

data_path = "data/Global-Refugee-Dataset-1951-2015.csv"

# list column names which may not contain nulls (rows with nulls in
# ANY column will be dropped)
null_drop_list = ["Year", "Country / territory of asylum/residence", "Origin"]

# list of column names to be changed to numeric type
numeric_col_list = [
    "Refugees (incl. refugee-like situations)",
    "Asylum-seekers (pending cases)",
    "Returned refugees",
    "Internally displaced persons (IDPs)",
    "Returned IDPs",
    "Stateless persons",
    "Others of concern",
    "Total Population",
]

# year to visualise
year = 2015

# maximum number of largest chords to be visualised
max_chords = 60

# read in the csv and return a dataframe
df_raw = read_data(data_path)

# create an instance of the data cleaning class
cleaned_data = CleanData(df_raw)

# run the CleanData methods to prepare the data
cleaned_data.drop_nans(null_drop_list)

cleaned_data.make_numeric(numeric_col_list)

cleaned_data.replace_nans()

# create an instance of the MakeChordDiagram class
chord_diagram = MakeChordDiagram(
    cleaned_data.df,
    "Origin",
    "Country / territory of asylum/residence",
    "Total Population",
    year,
)

# run the class methods to create and display the chord diagram
chord_diagram.subset_data()

chord_diagram.make_diagram(max_chords)

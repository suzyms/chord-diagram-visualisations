# visualisations.py
"""
This module is used to create visualisations using the holoviews and bokeh
packages.

Classes:
    MakeChordDiagram: Formats required data and creates a chord diagram.
"""
import pandas as pd
import holoviews as hv
from holoviews import opts
from bokeh.plotting import show

hv.extension("bokeh")
hv.output(size=200)


class MakeChordDiagram:
    """
    This class is used to create a chord diagram.

    Attributes:
        df (df): dataframe containing cleaned data
        source (str): name of column containing chord start locations
        target (str): name of column containing chord end locations
        value (str): name of column containing magnitude of chord
        year (int): the year to visualise

    Methods:
        subset_data: create a new dataframe containing the source, target and
        value data for the specified year
        make_diagram: create and display the chord diagram in a new browser
        window
    """

    def __init__(
        self, df: pd.DataFrame, source: str, target: str, value: str, year: int
    ):
        self.df = df
        self.source = source
        self.target = target
        self.value = value
        self.year = year

    def subset_data(self) -> None:
        """
        Create a new dataframe containing the source, target and
        value data for the specified year.

        Raises:
            ValueError: if selected year is out of range of available data

        Outputs:
            self.chord_df: dataframe of
        """
        if self.year not in range(self.df["Year"].min(), self.df["Year"].max() + 1):
            raise ValueError(
                f'Year out of range. Select a value between {self.df["Year"].min()}'
                f' and {self.df["Year"].max()}.'
            )
        else:
            chord_df = self.df[self.df["Year"] == self.year][
                [self.source, self.target, self.value]
            ]
            chord_df.sort_values(self.value, ascending=False, inplace=True)
            chord_df.reset_index(inplace=True, drop=True)
            self.chord_df = chord_df

    def make_diagram(
        self,
        max_chords: int,
        node_color: str = "index",
        label_index: str = "index",
        cmap: str = "Category20",
        edge_cmap: str = "Category20",
    ) -> None:
        """
        Create and display chord diagram in new browser window.

        Args:
            max_chords: the number of largest chords to display
            node_color: the color of the outer nodes
            label_index: node labels
            cmap: color palette for the chords
            edge_cmap: color palette for the node edges
        """
        links = self.chord_df.head(max_chords)
        chord = hv.Chord(links)
        chord.opts(
            node_color=node_color,
            edge_color=self.source,
            label_index=label_index,
            cmap=cmap,
            edge_cmap=edge_cmap,
        )
        show(hv.render(chord))

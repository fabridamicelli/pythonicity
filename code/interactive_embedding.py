"""
Simple function for interactive visualization labels of a 2D embedding
(e.g., PCA projection).

Altair Chart is generated (as html), where one can brush over the scatter
plots and given labels are shown.
Color can be optionally mapped to values as well (e.g., to compare embedding
with a clustering method).

This is a quick adaptation of this example:
https://altair-viz.github.io/gallery/scatter_linked_table.html

Author: Fabrizio Damicelli (2019)
"""
import altair as alt


def plot_interactive_embedding(
    source=None,
    x=None,
    y=None,
    target_col=None,
    color_col=None,
    alpha=0.9,
    markersize=40,
    grid=True,
    max_n_show = 25,
    figsize=(500, 500),
    filename=None
):
    """
    Parameters
    ----------
    source: pandas Dataframe
        Data to plot.
    x: str
        Column name of x coordinate data.
        This name will be also used as axis label.
    y: str
        Column name of y coordinate data.
        This name will be also used as axis label.
    target_col: str
        Column name of target data, i.e., the labels to brush over.
    color_col: str, optional. Default None.
        Column name of data encoding color.
        If None, all points will have same color.
    alpha: float (0-1), optional. Default .9.
        Opacity of points.
    markersize: float, int, optional. Default 40.
        Size of the points.
    grid: bool, optional. Default True.
        Grid in the background. Set to False to remove it.
    max_n_show: int, optional. Dafault 25.
        Maximum number of (target) labels to show when brushing over the points.
    figsize: tuple (floats), optional. Default (500, 500).
        Values for (width, height)
    filename: str, optional. Default None.
        If given, the chart will be saved.
        The name must include extension - one of [.json, .html, .svg, .png].

    Returns
    -------
    chart: Altair Chart
        Instance of chart for further tweaking

    """
    width, height = figsize
    # Brush for selection
    brush = alt.selection(type='interval')

    # Scatter Plot
    points = alt.Chart(
        source,
        width=width,
        height=height
    ).mark_circle(size=markersize).encode(
        x=x,
        y=y,
        color=alt.value('steelblue')
              if color_col is None
              else alt.Color(color_col+":N", scale=alt.Scale(scheme='Spectral'))

    ).add_selection(brush)

    # Base chart for data tables
    ranked_text = alt.Chart(source).mark_text().encode(
        y=alt.Y('row_number:O',axis=None)
    ).transform_window(
        row_number='row_number()'
    ).transform_filter(
        brush
    ).transform_window(
        rank='rank(row_number)'
    ).transform_filter(
        alt.datum.rank < max_n_show
    )

    # Data Tables
    text = ranked_text.encode(text=target_col+":N").properties(title=target_col)

    chart = alt.hconcat(
    points,
    text,
    ).configure_axis(grid=grid)

    if filename:
        chart.save(filename)

    return chart

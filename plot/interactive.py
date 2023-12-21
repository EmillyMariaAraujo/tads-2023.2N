import plotly.express as px
from data.download import download_data


def plot_line_1(ticker:str):
        
    """ Plot an interactive.
    Args:
        ticker (str):  The ticker of financial asset.

    Returns:
        plotly: a plot.
    """

    data = download_data(ticker)

    fig= px.line(
                    data.reset_index(),
                    x= 'Date', y= 'Close', title= ticker,
                    labels={'Close': 'Fechamento', 'Date': 'Data'}
                )

    return fig
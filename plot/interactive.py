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
    data['SMA'] = data['Close'].rolling(window = 9).mean()
    data['LMA'] = data['Close'].rolling(window = 72).mean()

    fig= px.line(
        data.reset_index(),
        x= 'Date', y= ['Close', 'SMA', 'LMA'],
        title= ticker,
        labels={'Close': 'Fechamento', 'Date': 'Data'},
        color_discrete_map = {
        'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
    )

    return fig
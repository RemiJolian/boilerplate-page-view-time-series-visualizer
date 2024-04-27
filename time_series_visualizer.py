import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
file_path = (
           "D:\\1-Programming\\1-Training_Files & Codes\\Python\\1-Ramin's Codes\\Data_Analysis\\"
            "5 Projects\\boilerplate-page-view-time-series-visualizer\\fcc-forum-pageviews.csv")

df = pd.read_csv(file_path)
#df['date'] = pd.to_datetime(df['date'])
df.set_index('date')

# Clean the data by filtering out days when the page views were in the top 2.5% of
# the dataset or bottom 2.5% of the dataset.
# Filter out days in the top 2.5% and bottom 2.5%
top_threshold = df['value'].quantile(0.975)
bottom_threshold = df['value'].quantile(0.025)

# Filter to keep only the top 2.5% and bottom 2.5% of page views
df = df.loc[(df['value'] < bottom_threshold) | (df['value'] > top_threshold)]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(16, 9))  # Create a figure and axis
    df.plot(ax=ax, title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

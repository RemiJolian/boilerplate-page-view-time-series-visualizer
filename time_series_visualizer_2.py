import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import os

# Get the directory where the script is located
script_dir = os.path.dirname(__file__)

# Change the working directory to the script's directory
os.chdir(script_dir)

# Now, the file_path should be a relative path from the script's location
file_path = 'fcc-forum-pageviews.csv'

df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')

# Clean the data by filtering out days when the page views were in the top 2.5% of
# the dataset or bottom 2.5% of the dataset.
# Filter out days in the top 2.5% and bottom 2.5%
top_threshold = df['value'].quantile(0.975)
bottom_threshold = df['value'].quantile(0.025)

# Filter to keep only the top 2.5% and bottom 2.5% of page views
df = df[(df['value'] >= bottom_threshold) & (df['value'] <= top_threshold)]


def draw_line_plot():
    # Create a figure and axis with a specific size (16x9 inches)
    fig, ax = plt.subplots(figsize=(10, 5))  
    # Plot the data from the DataFrame 'df' on the specified axis with a title
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    # Set the label for the x-axis & y-axis and title
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')  
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    plt.show()
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, figsize=(10, 10), ylabel='Average Page Views',
                          xlabel='Years').figure
    plt.legend(['January', 'February', 'March', 'April',
                'May', 'June', 'July', 'August',
                'September', 'October', 'November', 'December'])

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=15)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    plt.show()
    return fig


def draw_box_plot():
    # Assuming df is defined and contains your data
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    # Year-wise Box Plot (Trend) with colorful boxes
    axes[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0], palette="tab10")
    # Month-wise Box Plot (Seasonality) with colorful boxes
    axes[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=axes[1], palette="tab10")

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    plt.show()
    return fig

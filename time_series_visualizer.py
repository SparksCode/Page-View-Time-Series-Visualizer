import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
  'fcc-forum-pageviews.csv',
  index_col = 'date',
  parse_dates = ['date']
)

# Clean data
df = df[
  (df['value']>=df['value'].quantile(0.025)) & 
  (df['value']<=df['value'].quantile(0.975))
]
df.index = pd.to_datetime(df.index)

def draw_line_plot():
  # Draw line plot
  fig,ax = plt.subplots(figsize = (18, 6))

  plt.plot(df.index, df['value'], color = 'red')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['month'] = df_bar.index.month
  df_bar['year'] = df_bar.index.year
  df_bar = df_bar.groupby(['month', 'year'])['value'].mean().unstack()

  # Draw bar plot
  fig=df_bar.plot.bar().figure
  plt.xlabel("Years")
  plt.ylabel("Average Page Views")
  plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
  plt.show()

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



  fig = plt.subplots()
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig

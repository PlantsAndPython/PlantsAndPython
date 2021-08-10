#!/usr/bin/env python
# coding: utf-8

# # Lesson 4.0

# # Pandas, dataframes, and seaborn 🐼

# ____
# 
# In the previous lessons, we have been focusing on learning the nuts and bolts of Python: lists, matplotlib, and, loops. We used these to make models of phyllotaxy and growing sunflowers.
# 
# Now, we shift our focus from formal coding and modeling to data analysis. Data analysis means dataframes, pandas, and seaborn!
# 
# Often, your data will be a lot like an Excel spreadsheet, with rows, columns, and column headers. But we need more functionality than Excel can provide. That's where pandas comes in. Pandas is a lot like the Python version of R, which means that it is built to use dataframes and has a lot of built-in statistical capabilities. For plotting, Seaborn is a Python graphing module that, although lacking the versatiity of matplotlib, is built for graphing with statistical needs in mind.
# 
# We can't cover all that pandas does in a few notebooks. But as you continue your studies and need to do something specific with respect to data wrangling or analysis, there are many [tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html) that will certainly have what you need. And of course, google your question!
# 
# The best way to use Seaborn is to gaze the [gallery of plots](https://seaborn.pydata.org/examples/index.html) and select what you need! The documentation and examples will be there.
# 
# Watch the video below to get started using pandas and seaborn. We will be analzying a dataset examining harvest dates in European grapevines with respect to a warming climate later in the notebook. So, in this video, we will be looking at measurements of CO2 levels in ppm from the [Mauna Loa Observatory in Hawaii](https://www.co2levels.org/#sources). You can download the dataset used in the video tutorial [here](https://github.com/DanChitwood/PlantsAndPython/blob/master/co2_mlo_weekly.csv).
# 
# Pay attention to the following points:

# ## 🐍 Python learning objectives
# 
# - How to read in a dataframe using `pandas` (*1:32*)
# - How to quickly assess dataframe properties, using `head` and `tail` (*2:28*)
# - How to select columns of a dataframe (*4:10*)
# - How to perform descriptive statistics using `pandas` (`.min`, `.max`, `.std`, `.value_counts`) (*6:09*)
# - How to mask data (a Boolean statement to fish out data that you want, square brackets after a dataframe) (*8:00*)
# - How to use `iloc` to isolate data within a dataframe (rows first, columns second, start:end, and square brackets) (*12:13*)
# - Plotting with `seaborn` (specialized plotting for statistics) (*16:32*)

# ## 🌻 Plant learning objectives
# 
# - CO2 levels are increasing, which increases global temperatures
# - Plants respond to increases in CO2 and temperature
# - In the next activity, we'll examine the effects of global warming on crop plants
# - Statistics and data visualization are powerful techniques to explore global trends

# ## How to read in a dataframe using `pandas`
# ____

# ***Watch this video from 0:00 to 2:25***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=2, seconds=25).total_seconds())

YouTubeVideo("jEQRU55x0e4",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# Let's learn how to read in a dataframe using the pandas module.
# 
# Pandas is usually imported as pd so you press shift + enter to import pandas and the most useful function in pandas is probably 
# `read_csv()`. This is a function that will take .csv data and read it in as a dataframe. Dataframes have rows and columns and the columns have names. By default, the files should be in your home directory but you can also provide a path to it. 
# 
# So for example I'll be loading in this data from my desktop so I added "./Desktop" and then the name of the file. So we hit shift + enter and now we've created a variable, `data`, that contains our dataframe. 
# 
# NOTE: In the video the file is read in locally from the Desktop, but here we will load in the data using a link from GiHub where the data is posted.

# In[2]:


# Pandas is usually imported in as "pd"

import pandas as pd


# In[3]:


# A useful function is pd.read_csv()
# which reads in a CSV as a dataframe
# Dataframes have rows and columns with names

# By default the the file should be in your home directoty
# but you can also provide a path
# For example, I'll load it in from my Desktop

# data = pd.read_csv("./Desktop/co2_mlo_weekly.csv")

# NOTE: in the video the file is read in locally from the Desktop
# but here we will load in the data using a link from GitHub 
# where the data is posted

data = pd.read_csv('https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/co2_mlo_weekly.csv')


#!/usr/bin/env python
# coding: utf-8

# # 4.3 Descriptive Statistics

# ## How to perform descriptive statistics using `pandas` (`.min`, `.max`, `.std`, `.value_count`)
# ____

# ***Watch this video from 6:01 to 8:06***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=6, seconds=1).total_seconds())
end=int(timedelta(hours=0, minutes=8, seconds=6).total_seconds())

YouTubeVideo("jEQRU55x0e4",start=start,end=end,width=640,height=360)


# > 💡 ***Remember:*** Import `pandas` and read in the dataset below to complete this lesson.

# In[2]:


# Import pandas

import pandas as pd


# In[3]:


# Download the dataset from the
# Jupyter Book to read in locally or 
# read in from GitHub, below:

data = pd.read_csv('https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/co2_mlo_weekly.csv')


# ***The following is a transcript of the video.***

# Next, let's look at how to perform some descriptive statistics in pandas, things like finding minimums, maximums, standard deviations, how many there are of each factor level.
# 
# This is incredibly simple. You just saw that we can refer to a specific column using a string. Let's say we want CO2 parts per million, but we want the minimum value of CO2 parts per million for that column. So we refer to the specific column and all we do is we add dot min as a function. And we get back that the minimum is 402.76.

# In[4]:


# There are a series of functions to perform simple statistics on columns

# .min()

data['CO2ppm'].min()


# If we want the max, we do the same thing: dot max, we get 415.39.

# In[5]:


# .max()

data['CO2ppm'].max()


# If we want the mean, we just take dot mean we get 408, somewhere in between them.

# In[6]:


# .mean()

data['CO2ppm'].mean()


# And if we want the median, we use the dot median function and we also get something somewhere in between the minimum and the maximum. 

# In[7]:


# .median()

data['CO2ppm'].median()


# There's a lot of these functions and you can quickly look these up. They're very useful. You can use unique to give you the levels of a column, what types of different things are in that column. So for example, if we look at the specific column of month, the different levels 
# of that column are the months of the year.  

# In[8]:


# .unique() gives the levels of a column, the different values

data['month'].unique()


# You can also get how many things there are of each one. This is called value counts. Again for month, maybe we want to get the value counts and you can see for each month it's going to give us how much data points there are for each month.

# In[9]:


# .value_counts() returns how many data points there are for each level

data['month'].value_counts()


# There's a lot of really useful functions. Some of them even do plotting. For example, `.hist()`, will give you a histogram (a plot showing the count of samples over a range of values).

# In[10]:


# .hist() will return a histogram

data['CO2ppm'].hist(bins=10) # have to shift-enter twice


# So that was how by very simply referring to the names of columns and then using functions and pandas you can get very basic statistical parameters back.

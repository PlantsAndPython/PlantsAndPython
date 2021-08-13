#!/usr/bin/env python
# coding: utf-8

# # 4.1 Head and Tail

# ## How to quickly assess dataframe properties, using `head` and `tail`
# ______

# ***Watch this video from 2:25 to 4:12***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=2, seconds=25).total_seconds())
end=int(timedelta(hours=0, minutes=4, seconds=12).total_seconds())

YouTubeVideo("jEQRU55x0e4",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# > 💡 ***Remember:*** Import `pandas` and read in the dataset below to complete this lesson.

# In[2]:


# Import pandas

import pandas as pd


# In[3]:


# Download the dataset from the
# Jupyter Book to read in locally or 
# read in from GitHub, below:

data = pd.read_csv('https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/co2_mlo_weekly.csv')


# Now let's see how to look at our dataframe using head and tail.
# 
# So it's important to know what you're working with, to "see" the dataframe. Head and tail allow us to do that. Remember that the data is stored in the variable `data`. We use `.head()` to see a preview of the first five rows and we'll also get the column names.

# In[4]:


# It's important to know what you are working with
# to "see" the dataframe
# .head() shows the first rows and column names

data.head()


# We can also use tail. And tail, if the head is at the beginning, then the tail is the end. You can see that we get the last rows in our dataset. Tail is very useful to see just how many rows that you have overall. Remember that we're beginning with zero, so we have 714 rows or data points in this dataset. 

# In[5]:


# .tail() shows the las rows

data.tail()


# Describe is a very useful function that gives you back summary statistics for your continuous variables. If we use describe on our data we get back information for running date, which is just a number that is increasing to keep track of day; year is included as a continuous variable, even though we do not want it to be a 
# continuous variable; and CO2 parts per million, which is of course a continuous variable as well. We get back how many entries of each variable that we have. We have 714 of each. We get the mean of each; the standard deviation; the minimum; the quartiles at the 25th, 50th, and 75th percentiles; and the maximum value as well. 

# In[6]:


# .describe() is very useful, showing summary statistics
# it provides stats for continuous variables

data.describe() 


# So that's how to read in a dataframe, how to quickly look at the dataframe and get summary statistics of the continuous variables. 

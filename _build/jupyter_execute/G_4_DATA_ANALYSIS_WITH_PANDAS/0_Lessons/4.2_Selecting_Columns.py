#!/usr/bin/env python
# coding: utf-8

# # 4.2 Selecting Columns

# ## How to select columns of a dataframe
# ____

# ***Watch this video from 4:12 to 6:01***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=4, seconds=12).total_seconds())
end=int(timedelta(hours=0, minutes=6, seconds=1).total_seconds())

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


# Let's learn how to select specific columns of the data frame.
# 
# 
# If you remember in the previous example, that year was treated as a continuous variable. The data that you read in has the years 2017, 2018, and 2019. But we don't want those to be treated as numbers, we want them to be treated as a categorical variable, as if they were year "A", year "B", or year "C".  
# 
# So let's try to change our year column into a categorical variable. But to do that we need to know how to refer to specific columns in pandas, and this is extremely easy. This is one of the the great things of using a dataframe is that you can simply refer to the columns by name, rather than by an index number. 
# 
# 
# If we want the year column, all we do is for our dataframe data, we have square brackets and we just refer to year as a string in quotations. If we want to set year to a categorical variable, we use the `astype()` function to convert it into a string, which makes it a categorical variable. So we say for the year column, referring to it as a string, we want to convert it `astype()` into string, and we set the year column back using a string referring to itself.

# In[4]:


# In the previous example 'year' was continuous
# but we want year to be categorical

# How do we refer to a specific column?

# Simply use the name of the column in brackets, as a string!

# After getting the 'year' column, simply use .astype() to change to string

data['year'] = data['year'].astype(str)


# So let's check that we were successful. You can see now when we use describe that we no longer see year here, because you can't take a mean or a minimum or a max of a categorical variable. We only have running dates and CO2 parts per a million now. This was to show you that you can access a specific column simply by referring to it as a string in square brackets for a data frame in pandas.

# In[5]:


# Let's check with .describe() now if 'year' is categorical

data.describe()


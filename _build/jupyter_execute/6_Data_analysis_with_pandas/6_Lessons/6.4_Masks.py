#!/usr/bin/env python
# coding: utf-8

# # Lesson 4.4

# ## How to mask data (a Boolean statement to fish out data that you want, square brackets after a dataframe)
# _____

# ***Watch this video from 8:06 to 12:06***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=8, seconds=6).total_seconds())
end=int(timedelta(hours=0, minutes=12, seconds=6).total_seconds())

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


# Next we're going to talk about something called masking. Masking is very important and it's a way to find specific data that fulfills a criteria that is a Boolean statement; remember, a Boolean statement is something that can only evaluate to `True` or `False`, to find all the data in your data frame that is true with respect to the Boolean statement.  
# 
# So this is what masking does: it gives us specific data and as I said it's very simple, a mask is just a Boolean statement.
# 
# We can create a mask variable and set it equal to a Boolean statement. For the data in the month column, let's make a Boolean statement saying that month equals August. We use a double equals here because remember, when we're using Python you can have less than or equal to, greater than or equal to, but equals equals is truly equal. So the Boolean statement is, is it the month `august`, `True` or `False`? That is the mask. And we're setting this Boolean statement equal to the mask.
# 
# So we hit shift + enter and then we can see what the mask is. 

# In[4]:


# How do we get specific data?
# What if we want all data points from just the month of August?
# We create a mask!
# A mask is a Boolean statement where the data you want is TRUE

mask = data['month']=='aug'


# And we can see what the mask is: it returns the rows of the dataframe that fulfill the criteria of the Boolean statement. This is a large dataframe. It starts at the beginning then it breaks and then it goes all the way to the end. If you remember, the month of `august` was the very first data values. So you can see that these `august` dates, which were at the top of the  dataframe, are evaluating as `True`. But then they evaluate as `False` when the month is not `august` at the end.  

# In[5]:


# The mask returns which rows evaluate as TRUE for the Boolean statement

mask


# We can get the full data back as well. This is what a mask does: it is returning the rows which are `True` and `False`, but if you put the mask within the dataframe brackets what you get back is the whole dataframe, those rows of the dataframe that evaluate as `True`.  
# 
# For example, here you can see what we get returned is only data that is the month  
# of `august`. These were the only rows that fulfilled the Boolean statement of being `True` that they were `august`.
# 
# So that's all the mask is: remember a mask is just a Boolean statement and we put the mask in the brackets of the dataframe to return those rows that evaluate as `True` for the Boolean statement.

# In[6]:


# If we place the mask inside the dataframe brackets
# then the rows where the statement is True are returned

data[mask]


# You can use this technique also with a specific column. For example, if you say you're only interested in the CO2 parts per million values,  you refer to that column and the square brackets to get it, but you have a second set of brackets with the mask and when you do this you will have only returned the CO2 parts per million values, none of the rest of the dataframe, because you specified this specific column.  

# In[7]:


# We can limit what is returned by refering to a specific column
# and placing the mask in a double bracket

data['CO2ppm'][mask]


# You saw that we created a mask, and we called it mask, and we were writing out the mask into our code. But usually people don't do that. They do it much more simple, where they just write out the mask.
# 
# You just put the mask, all in one line of code, with the data or the specific column that you want. This is a little complicated to look at but always remember go to the mask first and it will be in the second set of brackets or it will be in the first set of brackets if you are returning all the data and it's just a Boolean statement. And it will return those rows that are true for the Boolean statement. And this is a way that you get specific data that you want. 

# In[8]:


# Usually, the mask is written out straight into the line of code
# Always look to the second set of brackets to see
# what the mask is

data['CO2ppm'][data['month']=='aug']


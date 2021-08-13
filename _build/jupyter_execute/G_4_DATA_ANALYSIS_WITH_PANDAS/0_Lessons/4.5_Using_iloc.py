#!/usr/bin/env python
# coding: utf-8

# # 4.5 Using iloc

# ## How to use `iloc` to isolate data within a dataframe (rows first, columns second, start:end, and square brackets)
# ____

# ***Watch this video from 12:06 to 16:25***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=12, seconds=6).total_seconds())
end=int(timedelta(hours=0, minutes=16, seconds=25).total_seconds())

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


# Next, let's look at another way to find specific data and this is called the `iloc` function. And this is going to use rows and columns to find the data that you want. It's kind of like excel, thinking of which rows, which columns, that you want to isolate the data from. And you can, for both the rows and the columns, use indexing with the start end colon notation that you learned about before.
# 
# So let's just review again what our data looks like. Remember we use `head` for that, it brings back the first five rows, but most importantly it gives you the column names. And we can see that the first column is date, the second column is a running date, the third column is a month, the fourth is the year, and the fifth is CO2.

# In[4]:


# We can also access specific rows and columns
# using indexing with .iloc()

# Let's look at the data again using .head()

data.head()


# So all you need to know about `iloc` is that the first position is rows, the second position is columns, and you can use indexing for rows and columns.
# 
# If we just use `data.iloc` and we put in one number, it's the rows slot. Remember, indexing starts at zero, so this should give us back just the first row of data.
# 
# And you can see this is August 13th 2017, running date 1, august, year 2017, and parts per million 405.2, which is the first row of data. So rows and then the index give us the first row of data.  

# In[5]:


# The first position in .iloc is rows
# The second position in .iloc is columns
# We use indexing and a colon start:end
# to reference which rows and columns we want

# Indexing starts at 0, so we get back the first row

data.iloc[0]


# Remember, negative one in indexing is a way to get the last element and so if we do just negative one and again, the row position, we get back the last row. And you can see it's the last row because it has the running date of 714.

# In[6]:


# -1 with indexing is the last element
# it returns the last row

data.iloc[-1]


# We can reference both rows and columns, so we could say the last row, and remember, if we just put a colon, which should have the start and the end but we don't put any numbers we're just going to get back all the values, so this will be the last row but all the columns. And indeed that's what we get: last row, 714, but all the columns, which is equivalent to just putting negative 1. But it also works this way because this is formally saying we want all the columns.  

# In[7]:


# We can reference the last row and all columns

data.iloc[-1, :] # start:end, but : refers to all columns


# In this case, with just an empty colon for rows, we're saying we want all the rows, but we just want the first column, the zero index column (remember that's date). So we get all the dates because we ask for all rows of just the the first column.

# In[8]:


# Here : refers to all rows
# for the first column referred to with 0

data.iloc[:,0]


# We could also get all the rows for the second column, remember the second column is the running date, so that's one through 714.

# In[9]:


# We could also get all rows and the second column, at index 1

data.iloc[:,1]


# Remember, you can use indexing for both the rows or the columns. The indexing is inclusive of the start but up to and not including the end. So in this case we're saying we want rows two and three because we're going up to but not including four, so this is rows two and three for columns from two to the end, which would be the third column to the end. 
# 
# You can see we get rows two and three inclusive of start up too and not including four, rows two and three, and we get the second index position of columns, which is the third column to the end. 

# In[10]:


# Indexing can be used for both the rows and columns

data.iloc[2:4, 2:] # indexing inclusive of start but not the end


# You can use brackets separated by commas to get very specific rows in very specific columns. So what if you wanted index positions 0, 3, 5, and 7 for rows and column positions 0, 2, and 4? And then you can see that's exactly what we get: we get the rows indexed by those random numbers and then the first, third, and fifth columns, because remember indexing starts at zero. 

# In[11]:


# Brackets in brackets can be used to refer to specific rows and columns

data.iloc[[0,3,5,7],[0,2,4]]


# So `iloc` is a way to get very specific data by row or by column.

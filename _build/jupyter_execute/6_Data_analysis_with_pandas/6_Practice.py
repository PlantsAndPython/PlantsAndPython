#!/usr/bin/env python
# coding: utf-8

# # Lesson 4.7

# ## Practice with Pandas, Dataframes, and Seaborn 🐼

# ---
# ## Data exploration
# 
# ### Loading and inspecting the data
# 
# After visiting Michigan and learning that wine grapes can be grown (and that wine can be made!) in such a cold place, you decide that you would like to start a vineyard there. You've seen the vineyards and know that, although it is possible to grow wine grapes there, that sometimes it is too cold. You wonder if because of climate change, Michigan might soon have a warmer, more suitable climate for growing grapes. 
# 
# You know that Europe has a long history of growing grapes, and you wonder if they kept records that might indicate how grapes respond to changes in temperature. You find a [study](https://www.clim-past.net/8/1403/2012/cp-8-1403-2012.pdf) that has compiled numerous records of grape harvest dates for more than four centuries and also a [database](http://www.climatemonitor.it/?page_id=40210&lang=en) of temperature anomalies in Europe dating back to 1655.
# 
# Using the provided dataset, `grape_harvest.csv` (download [here](https://github.com/DanChitwood/PlantsAndPython/blob/master/grape_harvest.csv)), you're going to explore how the European grape harvest date changes with respect to temperature across centuries of data.
# 
# To get started, import `pandas` in the cell below:

# In[1]:


# Import pandas here



# Then, read in `grape_harvest.csv` using the `pd.read_csv()` function a pandas dataframe.

# In[2]:


# Read in the grape harvest data here
# Put grape_harvest.csv in the same directory you are running this .ipynb from
# If in a different directory, you will need to specify the path to the file

# Alternatively, you can read in the data from GitHub using the following url:
# https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/grape_harvest.csv



# Now, write some code to inspect the properties of the data and then answer the following questions:
# 
# Use a pandas function to look at the first five lines of data:

# In[3]:


# Put your code here



# Use a pandas function to look at the last five lines of data:

# In[4]:


# Put your code here



# Use a pandas function to look at summary statistics (like the count, min, max, and mean) for columns with continuous data:

# In[5]:


# Put your code here



# Use a pandas function to retrieve the names of the columns. 

# In[6]:


# Put your code here



# For one of the columns that is a categorical variable, use a function to list all the levels for that variable.

# In[7]:


# Put your code here



# For the categorical variable, also use a function to determine how many rows there are representing each level.

# In[8]:


# Put your code here


# How many rows are in this dataset?

# In[9]:


# Put your code here



# Congratulations on reading in the data and exploring its structure! In the next activity, we will be exploring the relationship between grape harvest dates and climate!

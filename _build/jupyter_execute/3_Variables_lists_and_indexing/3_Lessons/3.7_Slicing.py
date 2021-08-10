#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.7

# # Slicing and data types
# ______

# You just learned about lists and indexing. But most of the examples were with strings and about names. What about numbers?
# 
# In the next video you'll be using lists with numbers. You will also be learning about slicing, which takes indexing to the next level adding an additional `step` value that can return values from every nth term of a list.
# 
# The learning objectives for this video are below:

# ### Python learning objectives
# 
# - Using numbers with lists (*1:04*)
# - Slicing can access list elements with a start, end, and step
# - The slicing start is inclusive, the slicing end is not
# - Different data types in Python: strings, integers, floats (*3:11*)
# - How to check which data type you are using with `type()`
# - You can convert between different data types using `str()`, `int()`, `float()`
# 
# ### Plant learning objectives
# 
# - The Golden Angle is an irrational number, derived from the Fibonacci sequence, that underlies the spiral arrangement of leaves and other organs (phyllotaxy) in plants (*3:16*)

# ## Using numbers with lists and slicing
# ____

# ***Watch this video from 0:00 to 3:09***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=3, seconds=9).total_seconds())

YouTubeVideo("CIlwbP_QM1w",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# Remember that lists can include any data type, even other lists. We initialize a new list with empty brackets and then we put numbers in it. So let's make a very easy list and use actual index numbers with it. So, we'll create a list called numbers, with brackets, and it's going to start on 0, the first index, and go to 20. We hit shift + enter to create the list. 

# In[2]:


# Remember, lists can include any data type,
# even other lists!
# We can initialize a new list with empty brackets [ ]
# and then put in numbers

# Let's make it easy and make a list
# with actual index numbers

numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# Previously you learned about indexing and using start and end values. With slicing there's an additional step value. Slicing uses two colons and three values with the square brackets and it has the form of start, end, and step. So, using our list of numbers let's try with a start of 2 and end of 16 in a step of 2 and see what we get. You can see that the start is inclusive, it begins on 2 but the end of 16 is not inclusive, it goes up to but not including 16. So it includes 14. And, you can see there's also a step of 2. It's every other number.  

# In[3]:


# There is more to indexing than [start:end]
# With slicing, there is a "step" value
# Slicing uses two colons and three values
# with the form of [start:end:step]

# Let's try start = 2, end = 16, and step = 2

numbers[2:16:2]


# Let's do the same thing but with a step of 3, and see what we get. So we start on 2, we don't go up to 16, only 14, and you can see that we're using steps of three. 

# In[4]:


# Let's try the same again but with step = 3

numbers[2:16:3]


# You can do shorthands as well. You can leave the start number out and indexing will always begin at zero. If you leave out the end number indexing will continue all the way to the end. It will be inclusive of the last number. And if you leave out the step, increments of 1 are used. So you can see here, we left out the start, and we start on 0 still. Here, we leave out the end number and we go all the way to 20. And here we leave out the step and we're using increments of one.

# In[5]:


# If you leave out the start number, indexing begins at 0

print(numbers[:16:3])

# If you leave out the end number, indexing continues to the end

print(numbers[2::3])

# If you leave out the step number, increments of 1 are used

print(numbers[2:16])


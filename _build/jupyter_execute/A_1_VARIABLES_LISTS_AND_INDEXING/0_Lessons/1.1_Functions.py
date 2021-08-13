#!/usr/bin/env python
# coding: utf-8

# # 1.1 Functions

# ## Our first function: `print()`
# ___

# ***Watch this video from 2:28 to 3:35***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=2, seconds=28).total_seconds())
end=int(timedelta(hours=0, minutes=3, seconds=35).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# > 💡 ***Remember:*** In the previous notebook you created a variable called `genus`. Create the variable `genus` again in the cell below to complete this lesson.

# In[2]:


# Create the variable genus

genus = "Vitis"


# You can also get the value back of a variable using a function. So let's go over our very first function, the simplest which is `print()`. A function in Python has a name 
# like print and it has a set of parentheses. You put an input inside the parentheses and 
# the function processes the input to produce an output. So for example, the output of 
# the `print()` function is to simply print out the value of our variable. So if we 
# print `genus` what we get back is `"Vitis"`.

# In[3]:


# You can use the print() function to see a variable value
# A function always has a set of parentheses
# You place the input inside the parentheses
# The function processes the input to produce an output
# The output of the print() function is to print out our variable

print(genus)


# You can use commas to separate print outputs by a space and both variables and strings can be used with the print function. So for example, in our print function if we put a string in quotation marks `"The variable genus is equal to"` and then we put a comma and then we put our variable `genus`, if we execute the print function what we get is `The variable genus is equal to Vitis`.  

# In[4]:


# Use commas to separate print() outputs by a space
# Both variables and strings can be used with print()

print("The variable genus is equal to", genus)


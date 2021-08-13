#!/usr/bin/env python
# coding: utf-8

# # 1.0 Variables

# ## Variables, Functions, Lists, & Indexing
# _____

# In our very first video tutorial, we are going to learn the fundamentals of Python. You will learn how to create a variable. You you will use functions to process variables and create outputs. And you will learn about indexing, a way to keep track of data, access it, modify it, and use it.
# 
# The learning objectives that are covered in the video tutorial are outlined below. The time stamp for each objective is provided. Feel free to type out the examples in the video, creating new cells in this notebook, and go at your own pace. Pause the video and rewind it as needed to go over concepts. Play around with your own examples and explore!
# 
# There are both Python and plant learning objectives:

# ### 🐍 Python learning objectives
# 
# - **How to create a variable** (*1:15*)
#     - The variable does not have quotations
#     - A string always has quotations, either " " or ' '
# - **Our first function: `print()`** (*2:31*)
#     - Arguments go inside the parentheses
# - **What is indexing?** (*4:05*)
#     - Indexing takes the form of [start:end]
#     - Indexing always starts at zero
#     - Start is inclusive
#     - The end is not inclusive
#     - Indexing can be used to access specific string characters
# - **How to create lists** (*9:17*)
#     - Use empty brackets [ ] 
#     - Fill with variables or strings
#     - The `type()` functions gives back the data type (list, str, int, float)
#     - The `len()` function gives back the length of a list
# - **How to use indexing to access specific list elements** (*12:25*)
# - **How to modify lists** (*13:36*)
#     - List elements can be reassigned using indexing
#     - The `.append()` function can be used to add an element to a list
# - **How to create a list of lists** (*16:31*)
#     - Elements within a list of lists can be indexed using double brackets

# ### 🌻 Plant learning objectives
# 
# - **Plants are essential to human life** (*16:46*)
#     - Plants feed, clothe, shelter, medicate, and inspire us
#     - Plants regulate global cycles of water and carbon
# - **Plants are diverse, more diverse than just the plants we see on land or those that flower**
# - **Plants are hierarchically organized, reflecting evolutionary history**
# - **Species are referred to by a genus and species name**
# - **Plants are defined by a single, ancient endosymbiotic event that created choloroplasts**
# - **An overview of plant evolution:**
#     - Red and green algae (Rhodophyta and Chlorophyta)
#     - Non-vacular plants (Bryophytes: mosses, liverworts, and hornworts)
#     - Vascular seedless plants (Lycophytes, ferns/Pteridophytes, Gymnosperms)
#     - Seed plants (Gymnosperms and Angiosperms)

# ## How to create a variable
# ____

# ***Watch this video from 0:00 to 2:28***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=2, seconds=28).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# The first topic we'll be going over is how to create a variable. Please feel free to type along in your own Jupyter notebook or pause or rewind the video to go over a point again. A variable is a data type in Python that gives you a value back. The value can be a number like an integer or a float or it can be a string. A string is a series of characters. Variables do not have quotations. They can be a combination of letters and numbers and they are assigned a value. Strings, which are a type of value, always have quotation marks. The quotation marks can be double quotation marks or they can be single quotation marks. Let's create two variables, `genus` and `species`, and we're going to give them the values of strings. `Genus` 
# for `"Vitis"` and `species` for `"\_vinifera"`. Remember in order to create your variables you need to execute the Jupyter cell. The way you do that is by hitting shift + enter.

# In[2]:


# A variable has no quotation marks
# A string has quotations, double or single
# Reminder: you must execute a cell with shift + enter
# in order to create your variables

genus = "Vitis"
species = '_vinifera'


# Now that we've created our variables we can see what they are. They'll be able to give us a value back. So for example, if we type `genus` now that we've assigned it a value, if we execute the cell with genus we get `"Vitis"` back.

# In[3]:


# Executing a cell with a variable will print its value

genus


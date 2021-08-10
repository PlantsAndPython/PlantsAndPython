#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.8

# ## Different data types in Python and converting between them
# ____

# ***Watch this video from 3:10 to 7:15***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=3, seconds=10).total_seconds())
end=int(timedelta(hours=0, minutes=7, seconds=15).total_seconds())

YouTubeVideo("CIlwbP_QM1w",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# The next topic we're going to discuss are the different data types in python and converting between them.  
# 
# Let's take a real number, it's an approximation of the golden angle in degrees. The golden angle is found everywhere in nature and it's derived from the Fibonacci sequence. Later in this course we're going to learn more about the Fibonacci sequence and use it to approximate the golden angle so that we can model the growth of sunflowers. But for now, here is an approximation of this irrational number. We're going to call this variable `golden_ang`. We hit shift + enter to create it.

# In[2]:


# Let's take a real number, an approximation
# of the golden angle in degrees

# From the Online Encylcopedia of Inted Sequences
# https://oeis.org/A096627

# The golden angle is derived from the Fibonacci sequence,
# which we will learn about and use to approximate this
# value ourselves later to model the growth of sunflowers

golden_ang = 137.5077640500378546463487396283702776206886952699253696312384958261062333851951


# We can ask, remember, what data type we're using using the `type()` function. So if we do this with the golden angle we see that we get this answer back called float. 

# In[3]:


# We can ask what data type it is
# and we get "float" back

type(golden_ang)


# There are three major data types in Python that we'll be working with. You've already seen strings in the previous video. These are collections of characters but there are two major numerical types: they are floats and integers. The difference is very simple. Floats have decimals and integers don't. You can convert data into different types in Python using the `float()`, `int()`, and `str()` functions. For example, if you convert the golden angle to an integer it becomes a whole number. We take the golden angle, we put it in the `int()` function, and we use `print()`, and we get back just 137 with no decimal places.  

# In[4]:


# There are 3 major data types in Python
# You have already used strings, collections of characters
# There are two major numerical types: floats and integers
# Floats have decimals and integers don't

# You can convert data into different types using the
# float(), int(), and str() functions

# If you convert golden_ang to an integer, it becomes a whole number

print(int(golden_ang))


# You can convert an integer back to a float, but it will lose the decimal information. So again, if we convert golden angle, an irrational number, first into an integer, just 137, and then we convert this 137 integer into a float, the answer we get back is a decimal, but it's point zero because we lost all the decimal information when we use that integer function.  

# In[5]:


# You can convert the integer back to a float,
# but it loses the decimal information

# Notice the ".0" decimal

float(int(golden_ang))


# You can convert an integer or a float into a string, this makes sense because a string is just a collection of characters, they can be numbers too. You can use the `str()` function for this. You can use `str()` on golden angle and we'll create a string of the golden angle. We can print it out and see what type it is.
# 
# And you can see that when we print out the string golden angle it looks just like the number, we really can't tell the difference. But when we use `type()` we can see indeed it is a string. 

# In[6]:


# You can convert an integer or a float to a string

str_golden_ang = str(golden_ang)

print(str_golden_ang)

type(str_golden_ang)


# You can turn a string of numbers into actual numbers. For example, if you have the string 
# of golden angle and turn it into a float, it will be a number, a float.

# In[7]:


# You can turn a string of numbers into numbers

print(float(str_golden_ang))

type(float(str_golden_ang))


# You cannot turn characters into numbers, though. Remember, if we use quotation marks that creates a true string and these are letters so it's hard to imagine how you would convert these into a number. Let's take the string of letters golden angle and try to convert it into a float. If we do that we get an error and it says you cannot convert a string to a float, which we might have predicted.

# In[8]:


# You can not turn characters into numbers though

float("golden_ang")


# **So, what did we learn?**

# **Python learning objectives**
# 
# - Using numbers with lists
# - Slicing can access list elements with a start, end, and step
# - The slicing start is inclusive, the slicing end is not
# - Different data types in Python: strings, integers, floats
# - How to check which data type you are using with `type()`
# - You can convert different types into each other using `str()`, `int()`, `float()`
# 
# **Plant learning objectives**
# 
# - The Golden Angle is an irrational number, derived from the Fibonacci sequence, that underlies the spiral arrangement of leaves and other organs (phyllotaxy) in plants.

# # Thank you!

#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.3 Lists

# ## How to create lists
# 
# - Use empty brackets `[ ]` to initialize an empty list
# - Then, fill the brackets with variables or strings separated by commas
# ____

# ***Watch this video from 9:10 to 12:22***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=9, seconds=10).total_seconds())
end=int(timedelta(hours=0, minutes=12, seconds=22).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# > 💡 ***Remember:*** In the previous notebook you created variables called `wine`, `tequila`, and `beer`. Create the variables again in the cell below to complete this lesson.

# In[2]:


# Create the variables wine, tequila, and beer

wine = "Vitis_vinifera"
tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"


# Previously, we made all those variables because now we're going to create something called lists. Lists are just like they sound. They are a list of data types. The data types can be strings, they can be numbers, they can be integers, they can be floats, they can even be lists and we'll talk soon about creating a list of lists. You can put anything in your list that you want. Creating lists is very easy. You just use empty brackets. These brackets will not be touching another word like when you index, This will initialize an empty list. Then we just fill the brackets with variables or strings and they're separated by commas.
# 
# Let's create an empty list. We'll create a variable name `angiosperms`, which is the name for the flowering plants. We're going to set it equal to an empty list. And all an empty list is is just an empty set of brackets. We hit shift + enter and we will have created our new list.

# In[3]:


# Let's create an empty list called angiosperms, or the flowering plants

angiosperms = [ ]


# It's very convenient to know we can create all these variable types, they're just a collection of letters. They are just names, and sometimes you might be confused "what 
# do I have?": is it a string, is it a list, is it a number? Let's learn about our second 
# function in python, it's called `type()`. For the function `type()` we have a set of parentheses and we put an input into it, a variable of some sort, and `type()` will return back to us what type of variable it is. So we just created an empty list for our variable `angiosperms` and using `type()` we see indeed that's what we have, it is a list.  

# In[4]:


# We can always check what type of variable we have with the function type()
# Let's check if angiosperms is a list

type(angiosperms)


# You can test this further. For example `wine`, if you remember was a string, it's "Vitis_vinifera", it's just a collection of characters and it's not a list. So `type()` will tell you what sort of data type that you're working with.  

# In[5]:


# In contrast to the list angiosperms, wine is a string

type(wine)


# If we look at the contents of our angiosperm list it should be empty, right?, we haven't put anything into it and indeed we just get empty brackets back.

# In[6]:


# If we look at the contents of our list angiosperms,
# it should be empty

angiosperms


# But let's fill it up now. Filling up a list is really easy. All you do is you put in variables separated by commas. So in our list angiosperms we're going to put in wine, tequila and beer.  

# In[7]:


# Let's fill up our list angiosperms!
# We simply type in our variables, separated by commas

angiosperms = [wine, tequila, beer]


# We execute that cell. And now if we look at our variables in our list `angiosperms`, because we put `wine`, `tequila` and `beer` in it, we get back the values for those variables, which are "Vitis_vinifera", "Agave_tequilana", and "Hordeum_vulgare". So that's how you create a list, a set of empty brackets. You put in variables, numbers, strings, other lists, and as you'll see soon, anything you want. 

# In[8]:


# Now, when we look at the contents of angiosperms
# we should get back the variables we input

angiosperms


# Another convenient function is something called `len()`, for length. Length will give you back the length of a list, how many elements are in it. For example, we know that our angiosperm list has three elements in it. So if we put the list in the function length we get back three.

# In[9]:


# Another convenient function is len()
# len() gives back the length of a list, how many elements it has
# For example, our list angiosperms has 3 elements

len(angiosperms)


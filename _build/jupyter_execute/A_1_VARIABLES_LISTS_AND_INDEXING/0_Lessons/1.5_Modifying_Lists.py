#!/usr/bin/env python
# coding: utf-8

# # 1.5 Modifying Lists

# ## How to modify lists
# ____

# ***Watch this video from 13:34 to 16:25***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=13, seconds=34).total_seconds())
end=int(timedelta(hours=0, minutes=16, seconds=25).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# > 💡 ***Remember:*** In the previous notebook you created a list called `angiosperms` containing the strings `wine`, `tequila`, and `beer`. Create the list again in the cell below to complete this lesson.

# In[2]:


# Create the list angiosperms

wine = "Vitis_vinifera"
tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"

angiosperms = [wine, tequila, beer]


# So how can we modify a list? List elements can just be reassigned using indexing. For example, other species than *Vitis vinifera* can be used to make wine. Some species we'll talk about later in this course are used for rootstocks instead, or they're hybridized with *Vitis vinifera* to make different types of wine. So maybe it's not right of us to call wine just *Vitis vinifera* that specifically, maybe we should say that it's all *Vitis*. So let's try to turn *Vitis vinifera* back into just *Vitis*.
# 
# We can print out the first element of our angiosperm list with zero and see what it is. It should be *Vitis vinifera*. We specify that we're talking about the first element of angiosperms through indexing, so we say angiosperms index zero, and we just set it equal to *Vitis*. Remember it will be currently set to *Vitis vinifera* but then it changes into *Vitis*. Then, if we print out the list again we shouldn't have *Vitis vinifera* we should have just *Vitis*.
# 
# You can see that the first element is *Vitis vinifera*, we reassign it, and then when we print the list again you can see that *Vitis vinifera* has been transformed into *Vitis*. All we did is used an equal sign and specified the first element with zero.

# In[3]:


# List elements can be reassigned using indexing
# Other species than Vitis vinifera can be used to make wine
# For example, some species of Vitis we will talk about
# are used as rootstocks
# Let us reassign "Vitis_vinifera" in our list to just "Vitis"

print(angiosperms[0])

angiosperms[0] = "Vitis"

print(angiosperms)


# Another way to modify lists that we will use very often is  called the `.append()` function.
# 
# Step one for using this is to add the `.append()` after a list name.  
# 
# Step two is to add within the parentheses the additional element that you would like to append to the list. The appended element will be added to the end of the list.
# 
# So using length we already know that our current list angiosperms has three elements.

# In[4]:


# Another way to modify lists is using the .append() function
# Step 1 is to add ".append()" after a list name
# Step 2 is to add within the parentheses the additional element
# that you want to append to a list
# The appended element will be added to the end of the list
# Currently our list angiosperms has 3 elements

len(angiosperms)


# But let's say we wanted to add rice, used to make sake, to the end of our list.
# 
# We specify the list `angiosperms` and we add `.append()`. You should think of this as the `append()` is going to modify this list and we put in the string value that we want to add, the name for rice, which is `Oryza`. If we hit shift + enter we should be adding `Oryza` to the end of our angiosperm list. 

# In[5]:


# But let's add rice, used to make sake, to the end of our list

angiosperms.append("Oryza")


# Let's print out our angiosperm list. Now you see we have four things. Oryza, rice has been added to the last position. If we print out the length of our new angiosperms list we see that it's four, not three. So we successfully appended this value to the end of the list.

# In[6]:


# Now, our list should have 4 elements

print(angiosperms)

print(len(angiosperms))


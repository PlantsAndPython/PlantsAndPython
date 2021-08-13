#!/usr/bin/env python
# coding: utf-8

# # 1.4 Indexing List Elements

# ## How to use indexing to access specific list elements
# ___

# ***Watch this video from 12:22 to 13:33***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=12, seconds=22).total_seconds())
end=int(timedelta(hours=0, minutes=13, seconds=33).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# > 💡 ***Remember:*** In the previous notebook you created a list called `angiosperms` containing the strings `wine`, `tequila`, and `beer`. Create the list again in the cell below to complete this lesson.

# In[2]:


# Create the list angiosperms

wine = "Vitis_vinifera"
tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"

angiosperms = [wine, tequila, beer]


# We can use indexing to access specific list elements, just like you saw how you could access characters within a string, and it's done the exact same way.
# 
# If we have our list `angiosperms`, we can print it out but we can also index it. We can index and see what the first element is, the 0 index position. We can see what the third element is, which is the second index position. Or we can try to see what the entire list is. Remember, there's three elements which normally would be zero to two but we need to go up to three, because we'll go up to three but not include it.
# 
# So if we look at the whole list we have our three elements there. With zero index we fish out just the first element. With an index of two that ends up being the third element. And then we can retrieve the entire list by specifying four index positions, because the last position three it will go up to there but not include it.

# In[3]:


# You can use indexing to access elements of a list

print(angiosperms)

print(angiosperms[0])

print(angiosperms[2])

print(angiosperms[0:3])


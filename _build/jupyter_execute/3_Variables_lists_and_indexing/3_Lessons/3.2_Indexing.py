#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.2

# ## What is indexing?
# - Indexing is a way for us to keep track of and to access characters in a string or elements of a list
# - Indexing takes the form of `[start:end]`
# - The first element is always zero
# - The start is inclusive
# - The end is not inclusive
# ______

# ***Watch this video from 3:35 to 9:10***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=3, seconds=35).total_seconds())
end=int(timedelta(hours=0, minutes=9, seconds=10).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# > 💡 ***Remember:*** In the previous notebooks you created variables called `genus` and `species`. Create the variables again in the cell below to complete this lesson.

# In[2]:


# Create the variable genus
# and the variable species

genus = "Vitis"
species = "_vinifera"


# So that's how you create a variable. That's your first introduction to your first data type in Python: a string, a collection of characters.
# 
# Let's learn a little bit about indexing. Indexing is a way for us to keep track of and to access characters in a string or the elements of a list, which we're going to learn about soon. Indexing takes the form of square brackets and it has a start value and an end value separated by a colon. The first element in a series in Python is always zero. It's not one. It starts at zero. A start value of indexing is inclusive. It is the number itself, but importantly the end value is not inclusive. The indexing goes up to the end value but does not include it.
# 
# So let's remember: we had our variable genus. Remember that we assigned it the value the string of `"Vitis"`. Let's try to access the first letter of that string, the "V". Your first intuition might be that to get to the first element you would say "1". So we take our variable genus, we put in the square brackets, and we put in a "1" hoping to get back the first character. And we get back the second character instead, the "i", not the first and so this is why it's important to remember that in Python the first element for indexing always starts at zero.

# In[3]:


# Remember, our genus variable is "Vitis"
# Let's try to access the first element
# You might think the first element is 1

genus[1]


# When we use zero now we get back the first letter, which was a "V" and you can see how you're using this number to say which letter of the string that you want to get back.

# In[4]:


# But in Python the first element is always 0

genus[0]


# We can also access multiple elements in a string using indexing. Remember indexing takes the form of square brackets. It has a start, a colon, and an end value. Remember the start is 
# inclusive and the end is not inclusive. It goes up to the value of the end but does not include it. So let's try to get back all the letters of "Vitis".  
# 
# There are five letters in "Vitis" and you might think we need five index places and we remember that the indexing starts at zero, so to have five index places would be zero, one, two, three, four. Maybe to get the whole 'Vitis" back we go from zero to four?
# 
# But that is not the case. Remember the reason is because the start value is inclusive, so this will be index of 0, but this will go up to the value of 4 but not included. The fourth element is "s". If we index using 4, it does not include "s", it just goes right up to it.

# In[5]:


# We can also access multiple elements using indexing
# Indexing takes the form of [start:end]
# The start is inclusive
# The end is not inclusive
# "Vitis" has five characters
# To access the whole world, maybe we might try:

genus[0:4]


# And so to get back the whole value of "Vitis" from our variable genus we have to remember that the end is not inclusive. We're going to go up to it but not include it. So if we go from 0 to 5 that's 6 characters but remember it doesn't include the five it just goes right up to it. So if we index 0:5, we are going up to but not including the 6th position and we include all 5 characters of "Vitis".

# In[6]:


# But remember, the end is not inclusive
# We need to add one more value to include the last character

genus[0:5]


# Because characters in a string can be indexed, they're assigned values. You can do arithmetic with strings, believe it or not. Let's create some more variables to set ourselves up for the next section. Let's add genus plus species together. We're going to create a new variable now called wine. If we create our new variable, wine, and we say it's equal to genus (which was "Vitis") plus species (which is the string "\_vinifera") we create that new variable and then we can print it. Let's see what we get then: We get "Vitis_vinifera" all together as one because we added the two strings together.

# In[7]:


# Because characters can be indexed, you can do artihmetic with strings!
# Let's create some more variables to set ourselves up for the next section
# Let's add genus + species together and call the new variable "wine"

wine = genus + species

print(wine)


# For the next section, let's create two more variables. Let's call one tequila in the same theme and it comes from the plant "Agave_tequilana". And we have beer and that comes from barley, "Hordeum_vulgare". Remember to execute this cell so that we can get those variables back.

# In[8]:


# Let's also create two other variables in the same theme

tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"


# So let's print out our variables to make sure that they are okay and remember we can put multiple variables into our print function between the parentheses. They're separated by a comma. We get the values back for our three variables. For wine we get "Vitis_vinifera"; tequila, "Agave_tequilana", and beer we get "Hordeum_vulgare". Notice that we have common names for all these: grapes, agave and barley but we have these very scientific names in Latin for these species. There's always something called a genus, which is the first word and a second word, which is called the species epithet, and together these formally name a species.

# In[9]:


# Let's print our variables to check that they are OK

print(wine, tequila, beer)


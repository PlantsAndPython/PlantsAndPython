#!/usr/bin/env python
# coding: utf-8

# # Practice with Variables, Functions, Lists, & Indexing
# _______

# **Now you give it a try!**
# 
# Think of your favorite plant. It could be a food or a beautiful flower that you love. You just learned about the remarkable diversity among plants, from algae to land plants. There are so many to choose from!
# 
# Now google your favorite plant and find it's Latin name, both the genus and species epithet.
# 
# **Do this:**
# 
# In the cell below, create two variables, `genus` and `species`. Assign the variables the genus and species epithet names of your favorite plant.
# 
# Then, create a new variable called `my_fav` that combines the genus and species names together. **Hint:** place an underscore `_` preceding the species name so that when you combine genus and species they are separated!
# 
# Finally, use the print function `print()` to print out your favorite species.

# In[1]:


# Put your answer here


# Now, using wikipedia, look up the genus of your favorite plant. Find two other species in the genus besides your favorite plant. 
# 
# **Do this:**
# 
# Create two new variables, `species1` and `species2`. Using the `genus` variable you previously created and strings for the epithets of the two new species, assign the two new species variables the full species names (with genus) of the two new species.

# In[2]:


# Put your answer here


# Finally, create a list named after your genus with your variables `my_fav`, `species1`, and `species2`. Then, using indexing with your newly created list, print out the name of your favorite plant species.

# In[3]:


# Put your answer here


# ## Practice with Slicing and Data Types
# _______

# In the video you learned about the Golden Angle, an irrational number based on the Golden Ratio and Fibonacci sequence that appears often in nature. In plants, the Golden Angle determines the spiral phyllotactic angle, the arrangement of leaves and other organs in plants, like the beautiful arrangement of florets in a sunflower. In later lessons you will calculate the Golden Angle yourself using loops and use the value to model the growth of a sunflower.
# 
# What is theh Fibonacci sequence? We will learn more later, but it is a sequence of numbers where every number in the series is the sum of the previous two numbers.
# 
# In the cell below, the list `fibonacci` has the first 16 numbers in the series. Execute the cell to create the list and look it over, verifying that each number is the sum of the previous two.

# In[4]:


fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]


# In the cell below, use the `len()` function to verify there are 16 numbers in this list.

# In[5]:


# Put your answer here


# The Fibonacci sequence has numerous special mathematical properties. For example, every nth element of the series is divisable by the nth element. For example, the third element of the series is `2`. Every third element of the series should be even. The fourth element of the series is `3`. Every fourth element should be divisible by `3`.
# 
# In the last video, you learned about slicing and how to use a `step` value to select every nth element in a series.
# 
# Let's explore this interesting property of the Fiobonacci series!
# 
# **Do this:**
# 
# In the cell below, starting on the 4th element of the series, select every 4th number thereafter. What is the 4th element and are all the numbers you sliced divisible by it?
# 
# **Hint:** Remember, the first element of a list is indexed as 0 and the nth element in the list is not indexed as n!

# In[6]:


# Put your answer here


# Try it out for the 5th element of the series, and select every 5th number thereafter.

# In[7]:


# Put your answer here


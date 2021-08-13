#!/usr/bin/env python
# coding: utf-8

# # 3.3 Using Lists and Loops

# ## How to create an empty list outside of a loop and fill it with loop outputs
# ______

# ***Watch this video from 13:17 to 20:31***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=13, seconds=17).total_seconds())
end=int(timedelta(hours=0, minutes=20, seconds=31).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# Let's learn about creating an empty list outside of a loop and filling it with loop outputs.
# 
# Let's use the same for loop that we used before, range 0 to 12 step 2, and we have a counter just like we had before with plus equals i. What we're going to do instead now is we're going to create empty lists that are outside of the loop. Let's create one called `i_values`. It's initially going to be empty. Nothing is in it, just the empty square brackets like you learned before, and let's create one called `countup_values`. The idea is is that using the `.append()` function, which you learned before, if you add dot append to a list you can add the elements in the parentheses to the list that is specified. Let's add i to our `i_values` with each loop iteration and let's add the count up values of the counter to the list `countup_values` using append as well. And again we're going to print i and count up just to make sure that our loop is running.
# 
# So you can see from `print()` that the loop did run. We can also see that our counter did work but we had these lists that we created and these values should have been appended to the list with each loop iteration.

# In[2]:


# You can create an empty list outside of the loop to store variables
# Use the .append() function in the loop to append to a list outside

count_up = 0
i_values = [] # store i values here
countup_values = [] # store count_up values here

for i in range(0,12,2):
    count_up += i
    i_values.append(i) # append to list i_values
    countup_values.append(count_up) # append to list countup_values
    
    print(i, count_up) # always use print to make sure loop worked!


# So if we say print `i_values` you can see we have a list that contains the values of i because every time the loop ran it was appending i to the list i values. 

# In[3]:


print(i_values)


# And then let's look at our list `countup_values`, and it's the same thing: we appended the updated value of the counter to the list `countup_values` and it worked.
# 
# This is a good strategy that you can use loops for processing to compute and create new values based on i and then store the outputs into a list outside of the loop. 

# In[4]:


print(countup_values)


# We've been using the range function up until now but it's important to know that you can just use any list. The values of i don't necessarily have to be in sequence or have a start or end or a step like the `range()` function. You can just create a list, and then it says for each value in list, it will iterate over the values in sequence of that list.  
# 
# Remember the variable that we're using to denote the iterator. It can be anything that you want. So here we call it `val`. We're saying for val in the list of i values. And we'll just iterate over the list as if it were just indexing right over it.
# 
# We can just print. So the i value list was 0, 2, 4, 6, 8, 10 and that's what we get back.

# In[5]:


# You can provide the sequence of integers for a loop using a list
# From the previous loop, i_values was 0, 2, 4, 6, 8, 10

for val in i_values:
    print(val) # always use print to make sure loop worked!


# We can construct a loop from a list of values and we can do all the things that we just talked about, processing and storing. And what I mean by processing is that the iterator "i", "value", whatever you call it, whether you're iterating over range or if you're iterating over a list, for the same value of i or value you can do all sorts of different computations.  
# 
# Let's really max out all the mathematical things we could possibly think of. For example, let's store our values again in a list. Just to know what the values were, let's do some math. We're going to append to the list `multiply_2`, the value multiplied by 2. To the list of `exponent_2` outside of the loop we're going to append the value to the exponent 2. And remember that the way we denote exponents in python is with two asterisks. And let's create some really big numbers. Let's create a list called `exponent_val` and to that we're going to to append value to the power of value. We'll print value each time just to make sure that our loop is working.

# In[6]:


# We can construct a loop from a list of values

vals = [] # Store loop "val"s here
multiply_2 = [] # Store val*2 here
exponent_2 = [] # Store val**2 here
exponent_val = [] # Store val**val here

for val in i_values:
    vals.append(val) # append to vals
    multiply_2.append(val*2) # append to multiply_2
    exponent_2.append(val**2) # append to exponent_2
    exponent_val.append(val**val) # append to exponent_val
    
    print(val) # always use print to make sure loop worked!


# This list of i values, remember, was 0, 2, 4, 6, 8, 10. But now we have all of these lists: multiply 2, exponent 2, exponent val, and we want to check that they got processed correctly. So to check on those lists we should print them.
# 
# Let's add some abilities to the print function. You can use in quotation marks backslash n (`\n`) to create a line break for the `print()` function. You already know if we separate by a comma that will create a space. So we're going to say the values are, and then we're going to put the list `vals`, so we can see what the list of vals is. But then we're going to place a comma and we're going to say in quotation marks backslash n (`\n`) so this will create a line break so we can actually read some of these outputs. Next we're going to say val times 2 values are. So multiplied by 2, right? We're going to take the list `multiply_2` and put it after that comma. And then again a line break then we're going to say values to the exponent 2 are and put our list `exponent_2`. And then we're going to say vals to the exponent val values are and we're going to put our `exponent_val` list. And so using this backslash n (`\n`) you can see that we get these line breaks which really helps us read the outputs.

# In[7]:


# You can use "\n" as a line break for the print function

print("The vals are:", vals, "\n","val*2 values are:", multiply_2, "\n",
      "val**2 values are:", exponent_2, "\n", "val**val values are:", exponent_val)


# So the important thing to know is that, if you create these empty lists and then you iterate over range or over a list of values, and you mathematically process and use code, you can use these iterators in 
# very creative ways to do some very powerful functionalities in Python. In many ways loops are at the heart of programming because we're automating a process to process lots of things quickly and to create very large data sets. 

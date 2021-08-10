#!/usr/bin/env python
# coding: utf-8

# # Lesson 3.5

# ## How to write a `while` loop using a counter
# _____

# ***Watch this video from 26:29 to 30:40***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=26, seconds=29).total_seconds())
end=int(timedelta(hours=0, minutes=30, seconds=40).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# So that's all about `for` loops. Let's learn about one other major loop style today, which is the `while` loop, which is very much related to a counter.
# 
# You can read a for loop and it kind of makes sense as you use language. You can also use while in the same way, and it's basically saying "while" a value, let's call it counter is less than 25, run the loop.
# 
# So a while loop continues while the condition is true. Almost always a while loop has a Boolean statement. A  Boolean statement is a mathematical statement that is either `True` or `False`. There's no in between. These are very useful, especially because a while loop will run while the condition is true.  
# 
# So if we use our counter, let's set the counter initially equal to two, because we're going to initialize a Fibonacci list with two elements because we need to calculate the third. We're going to use that one line of code that we just made and we have been using to calculate the Fibonacci sequence and then when we're done with the code in our loop we're going to use plus equals to make the counter go to three, and then we're going to run the loop again, calculate the code, append the next element to our fibonacci list, the counter goes up by one again, and eventually the counter will equal 25. When it's 25 it will no longer be true that the counter is less than 25. And when that happens the counter, and the while loop, will not proceed further.  

# In[2]:


# A while loop continues WHILE the condition is TRUE
# A Boolean statement is either TRUE or FALSE

fibonacci = [0,1]
counter = 2

while counter < 25: # Loop continues one more time IF this is TRUE
    
    fibonacci.append(fibonacci[counter-2] + fibonacci[counter-1])
    
    counter += 1


# We can check the length of our Fibonacci sequence that we produced. Remember we have the first two elements and then we're going up to but not including 25, which seems like it's 24 but remember we're starting on index position 0. So going between 0 and 24 there should be 25 elements and that's the case.

# In[3]:


# Check length of the sequence
# We used < 25 starting on 0

len(fibonacci)


# And if we print out our Fibonacci sequence with 25 elements you can see again we get the Fibonacci sequence back. One is the sum of zero and one, two is a sum of one and one, three is the sum of one and two, five is the sum of two and three, and eight is the sum of three and five.

# In[4]:


# We get the Fibonacci sequence back

print(fibonacci)


# **So what did we learn?**

# **Python learning objectives**
# 
# * The `range()` function and how it produces a series of integers to iterate over in a loop
# * How to write a `for` loop
# * How to use the `+=` sign as a counter
# * How to create an empty list outside of a loop and fill it with loop outputs
# * How to use a `for` loop to calculate the Fibonacci sequence
# * How to write a `while` loop using a counter
# 
# **Plant learning objectives**
# 
# * Plants are computers!
# * They interatively produce outputs (like leaves and flowers), just like loops do
# * Modeling tries to recapitulate phenomena in nature. No model is perfect.
# * The Golden angle that plants use and we will calculate is based on computational mathematics
# * We will use sunflowers and the Golden angle as inspiration to learn from plants.

# # Thank you!

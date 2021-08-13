#!/usr/bin/env python
# coding: utf-8

# # 3.1 For Loops

# ## How to write a `for` loop
# ___

# ***Watch this video from 2:35 to 7:19***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=2, seconds=35).total_seconds())
end=int(timedelta(hours=0, minutes=7, seconds=19).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# Writing loops is easy. Writing loops is powerful.
# 
# To write a for loop you begin with the first line. It's very important to write this line exactly with the syntax as it's given here. You always start with `for` and then you create a variable. We often use "i", kind of like an index that you've used before, but you can call this variable anything you want. We say for "i" in and then we usually have either a sequence of integers that can be produced by the range function or we can even put in a list. We're saying "for i in range" or "a list" and we're going to iterate over the list or the `range()` function. This is important too: you need to end with a colon on the first line of your for loop. You say "for i in range" up to a certain number. Let's say 8 and colon. 
# 
# Next, if you press enter after this line, you're going to see that your code will now be indented. This is another important piece of syntax in writing a for loop. The code within the for loop needs to be indented. Within the for loop, as you'll see you can put anything that you want, the sky is the limit. Your code goes in the for loop and what the loop will do is iterate over values of "i". So what that means is "for i in" and the first value of range is going to be 0. So i is going to be set to 0. Any code you put within the loop using the variable i will be processed using i equals 0. After the loop completes with your code, it will go back up to the beginning of the loop again and i is going to be assigned the second value which will be one. And then when i is one we'll go through the code again, and go back up start the loop again. Next i equals two and we're going to keep on doing the loop for all the elements in range or a list.
# 
# If we execute this loop, pressing shift + enter, you can see we're printing i with each iteration. i is initially zero so it prints zero. Then i goes to one: it prints one. And it goes all the way up to seven. In this context we can see what the function of `range()` is. It's to produce a series of integers that we can iterate over in a for loop.

# In[2]:


# Writing for loops is easy!!!

for i in range(8): # First, say which values of "i" you would like to use

    # Your code using "i" goes here
    
    print(i)


# Remember that the `range()` function is just like slicing and indexing as you learned before. It has a start value and an end value and a step value. Remember always that in Python that the start is inclusive, for example this is going to start at negative eight, it's going to go up to but not including ten and it's going to do it in steps of two. If we say for i in this sequence of numbers it's going to start with -8, because the start is inclusive. It'll go back up to do a second iteration. If we're using step two, the next value of i should be negative six, and we should get a negative six. It will go all the way up to eight but not ten because it's going to go up to ten but not including it. So the last number with a step of 2 should be 8.
# 
# Let's see what we get for this loop. Indeed we start at negative 8, we have steps of 2 going all the way up to but not including 10. So the last number is eight.
# 
# You'll notice that I put a comment, which is to always use the `print()` function. As you'll see when your code gets more complicated, using `print()` allows you to see that your loop is running. It's good just to print i to make sure that the loop is actually processing. So that's your first for loop, the simplest for loop!

# In[3]:


# Remember, you can specify start (inclusive), stop (not inclusvie)
# and step with range, just like slicing and indexing!

for i in range(-8,10,2): # inclusive of start, but not of the end
    
    print(i) # always use print to make sure loop worked!


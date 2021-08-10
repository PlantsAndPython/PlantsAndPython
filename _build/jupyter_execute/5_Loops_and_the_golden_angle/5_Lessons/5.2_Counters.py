#!/usr/bin/env python
# coding: utf-8

# # Lesson 3.2

# ## How to use the `+=` sign as a counter
# ____

# ***Watch this video from 7:20 to 13:17***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=7, seconds=20).total_seconds())
end=int(timedelta(hours=0, minutes=13, seconds=17).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# Let's look at more tricks that we can use with for loops, including a plus equal sign as a counter. 
# 
# You can put a variable (or as you'll see very soon even a list) outside of a loop. You can then run your loop and you can modify the variable outside of the loop. And so the variable will be continually updated as it's modified every single time the loop runs. Something very common is to create a counter. For example, if you create a variable, let's call it `count up`, and you set it initially to zero, if you run your loop you could for example add i to the counter `count up` every single time the loop runs, so that every single time the loop runs i is going to be added to the counter. So the value of i is going to change. Even though it's initially set at zero, notice that you set it to zero outside of the loop then when you do your loop, the counter is going to be modified and it's basically ignoring what that initial value was so we can constantly modify the value of the counter as the loop runs. 
# 
# This is a little bit of trickery with respect to math because this is not a mathematically true statement, but it's important to know how it works. For example, here we have a `range()` function starting at zero going to 12 and steps of two. So this will go zero, two, four, six, eight, ten. The counter is initially set at zero and so in the first time the loop runs it will be zero. And then i is going to be zero, so count up will be set to zero again. In the second iteration, count up is still zero but now i will be two: so count up is still zero but now i is two, and so count up becomes two. We run the loop again, it will be four then. Now count up is 2 and we're going to add 4 to it and so now it will be 6. So basically this is saying whatever the counter was before we're going to modify it with i and we're going to reset it to that new value by adding i to it. And we're going to put in this for loop a statement where we print both i as well as the count up value, so we can track what the loop is doing.
# 
# And so you can see for range 0 through 12, step 2, it goes 0, 2, 4, 6, 8, 10, as we would expect. These are the values of i. Count up is initially zero then we add zero to zero and we're still at zero, but then in the next iteration i is set to two. So i was zero we add two to it and now the counter is two. In the next iteration the counter is at two but now i is four and so then the counter becomes six. In the next iteration then the i value becomes six we add it to the counter of six and we get twelve. And so on. So you can see that i is being added to the previous value of what the counter is currently but then it's updated every time we run the loop.

# In[2]:


# We can create a variable outside the loop and have it modified by the loop
# The variable can start at 0 and "count" every loop iteration

count_up = 0

for i in range(0, 12, 2):
    
    count_up = count_up + i
    
    print(i, count_up) # always use print to make sure loop worked!


# This notation is very handy, as you can see we basically created a counter. It keeps track of how many times our loop has run which is very convenient. Because it's so convenient, this whole notation (which as you know is not the best mathematically, because it's not technically equal) has a whole mathematical sign that people created for it, and it's called the plus equals sign (+=). You can just say count up "plus equals" i. Basically we're going to add i to whatever count up currently is to update the count up value. That's the only difference between these two different loops and if we execute this loop you can see that the outputs are the same. So plus equals is a way to update the current value of the counter and revise it every time the loop runs.  

# In[3]:


# The += sign is the same as adding "i" to the counter

count_up = 0

for i in range(0, 12, 2):
    count_up +=  i
    print(i, count_up) # always use print to make sure loop worked!


# Plus equals is the most commonly used version of this, but you can use all the other arithmetic. For example you can use minus equals instead. If you use minus equals you can see that i is being subtracted from the counter with each iteration.

# In[4]:


# You can use a -= sign too

count_up = 0

for i in range(0, 12, 2):
    count_up -=  i
    print(i, count_up) # always use print to make sure loop worked!


# You can do a multiply equals but you can see that it's not a very useful thing to do if you start with zero. If you start with zero what happens is that because the counter is zero any i that you multiply it by it keeps on going back to zero. So you don't see much activity on it.

# In[5]:


# Or you can use a *= sign
# But it's not useful starting at 0

count_up = 0

for i in range(0, 12, 2):
    count_up *=  i
    print(i, count_up) # always use print to make sure loop worked!


# But for example if you set the counter initially equal to one then you can see how every single time it is multiplied by i and it is updated.

# In[6]:


# Here is the *= sign starting on 1 

count_up = 1 # change to 1 to get results with *=

for i in range(1, 12, 2):
    count_up *=  i
    print(i, count_up) # always use print to make sure loop worked!


# And you can do also a divide equal and as you might imagine dividing by i with every iteration you quickly get a decreasing value that gets vanishingly small.

# In[7]:


# Or you can use a /= sign

count_up = 1 

for i in range(1, 12, 2):
    count_up /=  i
    print(i, count_up) # always use print to make sure loop worked!


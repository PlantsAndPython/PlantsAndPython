#!/usr/bin/env python
# coding: utf-8

# # Lesson 3.4

# ## How to use a `for` loop to calculate the Fibonacci sequence
# ____

# ***Watch this video from 20:31 to 26:29***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=20, seconds=31).total_seconds())
end=int(timedelta(hours=0, minutes=26, seconds=29).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# Let's look at how we can use the for loop to actually do something mathematically useful. Let's try to calculate the Fibonacci sequence.
# 
# If you remember every number in the Fibonacci sequence is the sum of the two values before it. If we're going to create the Fibonacci series it's important that we don't create an empty list initially, that we initialize it with two initial values. And the reason for this is because we need two values in order to compute the next. A lot of people start the Fibonacci sequence with one and one, so that the next value would be two. After that the next value is three, after that the next value is five. But you can also start the sequence with zero and one and because we start with zero for indexing in Python, maybe this makes sense and we'll do it this way for this loop.  
# 
# We have two elements in our list already, 0 and 1. We're going to say for i in range 2 to 10. It's important that we start on index position 2 because 2 is the next element of this series, the third element.
# 
# The next position of the series will be the sum of the two previous numbers. So let's create a variable. We're going to call it `two_previous`. We want the number that's two previous of the current number that we're on. So using indexing this would be the list of Fibonacci for i (which in the first iteration is going to be 2, remember) minus 2, because you want two previous of the current position. So at first this is going to be position 0 which is exactly what we want it to be. Then we'll create a variable called `one_previous` and it will be i minus 1. With an i initiating as two, if we subtract one we're going to have position one, which is exactly what we want as well. These will always give you the two previous or the one previous values.
# 
# The next value, or the new value of the Fibonacci sequence, will be the two previous value plus the one previous value. So we create the new value equal to two previous plus one previous. We append the new value to the list. Now when we go to the next value of i, because we have this new value, it will now be the one previous, and we'll always of course have the two previous, we'll add them together again and we'll append the new value.
# 
# Spend some time looking over this loop if you're having trouble understanding it. It's using all the concepts of index that you have learned before, except that it's doing it with this value of i and it's modifying the index value by -2 or -1 so that we can get the previous values, the two previous values to calculate the next value of the series. We add the next value of the series and our list grows and grows as i continues to go upward. Again we always print i just to make sure that the loop is working.
# 
# We can see that it did work. We wanted to start on the second index position, it does start at 2, and it goes up to but not including 10 up until 9.  

# In[2]:


# Let's use a for loop to calculate the Fibonacci sequence
# Each value in the Fibonacci sequence is the sum of the
# two values before it

# We need to initialize our list with two values,
# Because we need to add them together to calculate the next!

fibonacci = [0,1]

for i in range(2,10):
    
    two_previous = fibonacci[i-2]
    one_previous = fibonacci[i-1]
    new_value = two_previous + one_previous
    fibonacci.append(new_value)
    
    print(i) # always use print to make sure loop worked!


# We should check the length of our Fibonacci sequence. Let's make sure we got it right. Remember we start with two elements and then we range from two to ten. So this would be two, three, four, five, six, seven, eight, nine, which is eight elements, so 2 plus 8 should be 10. The length of our Fibonacci sequence should be 10 and it is. 

# In[3]:


# Check the length
# We started with two elements
# Then we range(2,10), so 8 elements more
# It should be 10
 
len(fibonacci)


# And finally let's check the Fibonacci sequence. One is the sum of zero and one, two is the sum of one and one, three is the sum of one and two, five is the sum of two and three, eight is the sum of three and five. So it looks like it is working. 

# In[4]:


# Let's check the sequence!

fibonacci


# I want to point out that you can always make your code more efficient but sometimes it helps to write out every single step first and then after writing out every single step then go back and try to see if you can make it more efficient.
# 
# So for example I'll do some cut and pasting to show you how this works. We have two previous is equal to this, one previous is equal to that, and new value is equal to two previous plus one previous. We could just directly calculate the new value using the two and one previous values (without storing them in variables first), but then you can see that we're just appending the new value to the Fibonacci sequence directly in one line of code.

# In[5]:


# You can always make your code more efficient

# After reducing the code

fibonacci = [0,1]

for i in range(2,10):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])


# You can see that we've reduced everything to just one line of code so we can execute and we can see, do we get the same result? And we do. We get the Fibonacci sequence back and you can see the we were just replacing the variables and reducing the lines in our code.
# 
# But you can always write out each step and sometimes that really helps a lot to try to figure out your way through code.

# In[6]:


# Same result with shortned code

fibonacci = [0,1]

for i in range(2,10):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

print(fibonacci)


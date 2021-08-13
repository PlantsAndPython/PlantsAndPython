#!/usr/bin/env python
# coding: utf-8

# # 2. Coding cells
# _____

# ***Watch this video from 3:33 to 9:51***

# In[1]:


# To load the video, execute this cell by pressing shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=3, seconds=33).total_seconds())
end=int(timedelta(hours=0, minutes=9, seconds=51).total_seconds())

YouTubeVideo("FrDYpLVuTkQ",start=start,end=end,width=640,height=360)


# ***The following is a transcript of the video.***

# You're going to learn all about how to create variables and how to code in the coming lessons, but let's just do some very simple code to just see how Jupyter works. Let's create code to calculate the area of a circle. Creating variables in Jupyter is easy, you just pick a name. Once you pick a name you use the equal sign to assign them a value. Values assigned to variables can either be strings of characters, they're called strings, or they can be numbers. Let's create a string of characters first. To create a string you always use quotation marks and let's set the value to `"pi_is_a_number"`. That is what our variable `pi` will be. Once you put your code in your cell, you need to execute the cell. You need to tell the cell to process the code that is in it. To execute a cell, all you do is you press shift + enter. You can see that a number appears saying that our cell has been processed and a new cell appears below.  

# In[2]:


pi = "pi_is_a_number"


# Maybe we want to double check that in fact `pi` is set to the value `"pi_is_a_number"` so we simply type `pi` alone and we press shift + enter and the output, what is returned to us by Jupyter, is `"pi_is_a_number"`. So we had set `pi` to that string. 

# In[3]:


pi


# Maybe, though, we really want `pi` to actually be a number. So we just write again `pi` equals 3.14159 and we press shift + enter again. We want to see has `pi` been assigned the correct value and it is now 3.14159.

# In[4]:


pi = 3.14159


# In[5]:


pi


# Notice that it's very easy for us to create a variable, but it's also very easy for us to write over a variable and notice too that the order that we execute cells matters. This will be important later when you're writing code, that the order that you execute the cells is the 
# code that you're executing and it affects the assignment of values to variables and that very much can affect your code. So order does matter.  
# 
# Let's create some more variables. Let's create a variable `r` for radius, set it equal to one. Something that's very important in coding is commenting. If you use the `#` any characters or writing after the hashtag will not be processed by Python. It's a convenient way to leave comments in your code and help guide you in the future of what your code actually means, so we should get in the into the practice of using comments often. Let's remind us what this variable was. We can say `# r is radius`. You can create multiple lines of code within one cell. Let's create another variable. We'll call it `A` for area. It matters whether something is lowercase or uppercase, so you have to keep track of that, and if this is the area of the circle, let's say that it is `pi` times `r` squared and notice that an asterisk, one asterisk, is for multiplication. Two asterisks is for exponents. So we can hit shift + enter. We have assigned the value to `r` and using `r` and `pi` we then have calculated `A`. So let's see what `A` is equal to and the area of our circle is equal to  3.14159, as we would expect.

# In[6]:


r = 1 # r is radius

A = pi*r**2


# In[7]:


A


# When you have code, it's really easy with variables to reassign their values and this way it's really easier to tinker with things and do calculations. That's one of the powers of coding. So let's give an arbitrary number with a complicated decimal to our radius and if we recalculate the area of the circle now we can see that it's a much more different and complicated number.

# In[8]:


r = 4.234678236728465724 # r is radius

A = pi*r**2


# In[9]:


A


# As you saw math is trivial and easy to do in python. `+` is to create a sum, `-` is to subtract, as you saw `*` is for multiplication, `/` is for division, as you saw `**` is for exponents. There's also things called Boolean statements in computing that are very important. Boolean statements can evaluate only to `True` or `False`. These are  statements that create conditions that can only be said to be `True` or `False`. For example, maybe we want to say that 3 is greater than or equal `>=` to pi. That is not true, because 3 is less than pi, but if we evaluate this statement it comes out as `False`.

# In[10]:


3 >= pi


# So if we now say a Boolean statement of 3 is less than or equal `<=` to pi,that statement will be `True`.

# In[11]:


3 <= pi


# And if we said 3.14159 is not equal `!=` to pi that statement is `False`<
# because 3.14159 is equal to pi. 

# In[12]:


3.14159 != pi


# We could say 3.14159 is double equal `==` to pi.  This is a computational way to say equals, because we're using just a single equal sign `=` to  assign variables, but here we really mean, is 3.14159 equal to pi, and that is a `True` statement.  

# In[13]:


3.14159 == pi


# You will also learn a lot about functions. You give inputs to functions and they give you outputs back. The simplest function is `print()`, which will simply give you back the value of a variable. So we can say `print(pi)` and we can see that the print function gives us back 3.14159 from the variable `pi`.

# In[14]:


print(pi)


# So that's about coding cells. You're going to learn a lot more about coding in the following lessons.

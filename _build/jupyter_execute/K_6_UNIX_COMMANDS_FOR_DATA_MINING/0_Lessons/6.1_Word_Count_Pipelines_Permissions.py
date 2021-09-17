#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F">6.1 Word Count, Pipelines & Permissions
# 
# ***Author:  Alejandra Rougon*** 
# 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# 
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >After completing this lesson you will learn how to:
# >
# >* Count characters, words and lines
# >* Create pipelines
# >* Change permissions
# 
# 
#  [![08.Word Count, Pipelines & Permissions](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide8.png?raw=true)](https://youtube.com/embed/bgznxzyqFsk "08.Word Count, Pipelines & Permissions")
# 
# 
# ## <p style="color:#2C6A7F"> `wc`
# 
# The `wc`command which stands for *word count* counts **characters**, **words** and **lines**. 
# 
# ```
# $ more amounts.txt
# 10
# 50
# 20
# 30
# ```
# 
# ```
# $ wc amounts.txt
#  4  4 12 amounts.txt
# ```
# The numbers mean amount of **lines**, **words**, and **characters** respectively. Four lines, four words and ... wait! why do we get 12 characters if we can only see 8? This is because the **new line** is also a character 👆
# You can specify lines with `-l`, words with `-w` and characters with `-c`.
# 
# ```
# $ wc -l amounts.txt
#  4 amounts.txt
# ```
# ## <p style="color:#2C6A7F"> Pipelines `|`
# Many times you may want to use the output of a command as the input to another command. That is called a pipeline and we can do that with a **pipe** `|`.
# 
# Now print the lines that contain a letter `e` in the file `allfruits` in alphabetical order. So first you have to find the lines with `grep` and then sort them in alphabetical order with `sort`. *Remember that `allfruits` is in  the folder `Documents` so you have to either change directory or write the path to it.*
# 
# ```
# $ grep 'e' /root/sandbox/Documents/allfruits
# pear
# orange
# melon
# ```
# If you want to add the previous output as an input of `sort` add `|` and then `sort`
# 
# ```
# $ grep 'e' /root/sandbox/Documents/allfruits | sort
# melon
# orange
# pear
# ```
# 
# 
# The `|` will take the output of one command to the next command. But what if you just want to perform two different commands? For example, change directory and then look for a string inside a file. In this case you can use a **semicolon** `;`
# 
# Now let's find out how many characters contain the words that have a `p` in the file toygenes.txt that is in the folder `Practice`. So first you have to go to the folder `Practice`, then look for the letter `p` with `grep` and take the output into `cut` to select only the column that has the words, and then count the letters with `wc`. 
# 
# 
# ```
# $ cd Practice ; grep 'p' toygenes.txt | cut -f 1 | wc -c
# 5
# ```
# 
# Indeed, the word `apple` contains  `5` characters and is the only word that contains a `p`. This will become very useful when we start mining biological data. 
# 
# 
# ## <p style="color:#2C6A7F"> `chmod`
# 
# In UNIX and UNIX-like systems all files and folders can have different permissions for the **user** [owner of the file]`u`, the **group** [specific users assigned by the administrator] `g` and **others** [anyone else] `o` and **all** [user, group and others]. This allows you to protect your files even from yourself.
# The different permissions are **reading** `r`, **writing** `w`, and **executing** `x`.
# To see the permissions of your files and folders in the `Documents` directory, change working directory `cd /root/sandbox/Documents` and then type `ls -l`
# 
# 
# ```
# $ ls -l
# total 5
# drwxr-xr-x 2 root root  2 Apr 10 21:35 Genomes/
# drwxr-xr-x 2 root root  6 Apr 24 18:22 Practice/
# -rw-r--r-- 1 root root 87 Apr 24 17:02 Readme.copy
# -rw-r--r-- 1 root root 64 Apr 23 21:03 Readme.txt
# -rw-r--r-- 1 root root 31 Apr 24 20:26 allfruits
# -rw-r--r-- 1 root root 70 Apr 23 14:49 contents.txt
# -rw-r--r-- 1 root root 31 Apr 23 20:52 fruitall.copy
# -rw-r--r-- 1 root root 31 Apr 23 20:47 new_fruitall
# ```
# 
# You can see how permissions are distributed in different positions in the following picture
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/22.Permissions.png?raw=true)
# 
# 
# The first position indicates if it is a **file** or a **directory**, the next three positions belong to the **user** [owner]. If she/he has reading, writing, and executing permissions you will see `rwx` if any of those permissions is not available it will be represented with a `-`. The three positions in the middle represent the permissions of the **group**, and the last three represent **others**, everyone else's permissions.
# 
# There are two different ways to change permissions. One is through **characters** and the other one is through numbers, which is called the **octal** mode.
# 
# ### Character mode
# In this mode  you can change permissions with symbols. Add `+`, remove `-`, specifies a permission `=`. For example:
# 
# * `chmod +r myfile.txt`  adds **read** permissions to **all**
# * `chmod g-w myfile.txt`  removes **write** permissions to the **group**
# * `chmod u+x myfile.txt` adds **execute** permissions to the **user**
# * `chmod u=rw, go=  myfile.txt` adds **read & write** permissions to the **user** and removes **read, write & execute** permissions to the **group & others**
# 
# ### Octal mode
# In the octal mode each permissions combination is represented by a number
# 
# | Number | Binary | Read [r] | Write [w] | Execute (x) |
# |:------:|:------:|:--------:|:---------:|:-----------:|
# | 0      | 000    |      ❌    |      ❌     |       ❌      |
# | 1      | 001    |      ❌    |      ❌     |      👍      |
# | 2      | 010    |      ❌    |     👍     |       ❌      |
# | 3      | 011    |      ❌    |     👍     |      👍      |
# | 4      | 100    |     👍    |      ❌     |       ❌      |
# | 5      | 101    |     👍    |      ❌     |      👍      |
# | 6      | 110    |     👍    |     👍     |       ❌      |
# | 7      | 111    |     👍    |     👍     |      👍      |
# 
# The permissions will be assigned by the number in the corresponding position. For example,
# 
# * `chmod 777 myfile.txt` will give all permissions to everyone
# *  `chmod 766 myfile.txt` gives all permissions [read, write & execute] to the **user** and **read & write** to the **group & others**
# *  `chmod 635 myfile.txt` gives **read & write** permissions to the **user**, **write & execution** to the **group**, and **read and execution** to **othrers**.
# *  `chmod 444 myfile.txt` allows everyone to read the file but removes **write & execution** permissions. **This is very useful in bioinformatics to protect your raw data from unintended corruption, even from yourself.**
# 
# Now let's see the permissions of the file `allfruits` and change them to all permissions to everyone. Then check again to see if the perrmisions have been changed correctly. 
# 
# 
# ```
# $ ls -l allfruits
# -rw-r--r-- 1 root root 31 Apr 24 20:26 allfruits
# $ chmod 777 allfruits
# $ ls -l allfruits
# -rwxrwxrwx 1 root root 31 Apr 24 20:26 allfruits*
# ```
# 
# The asterisk may appear in some configurations of `ls` to indicate it is an executable file.
# 
#     
# --------
# 🔑 **In this lesson you have learned to:**
# 
# * Count characters, words and lines with `wc`
# * Create pipelines  with `|`
# * Change permissions with `chmod`
# 
# 

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 5.5 Copy, Move & Remove Files
# 
# ***Author:  Dr. Alejandra Rougon*** 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >After completing this lesson you will learn how to:
# >
# >* copy files and folders
# >* move files and folders to a different location
# >* remove files and folders
# >* use wildcards to select multiple files
# 
# 
# 
# 
#  [![06.Copy Move and Remove Files](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide6.png?raw=true)](https://youtube.com/embed/tab0cbwOACQ "06.Copy Move and Remove Files")
# 
# 
# ## <p style="color:#2C6A7F">`cp`
# The command `cp` is used for copying files and folders. You can use it in different ways. 
# 
# * to copy a file to the same location with a different name  `cp file file.copy`
# * to copy a file to a different location with the same name  `cp file new/location/file`
# * to copy a file to a different location with a different name  `cp file new/location/file.copy`
# 
# In the previous examples we copied a file that was in our working directory. You can also copy from another location if you specify the path. 
# 
# * copy from location A to location B  `cp /location/A/file /location/B/file`
# * copy from location A to the current working directory  `cp /location/A  .`
# 
# The current working directory is represented by a dot `.`
# 
# Now let's try it in your [Virtual Terminal](https://bit.ly/3d9BRCG) You can also  go back to the terminal you have been working in at the CS50 Sandbox [https://sandbox.cs50.io/](https://sandbox.cs50.io/) in the tab *recent sandboxes*.  
# 
# 
# First, go to your home directory, which is `/root/sandbox/`. You can do it with `cd`. Then copy the file `fruitall` to the folder `Documents`, and verify it has been copied. Change your working directory with `cd Documents` and then list the contents. You should see the file `fruitall`.
# 
# ```
# $ cd
# $ fruitall Documents
# $ cd Documents
# $ ls
# Genomes/  fruitall
# ```
# Now copy the file `fruitall` to the same location with another name `fruitall.copy` and again verify it afterwards.
# 
# ```
# $ cp fruitall fruitall.copy
# $ ls
# Genomes/ fruitall fruitall.copy
# ```
# Remember you can also check the directory contents in the file browser in the left side of your virtual terminal labeled as filetree. Now that we are in the `Documents` folder, let's copy from our home directory to the `Documents` folder, which is now our working directory. 
# 
# We have to specify the location of the file we want to copy. We can do that using either the **relative** or the **absolute** path. I will use the relative path. Remember that two dots `..` refer to one folder backward, in other words, the folder containing our current folder.  If we want to keep the same name, we can just specify the location, which in this case is our working directory and can be specified with a dot `.` 
# 
# ```
# $ cp ../Readme.txt .
# ```
# 
# We can also copy the same file but with a different name `Readme.copy`
# 
# ```
# $ cp ../Readme.txt ./Readme.copy
# ```
# Remember that cp will keep the original file. If you don't want to keep the original file you can use `mv`.
# 
# ## <p style="color:#2C6A7F">`mv`
# The command `mv` will **move** your file either to another location or to the same location but with a different name. It won't keep the original file. Let's move the file `contents.txt` from your home directory to `Documents`.
# 
# ```
# $ mv ../contents.txt .
# ```
# 
# In case you want to use the absolute path remember you can print the path of the working directory with `pwd`. Now, move the file fruitall from your home directory to `Documents` but with a different name `allfruits`.
# 
# ```
# $ pwd
# /root/sandbox/Documents
# $ mv /root/sandbox/fruitall allfruits
# $
# ```
# 
# The original file `fruitall` has been removed and we have a copy of it in the `Documents` folder called `allfruits`.
# 
# Now, use the command `mv` to change the name of `fruitall` to `new_fruitall`. You can verify it with `ls`.
# 
# ```
# $ mv fruitall new_fruitall
# $ ls
# Genomes/  Readme.copy  Readme.txt  allfruits  contents.txt  fruitall.copy  new_fruitall
# $
# ```
# ## <p style="color:#2C6A7F">`rm` & `rmdir`
# The command `rm` and `rmdir` are used to remove files and folders respectively. Note that in order to remove a folder, it has to be empty. Now, let's clean up our home directory. First, make sure you are in your home directory. Then list the contents to see which files we want to erase. Remove the file `fruit1`.
# 
# ```
# $ cd
# $ pwd
# /root/sandbox
# $ ls
# Documents/  Readme.txt  fruit1  fruit2
# $ rm fruit1
# rm: remove regular file 'fruit1'?  y
# 
# ```
# The virtual terminal is configured to ask you if you want to remove the file. And you can confirm it with the letter `y`. However, most terminals won't ask anything and will just remove the file immediately. 
# 
# Now, if we want to remove several files at the same time, we can use **wildcards**. They are used to perform actions on more than one file at a time, or to find part of a phrase in a text file. At the moment we will see the wildcard asterisk or star `*`, which represents any number of characters. For example, `ls gen*`  will be able to list the files `gen` `gen1` `genA.txt` `genes_prot` and `genomes`. You can also use `*` to find all files with an specific extension, such as `.pdf`.
# 
# ```
# $ ls *.pdf
# my_paper.pdf summary.pdf
# ```
# 
# Now, let's remove the two files that start with the string `fruit`
# 
# ```
# $ ls
# Documents/   fruit1  fruit2
# $ rm fruit*
# $ ls
# Documents/
# ```
# 
# ----------
# 🔑 **In this lesson you have learned how to:**
# 
# * copy files and folders `cp`
# * move files and folders to a different location `mv`
# * remove files and folders `rm` & `rmdir`
# * use wildcards to select multiple files  `*`
# 
# 

# In[ ]:





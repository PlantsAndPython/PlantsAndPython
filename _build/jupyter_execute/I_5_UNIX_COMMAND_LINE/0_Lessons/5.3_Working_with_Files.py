#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F"> 5.3 Working with Files
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >After completing this lesson you will learn:
# >
# > * Output redirection `>` & `>>`
# > * Create, write, view and concatenate files with `cat`
# > * View file contents with `more`, `less`, `head`, and `tail`
# 
# 
# 
# 
# 
#  [![04. Working with Files](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide4.png?raw=true)](https://youtube.com/embed/oRmLSaVD3h8 "04. Working with Files")
# 
# For this lesson go to your Virtual Terminal at the CS50 sandbox [https://sandbox.cs50.io/](https://sandbox.cs50.io/).
# 
# 
# Some commands give an output that is printed on the command line screen by default. We can redirect that output to a file with the `>` character. The syntax is `command > file_name`. If the file doesn't exist it will be created. But if the file already exists **it will be overwritten**, so you have to be careful and make sure you don't overwrite a file by mistake. 
# Let's  try it with the command `ls` that lists the directory contents.
# 
# First go to your home directory with `cd`. Then if we just type `ls` it will print the contents of the current directory.
# 
# ```
# $ ls
# Documents/ Readme
# ```
# The output goes to the screen. Let's send the output to a file called `contents.txt`. Remember the syntax `ls > filename`.
# 
# ```
# $ ls > contents.txt
# ```
# This time no output will be printed to the screen. We can verify it by clicking in the file `contents.txt` in the *Filetree* section and  the file will be opened  in the *Editor* section. We can see the two lines of output being saved and also a third line with the name of the file.
# 
# <img src="https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/12.Files.Redir.png?raw=true" width=300\>
# 
# If we want to redirect the output to a file that already exists without overwriting the previous content we use `>>` and then the filename. And we can see how the new lines were appended to the end of the file. 
# 
# <img src="https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/13.Files.Append.png?raw=true" width=300\>
# 
# ## <p style="color:#2C6A7F">`cat`
# The `cat` command has different functions
# 
# * Create a file
# * Write into a file
# * View the contents of a file
# * Add text to an existing file
# * Concatenate files
# 
# 
# Let's create a file called `fruit1` so  you have to type  
# 
# ```
# cat > fruit1
# ```
# 
# Then you will be able to type the contents. After writing the file contents, you can save changes and exit by pressing the keys `Ctrl` and `d`.
# 
# ```
# pear
# mango
# ```
# 
# Type Ctrl + d to save changes and exit
# 
# 
# To view the contents of the new file just type `cat fruit1` and you will see the contents on the screen.
# 
# ```
# $ cat fruit1
# 
# pear
# mango
# ```
# 
# Now append `orange` in another line to `fruit1`
# 
# ```
# $cat >> fruit1
# orange
# 
# # Ctrl + d to save and close
# ```
# 
# Visualize `fruit1` contents
# 
# ```
# $ cat fruit1
# pear
# mango
# orange
# ```
# Now create another file `fruit2`
# 
# ```
# $ cat > fruit2
# banana
# melon
# 
# #Ctrl + d
# ```
# 
# To **concatenate** files [merge them one after the other] you have to put them in the order you want them to be appended. The output will go to the screen but you can also redirect it to a new file.
# 
# ```
# $ cat fruit1 fruit2
# pear
# mango
# orange
# banana
# melon
# ```
# 
# ```
# $ cat fruit1 fruit2 > fruitall
# ```
# 
# ## <p style="color:#2C6A7F">`more`
# The function of the command `more` is to view file contents. 
# 
# So view the file `fruitall` with `more`
# 
# ```
# $ more fruitall
# pear
# mango
# orange
# banana
# melon
# ```
# As you can see, the output goes to the command line screen.
# 
# ## <p style="color:#2C6A7F">`less`
# Another command to view file contents is less. This one is particularly helpful in bioinformatics since you can visualize huge files without collapsing your computer. *If you try to open a 50 Gb file in a normal text editor, it will freeze your screen due to lack of memory*. Let's view the file `fruitall`.
# 
# ```
# $ less fruitall
# ```
# 
#  This command will show the contents in a different screen. If your file cannot fit one screen you can go through it with the arrows or the space bar. To go back to the command line type `q`.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/14.less.png?raw=true)
# 
# ## <p style="color:#2C6A7F">`head` & `tail`
# These two commands will also show you the file contents to the screen. However, `head` will only show you the top lines. By default, the first 10, unless you specify otherwise. On the contrary, `tail` will only show you the bottom lines. In order to specify a different number of lines you can use the option `-n`.
# 
# ```
# $ head -n 2 fruitall
# pear
# mango
# $ tail -n 2 fruitall
# banana
# melon
# $
# ```
# 
# ---------
# 
# 🔑 **In this lesson you have learned**
# 
# > * Output redirection `>` & `>>`
# > * Create, write, view and concatenate files with `cat`
# > * View file contents with `more`, `less`, `head`, and `tail`
# 
# 

# In[ ]:





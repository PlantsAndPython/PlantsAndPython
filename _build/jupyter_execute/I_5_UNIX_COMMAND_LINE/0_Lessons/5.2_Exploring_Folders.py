#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 03. Exploring Folders
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# 
# 
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >
# >After completing this lesson you will learn to: 
# >
# > * Identify the hierarchical file architecture
# > * Print working directory
# > * Change directory
# > * Use absolute and relative paths
# > * Create directories
# > * Tab completion  ↹
# 
# 
# 
#  [![03.Exploring Folders](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide3.png?raw=true)](https://youtube.com/embed/HPDGwi95r78 "03. Exploring Folders")
# 
# ## <p style="color:#2C6A7F">`pwd`, `cd`, `ls`, `mkdir`
# 
# Linux directory or folder structure is **hierarchical**, and referencing directories is accomplished by using the sequentially deeper directory name connected by forward slashes `/`. For example, in the following picture the folder `project1` is inside `my_docs` which is at the same time, is inside the folder `home`. To reference its location we use `/home/my_docs/project1. This location reference is called a **path**.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/01.01.path.png?raw=true)
# 
# There is a symbol called **prompt** that appears in the terminal when the system is ready for a new request. Depending on the shell that you are using, your prompt symbol will vary. For example, for **bash**, the prompt is a dollar sign `$` and for **zsh** the prompt is a per cent sign `%`. If you are logged in as **root**, which is the main **system administrator**, you will have a hash `#` as a prompt. 
# Now, let's go again to your Virtual Terminal at the [CS50 sandbox](https://sandbox.cs50.io/). First we need to know in which folder are we standing. What is the path to our current **working directory**? And for that, we use the command `pwd` in our terminal. So, type the following (Remember that you don't have to type in the `$` since it is the command prompt that is already in your terminal).
# 
# 
# **Note:** If at any time your command line gets stuck and you are not able to type anything in just press `Ctrl` `c` and  whatever you where doing will be canceled. 
# 
# ```
# $ pwd
# ```
# and the output is the path to your current working directory
# 
# ```
# /root/sandbox
# ```
# Now, let's **change directory**.  In order to move to a directory which is inside the directory you are working in, in other words, in order to move to a directory that is forward, you have to type the command `cd` space and the directory's name.
# 
# ```
# $ cd Documents
# ```
# and now verify it with `pwd`
# 
# ```
# $ pwd
# /root/sandbox/Documents
# ```
# Now your working directory is `Documents`. If you want to move one folder backward, that is to say, the directory that contains your working directory, you have to type `cd ..`.
# 
# ```
# $ cd ..
# $ pwd
# /root/sandbox
# ```
# In linux, we can reference a file or folder location, either, through an **Absolute** or a **Relative** path. Imagine that you want to give a friend the instructions to get from your home to the supermarket. So, you start, 'go straight, then in the traffic lights turn left, and in the lamppost turn right and you will reach the supermarket'. This would be similar to the absolute path, which starts from the **first directory** on your system that is called **root** and it is represented by a `/`.
# 
# Now imagine that your friend is lost and calls you from the lamppost. You won't give her the same directions. You will start from the lamppost and not from your home. So you will probably say, 'turn right and you will reach the supermarket'. That would be similar to a **relative** path which starts from your **working directory**.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/01.02.AbsolutePath.png?raw=true)
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/01.02.RelatPath.png?raw=true)
# 
# Now let's move backward to the folder named `root`, using the **absolute path**
# 
# ```
# $ cd /root
# $ pwd
# /root
# ```
# Now move to the system's root directory which is the first directory of your system.
# ```
# $ cd /
# $ pwd
# /
# ```
# Now let's type `ls` to list the directory contents
# 
# ```
# $ ls
# bin/   dev/  home/  lib32/  media/  opt/   root/  sbin/  src/  sys/  usr/  
# boot/  etc/  lib/   lib64/  mnt/    proc/  run/   snap/  srv/  tmp/  var/
# ```
# 
# Go back to your home directory, which is usually the directory that has your user name. In the virtual terminal it is `/root/sandbox/`
# 
# ```
# $ cd
# $ pwd
# /root/sandbox
# ```
# 
# List the contents of your home folder (or sandbox)
# 
# ```
# $ ls
# Documents/  Readme.txt
# ```
# 
# Go to `Documents` and create a new folder inside `Documents` called `Genomes`
# 
# ```
# $ cd Documents
# $ mkdir Genomes
# ```
# 
# Go to the `Genomes` folder with the `TAB` key  ↹
# 
# ```
# $ cd TAB
# $ cd Genomes
# 
# ```
# ----------
# 🔑 **In this lesson you have learned:**
# 
# * The hierarchical architecture of linux folders
# * `pwd`	 command for printing working directory
# * `cd`	command for changing directory
# * Absolute and relative paths
# * `mkdir`	command for creating directories
# * `ls`  command for listing directory contents
# 
# 
# 

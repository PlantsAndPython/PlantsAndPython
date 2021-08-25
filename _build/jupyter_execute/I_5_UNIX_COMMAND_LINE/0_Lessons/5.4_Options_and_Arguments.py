#!/usr/bin/env python
# coding: utf-8

# 
# 
# # <p style="color:#2C6A7F"> 05. Options and Arguments
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# 
# 
#  [![05. Options & Arguments](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide5.png?raw=true)](https://youtube.com/embed/KI7YtuHAGUU "05. Options & Arguments")
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >After completing this lesson you will learn:
# >
# > * Command Options
# > * Command Arguments
# > * How to add comments
# > * Access commands manuals through `man`
# > 
# 
# We can modify command behavior using **options** and **arguments**. For example the command `mkdir` needs the name of the folder that you want to create. The name of the folder is the argument. Each argument is generally separated by a **space**  `mkdir new_folder`. That is why you should **avoid spaces** in the names of files and directories. You should also avoid other symbols, as they have special meanings in the bash terminal. **Underscore** `_` and **dot** `.` are acceptable symbols to be used in file and folder names. Commands can have more than one argument. For example to concatenate three files we need the name of three files 
# 
# ```
# $ cat file1 file2 file3  #three arguments
# ```
# 
# >**Note** If you see a `#` symbol in the command line or in a bash script (*program*) it means there is a comment unless it is followed by an exclamation mark `#!` at the beginning of a script. In this case it is used to indicate the path to the correct interpreter for a script `#!/bin/bash`  or `#!/bin/python`. Comments are used for explaining code only for your information. In the previous example, you don't have to type in what comes after the `#` in the command line as it won't be executed. 
# 
# Some arguments are **compulsory**. For example `head file.txt` to indicate the file that head will read or `mkdir Folder.txt` to indicate the name of the folder to be created. Other arguments are **optional**.  The command `ls` will list the current directory contents unless we specify a particular folder. Thus `ls Documents` will list the contents of the folder `Documents`.
# 
# Commands also have **options**. Options are usually indicated with a hyphen (dash) or two  `-v` or `--version`. Usually a single dash is followed by a letter and double dash by a whole word. In order to learn about the different options of a particular command you can check out the **manual** that can be accessed with the command `man` and the name of the command you want to learn about. Let's go to your terminal and look at the manual of the command `ls`.
# 
# ```
# $ man ls 
# ```
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/14.manls.png?raw=true)
# 
# The manual will appear on another screen. To quit the manual just type `q`.
# 
# There are many commands and they have many options. You don't have to worry to learn them all as you will only use a few commands and a few options. For example, here are some useful options for `ls`. Try them all to see how they work. 
# 
# * `ls -a` lists **all** files and folders including hidden ones which start with `.` or `..`
# * `ls -l` includes **long description**. [file/directory, permissions, number of items, ownership, group, file size, modification date, file name]
# * `ls -h` used with `-l` shows the file size in a **human readable** way representing bytes, kilobytes, gigabytes, terabytes, etc with B, K, G, and T respectively.
# * `ls -p` adds a `/` at the end of  every folder name.
# *  `ls -t` the list is printed in order of time creation. 
# * `ls -r` used with `-t` the list is printed in **reverse order** from oldest to newest. 
# 
# Some options can be used together. There are two ways of writing them `ls -lhtrp` or `ls -l -h -t -r -p`.
# 
#     
# ---------
# 🔑 **In this lesson you have learned**
# 
# > * Command Options
# > * Command Arguments
# > * How to add comments
# > * Access commands manuals through `man`
# 

#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F">6.0 EDIT, SORT, CUT & GREP
# 
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
#  
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >After completing this lesson you will learn how to:
# >
# >* Edit files in the command line
# >* Sort file contents alphabetically or numerically
# >* Cut columns from files
# >* Look for specific strings inside files
# 
#     
#  [![07.Edit, sort, cut & grep](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide7.png?raw=true)](https://youtube.com/embed/o7k4Z_enMd0 "07.Edit, sort, cut & grep")
# 
# You have already learn how to create a file with `cat > New_file`, however, `cat` is not a text editor. There are several text editors for the command line. The most common ones are `vi`, `vim` and `nano`. In your virtual terminal you have a text editor with a graphical interface. However, when you work remotely on a bioinformatics computer cluster for **High Performance Computing [HPC]** you may not be able to use any graphical interface software. So it is very important that you learn how to use **text editors in the command line**. 
# 
# ## <p style="color:#2C6A7F"> `vim` & `vi`
# The text editors `vim` and `vi` are very similar. We will learn the most important commands for `vim` and they will also work for `vi`. However, if you want to learn more options you can check the [vim documentation](https://vimhelp.org/).
# 
# * Create file `vim Name_Of_File`
# * Edit file `i` which stands for *insert*
# * Save file and quit `Esc` `:wq!`
# * Quit without saving `Esc` `:q!`
# 
# Now let's create a folder inside the folder `Documents` named `Practice`. Then go inside `Practice` and create a file called `numbers.txt`
# 
# ```
# $ cd /root/sandbox/Documents
# $ mkdir Practice
# $ cd Practice
# $ vim numbers.txt
# ```
# You will enter a new screen 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/15.vimscreen.png?raw=true)
# Then you have to type `i` in order to be able to **insert** text. Now enter the following text:
# 
# ```
# 1
# 3
# 2
# 12
# ```
# Once you finish editing your file you have to save it and quit with the key `Esc` followed by `:wq!` and `Enter`.
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/16.vimSave.png?raw=true)
# 
# you can check the contents with `less`, `more`or `cat`. **Note:** *Don't add a `>` when opening your file, otherwise you will erase previous contents and overwrite them.*
# 
# ```
# $ cat numbers.txt
# 1
# 3
# 2
# 12
# $ 
# ```
# ## <p style="color:#2C6A7F"> `nano` 
# The advantage of using `nano` is that you don't have to learn the menu, as it is shown on the screen. The key `Ctrl` is specified by a caret `^`. The problem is that `nano` sometimes is not installed in servers. So you may have to install it. 
# 
# * Create file `nano Name_Of_File`
# * Save file `Ctrl` + `o` `Enter`
# * Quit `Ctrl` `x`
# 
# Let's create the file called `toygenes.txt` in the same folder `Practice`.
# 
# ```
# $ nano toygenes.txt
# ```
# Then you will see the following screen where you can edit your file. 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/18.nano.png?raw=true)
# 
# This time we will write a **tabular** file. That means our file will have **columns** and we will separate the columns with a `tab` using the  `tab` key instead of the `space bar`. Write the following contents (using one `tab` after each name):
# 
# ```
# fly	20	
# apple	10
# bear	40
# tomato	30
# ```
# 
# To save [*write out*] your file type in `Ctrl` `o`.
# Then, you will see this screen
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/19.NanoSave.png?raw=true)
# 
# Just press `Enter` and then quit with `Ctrl` `x`
# Remember to verify that the file is correct.
# 
# ## <p style="color:#2C6A7F"> `sort`
# 
# The `sort`command is used to **sort** a file, in other words, arranging the records on a list in a particular order. By default it gets sorted in **alphabetical order**.
# 
# Try it with the file `toygenes.txt`
# 
# ```
# $ sort toygenes.txt
# apple   10
# bear    40
# fly     20        
# tomato  30
# ```
# `sort` will also sort numbers in **alphabetical** order by default. So in order to sort numbers **numerically** we need de option `-n`.
# 
# ```
# $ sort numbers.txt 
# 1
# 12
# 2
# 3
# $ sort -n numbers.txt 
# 1
# 2
# 3
# 12
# $ 
# ```
# 
# If you have a mixsure of letters and numbers you can use the option `-V` to sort **numerically** as in software **version** names. As in the following example.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/20.sortV.png?raw=true)
# 
# Now create a file called `amounts.txt` with the following content:
# 
# ```
# 10
# 50
# 20
# 30
# ```
#  You can use whatever text editor you prefer.
#  
#  The `sort` command has several useful options. If you want to reverse the order use `-r`
# 
# ```
# $ more amounts.txt 
# 10
# 50
# 20
# 30
# $ sort -r amounts.txt 
# 50
# 30
# 20
# 10
# $ 
# ```
# You can also sort a file specifying a particular column with `-k`. For example let's sort `toygenes.txt` based on the second column. 
# 
# ```
# $ more toygenes.txt
# fly	20	  
# apple	10
# bear	40
# tomato	30	
# ```
# 
# ```
# $ sort -k 2 toygenes.txt
# apple	10
# fly	20
# tomato	30
# bear	40
# ```
# You can also sort a file and remove duplicates in order to get only the **unique** records with `-u`. For example try it with the following file.
# 
# ```
# $ more species.txt
# fly
# fly
# apple
# apple
# apple
# bear
# tomato
# ```
# 
# ```
# $ sort -u species.txt
# apple
# bear
# fly
# tomato
# ```
# Remember that you can always save your results by redirecting the output with `>`to a new file.
# 
# ```
# $ sort -u species.txt > sortunique.txt
# $ more sortunique.txt
# apple
# bear
# fly
# tomato
# ```
# You can also sort months in order with `sort -M`.
# 
# ```
# $ more months.txt
# March
# January
# February
# April
# ```
# 
# ```
# $ sort -M months.txt
# January
# Febrary
# March
# April
# ```
# 
# ## <p style="color:#2C6A7F"> `cut`
# 
# The `cut`command will cut specific columns that are separated by a `tab` by default. You can specify the column with `-f`, which stands for **field**. Select the second column for the file **toygenes.txt**
# 
# ```
# $ more toygenes.txt
# fly	20
# apple	10
# bear	40
# tomato	30
# ```
# 
# ```
# $ cut -f 2 toygenes.txt
# 20
# 10
# 40
# 30
# ```
# to change the delimiter use `-d`. For example, for a list that has columns separated by a space
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/21.CutSpace.png?raw=true)
# 
# You can also select columns specifying the byte position with `-b`. To see more options, remember that you can always check the manual `man cut`.
# 
# ## <p style="color:#2C6A7F"> `grep`
# 
# One of the most useful commands is `grep` which allows you to look for strings. It will print only the lines that contain the string that you have indicated. For example, let's look for the string `tomato` in the file `toygenes.txt`
# 
# ```
# $ more toygenes.txt
# fly     20        
# apple   10
# bear    40
# tomato  30
# ```
# 
# ```
# $ grep 'tomato' toygenes.txt
# tomato  30
# ```
# You can also look for the **inverse** of the string with `-v`. It will show you the lines that don't contain the string.
# 
# ```
# $ grep -v 'tomato' toygenes.txt
# fly     20        
# apple   10
# bear    40
# ```
# 
# You can also count the **number of ocurrences of a string** with `-c`. How many lines contain a letter `a` in  `toygenes.txt`?
# 
# ```
# $ grep -c 'a' toygenes.txt
# 3
# ```
#     
# --------    
# 🔑 **In this lesson you have learned how to:**
# 
# * Edit files in the command line with `vim`, `vi` & `nano`
# * Sort file contents alphabetically or numerically with `sort`
# * Cut columns from files with `cut`
# * Look for specific strings inside files with `grep`
# 

# In[ ]:





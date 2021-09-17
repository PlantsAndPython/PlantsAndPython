#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F">7.1 Scripting with Bash
# 
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
#  
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >After completing this lesson you will learn:
# >
# >* What is a bash script
# >* The basics of bash scripting
# >* How to use variables in bash
# >* How to make a for loop in bash
# 
# 
# Sometimes you may need to run the same command or the same series of commands on many files. Or you may want to look not only for a string but for a list of strings, or iterate over some commands a number of times. In these cases, you can write **scripts** in bash, just like in other programming languages (e.g. python, perl). A script is a program that will be executed by an interpreter. In this case the interpreter will be bash. It doesn't have to be compiled as programs written in other languages (e.g. C, C++).
# 
# The simplest script would be to print to the screen `Hello world!`. Let's create a folder called `Activity` in the folder `Documents` and just create the following file and run it with `sh`. 
# 
# ```
# $ cat > helloworld.sh
# echo Hello world!
# 
# $ sh helloworld.sh
# Hello world!
# ```
# 
# ### <p style="color:#2C6A7F"> Good practices
# 
# It is a good practice to add the extension `.sh` to bash scripts. It is also a good practice to add a `#!` in the first line followed by  the path to bash. In that way you can also run it by making it executable and without the command `sh`. And finally it is also recommended to add comments that explain your code. You can also add empty lines where needed so it looks neat. So our first bash script could be improved like this.
# 
# ```bash
# 
# #!/bin/bash
# 
# # This is my first script and will 
# # print Hello world! to the screen
# 
# echo Hello world!
# 
# ```
# 
# And now you can run it either with
# 
# ```sh helloworld.sh```<br>
# 
# or with<br>
# 
# ```chmod +x helloworld.sh```<br>
# ```./myfirstscript.sh```<br>
# 
# If you want to run a series of commands sequentially only add the next command in the following line.
# 
# 

# ```bash
# #!/bin/bash
# 
# # This is my first script and 
# # will print Hello world! to the screen
# 
# echo Hello world!
# echo This is my first file
# echo It is stored in the following path
# pwd
# 
# ```
# 
# ```
# $ sh helloworld.sh 
# Hello world!
# this is my first file
# it is stored in the following path
# /root/sandbox/Documents/Activity
# ```

# 
# ### <p style="color:#2C6A7F"> Variables
# 
# A **variable** in bash shell scripting, as in other programming languages, is a memory location that is used to contain a number, a character, a string, etc. The most commonly used data type of variables are integer (46), string (apple), float (0.24), and boolean (FALSE). The data type of any variable has to be defined when the variable is declared for strongly type programming languages. However Bash is a weakly typed or loosely typed programming language and there is no need to define a data type.
# 
# Variables are declared with the `=` sign, and are called with the `$` sign.
# 
# ```
# $ a=apple
# $ echo $a
# apple
# 
# ```
# It is recommended to add quotes. Single and double quotes have different meaning.
# 
# Double quotes are also called "weak quotes". If you store a variable and you call it with double quotes it will give you the contents stored in the variable.
# 
# ```
# $ a=apple
# $ b="Value of a is $a"
# $ echo $b
# Value of a is apple
# ```
# 
# Single or 'strong quotes' will give you a literal interpretation.
# 
# ```
# $ a=apple
# $ b='Value of a is $a'
# $ echo $b
# Value of a is $a
# ```
# when you are not calling a variable or you are not using regular expression it doesn't make any difference to use single or double quotes.
# 
# ```
# a='apple'
# ```
# or
# 
# ```
# a="apple"
# ```
# 
# Let's create a script called `variable.sh` 
# 
# ```bash
# #!/bin/bash
# 
# #This script prints Hello world! 
# #to the screen and uses a variable.
# 
# Greet='Hello world!'
# echo "$Greet"
# ```
# ```
# $ sh variable.sh
# Hello world!
# ```
# 
# ### <p style="color:#2C6A7F"> Loops
# In order to iterate over commands we can use loops. The **for loop** is represented in the following examples:
# 
# ```bash
# for variable in 1 2 3 4 5 .. N
# do
# 	command1
# 	command2
# 	commandN
# done
# ```
# 
# ```bash
# for variable in file1 file2 file3
# do
# 	command1 on $variable
# 	command2
# 	commandN
# done
# ```
# Let's create a greetings script with a for loop. Now instead of printing `Hello world!` let's print a greeting for each continent.
# 
# ```bash
# #!/bin/bash
# 
# #This script prints a greeting for each continent. 
# 
# continents="Africa Americas Antartica Asia Australia Europe"
# 
# for item in $continents
# do
#   echo "Hello $item" 
# done
# 
# ```
# 
# 
# The variable <font color="#2C6E3B"> continents </font> contains 6 items `Africa` `Americas` `Antartica` `Asia` `Australia` `Europe`. In the for loop the variable <font color="#9E3147"> item </font> will go through each one of the items of the variable <font color="#2C6E3B"> continents </font>, called with <font color="#2C6E3B"> $continents </font>.
# 
# Each one of them will be printed on each cycle of the loop with `echo` as they are being called with <font color="#9E3147">$item </font> on each iteration.
# 
# 
# 
# ```
# $ sh hellocontinents.sh 
# Hello Africa
# Hello Americas
# Hello Antartica
# Hello Asia
# Hello Australia
# Hello Europe
# ```
# 
# If we want to save the output of our script to a single file we would redirect the output with `>>`
# 
# 
# 
# ```bash
# #!/bin/bash
# 
# #This script prints a greeting for each continent and saves the output to the file Greetings.txt 
# 
# continents="Africa Americas Antartica Asia Australia Europe"
# 
# for item in $continents
# do
#   echo "Hello $item" >> Greetings.txt
# done
# ```
# 
# If we want to save the output into different files we could do this
# 
# ```bash
# #!/bin/bash
# 
# #This script prints a greeting for each continent and saves the output into a different file for each continent.
# 
# continents="Africa Americas Antartica Asia Australia Europe"
# 
# for item in $continents
# do
#   echo "Hello $item" > Greet.$item
# done
# 
# ```
# 
# 
# ___
# 🔑 **In this lesson you have**
# 
# * What is a bash script
# * The basics of bash scripting
# * How to use variables in bash
# * How to make a for loop in bash
# 
# 
# 
# 

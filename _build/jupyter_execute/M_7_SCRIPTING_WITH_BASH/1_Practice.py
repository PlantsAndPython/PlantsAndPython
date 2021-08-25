#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 03. Bash scripting
# ## <p style="color:#2C6A7F"> Practice
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# 
# 
# For this practice go to the folder  `Analysis` that you have created on the previous activity.
# 
# Download the following files and upload them to your [virtual terminal](https://bit.ly/3d9BRCG) <br>[Hp1.fasta](https://drive.google.com/file/d/1FfirIu5Opm5y6aFB9sl20djUSK2YNuhV/view?usp=sharing) (this file was used in the previous activity)<br> 
# [Hp2.fasta](https://drive.google.com/file/d/1qzfHqaPpFriJ8BMxZ7hbiS1eE7_9Au4B/view?usp=sharing) <br>[Hp3.fasta](https://drive.google.com/file/d/1n5mEkiUrWZUT5WeaQ2ihAheM09X62zWP/view?usp=sharing)
# 
# ### <p style="color:#7f2c40">🚴 Exercise 1
# In the previous activity you answered the following questions for the file `Hp1.fasta`. 
# 
# a. How many records does `Hp1.fasta` have?
# 
# b. How many of those records are **RxLR** proteins?
# 
# c. How many of those records are **cysteine-rich** proteins?
# 
# d. How many of the **RxLR** proteins belong to the strain **Emoy2**?
# 
# 
# 1. Now, create a Bash script called `Hp1_yourname.sh` that answers the previous questions. Make sure it uses at least one variable.
# 
# ### <p style="color:#7f2c40">🚴 Exercise 2
# 
# 2. Make a copy of your script with the name `Hploop_yourname.sh` and modify it so it iterates over the files Hp1.fasta, Hp2.fasta, and Hp3.fasta to answer the questions of exercise 1.
# 
# ### <p style="color:#7f2c40">🚴 Exercise 3
# 1. If you have access to an HPC cluster or remote server and you have your user name and password it is time to practice uploading your script from exercise 2 to the HPC cluster to your home directory via `scp`. Connect to the cluster with `ssh` to verify your file is there.
# 
# 
# ### <p style="color:#7f2c40">🚴 Exercise 4
# We have performed homology searches using BLAST with the scaffolds of a recently sequenced genome of a phytopathogenic nematode against the chromosomes of the model organism *Caenorhabditis elegans*. We have 6 tabular BLAST results files. Each one containing the sequences that are similar [*hits*] to each one of *C.elegans* chromosomes.
# 
# [blastnCeChr1.tab](https://drive.google.com/file/d/1TEhoHr02HYtutp1WJaPquXCY_zfQygn3/view?usp=sharing)<br>
# [blastnCeChr2.tab](https://drive.google.com/file/d/1JI0rlPMoznZ9ply15qzxcd1i-_gcKUtJ/view?usp=sharing) <br> 
# [blastnCeChr3.tab](https://drive.google.com/file/d/1zbcEoeQaBh9KzX0fewTKZQ8nus2JLMsL/view?usp=sharing) <br>
# [blastnCeChr4.tab](https://drive.google.com/file/d/1nJ-elJ9eKQfQShaTm-DKLdvIoVQ8BcRu/view?usp=sharing)
# <br>
# [blastnCeChr5.tab](https://drive.google.com/file/d/1WlroNsag1bk7PFL6J2AbAMBIL2YLTPUW/view?usp=sharing)
# <br>
# [blastnCeChrX.tab](https://drive.google.com/file/d/1GiOB4xWPf0ooumw1VUDotuYhEp6nVHx6/view?usp=sharing)
# 
# We want to know how many hits has each scaffold got to each one of the chromosomes. The scaffolds are indicated in the first column and the chromosomes in the second one. To answer this question we have to count for each scaffold (there are 5 scaffolds) how many times each chromosome appears in the same line.
# 
# 1. Write a Bash script that tells you how many hits has each scaffold got for each chromosome (each file contains a different chromosome). 
# 2. Again if you have access to an HPC cluster try to upload your file.
# 
# ----------
# 
# Thanks for completing this activity!

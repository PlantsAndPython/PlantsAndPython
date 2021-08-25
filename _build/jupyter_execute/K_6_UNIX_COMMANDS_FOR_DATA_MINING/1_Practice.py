#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 02. Unix Commands for Data Mining
# ## <p style="color:#2C6A7F"> Practice
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# 
# 
# ## <p style="color:#7f2c40">🚴 Exercise 1 
# Now is time for you to practice what you have learned. Try to solve as many questions as possible. There are usually various ways to solve the problems. 
# 
# 
# Now let's do some data mining in some tiny files. Once you have learn to do this, you will be able to work with large genomic data files. 
# 
# 1. On your home directory create a new directory called `Exercise1`.
# 2. Create a new file inside the folder `Exercise1` with `vim` called `ToyPlant.fasta`
# 
# 	you can copy/paste the following contents
# 	
# 	```
# 	>Plant_1
# 	ACCACCGATACATGCGGTGCGTTGT
# 	>Plant_3
# 	CCACTGTGTTCGAGTTGTGATACAG
# 	>Plant_3
# 	CCACTGTGTTCGAGTTGTGATACAG
# 	>Plant_2
# 	CCAGCATTTGTAGTCACAACGCCGC
# 	>Plant_4
# 	TAGAGTTGTACACGCGTTTGTACGA
# 	>Plant_4
# 	TAGAGTTGTACACGCGTTTGTACGA
# 	>Plant_1 
# 	ACCACCGATACATGCGGTGCGTTGT
# 	```
# 3. See the file permissions
# 3. Give permissions of writing, reading and executing to everyone in ToyPlants.fasta
# 4. How many lines does the file have?
# 5. How many records does the file have?
# 6. How many unique records does the file have?
# 7. Calculate the total amount of bases [the genome size]
# 8. How many sequences contain the string `GATACA` [Specific sequence strings that may have a particular function or structure are called **motives** or **domains**.]
# 9. Make a backup of that file in `Documents`.
# 10. In the folder `Exercise1` create the following file called ToyPlant.genes
# 		
# 	```
# 	chr1 height ht-1 100 1000 + (100-150,400-500,900-1000)
# 	chr1 height ht-2 100 1000 + (100-150,900-1000)
# 	chr1 resist res-1 1500 2000 + (1500-1750,1800-1850,1099-2000)
# 	chr1 resist res-2 1500 2000 + (1500-2000)
# 	chr2 color color-1 3400 4200 - (3400-3600,4000-4200)
# 	chr2 color color-2 3400 4200 - (3400-3550,3800-3900,4000-4200)
# 	chr2 color color-3 3400 4200 - (3400-3600,3800-3900,4100-4200)
# 	chr3 fruit fru-1 50 800 + (50-400,700-800)
# 	chr3 fruit fru-1 1100 1500 + (1100-1200,1450-1500)
# 	chr3 smell smell-1 2000 2600 - (2000-2300,2500-2600)
# 	chr3 smell smell-2 2000 2600 - (2000-2050,2200-2300,2500-2600)
# 	chr4 dev dev-1 3100 3700 - (3100-3500,3600-3700)
# 	chr4 dev dev-2 3100 3700 - (3100-3200,3400-3500,3600-3700)
# 	chr4 height2 ht2-1 4500 4800 + (4500-4800)
# 	chr5 shape shape9-1 200 1000 - (200-450,550-650,800-1000)
# 	chr5 shape shape10-1 110 1700 + (110-1400,1500-1700)
# 	```
# 
# 11. How many transcripts does the file show? (all lines)
# 12. How many different chromosomes does the file have? (column 1; the file separator is a space)
# 13. How many different genes does the genome have? (column 2)
# 
# 
# ### <p style="color:#7f2c40">🚴 Exercise 2
# We are studying some proteins that are involved in pathogenicity called effectors found on the sequences of the phytopathogen *Hyaloperonospora arabidopsidis*. We want to know how many of those sequences are **RxLR** effectors (RxLR for containing Arginine, any amino acid, Leucine and Arginine). We also want to know which ones are cysteine-rich. And which of the RxLR effectors belong to a specific strain called Emoy2.
# 
# 1. Go to the folder `Exercise1` and create a new directory called `Analysis`
# 2. Upload the following file to your [virtual terminal](https://bit.ly/3d9BRCG) <br>[Hp1.fasta](https://drive.google.com/file/d/1FfirIu5Opm5y6aFB9sl20djUSK2YNuhV/view?usp=sharing) <br> 
# 3. How many records does `Hp1.fasta` have?
# 	
# 	 For the next three questions we will analyze the identifiers and not the sequences
# 
# 4. How many of those records are **RxLR** proteins?
# 5. How many of those records are **cysteine-rich** proteins?
# 6. How many of the **RxLR** proteins belong to the strain **Emoy2**?
# 
# -----------
# 
# Thank you for completing this activity!
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

#!/usr/bin/env python
# coding: utf-8

# ![plants_python_logo.jpg](../images/plants_python_logo.jpg)

# # Practice: Genome visualization and comparative genomics

# ## Orthology and Gene Family Analysis

# Synteny is a good way to identify orthologous genes between species, but sometimes genes move around the genome, and when they are in new places, syntenic approaches are unable to identify orthologous gene pairs. Very distantly related species like rice and moss also have undergone massive strucutral rearrangements and polyploidy, so many of the genes are no longer in the same places. Alternatively, we can cluster similar groups of genes into gene families or **orthogroups**. Here, we essentially use BLAST and set a threshold to group genes together based on similarity. Orthogroup analysis is a powerful way to identify corresponding genes across dozens of different species. This can be used to assign function or to identify gene losses or expansions related to important traits. 
# <br>
# We will use OrthoFinder to compare the gene content of 56 divere flowering plant genomes.
# https://github.com/davidemms/OrthoFinder
# ![orthofinder.jpeg](../images/orthofinder.jpeg)

# OrthoFinder can be used to cluster genes into orthogroups for any number of species and typcially, more species = more power. The input for OrthoFinder is a set of protein sequences in fasta format for each species. OrthoFinder is computationally intensive (All vs all alignment + phylogenetic tree construction), so we ran this already on a set of 56 species (see below). I have provided an example submission script on HPCC if you'd like to run it yourself!

# ## Challenge problem: Run OrthoFinder on a group of your favorite species!

# I have provided orthofinder results for a group of ~21 species, but you can run Orthofinder on a different set of species of your choosing. Orthofinder is relatively CPU intensive, but this depends on the number of species you include in the analysis and the total number of genes. <br>
# 
# I put an example  slurm submission script for Orthofinder under `/mnt/ufs18/rs-007/REU_Plant_Genome_2021/Orthofinder` as follows:
# 
#     #!/bin/sh --login
#     #SBATCH --time=96:00:00             # limit of wall clock time - how long the job will run (same as -t)
#     #SBATCH --nodes=1                 # number of different nodes - could be an exact number or a range of nodes (same as -N)
#     #SBATCH --ntasks=8                 # number of tasks - how many tasks (nodes) that you require (same as -n)
#     #SBATCH --cpus-per-task=1           # number of CPUs (or cores) per task (same as -c)
#     #SBATCH --mem-per-cpu=4g            # memory required per allocated CPU (or core) - amount of memory (in bytes)
#     #SBATCH -J Orthofinder
#     cd /mnt/ufs18/rs-007/REU_Plant_Genome_2021/Orthofinder/
# 
#     module purge
#     module load iccifort/2019.5.281  impi/2018.5.288
#     module load OrthoFinder/2.4.1-Python-3.7.4
# 
#     orthofinder -t 8 -a 8 -b /mnt/ufs18/rs-034/VanBuren_Lab/Bob/ -f /mnt/ufs18/rs-007/REU_Plant_Genome_2021/Orthofinder/Proteins_seqs/
# 
# Here, I have requested 1 node with 8 cpus to run orthofinder. I have only included protein datasets from 8 species (under `/mnt/ufs18/rs-007/REU_Plant_Genome_2021/Orthofinder/Proteins_seqs/`), so this should run in a reasonable amount of time with these resources. I would typically request 96 processors, but this should be fine. I have requested a wall time of 96 hours and 4 Gb of memory per node. We need to load a few modules including the Intel compilers toolchain and Intel MPI Library, which are useful to create, maintain, and test advanced programs on high performance computing clusters. We will also load Orthofinder version 2.41 and specify the correct version of Python to run. We could also install OrthoFinder locally ourselves using a conda virtual environment, but we won't get into that here. **If you decide to run Orthofinder yourself, make sure to change the starting directory and the -b flag in the command, as this controls where the files will be output. DO NOT OUTPUT THEM IN THE COURSE DIRECTORY**
# <br>
# If you want to run orthofinder of different/additional species, you simply need to download the protein file and include it in the directory containing protein sequences. 

# In[1]:


## Answer
## What species did you choose and what do the output files look like? 


# We will use the output files you generated or the ones I provided for the remainder of this exercise. 

# ## Phylogenetics with Bio.Phylo

# Orthofinder builds a consensus phylogenetic tree based on all of the individual gene trees it constructs for each orthogroup. We can visualize this tree using the Biopython function `Phylo`. This will give us a sense of the phylogenetic placement of the species we included. First, we need to import a few functions in Biopython as well as matplotlib: 

# In[2]:


import copy
from io import StringIO

from Bio import Phylo
from Bio.Phylo.Applications import PhymlCommandline
from Bio.Phylo.PAML import codeml
from Bio.Phylo.PhyloXML import Phylogeny
get_ipython().run_line_magic('matplotlib', 'inline')


# There are more powerful things that can be done with `Phylo` , but for now, we will simply read the tree file output from OrthoFinder and plot it. 
# <br>
# <br>
# **Note: Remember to provide the path for the species tree file!**

# In[3]:


tree = Phylo.read("Practice9_SpeciesTree_rooted_node_labels.txt", "newick") ## specify the location of the tree file and the format (in this case, newick)


# Printing the tree object as a string gives us a look at the entire object hierarchy.

# In[4]:


print(tree)


# The Tree object contains global information about the tree, such as whether it’s rooted or unrooted. It has one root clade, and under that, it’s nested lists of clades all the way down to the tips.
# 
# It's hard to draw meaning from this, but we can draw the tree in a more informative way. The function draw_ascii creates a simple ASCII-art (plain text) dendrogram. This is a convenient visualization for interactive exploration, in case better graphical tools aren’t available.

# In[5]:


Phylo.draw_ascii(tree)


# Here we can see we constructed OrthoGroups for 56 flowering plant species across ~20 plant families. See if you can figure out which species are which and read the tree correctly. 
# 
# You can also create a slightly nicer graphic using the draw function:

# In[6]:


Phylo.draw(tree, branch_labels=lambda c: c.branch_length)


# # Analyzing Orthofinder gene family results

# Now that we have a good sense of the phylogenetic placement of our species, we can play around with the OrthoFinder results. The primary output of OrthoFinder is a csv file where each row is a different orthogroup and each column is a different species  The numbers correspond to the number of genes in that orthogroup for each species. We can use this to get simple metrics on or more complex dynamics of expansion and contraction of genes in specific lineages. In terms of downstream analyses, you could identify an orthogroup that contains your favorite gene and find the orthologous sequences in all your other species of interest. You could identify expanded or contracted orthogroups in one species and use Gene Ontology terms or other classifiers to see what those duplicated genes are likely involved in. 
# <br>
# You could also use these orthogroups as common identifiers across species and map expression to each orthogroup (as we did in last year's class porject). 

# For simplicity, we will use `pandas` to read in, manipulate, and analyze our dataframe: 

# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd


# In[8]:


data = pd.read_csv("Practice9_Orthogroups.GeneCount.csv")
data.head()


# ### How many total orthogroups are there for this dataset?

# In[9]:


## Answer


# ### Which species has the most genes in orthogroups? 

# In[10]:


## Answer


# ### Which orthogroup has the most genes in it (across all species)?

# In[11]:


## Answer


# ### Which species has the most orthogroups with 0 genes? Why do you think that is? 

# In[12]:


## Answer


# ### Bonus challenge: Plot the distribution of orthogroup size 

# In[13]:


## Answer


# ### BONUS challenge 2X: Identify orthogroups that are expanded in one species of your choice. This can be simply based on some cutoff, or preferably, using a statistical test. 

# In[14]:


## Answer


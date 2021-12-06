#!/usr/bin/env python
# coding: utf-8

# ![plants_python_logo.jpg](../images/plants_python_logo.jpg)

# # Practice: Variant discovery, genetic diversity, and population genetics
# So far we have seen how Illumina short read data can be used to quantify elements in the genome and find differences in gene expression, small RNA accumulation, methylation, chromatin accessibility, and transcription factor binding, among others. These approaches align the reads against a reference genome to count how many align to a specific region for quantification, but ignore the actual sequence information contained in the reads. In RNAseq data for instance, there can be sequence differences between the RNAseq reads and the reference genome, but we ignore this information as we only care about how many reads align per gene. What if we care about the actual sequence? <br>
# <br>
# We can use Illumina data to identify differences between a reference genome and another individual. We could look at differences across varieties, cultivars or accessions of a crop plant. We could sequence siblings in a mapping population and identify which alleles they have. We could also identify causal mutations in an EMS, fast neutron, or transposon based mutant populaton. In all of these cases the workflow is the same, and the first step is to identify _variants_ or differences between the reference genome and our individual of interest. Using Illumina data, we can identify single nucleotide polymorphisms (or SNPs) which represent base pair differences (e.g. A -> G, C -> T, etc.), or we can identify short insertions or deletions (InDels) which represent differences that span a couple base pairs (e.g. a deletion of ACC or an insertion of GTGA). <br> <br>
# Identifying variants is significantly more computationally intensive than mapping RNAseq data, so we will not be doing it in this notebook (but the workflow is described below for those who are interested). Instead, we will learn about how to manipultate the output variant dataframes (VCF files) and simple downstream analyses of genetic diversity and population genetics. In this notebook, we will work with variant data for wild and domesticated pineapple and grape, but these approaches can be applied to your favorite species!

# # Reading, manipulating, and analyzing VCF files

# Like everything, there are many programs that we can use to read, manipulate, and analyze VCF files. There is even a python library! Here, we will use the package `scikit-allel` and analyze filtered VCF files from pineapple and grape (Vitis species). GATK produces a large raw VCF file that needs to be filtered (10-1,000 gigabytes, depending on how many variants, individuals, and genome size). Its not uncommon to get 10 or >100 million variants in a project, and not all of these are high confidence, and for some analyses, you only need a subset of the data. We can use `scikit-allel` to filter VCF files, but it is slow. The best program to filter VCF files is VCF-tools and it can be run on HPCC. It has a lot of functionality and can also be used for basic population genetics and genetic diversity analyses: <br>
# https://vcftools.github.io/man_latest.html
# <br>
# I have already used VCFtools to filter both the pineapple and grape datasets to make them more manageable for this notebook. We will import the filted files. 

# The `scikit-allel` package provides utilities for exploratory analysis of large scale genetic variation data. It is based on numpy, scipy and other general-purpose Python scientific libraries. We need to install `scikit-allel`, and the simplest way is to use Conda. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. You should be able to install it by running the following command in Jupyter, but you can also run this on the Anaconda command prompt (note this may take a few minutes to update/install all of the dependencies in the conda environment): 
# 
# 

# In[ ]:


conda install -c conda-forge scikit-allel


# Once 'conda install' is run, we can verify that the package was installed correctly. 

# In[ ]:


import allel; print('scikit-allel', allel.__version__)


# We'll need some other stuff too: 

# In[ ]:


import random
random.seed(42)
import time
import numpy as np
np.random.seed(42)
import h5py
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set_style('white')
sns.set_style('ticks')
import bcolz
import pandas
import allel


# The first step is to read in the vcf file, and we'll do this using allel.read_vcf. We will use `fields='*'` to import all the fields:

# In[ ]:


pineapple = allel.read_vcf('Practice11_pineapple_downsampled.vcf', fields='*')


# Now lets look at the vcf file we imported: 

# In[ ]:


print(pineapple)


# This is basically a raw NumPy array, so it's not intuitive to read if you are a human.  We can import it as a dataframe instead, so that we fellow humans can interpret it. **Note:** we aren't going to do anything with this NumPy array, _but you could_. 
# <br> <br>
# Importing the vcf file as a dataframe:

# In[ ]:


pineapple_df = allel.vcf_to_dataframe('Practice11_pineapple_downsampled.vcf', fields='*', alt_number=2)
pineapple_df


# The  object returned by read_vcf() is a Python dictionary with several NumPy arrays, each of which can be accessed via a key. Lets see the available keys:

# In[ ]:


sorted(pineapple.keys())


# As you can see, there are many keys, and you can learn more about each key in the description of vcf files above. The `samples` array contains sample identifiers extracted from the header line in the VCF file. We can use these later on when we plot things:
# 
# 

# In[ ]:


pineapple['samples']


# Now, lets take a step back, where did this data come from? This data is from a recent paper on the domestication history of pineapple: 
# https://www.nature.com/articles/s41588-019-0506-8
# 
# In this paper, we resequenced ~90 accessions of pineapple from around the world and a few dozen wild species as well. We will be replicating a few of the analyses in this paper. <br>
# 
# ![pineapple.webp](../images/pineapple.webp)
# 
# In this notebook, we imported a simplified vcf file containing a subset of the variants that were used in this paper. We can treat the file of variants as a character matrix and similar to the leaf shape and RNAseq data, use a principle component analysis to describe the data. There should be distinct sets of variants that are found in _only_ domesticated and _only_ wild pineapple, and they should lead to a strong separation of the two groups. The wild progenitor species of pineapple should contain a subset of variants that are shared with pineapple, so we might extpect these to be closer to the cultivated accessions than the wild. 

# To run a PCA, we need a simple dataframe of integers (0, 1, and 2) instead of the complex numpy arrays we have after importing a vcf file. We can use the `allel.GenotypeChunkedArray` function to pull out only the genotype data (key 'calldata/GT'):

# In[ ]:


g = allel.GenotypeChunkedArray(pineapple['calldata/GT'])
g


# This is simpler, but still not a simple enough input to run a PCA. We can use the `to_n_alt()` function transform each genotype call into the number of non-reference alleles. In this case, a 0/0 would be transformed into 0, 0/1 into 1, and 1/1 into 2:

# In[ ]:


gn = g.to_n_alt()
gn


# Then, we can use the `allel.pca` function to run the principle component analysis (PCA). We need to feed it our simplified array, the number of components (set to 10), and the scaler (Patterson is based on the methods from the first paper to use PCA to survey genetic diversity):

# In[ ]:


coords1, model1 = allel.pca(gn, n_components=2, scaler='patterson')


# Finally, we can plot the PCA. We will use matplotlib as we've done in the past. We will use the 'samples' array to label each sample. <br>
# Note: This PCA is pretty ugly and hard to interpret as is. See if you can relabel each data point or recolor the points by species or cultivar group. 

# In[ ]:


#plt.scatter(coords1[:,0], coords1[:,1])
import matplotlib.pyplot as plt

labels = pineapple['samples']
colors = pineapple['samples']
plt.figure(figsize=(15, 12))
plt.subplots_adjust(bottom=0.1)
plt.scatter(coords1[:,0],coords1[:,1], label='True Position')

for label, x, y in zip(labels, coords1[:, 0], coords1[:, 1]):
    plt.annotate(
        label,
        xy=(x, y), xytext=(-3, 3),
        textcoords='offset points', ha='right', va='bottom')
plt.show()


# We can similarly group the genetic data using a Hierarchical Clustering approach. This is similar to PCA and is often congruent with a phylogenetic approach. Below, samples are broken down into wild pineapple (in green) and domesticated (red):

# In[ ]:


from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

linked = linkage(coords1, 'ward')

labelList = pineapple['samples']

plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show()


# # Bringing it together

# We can apply this same framework to grape. Dan's collaborators have collected genotype data for diverse Vitis accessions. This includes many domesticated grape varieties and wild grape species. We previously used PCA with the shape data to cluster the accessions, but how does this compare to genotype data? Using the provided grape vcf file, run a PCA and heirarchical cluster. I have also provided a sample dataframe and you can get creative to color the samples by species instead of labeling them. How does this compare to the previous PCA based on shape alone? <br>
# The grape vcf file is derived from GBS data, and Dan's collaborator has heavily filtered the vcf file to contain only biallelic SNPs, with high depth and low missing data rates. 

# In[ ]:


## Load the grape vcf file
grape = allel.read_vcf('Practice_Grape.biallele.depth.missing.recode.recalc.vcf')


# In[ ]:


print(grape)


# How many vitis accessions are in this vcf file?

# In[ ]:


##Answer


# How many variants are in this vcf file? 

# In[ ]:


##Answer


# Run and plot a PCA from this datset
# Note, the code I provided above makes a pretty ugly PCA, how might you change the plotting/colors to make it more easily interpretable? 

# In[ ]:


##Answer


# Run a Hierarchical Clustering and plot a dendrogram of the grape dataset

# In[ ]:


##Answer


#!/usr/bin/env python
# coding: utf-8

# ![plants_python_logo.jpg](../../images/plants_python_logo.jpg)

# # 11.0 Variant discovery
# So far we have seen how Illumina short read data can be used to quantify elements in the genome and find differences in gene expression, small RNA accumulation, methylation, chromatin accessibility, and transcription factor binding, among others. These approaches align the reads against a reference genome to count how many align to a specific region for quantification, but ignore the actual sequence information contained in the reads. In RNAseq data for instance, there can be sequence differences between the RNAseq reads and the reference genome, but we ignore this information as we only care about how many reads align per gene. What if we care about the actual sequence? <br>
# <br>
# We can use Illumina data to identify differences between a reference genome and another individual. We could look at differences across varieties, cultivars or accessions of a crop plant. We could sequence siblings in a mapping population and identify which alleles they have. We could also identify causal mutations in an EMS, fast neutron, or transposon based mutant populaton. In all of these cases the workflow is the same, and the first step is to identify _variants_ or differences between the reference genome and our individual of interest. Using Illumina data, we can identify single nucleotide polymorphisms (or SNPs) which represent base pair differences (e.g. A -> G, C -> T, etc.), or we can identify short insertions or deletions (InDels) which represent differences that span a couple base pairs (e.g. a deletion of ACC or an insertion of GTGA). <br> <br>
# 

# ## Plant Biology Learning objectives
# 
# - Understand the principles of read alignment and variant detection
# - Understand the downstream applications and analyses associated with variant calling
# - Learn the distinction between small and large-scale variants
# - Introduce the concept of pangenomics
# 

# ## 11.1 Introduction to variant dection in plants
# Identifying variants is significantly more computationally intensive than mapping RNAseq data, so we will not be doing it in this notebook (but the workflow is described below for those who are interested). Instead, we will learn about how to manipultate the output variant dataframes (VCF files) and simple downstream analyses of genetic diversity and population genetics. Below is a video providing an introduction to variant discovery approaches and applications in plants.

# In[1]:


from IPython.display import YouTubeVideo

YouTubeVideo("7eMH1rdVbHM",width=960,height=540)


# # 11.2 Identifying variants

# ![variants_pipeline.png](../../images/variants_pipeline.png)

# The first step of variant discovery is the same as the RNAseq pipeline: we need to align Illumina reads against a  reference genome. Unlike RNAseq, where we can _quasimap_ or _pseudoalign_ reads to figure out the relative position for quantification, we need to know the exact alignment, at base pair resolution, to accurately identify differences between reads and the reference. We can use several aligners to do this, but the leading ones are **bowtie2** and **bwa**. After alignment, we need to filter out duplicated reads (from PCR),  sort the data, and feed it into the Genome Analysis Toolkit (GATK). GATK is the gold standard for identifying variants ( _for now_ ), and the workflow can be found below.  
# ![variant_workflow.png](../../images/variant_workflow.png)
# <br>

# GATK offers a wide variety of tools with a primary focus on variant discovery and genotyping. Its powerful processing engine and high-performance computing features make it capable of taking on projects of any size. GATK is a beast, and we could spend weeks discussing best practices for identifing variants. Accurately identifying variants is challenging in even the simplest systems, and it scales in difficulty for polyploids, highly repetitive genomes, and highly diverse or heterozygous species. The simplified workflow is outlined above, and the central algorithm of variant detection, the `HaplotypeCaller` is outlined below.
# ![haplotype_caller.png](../../images/haplotype_caller.png)
# 1. First, the program determines which regions of the genome it needs to operate on, based on the presence of significant evidence for variation.
# 2. For each ActiveRegion, the program builds a De Bruijn-like graph to reassemble the ActiveRegion and identifies the possible haplotypes present in the data. The program then realigns each haplotype against the reference haplotype using the Smith-Waterman algorithm in order to identify potentially variant sites.
# 3. For each ActiveRegion, the program performs a pairwise alignment of each read against each haplotype using the PairHMM algorithm. This produces a matrix of likelihoods of haplotypes given the read data. These likelihoods are then marginalized to obtain the likelihoods of alleles per read for each potentially variant site.
# 4.  For each potentially variant site, the program applies Bayes’ rule, using the likelihoods of alleles given the read data to calculate the posterior likelihoods of each genotype per sample given the read data observed for that sample. The most likely genotype is then assigned to the sample.
# 
# Read processing and HaplotypeCaller are run separately on each sample in the experiment, and the results are combined, recalibrated, and a dataframe of variants is output in the Variant Call Format (VCF). GATK and the associated processes can be run on HPCC. 

# # 11.3 VCF: a dataframe of variants

# The intermediate files for variant calling are huge, and we need a way to visualize, manipulate, and analyze variants across the genome for many individuals. There are several leading formats, but the most common is the VCF format. Below is an example:
# 
#     ##fileformat=VCFv4.0
#     ##fileDate=20090805
#     ##source=myImputationProgramV3.1
#     ##reference=1000GenomesPilot-NCBI36
#     ##phasing=partial
#     ##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">
#     ##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
#     ##INFO=<ID=AF,Number=.,Type=Float,Description="Allele Frequency">
#     ##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">
#     ##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">
#     ##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">
#     ##FILTER=<ID=q10,Description="Quality below 10">
#     ##FILTER=<ID=s50,Description="Less than 50% of samples have data">
#     ##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#     ##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
#     ##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
#     ##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">
#         #CHROM POS     ID        REF ALT    QUAL FILTER INFO                              FORMAT      Gala        Honeycrisp        Granny_Smith
#     Chr_20     14370   rs6054257 G      A       29   PASS   NS=3;DP=14;AF=0.5;DB;H2           GT:GQ:DP:HQ 0|0:48:1:51,51 1|0:48:8:51,51 1/1:43:5:.,.
#     Chr_20     17330   .         T      A       3    q10    NS=3;DP=11;AF=0.017               GT:GQ:DP:HQ 0|0:49:3:58,50 0|1:3:5:65,3   0/0:41:3
#     Chr_20     1110696 rs6040355 A      G,T     67   PASS   NS=2;DP=10;AF=0.333,0.667;AA=T;DB GT:GQ:DP:HQ 1|2:21:6:23,27 2|1:2:0:18,2   2/2:35:4
#     Chr_20     1230237 .         T      .       47   PASS   NS=3;DP=13;AA=T                   GT:GQ:DP:HQ 0|0:54:7:56,60 0|0:48:4:51,51 0/0:61:2
#     Chr_20     1234567 microsat1 GTCT   G,GTACT 50   PASS   NS=3;DP=9;AA=G                    GT:GQ:DP    0/1:35:4       0/2:17:2       1/1:40:3
# 
# There's a lot to unpack here, but for their complexity, VCF files contain a wealth of useful information. Lines that start with `##` contain info such as the file format, reference genome used, filters, and other useful information. These are largely ignored for any data analysis. 
# <br>
# There are 8 fixed fields per row (or sequence variant). All data lines are tab-delimited. In all cases, missing values are specified with a dot (”.”). Fixed fields are as follows:
# 
# 1. **CHROM** chromosome: an identifier from the reference genome. Could be a number, Chr_X, or SCAFFOLD_X / Contig_X among others. 
# 2. **POS** position: The reference position, with the 1st base having position 1. Positions are sorted numerically, in increasing order, within each reference sequence CHROM. (Integer, Required)
# 3. **ID** semi-colon separated list of unique identifiers where available. This can intuitive or a random string. Can mostly be ignored (Alphanumeric String)
# 4. **REF** reference base(s): This is the base in the reference genome and each base must be one of A,C,G,T or N for unknown. If this position is an indel (insertion or deletion), it may contain multiple bases.  
# 5. **ALT** comma separated list of alternate non-reference alleles called on at least one of the samples. This is the variant that was different from the reference. Options are base Strings made up of the bases A,C,G,T,N, or an angle-bracketed ID String. Note, there can be more than one alt. One individual could have a T at this position and another could have a C (while the reference is G) (Alphanumeric String; no whitespace, commas, or angle-brackets are permitted in the ID String itself)
# 6. **QUAL** phred-scaled quality score for the assertion made in ALT. High QUAL scores indicate high confidence calls. Although traditionally people use integer phred scores, this field is permitted to be a floating point to enable higher resolution for low confidence calls if desired. (Numeric)
# 7. **FILTER** filter: PASS if this position has passed all filters, i.e. a call is made at this position. Otherwise, if the site has not passed all filters, a semicolon-separated list of codes for filters that fail.(Alphanumeric String)
# 8. **INFO** Additional information: (Alphanumeric String) INFO fields are encoded as a semicolon-separated series of short keys with optional values in the format: <key>=<data>[,data]. Arbitrary keys are permitted, although the following sub-fields are reserved (albeit optional). 
# 
# The genotype fields are next, and these are the most important as these contain the variants . There will be one column for each sample/accession where variants were identified. In this example, that would be Gala, Honeycrisp, or Granny_smith apples. Genotypes can be denoted as: **0/0**, **0/1**, or **1/1** (in general, but there are other possibilities). The first record in this example has a reference allele of G, and the alternative allele is A. 0/0 is homozygous for the reference alleles (AA), 0/1 is heterozygous for the reference and alternate alleles (AG) and 1/1 is homozygous for the alternate allele (GG). ./. indicates missing data.  Now, this is for diploid species, a haploid or monoploid species would have 0 or 1, and a polyploid species would have more. An octoploid (like strawberry or sugarcane) would have eight such as 0/0/0/0/0/1/1/1 or 0/0/1/1/1/1/1/1/1. For simplicity, we will only use diploids!
# <br> <br>
# Now that we know what a VCF file is, we will learn how to read it, manipulate it, and use it for basic genetic diversity and population genetics analyses. 

#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 03. Biological Data Formats
# 
# ***Author:  Dr. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Learning Objectives**
# >After completing this lesson you will learn:
# >
# >* to recognize the most common biological data formats
# >* DNA and protein sequences [fasta]
# >* sequencing format [fastq]
# >* mapping formats [sam, bam]
# >* annotation formats [bed, gtf, gff, vcf]
# >* BLAST alignment results in tabular format
# 
# 
# 
#  [![09. Biological Data Formats](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide9.png?raw=true)](https://youtube.com/embed/76v6bI5DEXk "09. Biological Data Formats")
# 
# 
# 
# Most biological data is stored in text files. DNA  sequence data is shown in letters `A``G``C``T`. Each character represents the four nucleotides (bases) *adenine, guanine, cytosine and thymine* respectively. Similarly protein data is represented by letters, where one character is assigned to each amino acid. The letters can be either uppercase or lowercase. When you have a mixture of upper and lowercase letters in the same file it usually means the small letters are **masked bases** and they won't be taken into account for some processes by specific programs. There are specific letters to represent ambiguos sequences, in other words, where there are various options of nucleotides or amino acids for that particular position. Also if there is an unknown nucleotide it is represented with the letter `N`. If there is an unknown amino acid residue it is represented by an `X`.
# 
# | Amino acid                  | Three letter code | One letter code |
# |-----------------------------|:-------------------:|:-----------------:|
# | alanine                     | ala               | A               |
# | arginine                    | arg               | R               |
# | asparagine                  | asn               | N               |
# | aspartic acid               | asp               | D               |
# | asparagine or aspartic acid | asx               | B               |
# | cysteine                    | cys               | C               |
# | glutamic acid               | glu               | E               |
# | glutamine                   | gln               | Q               |
# | glutamine or glutamic acid  | glx               | Z               |
# | glycine                     | gly               | G               |
# | histidine                   | his               | H               |
# | isoleucine                  | ile               | I               |
# | leucine                     | leu               | L               |
# | lysine                      | lys               | K               |
# | methionine                  | met               | M               |
# | phenylalanine               | phe               | F               |
# | proline                     | pro               | P               |
# | serine                      | ser               | S               |
# | threonine                   | thr               | T               |
# | tryptophan                  | trp               | W               |
# | tyrosine                    | tyr               | Y               |
# | valine                      | val               | V               |
# 
# 
# ## <p style="color:#2C6A7F"> FASTA
# 
# 
# The most common format to store DNA and protein sequences is the `fasta` format, which was originated from a program that bears the same name. The `.fasta` file contains a `>` sign followed by the sequence identifier and in the next line the sequence in nucleotides or amino acids (represented with a single letter). The sequence could be in a single line
# 
# ```
# >sequence_1
# ATTTATGGCCCGCGATGTACGCCATCCAGACTTAACAGTGGGACATGGCACACAGTTGAGAGGGCACAAAATATTTAGACAGATAC
# ```

# or in multiple lines, usually of 60 characters each
# 
# ```
# >sequence_2
# AAGCTTCGGCATAGGACAAGATGGAGAGGGACGCATTGTGGAAGGCGCGCTGGGTGTTTTGGCAACCAGC
# GCAGTTGCCTGTTTGTGGTTAACATAGCTGTTACGAGAAGACGAGCGGCAAAGCTGTCATGCGTCTTGCT
# GTGCGAACGCAGTCGTCGGGCGAATTGTCCGTACGCGGGTGGTGGGGGGTGCAAATAGCCTGCGCTTGCA
# TTTCAGCCTGGGCATTCGAGTGGAATATTATTGTGTTACACTGTACAAAAAAAAAAAGCTT
# ```
# Records in a fasta file can also have descriptions. They will come after the id, usually separated by a space.
# 
# ```
# >QBF53359.1 RxLR [Phytophthora capsici]
# MSKVFLLLVLSVFALVSCDALSAPVGSKLSLSKTDELNAQPIDAKRMLRAQEEPTNAADEERGMTELANK
# FKAWAAAIKTWVTNSKLVQSMNNKLASLTQKGRVGQIEKLLKQDNVNVNVLYQNKVKPDELFLALKLDPK
# LKLIADAPAAWANNPGLSMFYQYATYYAKMTTKA
# ```
# 
# You can also have multiple sequences in a fasta file
# 
# ```
# >QBF53359.1 RxLR [Phytophthora capsici]
# MSKVFLLLVLSVFALVSCDALSAPVGSKLSLSKTDELNAQPIDAKRMLRAQEEPTNAADEERGMTELANK
# FKAWAAAIKTWVTNSKLVQSMNNKLASLTQKGRVGQIEKLLKQDNVNVNVLYQNKVKPDELFLALKLDPK
# LKLIADAPAAWANNPGLSMFYQYATYYAKMTTKA
# 
# >sp|D0N607.1|CRE4_PHYIT RecName: Full=RxLR effector protein CRE4; AltName: Full=Core RXLR effector 4; Flags: Precursor
# MLRSFLLIVATVSLFGQCKPLPLATSPVSDAVRAPHRSTHETRFVRTNDEERGATMTLAGVLRDKAQTKQ
# LLTSWLNSGKSVPSVSNKLGLKRMSLEQAIHHENWKALTTFQRMKSKKAKAYAKYGTGYQTEAKTKENLL
# QWVMRGDSPKEVSSTLGLLGLSRRKIIDHQNYEAFRTFLKYRKQWAEMQGNGFTKLTT
# 
# >sp|D0MRS3.1|RD21_PHYIT RecName: Full=RxLR effector protein PexRD21; AltName: Full=Core RXLR effector 1; Flags: Precursor
# MRLSYILVVVIAVTLQACVCATPVIKEANQAMLANGPLPSIVNTEGGRLLRGVKKRTAEREVQEERMSGA
# KLSEKGKQFLKWFFRGSDTRVKGRSWR
# ```
# The most common extensions used for these files are `.fasta`, `.fa`, `.fna`[for nucleotides], `.faa` [for amino acid residues], `.fsa`, or `.fas`.
# 
# ## <p style="color:#2C6A7F"> FASTQ
# 
# Next generation sequencing data can come in various formats, however, the most common format is **fastq** and the other formats are usually converted to fastq for their analysis. 
# 
# ### Characteristics of the `fastq` format
# 
# * Each record always contains **four** lines
# * The **first line** starts with a `@` sign followed by the **sequence identifier** 
# * The contents of the first line vary depending on the sequencing machine, version and the conversion software. However, it usually contains information about the sequencing run and cluster location.
# * The **second line** contains the **sequence** or **base calls (A,C,T,G)** or N if the base couldn't be identified.
# * The **third line** contains a `+` sign and in some cases it repeats the sequence identifier of line one.
# * The **fourth line** contains the **quality scores** of each base in ASCII format 
# 
# ```
# @<identifier and expected information>
# <sequence>
# +<identifier and other information OR empty string>
# <quality>
# ```
# 
# specific information of the data contained in the description of the first line can be found [here](https://help.basespace.illumina.com/articles/descriptive/fastq-files/)
# 
# ### Example of a single fastq record:
# 
# ```
# @SIM:1:FCX:1:15:6329:1045 1:N:0:2
# TCGCACTCAACGCCCTGCATATGACAAGACAGAATC
# +
# <>;##=><9=AAAAAAAAAA9#:<#<;<<<????#=
# 
# ```
# Each record represents a sequencing read
# 
# ### Paired libraries
# In paired-end or mate-paired libraries we obtain two sequences that are associated to the same record [they have the same identifier]. In fact, they come from both extremes of a single DNA fragment. Both pairs can come in **separated files** or in the same file, **interleaved**. The most common format is in separate files. In either case the pairs (that have the same identifier) have to be differentiated. 
# 
# Interleaved files have first the forward `F` pair, followed by the reverse pair `R`. And when they are in separate files they are indicated in the first line as `/1` and `/2` or in newer versions `1:Y:18:ATCACG` and `2:Y:18:ATCACG`
# 
# **Example of file with the first pair of each record** `1:N:0:1`
# 
# 

# ```
# @M02586:164:000000000-AYBV7:1:2119:13975:24958 1:N:0:1
# ACGTTGTGCCAGCCGGGTGAGAAAGTAGCTGTCCGTTTCGCTGGTCTGGTCAATATGCGGGATCTTAACGCTATCAAGTTCCTGCGGGATTACTGGCAGATCTAATTTATTCCGGCTTGAAATGATTCTGACAATCGCGCCGAGCGTGTAATCATCGTAAGACTGG
# +
# CCCCCGGGGGGGFGGGGGGFFEGGGGGGGFCFEEGFGFFFGGGGGGGGGGGGGGFGGFG@:CFGGGGGGGGGGGGGGFFGGFFGGDGGGGGGGGFGFGGFGGGGGGGGGGD<FGGGGGGGGGGGGGGGFFFFGFF8CGGDFFEGGGGGGFGGDFGGG<DCFGGCFG
# @M02586:164:000000000-AYBV7:1:2119:13272:24958 1:N:0:1
# CACTCACTAGCGACCCACTTGGAGGTCGCCAAAAGCAATATTATCCATATCTCGGAGGATTTGGACCAGATCCAGGTCGTCATCGAATTGCCTGGAGAACGGCACGAACTTGGTGCTACGACGAAGTGGAAACGCACAGCAACTTCTGGAGGGAGTGTTGGATCGA
# +
# CCCCCGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGFGGGGGGGGGGGGGGGGGGGGGGGGGGGDFFGGGGGGGGGGGGGGGGGGGGGGGGCFGGGGGGGGGGDGGGGGGGGGGGGFFG:@GGFGGGGGGG5>,
# ```

# 
# **Example of file with the second pair of each record** `2:N:0:1`

# ```
# @M02586:164:000000000-AYBV7:1:2119:13975:24958 2:N:0:1
# TNNNNNNNNNCAGTTACCCGTGGGGGCTCGCATCGCACCCGCATTCACGCTGACGATAAAAAATAAGGTGCTGGAAGAAAATATCTCTGCTCGGATCATCAGTTTATCTGTCACGGATAACAGCGGTTTTACCGCAGACACCTTGAATTTAACCTTCGATGACAGC
# +
# 8#########==CFCEDCFEGGGGGGCCGFGEGEGGCGGGGGGGD9@FFCFGFDGEGCFFCCCFGGEFGG8FFGGGFGFFFCCFA<FFGFGGGG:FEFGGFGGGFGGFGGGGA?CCFGGFFGGEG7CF@FGEF8+=CFGFEFF:=CFGGGAFGFFG6C?(*-1*)/
# @M02586:164:000000000-AYBV7:1:2119:13272:24958 2:N:0:1
# ANNNNNNNNNCTGGAAATTGTAACCCATAGGCGGTCCATGTGCGTTTCGTTCTGAGATCGTTTTTTCGTACATCGTTGACAAGCCCAAGTTCTCACCACAAGATTCGTTAGGCTCGTATCGTAATGTGGAAAGGTAGACAGGCGATTCGAGCGAGATCAAGTCGAC
# +
# 8#########=:CFGGFFGGGGGGGGG8FFGGGGFGGGGGG9FEGGGGGGGGFGGGGGGGF@FGGGGGGGGGGGGGGGGGFFGGEFGGGGGFGGCGGGGGEGFFGFFGFF7FFE<FCGGGGFEF@FGFF9EF<FFG,?;<F+DEGGCCGGGGECE*.4)72*)-5(
# ```

# 
# 
# ## <p style="color:#2C6A7F"> BAM & SAM
# 
# When sequencing a genome, one has to fractionate the DNA so pieces of the genome get sequenced. The result is a file with millions of sequences that have to be assembled back to form a genome. The fragments sizes depend on the technology that we have used. Second generation technologies produce small fragments (~35-400bp). Currently the most common sizes are 50-300bp from Illumina reads. Third generation sequencing technologies (Long Read Sequencing) provide much longer fragments (500bp-2.3Mb although they are usually 10-30kb). The task of reassembling a genome is usually not completely fulfilled. What we get are bigger fragments than those initially sequenced called contigs or scaffolds. 
# 
# If we already have a reference genome we can align [map] those sequences [reads] to the reference genome. The most common formats to show the positions at which each read has aligned in relation to the reference sequence are the **sam** format and its compressed binary version, the **bam** format. The bam format cannot be opened directly with a text editor as is in binary.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/24.MapReads.png?raw=true)
# 
# The sam format contains two sections. One is the **header** which is identified with an `@` and two Uppercase letters and then the **alignment information section** that contains the positions at which each read has aligned. The header position may be removed for analysis. 
# The alignment information is divided into 11 columns. Additionally some optional **tags** can be added for more alignment specifications.
# 
# 

# ```
# @HD     VN:1.0  SO:unsorted
# @SQ     SN:12   LN:50697278
# @PG     ID:bowtie2 PN:bowtie2  VN:2.2.5  CL:"bowtie2 -x ZV9 -S 2cells.sam -1 1.fq -2 2.fq"
# 
# ERR022484.110   137     chr12      4627377 42      76M     =       4627377 0       TTGTTCTCCACCAAGCCGCCCAGTTT    EEEEEEEEEEEEEE@EBBEEE;C AS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:76 YT:Z:UP
# ERR022484.110   69      chr12      4627377 0       *       =       4627377 0       CNGAAGCAAAGTGTGTGCGCGAAATG    !AA=CCCDBHAG=ADHADD>D>D    YT:Z:UP
# ```

# 
# 
# The main columns contain the following data. 
# 
# | Col | Field | Brief description                     |
# |-----|-------|---------------------------------------|
# | 1   | QNAME | Query template NAME                   |
# | 2   | FLAG  | bitwise FLAG                          |
# | 3   | RNAME | Reference sequence NAME               |
# | 4   | POS   | leftmost mapping POSition             |
# | 5   | MAPQ  | MAPping Quality                       |
# | 6   | CIGAR | CIGAR string                          |
# | 7   | RNEXT | Reference name of the mate/next read  |
# | 8   | PNEXT | Position of the mate/next read        |
# | 9   | TLEN  | observed Template LENgth              |
# | 10  | SEQ   | segment SEQuence                      |
# | 11  | QUAL  | ASCII of Phred-scaled base QUALity+33 |
# 
# We won't enter into detail of what the codes mean in the sam format. For further details you can check the [format specifications](http://samtools.github.io/hts-specs/SAMv1.pdf) and the [optional tags descriptions](https://samtools.github.io/hts-specs/SAMtags.pdf).
# 
# ## <p style="color:#2C6A7F"> Annotation formats
# 
# Genome **annotation** is the process of identifying the **locations of genes** and all of the coding regions in a genome [structural annotation] and determining what those genes do [functional annotation]. There are several formats for representing the locations of genes in a genome. Annotation formats contain the name of the gene, the positions at which each gene starts and ends in reference to the genomic sequence, and the positions of the different parts of the gene **[features]** that have been annotated [UTRs, Exons, Promoters, etc]. Some genes can have various forms **[transcripts]** due to **alternative splicing**. The genomic sequence can be in scaffolds or chromosomes. Here you can see some examples of different annotation formats. All of them are basically tables, contain columns that are usually separated by a `tab` and rows. Tables are in **tabular** format. Annotation formats are flexible. They vary since programs may require slight modifications. These are just general examples.
# 
# 
# **BED** [Browser Extensible Data]
# Basic format [columns 1-3 are required]. Genome start at position 0 [0-based]. 
# 
# ```
# #chr	start end
# chr12		10134		10600		
# chr12		10977		11008
# chr12		13409		14312
# ```
# **BED** Extended format - groups [Each line represents a transcript].
# 
# ```
# #chr start end name score strand block_count(number of exons) block_sizes(each exon size)
# chr22 1000 5000 cloneA 960 + 1000 5000 0 2 567,488, 0,3512
# chr22 2000 6000 cloneB 900 - 2000 6000 0 2 433,399, 0,3601
# ```
# **BED** Extended format - rgb  [indicates color of thick lines of transcripts in a genome browser].
# 
# ```
# #chr	start end	name	score	strand	thick_start	thick_end rb
# chr12	10134	10600	Exon1 100	+	10180	10600	255,0,0
# chr12	10977	11008	Exon2 100 + 10977	11000 255,0,0
# chr12	13409	14312	Exon3 100 + 13409	14300 255,0,0
# chr12	18114	18423	Exon4 100 - 18150	18423 0,0,255
# ```
# 
# **GTF** [Gene Transfer Format]
# Genome starts at position 1 [1-base]. Each line represents a feature. The whole transcript is represented in several lines containing all its features.
# 
# ```
# #chr	program feature start end strand  frame  gene_id; transcript_id
# chr12	GF	Exon	10135	10600	100	+	.	gene_id "genA"; transcript_id	"geneA.1";
# chr12	GF	Exon	10978	11008	100	+	.	gene_id	"genA";	transcript_id	"geneA.1";
# chr12	GF	Exon	13410	14312	100	-	.	gene_id	"genB";	transcript_id	"geneB.1";
# chr12	GF	Exon	18114	18423	100	-	.	gene_id	"genB";	transcript_id	"geneB.1";
# ```
# 
# **GFF** [General Feature Format] 
# Genome starts at position 1 [1-base]. Each line represents a feature. 
# 
# ```
# ##chr	program feature start end score	strand  frame  attributes
# chr3 GF mRNA            1300  9000  .  +  .  ID=mrna0001;Name=sonichedgehog
# chr3 GF exon            1300  1500  .  +  .  ID=exon00001;Parent=mrna0001
# chr3 GF exon            1050  1500  .  +  .  ID=exon00002;Parent=mrna0001
# chr3 GF exon            3000  3902  .  +  .  ID=exon00003;Parent=mrna0001
# ```
# 
# ## <p style="color:#2C6A7F"> Sequence variation
# 
# Each individual's genome sequence is unique. The differences in the DNA sequences of individuals are ultimately responsible for differences in observable traits, such as  eye color or height, as well as for the hidden ones. For instance, that differences may determine how susceptible or resistant a plant is to a disease, or how virulent a specific pathogen is. 
# 
# In humans, there are 0.1% differences between the genomes of any two individuals.  That means, that out of a three billion base sequence, there is roughly three million differences between any two individuals. This variation can be due to substitutions, insertions or deletions. The **VCF** [Variant Call Format], and its Binary format **BCF**  are  used for giving information about sequence variation.
# 

# ```bash
# ##fileformat=VCFv4.1
# ##ApplyRecalibration="analysis_type=ApplyRecalibration input_file=[] read_buffer_size=null phone_home=NO_ET gatk_key=/
# ##CombineVariants="analysis_type=CombineVariants input_file=[] read_buffer_size=null phone_home=STANDARD 
# ##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
# ##FORMAT=<ID=PL,Number=G,Type=Integer,Description="Normalized, Phred-scaled likelihoods for genotypes as defined in the VCF specification">
# ##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency, for each ALT allele, in the same order as listed">
# ##contig=<ID=chr1,length=101,assembly=Ddip,md5=bd01f7e11515bb6beda8f7257902aa67>
# ##contig=<ID=chr2,length=101,assembly=Ddip,md5=31c33e2155b3de5e2554b693c475b310>
# ##contig=<ID=chr3,length=101,assembly=Ddip,md5=631593c6dd2048ae88dcce2bd505d295>
# ##contig=<ID=chr4,length=101,assembly=Ddip,md5=c60cb92f1ee5b78053c92bdbfa19abf1>
# ##source= Ddip haplotype map vcf for testing
# #CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  Ddip1
# chr1    75      Dd1     C       A       .       .       .       GT      0/0
# chr3    25      Dd9     C       T       .       .       .       GT      0/1
# chr3    75      Dd6     A       T       .       .       .       GT      1/1
# chr3    100     Dd8     A       T       .       .       .       GT:PS   0/0
# ```

# 
# ## <p style="color:#2C6A7F"> Sequence alignments
# After having a genome structurally annotated we may want to know the functions of each gene. Specially if we have found variation that may represent a significant change in the fenotype of an individual. For example, a variation that may represent the loss of function of a disease resistant gene. The process of finding the function of the genes is called **functional annotation** and it involves the aligning of the genes or proteins to a database to try to find homologies to already annotated proteins. The results of those alignments can be obtained in a **tabular** format; as we saw earlier, this means, a table, with rows and columns. 
# 
# Here is an example of an alignment obtained after running a program called **BLAST**
# 
# 

# ```bash
# # BLASTP 2.5.0+
# # Query: gi|49146530|ref|YP_026090.1| NADH dehydrogenase subunit 5 (mitochondrion) [Steinernema carpocapsae]
# # Database: PlusMitoDB
# # Fields: query acc., subject acc., % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score
# # 500 hits found
# gi|49146530|ref|YP_026090.1|	gi|49146530|ref|YP_026090.1|	100.000	527	0	0	1	527	1	527	0.0	981
# gi|49146530|ref|YP_026090.1|	gi|910356121|ref|YP_009161998.1|	71.619	525	149	0	1	525	1	525	0.0	709
# gi|49146530|ref|YP_026090.1|	gi|910356106|ref|YP_009161984.1|	70.476	525	155	0	1	525	1	525	0.0	709
# gi|49146530|ref|YP_026090.1|	gi|910356145|ref|YP_009162020.1|	70.857	525	153	0	1	525	1	525	0.0	708
# gi|49146530|ref|YP_026090.1|	gi|116510842|ref|YP_817460.1|	70.857	525	153	0	1	525	1	525	0.0	701
# gi|49146530|ref|YP_026090.1|	gi|910356132|ref|YP_009162008.1|	72.800	500	136	0	26	525	27	526	0.0	686
# gi|49146530|ref|YP_026090.1|	gi|5834894|ref|NP_006964.1|ND5_10021	69.714	525	159	0	1	525	1	525	0.0	674
# gi|49146530|ref|YP_026090.1|	gi|188011122|ref|YP_001905895.1|	70.611	524	154	0	1	524	1	524	0.0	669
# gi|49146530|ref|YP_026090.1|	gi|620695076|ref|YP_009027244.1|	69.466	524	160	0	1	524	1	524	0.0	669
# ```

# ----------
# 🔑 **In this section you have learned**
# 
# * to recognize the most common biological data formats
# * DNA and protein sequences [fasta]
# * Sequencing results [fastq]
# * Mapping formats [sam, bam]
# * Annotation formats [bed, gtf, gff, vcf]
# * BLAST alignment results in tabular format
# 
# 

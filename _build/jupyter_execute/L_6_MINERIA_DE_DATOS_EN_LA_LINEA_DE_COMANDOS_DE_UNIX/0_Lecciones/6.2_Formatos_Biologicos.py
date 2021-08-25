#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 03. Formatos de Datos Biológicos
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de aprendizaje**
# >Después de completar esta lección aprenderás a:
# >
# >* reconocer los formatos de datos biológicos más importantes
# >* Secuencias de ADN y proteínas [fasta]
# >* formato de secuenciación [fastq]
# >* formatos de mapeo [sam, bam]
# >* formatos de anotación [bed, gtf, gff, vcf]
# >* formato tabular de resultados de alineamientos de BLAST
# 
# 
# 
# 
#  [![09. Biological Data Formats](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide9.png?raw=true)](https://youtube.com/embed/76v6bI5DEXk "09. Biological Data Formats")
# 
# 
# La mayor parte de los datos biológicos se almacena en archivos de texto. Los datos de secuencias de ADN se muestran con letras `A``G``C``T`. Cada carácter representa uno de los cuatro nucleótidos (bases) *adenina, guanina, citocina y timina* respectivamente. De manera similar los datos de proteínas se representan con letras; donde un carácter es asignado para cada aminoácido. Las letras pueden ser mayúsculas o minúsculas. Cuando tienes una mezcla de mayúsculas y minúsculas en el mismo archivo generalmente significa que las minúsculas son **bases enmascaradas** y no serán tomadas en cuenta en algunos procesos por ciertos programas. También si hay un nucleótido desconocido se representa con la letra `N` y un aminoácido desconocido se representa con la letra `X`. 
# 
# 
# 
# | Aminoácido                  | Código de tres letras | Código de una letra |
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
# El formato más común para almacenar información de secuencias de ADN y proteínas es el formato `fasta`, el cual se originó de un programa que lleva el mismo nombre.
# El archivo `.fasta` contiene un `>` seguido de un identificador y en la siguiente línea la secuencia en nucleótidos o aminoácidos (representados con una sola letra). La secuencia puede estar en una sola línea
# 
# 
# ```
# >sequence_1
# ATTTATGGCCCGCGATGTACGCCATCCAGACTTAACAGTGGGACATGGCACACAGTTGAGAGGGCACAAAATATTTAGACAGATAC
# ```
# o en más de una línea, usualmente de 60 caracteres por línea
# 
# 
# ```
# >sequence_2
# AAGCTTCGGCATAGGACAAGATGGAGAGGGACGCATTGTGGAAGGCGCGCTGGGTGTTTTGGCAACCAGC
# GCAGTTGCCTGTTTGTGGTTAACATAGCTGTTACGAGAAGACGAGCGGCAAAGCTGTCATGCGTCTTGCT
# GTGCGAACGCAGTCGTCGGGCGAATTGTCCGTACGCGGGTGGTGGGGGGTGCAAATAGCCTGCGCTTGCA
# TTTCAGCCTGGGCATTCGAGTGGAATATTATTGTGTTACACTGTACAAAAAAAAAAAGCTT
# ```
# Los registros en un archivo fasta también pueden tener descripciones. Estas vienen después del identificador, generalmente después de un espacio. 
# ```
# >QBF53359.1 RxLR [Phytophthora capsici]
# MSKVFLLLVLSVFALVSCDALSAPVGSKLSLSKTDELNAQPIDAKRMLRAQEEPTNAADEERGMTELANK
# FKAWAAAIKTWVTNSKLVQSMNNKLASLTQKGRVGQIEKLLKQDNVNVNVLYQNKVKPDELFLALKLDPK
# LKLIADAPAAWANNPGLSMFYQYATYYAKMTTKA
# ```
# 
# También puedes tienes múltiples secuencias en un archivo fasta.
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
# Las extensiones más comunes utilizadas en estos archivos son  `.fasta`, `.fa`, `.fna`[para nucleótidos], `.faa` [para aminoácidos], `.fsa`, or `.fas`.
# 
# ## <p style="color:#2C6A7F"> FASTQ
# 
# Los archivos de secuenciación masiva, también llamados de nueva generación pueden venir en varios formatos, sin embargo, el formato más común es **fastq** y los otros formatos usualmente son convertidos a fastq para su análisis. 
# 
# 
# ### Características del formato `fastq` 
# 
# * Cada registro siempre contiene **cuatro líneas** 
# * La **primera línea**  comienza con un `@` seguido del **identificador de la secuencia**
# * El contenido de la primera línea varía dependiendo de la máquina de secuenciación, versión, y programa de conversión. Sin embargo, usualmente contiene información acerca de la corrida de secuenciación y cluster de ubicación.
# * La **segunda línea** contiene la **secuencia** o **las bases llamadas (A,C,T,G)** o N si no se pudo identificar bien la base. 
# * La **tercer línea** contiene un signo `+` y en algunos casos se repite el identificador de la línea uno.
# * La **cuarta línea** contiene el puntaje de **calidad** de cada baseen formato ASCII
#  
# 
# 
# ```
# @<identifier and expected information>
# <sequence>
# +<identifier and other information OR empty string>
# <quality>
# ```
# La información específica contenida en la descripción de la primera línea puedes encontrarla [aquí](https://help.basespace.illumina.com/articles/descriptive/fastq-files/)
# 
# ### Ejemplo de un registro en formato fastq:
# 
# ```
# @SIM:1:FCX:1:15:6329:1045 1:N:0:2
# TCGCACTCAACGCCCTGCATATGACAAGACAGAATC
# +
# <>;##=><9=AAAAAAAAAA9#:<#<;<<<????#=
# 
# ```
# Cada registro representa una lectura de secuenciación
# 
# ### Librerías Pareadas
# En las librerías *paired-end* o *mate-paired* obtenemos dos secuencias que están asociados al mismo registro  [tienen el mismo identificador]. En realidad vienen de dos extremos de un mismo fragmento de ADN. Ambos pares pueden venir en **archivos separados** o en el mismo archivo **intercalados** [*interleaved*]. El formato más común es en archivos separados. En cualquiera de los dos casos los pares que tienen el mismo identificador tienen que ser diferenciados. Los archivos intercalados primero tienen el par sentido*forward* `F` seguido del antisentido *reverse* `R`. Cuando están en archivos separados se indican en la primera línea con   `/1` and `/2` o en versiones más recientes `1:Y:18:ATCACG` y `2:Y:18:ATCACG`
# 
# **Ejemplo del archivo con uno de los pares de cada registro** `1:N:0:1`

# In[1]:


@M02586:164:000000000-AYBV7:1:2119:13975:24958 1:N:0:1
ACGTTGTGCCAGCCGGGTGAGAAAGTAGCTGTCCGTTTCGCTGGTCTGGTCAATATGCGGGATCTTAACGCTATCAAGTTCCTGCGGGATTACTGGCAGATCTAATTTATTCCGGCTTGAAATGATTCTGACAATCGCGCCGAGCGTGTAATCATCGTAAGACTGG
+
CCCCCGGGGGGGFGGGGGGFFEGGGGGGGFCFEEGFGFFFGGGGGGGGGGGGGGFGGFG@:CFGGGGGGGGGGGGGGFFGGFFGGDGGGGGGGGFGFGGFGGGGGGGGGGD<FGGGGGGGGGGGGGGGFFFFGFF8CGGDFFEGGGGGGFGGDFGGG<DCFGGCFG
@M02586:164:000000000-AYBV7:1:2119:13272:24958 1:N:0:1
CACTCACTAGCGACCCACTTGGAGGTCGCCAAAAGCAATATTATCCATATCTCGGAGGATTTGGACCAGATCCAGGTCGTCATCGAATTGCCTGGAGAACGGCACGAACTTGGTGCTACGACGAAGTGGAAACGCACAGCAACTTCTGGAGGGAGTGTTGGATCGA
+
CCCCCGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGFGGGGGGGGGGGGGGGGGGGGGGGGGGGDFFGGGGGGGGGGGGGGGGGGGGGGGGCFGGGGGGGGGGDGGGGGGGGGGGGFFG:@GGFGGGGGGG5>,


# **Ejemplo del archivo del segundo par de cada registro** `2:N:0:1`

# In[ ]:



@M02586:164:000000000-AYBV7:1:2119:13975:24958 2:N:0:1
TNNNNNNNNNCAGTTACCCGTGGGGGCTCGCATCGCACCCGCATTCACGCTGACGATAAAAAATAAGGTGCTGGAAGAAAATATCTCTGCTCGGATCATCAGTTTATCTGTCACGGATAACAGCGGTTTTACCGCAGACACCTTGAATTTAACCTTCGATGACAGC
+
8#########==CFCEDCFEGGGGGGCCGFGEGEGGCGGGGGGGD9@FFCFGFDGEGCFFCCCFGGEFGG8FFGGGFGFFFCCFA<FFGFGGGG:FEFGGFGGGFGGFGGGGA?CCFGGFFGGEG7CF@FGEF8+=CFGFEFF:=CFGGGAFGFFG6C?(*-1*)/
@M02586:164:000000000-AYBV7:1:2119:13272:24958 2:N:0:1
ANNNNNNNNNCTGGAAATTGTAACCCATAGGCGGTCCATGTGCGTTTCGTTCTGAGATCGTTTTTTCGTACATCGTTGACAAGCCCAAGTTCTCACCACAAGATTCGTTAGGCTCGTATCGTAATGTGGAAAGGTAGACAGGCGATTCGAGCGAGATCAAGTCGAC
+
8#########=:CFGGFFGGGGGGGGG8FFGGGGFGGGGGG9FEGGGGGGGGFGGGGGGGF@FGGGGGGGGGGGGGGGGGFFGGEFGGGGGFGGCGGGGGEGFFGFFGFF7FFE<FCGGGGFEF@FGFF9EF<FFG,?;<F+DEGGCCGGGGECE*.4)72*)-5(


# 
# 
# ## <p style="color:#2C6A7F"> BAM & SAM
# 
# Cuando secuenciamos un genoma, uno tiene que fraccionar el ADN de manera que  se secuencian fragmentos del genoma. El resultado es un archivo con millones de secuencias que tienen que volver a ser ensambladas para formar el genoma. El tamaño de los fragmentos depende de la tecnología que utilicemos. Las tecnologías de segunda generación nos darán pedazos pequeños (~35-400bp). Actualmente, los tamaños más comunes son de 50-300bp de lecturas de Illumina.  Los secuenciadores de tercera generación (Secuenciación de lecturas largas) producen pedazos mucho más grandes (500bp-2.3Mb aunque generalmente de 10-30kb). La tarea de ensamblar todos los fragmentos del genoma generalmente no se logra. Lo que obtenemos son fragmentos más grandes que aquellos que secuenciamos inicialmente llamados contigs o scaffolds. 
# 
# Si ya tenemos un genoma de referencia,  podemos alinear [mapear] las secuencias [lecturas] al genoma de referencia. Los formatos más comunes para mostrar las posiciones a las que cada lectura ha alineado en relación a la secuencia de referencia son el formato **sam** y su versión binaria comprimida, el formato **bam**. El formato bam no se puede abrir directamente con un editor de texto, ya que es binario. 
# 
# 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/24.MapReads.png?raw=true)
# 
# El formato sam contiene dos secciones. Una es el **encabezado** es cual se identifica con el símbolo `@` y dos letras mayúsculas. La otra sección contiene **información del alineamiento**. Esta contiene las posiciones en las que cada lectura ha alineado. El encabezado puede ser eliminado para hacer los análisis. 
# 
# La información del alineamiento está dividida en 11 columnas. Adicionalmente algunas **etiquetas** opcionales con más especificaciones del alineamiento pueden ser agregadas. 
# 
# 

# In[3]:



@HD     VN:1.0  SO:unsorted
@SQ     SN:12   LN:50697278
@PG     ID:bowtie2 PN:bowtie2  VN:2.2.5  CL:"bowtie2 -x ZV9 -S 2cells.sam -1 1.fq -2 2.fq"

ERR022484.110   137     chr12      4627377 42      76M     =       4627377 0       TTGTTCTCCACCAAGCCGCCCAGTTT    EEEEEEEEEEEEEE@EBBEEE;C AS:i:0  XN:i:0  XM:i:0  XO:i:0  XG:i:0  NM:i:0  MD:Z:76 YT:Z:UP
ERR022484.110   69      chr12      4627377 0       *       =       4627377 0       CNGAAGCAAAGTGTGTGCGCGAAATG    !AA=CCCDBHAG=ADHADD>D>D    YT:Z:UP


# Las principales columnas contienen los siguientes datos: The main columns containg the following data. 
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
# En esta lección no entraremos en más detalles de lo que significan los códigos en el formato sam. Para mayores detalles puedes revisar las [especificaciones de formato](http://samtools.github.io/hts-specs/SAMv1.pdf) y las [descripciones de las etiquetas opcionales](https://samtools.github.io/hts-specs/SAMtags.pdf).
# 
# ## <p style="color:#2C6A7F"> Formatos de anotación
# 
# La **anotación** del genoma es el proceso mediante el cual se identifica la **ubicación de los genes** y todas las regiones codificantes en un genoma [anotación estructural] y se identifican las funciones de esos genes [anotación funcional]. 
# Existen diferentes formatos para representar la ubicación de los genes en un genoma. Los formatos de anotación contienen el nombre del gen, las posiciones en las que cada gene empieza y termina con referencia a la secuencia genómica, y las posiciones de las diferentes partes de cada gene **[features]** que han sido anotados [UTRs, Exones, Promotores, etc]. Algunos genes pueden tener varias formas diferentes  **[transcripts]** debido al proceso de **splicing alternativo**. La secuencia genómica puede estar en scaffolds y cromosomas. Aquí puedes ver algunos ejemplos de diferentes formatos de anotación. Todos son básicamente tablas; contienen columnas que usualmente están separadas por una tabulación `tab` y también contienen filas. A las tablas se les conoce como formato **tabular**. Los formatos de anotación son flexibles. Varían debido a que los programas pueden requerir algunas modificaciones. Estos son solamente unos ejemplos generales. 
# 
# 
# **BED** [Browser Extensible Data]
# Formato básico [las columnas 1-3 son requeridas]. El genoma empieza en la posición 0 [0-based]. 
# 
# ```
# #chr	start end
# chr12		10134		10600		
# chr12		10977		11008
# chr12		13409		14312
# ```
# **BED** Formato extendido - grupos [cada línea representa un transcrito].
# 
# ```
# #chr start end name score strand block_count(number of exons) block_sizes(each exon size)
# chr22 1000 5000 cloneA 960 + 1000 5000 0 2 567,488, 0,3512
# chr22 2000 6000 cloneB 900 - 2000 6000 0 2 433,399, 0,3601
# ```
# **BED** Formato extendido - rgb  [indica el color de las líneas gruesas cuando se usa el archivo en un explorador de genomas].
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
# El genoma comienza en la posición 1 [1-base]. Cada línea representa un *feature* El transcrito completo es representado en varias líneas que contienen estos *features*.
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
# El genoma comienza en la posición 1 [1-base]. Cada línea representa un *feature*  
# 
# ```
# ##chr	program feature start end score	strand  frame  attributes
# chr3 GF mRNA            1300  9000  .  +  .  ID=mrna0001;Name=sonichedgehog
# chr3 GF exon            1300  1500  .  +  .  ID=exon00001;Parent=mrna0001
# chr3 GF exon            1050  1500  .  +  .  ID=exon00002;Parent=mrna0001
# chr3 GF exon            3000  3902  .  +  .  ID=exon00003;Parent=mrna0001
# ```
# 
# ## <p style="color:#2C6A7F"> Variación de secuencia
# 
# El genoma de cada individuo es único. Las diferencias en las secuencias de ADN entre los organismos son finalmente responsables de las diferencias en las características observable, como el color de los ojos o la estatura, y de las no observables. Por ejemplo, esas diferencias pueden determinar qué tan susceptible o resistente es una planta para determinada enfermedad, o qué tan virulento es un patógeno. 
# 
# En humanos, existen 0.1% de diferencias entre el genoma de dos individuos. Eso significa que de una secuencia de 3,000 millones de bases existen al rededor de 3 millones de diferencias entre cada dos individuos. Esta variación puede ser debida a sustituciones, inserciones o deleciones. El formato **VCF** [Variant Call Format], y su formato binario  **BCF** se utilizan para dar información sobre la variación entre secuencias. 

# In[ ]:


##fileformat=VCFv4.1
##ApplyRecalibration="analysis_type=ApplyRecalibration input_file=[] read_buffer_size=null phone_home=NO_ET gatk_key=/
##CombineVariants="analysis_type=CombineVariants input_file=[] read_buffer_size=null phone_home=STANDARD 
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=PL,Number=G,Type=Integer,Description="Normalized, Phred-scaled likelihoods for genotypes as defined in the VCF specification">
##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency, for each ALT allele, in the same order as listed">
##contig=<ID=chr1,length=101,assembly=Ddip,md5=bd01f7e11515bb6beda8f7257902aa67>
##contig=<ID=chr2,length=101,assembly=Ddip,md5=31c33e2155b3de5e2554b693c475b310>
##contig=<ID=chr3,length=101,assembly=Ddip,md5=631593c6dd2048ae88dcce2bd505d295>
##contig=<ID=chr4,length=101,assembly=Ddip,md5=c60cb92f1ee5b78053c92bdbfa19abf1>
##source= Ddip haplotype map vcf for testing
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  Ddip1
chr1    75      Dd1     C       A       .       .       .       GT      0/0
chr3    25      Dd9     C       T       .       .       .       GT      0/1
chr3    75      Dd6     A       T       .       .       .       GT      1/1
chr3    100     Dd8     A       T       .       .       .       GT:PS   0/0


# ## <p style="color:#2C6A7F"> Alineamiento de secuencias 
# Después de anotar un genoma estructuralmente seguramente querremos saber las funciones de cada gen en específico. Especialmente si hemos encontrado variación que pueda representar un cambio significativo en el fenotipo (las características)  del individuo. Por ejemplo, una variación que pueda representar la pérdida de función de un gen de resistencia a enfermedades. El proceso para buscar la función de genes es llamado **anotación funcional** e involucra el alineamiento de genes o proteínas a una base de datos para tratar de encontrar homologías a proteínas que ya están anotadas. Los resultados de esos alineamientos pueden ser obtenidos en formato **tabular**. Como vimos anteriormente, una tabla, con filas y columnas. 
# 
# Aquí se muestra un ejemplo de un alineamiento obtenido después de ejectutar un programa llamado  **BLAST**

# In[ ]:



# BLASTP 2.5.0+
# Query: gi|49146530|ref|YP_026090.1| NADH dehydrogenase subunit 5 (mitochondrion) [Steinernema carpocapsae]
# Database: PlusMitoDB
# Fields: query acc., subject acc., % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score
# 500 hits found
gi|49146530|ref|YP_026090.1|	gi|49146530|ref|YP_026090.1|	100.000	527	0	0	1	527	1	527	0.0	981
gi|49146530|ref|YP_026090.1|	gi|910356121|ref|YP_009161998.1|	71.619	525	149	0	1	525	1	525	0.0	709
gi|49146530|ref|YP_026090.1|	gi|910356106|ref|YP_009161984.1|	70.476	525	155	0	1	525	1	525	0.0	709
gi|49146530|ref|YP_026090.1|	gi|910356145|ref|YP_009162020.1|	70.857	525	153	0	1	525	1	525	0.0	708
gi|49146530|ref|YP_026090.1|	gi|116510842|ref|YP_817460.1|	70.857	525	153	0	1	525	1	525	0.0	701
gi|49146530|ref|YP_026090.1|	gi|910356132|ref|YP_009162008.1|	72.800	500	136	0	26	525	27	526	0.0	686
gi|49146530|ref|YP_026090.1|	gi|5834894|ref|NP_006964.1|ND5_10021	69.714	525	159	0	1	525	1	525	0.0	674
gi|49146530|ref|YP_026090.1|	gi|188011122|ref|YP_001905895.1|	70.611	524	154	0	1	524	1	524	0.0	669
gi|49146530|ref|YP_026090.1|	gi|620695076|ref|YP_009027244.1|	69.466	524	160	0	1	524	1	524	0.0	669


# 
# 🔑 **En esta sección has aprendido a**
# 
# * reconocer los formatos de datos biológicos más importantes
# * Secuencias de ADN y proteínas [fasta]
# * formato de secuenciación [fastq]
# * formatos de mapeo [sam, bam]
# * formatos de anotación [bed, gtf, gff, vcf]
# * formato tabular de resultados de alineamientos de BLAST

#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 02. Comandos de Unix para minería de datos
# ## <p style="color:#2C6A7F"> Práctica
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# 
# 
# ## <p style="color:#7f2c40">🚴 Ejercicio 1 
# Ahora es tiempo de practicar lo que has aprendido. Trata de resolver la mayor cantidad de preguntas posible. Generalmente existen varias maneras de resolver cada problema. 
# 
# Hagamos un poco de minería de datos sobre algunos archivos pequeños. Una vez que hayas aprendido esto podrás trabajar con enormes archivos de datos genómicos.
# 
# 
# 1. En tu directorio de inicio (*home*) crea un nuevo directorio llamado `Exercise1`
# 2. Crea un nuevo archivo dentro del directorio  `Exercise1` con `vim` llamado `ToyPlant.fasta`
# 
# 	puedes copiar y pegar el siguiente contenido:
# 	
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
# 3. Visualiza los permisos del archivo `ToyPlants.fasta`
# 3. Dale permiso de escritura, lectura y ejecución a todos 
# 4. ¿Cuántas líneas tiene el archivo?
# 5. ¿Cuántos registros tiene el archivo? 
# 6. ¿Cuántos registros únicos tiene el archivo?
# 7. Calcula la cantidad total de bases [el tamaño del genoma]
# 8. ¿Cuántas secuencias contienen la cadena `GATACA` [Las secuencias específicas que pueden tener determinada función o estructura son llamadas **motivos** o **dominios**.]
# 9. Has una copia de ese archivo en `Documents`.
# 10. En el directorio `Exercise1` crea el siguiente archivo llamado `ToyPlant.genes`
# 
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
# 11. ¿Cuántos transcritos tiene el archivo? [todas las líneas] 
# 12. ¿Cuántos cromosomas diferentes muestra el archivo? (columna 1; el separador entre columnas es `espacio`)
# 13. ¿Cuántos genes diferentes tiene el genoma? (column 2)
# 
# 
# ### <p style="color:#7f2c40">🚴 Ejercicio 2
# Estamos estudiando algunas proteínas que están involucradas en la patogénesis llamadas *efectores*, que se encuentran en las secuencias del fitopatógeno *Hyaloperonospora arabidopsidis*. Queremos saber cuántas de esas secuencias son efectores *RxLR* (Arginina, cualquier aminoácido, Leucina y Arginina). También queremos saber cuáles son ricas en cisteína y cuáles de esos efectores RxLR pertenecen a la cepa Emoy2. 
# 
# 
# 1. Ve al directorio `Exercise1` y crea un nuevo directorio llamado `Analysis`
# 2. Sube el siguiente archivo a tu  [terminal virtual](https://bit.ly/3d9BRCG) <br>[Hp1.fasta](https://drive.google.com/file/d/1FfirIu5Opm5y6aFB9sl20djUSK2YNuhV/view?usp=sharing) <br> 
# 3. ¿Cuántos registros tiene el archivo `Hp1.fasta`?
# 	
# 	Para las siguientes tres preguntas analizaremos los identificadores, no las secuencias
# 	
# 4. ¿Cuántos de esos registros son proteínas **RxLR**? 
# 5. ¿Cuántos de esos registros son proteínas ricas en cisteína [cysteine-rich]
# 6. ¿Cuántos de las proteínas **RxLR** pertenecen a la cepa **Emoy2**?
# 
# ___
# 
# 
# Gracias por completar esta actividad!
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

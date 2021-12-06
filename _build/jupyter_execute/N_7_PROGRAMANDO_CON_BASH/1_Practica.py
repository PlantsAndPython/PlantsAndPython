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
# Para esta práctica ve al directorio `Analysis` que habías creado en la actividad anterior.
# 
# Descarga los siguientes archivos y súbelos a tu [virtual terminal](https://bit.ly/3d9BRCG) <br>[Hp1.fasta](https://drive.google.com/file/d/1JywPKMg_mtBeMPDYh_OORinlZc5VjTpj/view?usp=sharing) (este archivo ya lo utilizaste en la actividad anterior) <br> 
# [Hp2.fasta](https://drive.google.com/file/d/1OPMD4sggxe8-p381_6t15YE4o5ylu565/view?usp=sharing) <br>[Hp3.fasta](https://drive.google.com/file/d/1yg_su_cRH4c6UgpsonglH3mF8JezG4xZ/view?usp=sharing)
#    
# 
# 
# ### <p style="color:#7f2c40">🚴 Ejercicio 1
# En la actividad anterior contestaste las siguientes preguntas para el archivo 
# `Hp1.fasta`. 
# 
# a. ¿Cuántos registros tiene el archivo `Hp1.fasta`?
# 	
# 	Para las siguientes tres preguntas analizaremos los identificadores, no las secuencias
# 	
# b. ¿Cuántos de esos registros son proteínas **RxLR**? 
# c. ¿Cuántos de esos registros son proteínas ricas en cisteína [cysteine-rich]
# d. ¿Cuántos de las proteínas **RxLR** pertenecen a la cepa **Emoy2**?
# 
# 
# 1. Ahora, crea un script en Bash llamado `Hp1_TuNombre.sh` que conteste las preguntas anteriores. Asegúrate de que use al menos una variable. 
# 
# ### <p style="color:#7f2c40">🚴 Ejercicio 2
# 
# 2. Genera una copia de tu script con el nombre `Hploop_TuNombre.sh` y modifícalo para que haga una itere sobre los archivos Hp1.fasta, Hp2.fasta y Hp3.fasta para contestar las preguntas del ejercicio 1.
# 
# ### <p style="color:#7f2c40">🚴 Ejercicio 3
# 
# 1. Si tienes acceso a un cluster de alto rendimiento o a un servidor remoto  y tienes tu usuario y contraseña es tiempo de practicar subiendo tu script del ejercicio 2 a tu directorio *home* del servidor remoto via `scp`. Conéctate al servidor para verificar que tu archivo está ahí por `ssh`.
# 
# ### <p style="color:#7f2c40">🚴 Ejercicio 4
# Hemos realizado una búsqueda de homología utilizando BLAST con los scaffolds de un genoma secuenciado recientemente de un nematodo fitopatógeno contra los cromosomas del organismo modelo *Caenorhabditis elegans*. Tenemos 6 archivos tabulares con los resultados. Cada uno contiene las secuencias similares [*hits*] para cada uno de los cromosomas de *C. elegans*.
# 
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
# Queremos saber cuántos hits obtuvo cada scaffold para cada uno de los cromosomas. Los scaffolds están indicados en la columna 1 y los cromosomas en la columna 2. Para contestar esta pregunta hay que contar para cada scaffold (son 5 scaffolds) ¿cuántas veces aparece en la misma línea de cada uno de los cromosomas?
# 
# 1. Escribe un script de Bash que te diga ¿cuántos hits tiene cada scaffold para cada cromosoma (cada archivo contiene un cromosoma diferente).
# 2. De nuevo, si tienes acceso a un servidor remoto, practica copiando tu archivo al servidor. 
# 
# ---------------
# 
# Gracias por completar esta actividad!

#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F"> 01. Editar, ordenar, cortar y grep
# 
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
#  
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de aprendizaje**
# >Después de completar esta lección aprenderás cómo:
# >
# >
# >* Editar archivos en la línea de comandos
# >* Ordenar el contenido de archivos en orden alfabético y numérico
# >* Cortar columnas de archivos
# >* Buscar cadenas específicas dentro de archivos
# 
#     
#  [![07.Edit, sort, cut & grep](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide7.png?raw=true)](https://youtube.com/embed/o7k4Z_enMd0 "07.Edit, sort, cut & grep")
# 
# Ya has aprendido cómo crear un archivo con `cat > New_file`, sin embargo, `cat`no es un editor de texto. Existen varios editores de texto para la línea de comandos. Los más comunes son `vi`, `vim` y `nano`. En tu terminal virtual tienes un editor de texto con una interfaz gráfica. Sin embargo, cuando trabajes de manera remota en un cluster bioinformático para **Cómputo de Alto Desempeño [HPC]** es muy probable que no puedas usar ningún software con interfaz gráfica. Así es que es muy importante que aprendas a usar **editores de texto en la línea de comandos**.
# 
# ## <p style="color:#2C6A7F"> `vim` & `vi`
# Los editores de texto  `vim` y `vi` son muy similares. Aprenderemos los comandos más importantes para `vim` y también funcionarán para `vi`. Sin embargo si quieres aprender más opciones puedes ver la [documentación de vim](https://vimhelp.org/).
# 
# * Crear un nuevo archivo `vim Name_Of_File`
# * Editar el archivo con `i` de *insertar*
# * Guarda los cambios y sal del archivo `Esc` `:wq!`
# * Sal del archivo sin guardar cambios `Esc` `:q!`
# 
# Ahora vamos a crear un directorio dentro del directorio `Documents` llamado `Practice`. Ahora ve dentro de `Practice` y crea un archivo llamado `numbers.txt`
# Now let's create a folder inside the folder `Documents` named `Practice`. Then go inside `Practice` and create a file called `numbers.txt`
# 
# ```
# $ cd /root/sandbox/Documents
# $ mkdir Practice
# $ cd Practice
# $ vim numbers.txt
# ```
# Entrarás a una nueva pantalla
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/15.vimscreen.png?raw=true)
# 
# Después tienes que teclear `i` para poder **insertar** texto. Ahora escribe el siguiente texto:
# 
# ```
# 1
# 3
# 2
# 12
# ```
# Cuando hayas terminado de editar tu archivo, tienes que guardar los cambios y salir con la tecla `Esc` seguida de `:wq!` y `Enter`.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/16.vimSave.png?raw=true)
# 
# Puedes verificar el contenido con  `less`, `more` or `cat`. **Nota:** *No agregues `>` cuando abras un archivo para leerlo, ya que si lo haces eliminarás el contenido previo y se escribirá sobre él. 
# 
# ```
# $ cat numbers.txt
# 1
# 3
# 2
# 12
# $ 
# ```
# ## <p style="color:#2C6A7F"> `nano` 
# La ventaja de usar  `nano` es que no tienes que aprenderte el menú, ya que se muestra en la pantalla. La tecla `Ctrl` es especificada por un `^`. El problema de `nano` es que algunas veces no está instalado en los servidores. Así es que tendrías que instalarlo. 
# 
# * Crear un archivo `nano Name_Of_File`
# * Guardar los cambios `Ctrl` + `o` `Enter`
# * Salir `Ctrl` `x`
# 
# Vamos a crear un archivo llamado `toygenes.txt` en el mismo directorio `Practice`.
# 
# ```
# $ nano toygenes.txt
# ```
# Después verás la siguiente pantalla donde puedes editar tu archivo. 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/18.nano.png?raw=true)
# 
# En esta ocasión  vamos a escribir un archivo **tabular**. Eso significa que será un archivo con **columnas** y que van a estar separadas por una tabulación utilizando la tecla `tab` en lugar de la `barra espaciadora`. Escribe el siguiente texto (utilizando un `tab` después de cada nombre. 
# 
# ```
# fly	20	
# apple	10
# bear	40
# tomato	30
# ```
# Para guardar los cambios [*write out*] teclea `Ctrl` `o` 
# Después verás esta pantalla
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/19.NanoSave.png?raw=true)
# 
# Sólo presiona `Enter` y luego salte con `Ctrl` `x`
# 
# Recuerda verificar que tu archivo está correcto.
# 
# ## <p style="color:#2C6A7F"> `sort`
# 
# El comando `sort` es usado para ordenar un archivo. En otras palabras, acomodar las líneas en una list en un orden en particular. Por defecto, se ordenan en **orden alfabético**.
# 
# Inténtalo con el archivo `toygenes.txt`
# 
# ```
# $ sort toygenes.txt
# apple   10
# bear    40
# fly     20        
# tomato  30
# ```
# `sort` también ordenará los números en orden **alfabético**. Para ordenar los números en orden **numérico** necesitamos la opción `-n`. 
# ```
# $ sort numbers.txt 
# 1
# 12
# 2
# 3
# $ sort -n numbers.txt 
# 1
# 2
# 3
# 12
# $ 
# ```
# Si tienes una mezcla de letras y números, puedes usar la opción `-V` para ordenar **numéricamente**, como en las **versiones** de software. Como en el siguiente ejemplo.
# 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/20.sortV.png?raw=true)
# 
# Ahora crea el archivo llamado `amounts.txt` con el siguiente contenido:
# 
# ```
# 10
# 50
# 20
# 30
# ```
# Puedes usar cualquier editor de texto que prefieras. 
#  
# El comando `sort` tiene varias funciones útiles. Si quieres ordenar en orden reverso usa `-r` 
# 
# ```
# $ more amounts.txt 
# 10
# 50
# 20
# 30
# $ sort -r amounts.txt 
# 50
# 30
# 20
# 10
# $ 
# ```
# También puedes ordenar un archivo especificando una columna en particular con `-k`. Por ejemplo, vamos a ordenar `toygenes.txt` basándonos en la segunda columna.  
# 
# ```
# $ more toygenes.txt
# fly	20	  
# apple	10
# bear	40
# tomato	30	
# ```
# 
# ```
# $ sort -k 2 toygenes.txt
# apple	10
# fly	20
# tomato	30
# bear	40
# ```
# Puedes también ordenar un archivo y eliminar duplicados para obtener únicamente los registros **únicos** con `-u`. Por ejemplo, inténtalo con el siguiente archivo.
# 
# 
# ```
# $ more species.txt
# fly
# fly
# apple
# apple
# apple
# bear
# tomato
# ```
# 
# ```
# $ sort -u species.txt
# apple
# bear
# fly
# tomato
# ```
# Recuerda que siempre puedes guardar los resultados dirigiendo la salida con `>` a un nuevo archivo.
# 
# ```
# $ sort -u species.txt > sortunique.txt
# $ more sortunique.txt
# apple
# bear
# fly
# tomato
# ```
# También puedes ordenar meses con `sort -M`
# 
# ```
# $ more months.txt
# March
# January
# February
# April
# ```
# 
# ```
# $ sort -M months.txt
# January
# Febrary
# March
# April
# ```
# 
# ## <p style="color:#2C6A7F"> `cut`
# 
# El comando `cut` corta columnas específicas, por defecto separadas por una tabulación `tab`. Puedes especificar la columna con `-f` de *field*. Selecciona la segunda columna por el archivo **toygenes.txt**.
# 
# ```
# $ more toygenes.txt
# fly	20
# apple	10
# bear	40
# tomato	30
# ```
# 
# ```
# $ cut -f 2 toygenes.txt
# 20
# 10
# 40
# 30
# ```
# Para cambiar el separador se utiliza `-d`. Por ejemplo, para una lista que tiene columnas separadas por espacios
#  
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/21.CutSpace.png?raw=true)
# 
# También puedes seleccionar columnas especificando la posición de los bytes con `-b`. Para ver más opciones, recuerda que siempre puedes ver el manual `man cut`. 
# 
# ## <p style="color:#2C6A7F"> `grep`
# 
# Uno de los comandos más útiles es `grep`, el cual te permitirá hacer búsquedas de cadenas. Imprimirá sólo las líneas que contienen la cadena que hayas indicado. Por ejemplo, vamos a buscar la cadena `tomato` en el archivo `toygenes.txt`
# 
# ```
# $ more toygenes.txt
# fly     20        
# apple   10
# bear    40
# tomato  30
# ```
# 
# ```
# $ grep 'tomato' toygenes.txt
# tomato  30
# ```
# También puedes buscar el **inverso** de la cadena con `-v`. Te mostrará las líneas que no contengan la cadena. 
# 
# ```
# $ grep -v 'tomato' toygenes.txt
# fly     20        
# apple   10
# bear    40
# ```
# 
# También puedes contar el **número de ocurrencias** con `-c`. ¿Cuántas líneas contienen la letra `a` en `toygenes.txt`?
# 
# ```
# $ grep -c 'a' toygenes.txt
# 3
# ```
#     
# -------
# 🔑 **En esta lección has aprendido a:**
# 
# * Editar archivos en la línea de comandos con `vim`, `vi` & `nano` 
# * Ordenar el contenido de un archivo en orden alfabético o numérico con `sort`
# * Cortar columnas con `cut`
# * Buscar cadenas específicas  dentro de archivos con `grep`
# 

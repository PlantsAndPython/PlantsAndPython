#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F">5.5 Copiar, mover y eliminar archivos
# 
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo est谩 bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribuci贸n-NonComercial 4.0 Licencia Internacional</a>.
# 
# > ### <p style="color:#2C6A7F"> 馃攳 **Objetivos de aprendizaje**
# > 
# > Despu茅s de completar esta lecci贸n aprender谩s a:
# >
# >* copiar archivos y directorios
# >* mover archivos y directorios a otra ubicaci贸n
# >* eliminar archivos y directorios 
# >* uso de *wildcards* (comodines) para seleccionar m谩s de un archivo
# 
# 
#     
#  [![06.Copy Move and Remove Files](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide6.png?raw=true)](https://youtube.com/embed/tab0cbwOACQ "06.Copy Move and Remove Files")
# 
# ## <p style="color:#2C6A7F">`cp`
# El comando `cp` es utilizado para copiar archivos y directorios. Puedes usarlo de diferentes maneras.  
# 
# * para copiar un archivo a la misma ubicaci贸n pero con diferente nombre `cp file file.copy`
# * para copiar un archivo a diferente ubicaci贸n con el mismo nombre `cp file new/location/file`
# * para copiar un archivo a diferente ubicaci贸n con diferente nombre `cp file new/location/file.copy`
# 
# En los ejemplos anteriores hemos copiado un archivo que estaba en tu directorio de trabajo. Tambi茅n puedes copiar un archivo o directorio desde otra ubicaci贸n si especificas la ruta.
# 
# * copia desde la ubicaci贸n A a la ubicaci贸n B `cp /location/A/file /location/B/file`
# * copia desde la ubicaci贸n A al directorio actual de trabajo `cp /location/A  .`
# 
# El actual directorio de trabajo se representa por un punto `.`
# 
# Ahora int茅ntalo en tu [terminal virtual](https://bit.ly/3d9BRCG). Tambi茅n puedes regresar a la terminal en la que estabas trabajando en CS50 Sandbox [https://sandbox.cs50.io/](https://sandbox.cs50.io/) en la pesta帽a de *recent sandboxes*.
# 
# Primero, ve a tu directorio **home** que es  `/root/sandbox/`. Puedes hacerlo con `cd`. Y luego copia el archivo `fruitall` al directorio `Documents`. Luego verifica que se ha copiado. Cambia de directorio de trabajo con `cd Documents` y luego enlista el contenido. Deber铆as ver el archivo `fruitall`.
# 
# ```
# $ cd
# $ fruitall Documents
# $ cd Documents
# $ ls
# Genomes/  fruitall
# ```
# Ahora copia el archivo `fruitall` a la misma ubicaci贸n con otro nombre `fruitall.copy` y de nuevo verif铆calo.
# 
# ```
# $ cp fruitall fruitall.copy
# $ ls
# Genomes/ fruitall fruitall.copy
# ```
# 
# Recuerda que tambi茅n puedes verificar el contenido del directorio en el explorador de archivos del lado izquierdo de tu terminal virtual, etiquetado como *Filetree*. Ahora que estamos en el directorio `Documents`, copiemos de tu directorio **home** al directorio `Documents` que es ahora to directorio de trabajo. 
# 
# Tenemos que especificar la ubicaci贸n del directorio que queremos copiar. Podemos hacerlo utilizando la ruta **relativa** o la ruta **absoluta**. Aqu铆 voy a usar la ruta relativa. Recuerda que los dos puntos `..` se refieren a un directorio atr谩s. En otras palabras, el directorio que contiene nuestro directorio actual. Si queremos mantener el mismo nombre, podemos especificar la ubicaci贸n; que en este caso, es nuestro directorio de trabajo y puede ser especificado con un punto `.`
# 
# ```
# $ cp ../Readme.txt .
# ```
# 
# Tambi茅n podemos copiar el mismo archivo pero con un nombre diferente `Readme.copy` 
# 
# ```
# $ cp ../Readme.txt ./Readme.copy
# ```
# Recuerda que `cp` mantendr谩 el archivo original. Si no quieres mantener el archivo original puedes usar `mv`.
# 
# 
# ## <p style="color:#2C6A7F">`mv`
# El comando `mv` **mover谩** tu archivo ya sea a otra ubicaci贸n o a la misma ubicaci贸n pero con un nombre diferente. El archivo original se eliminar谩. Vamos a mover el archivo `contents.txt` de tu directorio home a `Documents`.
# 
# ```
# $ mv ../contents.txt .
# ```
# En caso de que quieras usar la ruta absoluta, recuerda que puedes imprimir la ruta de tu directorio de trabajo con `pwd`. Ahora mueve el archivo `fruitall` de tu directorio home a `Documents` pero con un nombre direrente `allfruits`.
# 
# ```
# $ pwd
# /root/sandbox/Documents
# $ mv /root/sandbox/fruitall allfruits
# $
# ```
# El archivo original `fruitall` ha sido eliminado y tenemos una copia de 茅l en el directorio `Documents` llamado `allfruits`.
# 
# Ahora, usa el comando `mv` para cambiar el nombre de `fruitall` a `new_fruitall`. Puedes verificarlo con `ls`.
# 
# ```
# $ mv fruitall new_fruitall
# $ ls
# Genomes/  Readme.copy  Readme.txt  allfruits  contents.txt  fruitall.copy  new_fruitall
# $
# ```
# ## <p style="color:#2C6A7F">`rm` & `rmdir`
# 
# El comando `rm` y `rmdir` son usados para eliminar archivos y directorios respectivamente. Ten en cuenta que para eliminar  un directorio, este tiene que estar vac铆o. Ahora vamos a limpiar nuestro directorio de trabajo. Primero, aseg煤rate de que est谩s en tu directorio *home*. Luego enlista el contenido para ver qu茅 archivos quieres borrar. Elimina el archivo `fruit1`.
# 
# ```
# $ cd
# $ pwd
# /root/sandbox
# $ ls
# Documents/  Readme.txt  fruit1  fruit2
# $ rm fruit1
# rm: remove regular file 'fruit1'?  y
# 
# ```
# La terminal virtual est谩 configurada para preguntare si quieres eliminar el archivo. Puedes confirmarlo con la letra `y`. Sin embargo, la mayor铆a de las terminales no preguntar谩n nada y s贸lo eliminar谩n el archivo inmediatamente.
# 
# Ahora, si quieres eliminar varios archivos al mismo tiempo, podemos usar **wildcards** (comodines). Se usan para ejecutar acciones en m谩s de un archivo al mismo tiempo o para encontrar parte de una frase en un archivo de texto. De momento vamos a ver 煤nicamente el *wildcard* asterisco `*`, el cual representa cualquier n煤mero de caracteres. Por ejemplo, `ls gen*` ser谩 capaz  de enlistar los archivos `gen` `gen1` `genA.txt` `genes_prot` y `genomes`. Tambi茅n puedes usar `*` para encontrar todos los archivos con una extensi贸n en espec铆fico, como por ejemplo  `.pdf`.
# 
# ```
# $ ls *.pdf
# my_paper.pdf summary.pdf
# ```
# Ahora vamos a eliminar dos archivos que comienzan con la cadena `fruit`
# 
# ```
# $ ls
# Documents/   fruit1  fruit2
# $ rm fruit*
# $ ls
# Documents/
# ```
# 
# ---------
# 馃攽 **En esta lecci贸n has aprendido c贸mo:**
# 
# * copiar archivos y directorios con `cp` 
# * mover archivos y directorios a una ubicaci贸n diferente con `mv`
# * eliminar archivos y directorios `rm` & `rmdir`
# * utilizar *wildcards* para seleccionar m谩s de un archivo `*`
# 

# In[ ]:





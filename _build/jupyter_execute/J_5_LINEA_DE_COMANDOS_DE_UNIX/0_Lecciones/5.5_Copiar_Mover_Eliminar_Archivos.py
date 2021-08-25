#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 06. Copiar, mover y eliminar archivos
# 
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de aprendizaje**
# > 
# > Después de completar esta lección aprenderás a:
# >
# >* copiar archivos y directorios
# >* mover archivos y directorios a otra ubicación
# >* eliminar archivos y directorios 
# >* uso de *wildcards* (comodines) para seleccionar más de un archivo
# 
# 
#     
#  [![06.Copy Move and Remove Files](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide6.png?raw=true)](https://youtube.com/embed/tab0cbwOACQ "06.Copy Move and Remove Files")
# 
# ## <p style="color:#2C6A7F">`cp`
# El comando `cp` es utilizado para copiar archivos y directorios. Puedes usarlo de diferentes maneras.  
# 
# * para copiar un archivo a la misma ubicación pero con diferente nombre `cp file file.copy`
# * para copiar un archivo a diferente ubicación con el mismo nombre `cp file new/location/file`
# * para copiar un archivo a diferente ubicación con diferente nombre `cp file new/location/file.copy`
# 
# En los ejemplos anteriores hemos copiado un archivo que estaba en tu directorio de trabajo. También puedes copiar un archivo o directorio desde otra ubicación si especificas la ruta.
# 
# * copia desde la ubicación A a la ubicación B `cp /location/A/file /location/B/file`
# * copia desde la ubicación A al directorio actual de trabajo `cp /location/A  .`
# 
# El actual directorio de trabajo se representa por un punto `.`
# 
# Ahora inténtalo en tu [terminal virtual](https://bit.ly/3d9BRCG). También puedes regresar a la terminal en la que estabas trabajando en CS50 Sandbox [https://sandbox.cs50.io/](https://sandbox.cs50.io/) en la pestaña de *recent sandboxes*.
# 
# Primero, ve a tu directorio **home** que es  `/root/sandbox/`. Puedes hacerlo con `cd`. Y luego copia el archivo `fruitall` al directorio `Documents`. Luego verifica que se ha copiado. Cambia de directorio de trabajo con `cd Documents` y luego enlista el contenido. Deberías ver el archivo `fruitall`.
# 
# ```
# $ cd
# $ fruitall Documents
# $ cd Documents
# $ ls
# Genomes/  fruitall
# ```
# Ahora copia el archivo `fruitall` a la misma ubicación con otro nombre `fruitall.copy` y de nuevo verifícalo.
# 
# ```
# $ cp fruitall fruitall.copy
# $ ls
# Genomes/ fruitall fruitall.copy
# ```
# 
# Recuerda que también puedes verificar el contenido del directorio en el explorador de archivos del lado izquierdo de tu terminal virtual, etiquetado como *Filetree*. Ahora que estamos en el directorio `Documents`, copiemos de tu directorio **home** al directorio `Documents` que es ahora to directorio de trabajo. 
# 
# Tenemos que especificar la ubicación del directorio que queremos copiar. Podemos hacerlo utilizando la ruta **relativa** o la ruta **absoluta**. Aquí voy a usar la ruta relativa. Recuerda que los dos puntos `..` se refieren a un directorio atrás. En otras palabras, el directorio que contiene nuestro directorio actual. Si queremos mantener el mismo nombre, podemos especificar la ubicación; que en este caso, es nuestro directorio de trabajo y puede ser especificado con un punto `.`
# 
# ```
# $ cp ../Readme.txt .
# ```
# 
# También podemos copiar el mismo archivo pero con un nombre diferente `Readme.copy` 
# 
# ```
# $ cp ../Readme.txt ./Readme.copy
# ```
# Recuerda que `cp` mantendrá el archivo original. Si no quieres mantener el archivo original puedes usar `mv`.
# 
# 
# ## <p style="color:#2C6A7F">`mv`
# El comando `mv` **moverá** tu archivo ya sea a otra ubicación o a la misma ubicación pero con un nombre diferente. El archivo original se eliminará. Vamos a mover el archivo `contents.txt` de tu directorio home a `Documents`.
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
# El archivo original `fruitall` ha sido eliminado y tenemos una copia de él en el directorio `Documents` llamado `allfruits`.
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
# El comando `rm` y `rmdir` son usados para eliminar archivos y directorios respectivamente. Ten en cuenta que para eliminar  un directorio, este tiene que estar vacío. Ahora vamos a limpiar nuestro directorio de trabajo. Primero, asegúrate de que estás en tu directorio *home*. Luego enlista el contenido para ver qué archivos quieres borrar. Elimina el archivo `fruit1`.
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
# La terminal virtual está configurada para preguntare si quieres eliminar el archivo. Puedes confirmarlo con la letra `y`. Sin embargo, la mayoría de las terminales no preguntarán nada y sólo eliminarán el archivo inmediatamente.
# 
# Ahora, si quieres eliminar varios archivos al mismo tiempo, podemos usar **wildcards** (comodines). Se usan para ejecutar acciones en más de un archivo al mismo tiempo o para encontrar parte de una frase en un archivo de texto. De momento vamos a ver únicamente el *wildcard* asterisco `*`, el cual representa cualquier número de caracteres. Por ejemplo, `ls gen*` será capaz  de enlistar los archivos `gen` `gen1` `genA.txt` `genes_prot` y `genomes`. También puedes usar `*` para encontrar todos los archivos con una extensión en específico, como por ejemplo  `.pdf`.
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
# 🔑 **En esta lección has aprendido cómo:**
# 
# * copiar archivos y directorios con `cp` 
# * mover archivos y directorios a una ubicación diferente con `mv`
# * eliminar archivos y directorios `rm` & `rmdir`
# * utilizar *wildcards* para seleccionar más de un archivo `*`
# 

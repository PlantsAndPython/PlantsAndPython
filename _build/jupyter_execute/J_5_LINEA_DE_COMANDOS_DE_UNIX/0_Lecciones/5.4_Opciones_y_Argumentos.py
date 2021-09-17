#!/usr/bin/env python
# coding: utf-8

# 
# 
# # <p style="color:#2C6A7F">5.4 Opciones y argumentos
# 
# **Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
#  [![05. Options & Arguments](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide5.png?raw=true)](https://youtube.com/embed/KI7YtuHAGUU "05. Options & Arguments")
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de Aprendizaje**
# >Después de completar esta lección aprenderás sobre:
# >
# > * Las opciones de los comandos
# > * Los argumentos para los comandos
# > * Cómo agregar comentarios
# > * Cómo acceder al manual de cada comando a través de `man`
# >
# >
# Podemos modificar el comportamiento de los comando usando **opciones** y **argumentos**. Por ejemplo, el comando `mkdir` necesita el nombre del directorio que quieres crear. El nombre del directorio es el *argumento*. Cada argumento está generalmente separado por **un espacio** `mkdir nuevo_directorio`. Es por eso que debes de evitar agregar espacios en los nombres de los archivos y directorios. También debes evitar otros símbolos, ya que tienen significados especiales en la terminal de bash. **El guión bajo** `_` y el **punto** `.` son símbolos aceptados en los nombres de los archivos y directorios. Los comandos pueden tener más de un argumento. Por ejemplo para concatenar tres archivos necesitamos el nombre de tres archivos 
# 
# 
# ```
# $ cat file1 file2 file3`  #tres argumentos
# ```
# 
# >**Nota** Si ves un símbolo de `#` en la línea de comandos on en un script (programa) de bash, significa que hay un comentario.  La única excepción es si está seguido de un signo de admiración `#!` al principio de la línea en *script*. en este caso es usado para indicar la ruta para el interprete correcto para correr ese *script* `#!/bin/bash` o `#!/bin/python`. Los comentarios son utilizados para explicar el código. Únicamente para información. En el ejemplo anterior no tienes que teclear lo que está después del `#` en la línea de comandos, ya que no será ejecutado. 
#  
# Algunos argumentos son **obligatorios**. Por ejemplo, `head` necesita el nombre de un archivo como argumento `head file.txt` para indicarle a head qué archivo va a abrir o `mkdir Folder.txt` para indicar el folder que será creado. Otros argumentos son **opcionales**. El comando `ls` enlistará el contenido del directorio actual a menos que especifiquemos un directorio en particular. Así `ls Documents` enlistará el contenido del directorio `Documents`. 
# 
# Los comandos también tienen **opciones**. Las opciones comúnmente están indicadas por un guión o dos  `-v` o `--version`. Usualmente un sólo guión va seguido de una letra y doble guión va seguido de una palabra completa. Para aprender sobre las diferentes opciones de un comando en particular puedes checar el **manual**. Puedes acceder a este con el comando `man` y el nombre del comando. Vamos a tu terminal y veamos el manual del comando `ls`.
# 
# 
# ```
# $ man ls 
# ```
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/14.manls.png?raw=true)
# 
# 
# El manual aparecerá en otra pantalla. Para salir del manual y regresar a la línea de comandos presiona `q`.
# 
# Existen muchos comandos y tienen muchas opciones. No tienes que preocuparte por aprendértelos todos ya que comúnmente sólo usarás algunos comandos y algunas opciones. Por ejemplo, aquí te muestro algunas opciones muy útiles para el comando `ls`. Prueba todas para que veas cómo funcionan.
# 
# 
# * `ls -a` enlista  **todos** los archivos y directorios, incluyendo los archivos ocultos que son los que comienzan con  `.` o `..`
# * `ls -l` incluye una **descripción larga**. [archivo/directorio, permisos, número de objetos, propiedad, grupo, tamaño del archivo, fecha de modificación y nombre del archivo]
# * `ls -h` usado con `-l` muestra el tamaño del archivo en una forma  **legible por humanos** representando bytes, kilobytes, gigabytes, terabytes, etc con B, K, G y T respectivamente.
# * `ls -p` agrega una `/` al final de cada nombre de directorio.
# *  `ls -t` la lista es impresa en orden de tiempo de creación. 
# * `ls -r` usado con `-t` la lista es impresa en **orden reverso**, de más antiguo a más nuevo.
# 
# Algunas opciones pueden ser utilizadas juntas y pueden escribirse de dos maneras `ls -lhtrp` or `ls -l -h -t -r -p`.
# 
#     
# --------    
# 🔑 **En esta lección has aprendido sobre** 
# 
# > * Las opciones de los comandos
# > * Los argumentos para los comandos
# > * Cómo agregar comentarios
# > * Cómo acceder al manual de cada comando a través de `man`

# In[ ]:





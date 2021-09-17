#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F">6.1 Contar palabras, tuberías & permisos
# 
# ***Autora:  Alejandra Rougon*** 
# 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# 
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de aprendizaje**
# >Después de completar esta lección aprenderás a:
# >
# * Contar caracteres, palabras y líneas 
# * Crear tuberías (*pipelines*)
# * Cambiar los permisos
# 
#  [![08.Word Count, Pipelines & Permissions](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide8.png?raw=true)](https://youtube.com/embed/bgznxzyqFsk "08.Word Count, Pipelines & Permissions")
# 
# 
# ## <p style="color:#2C6A7F"> `wc`
# 
# El comando `wc` que viene de *word count* cuenta **caracteres**, **palabras** y **líneas** 
#  
# 
# ```
# $ more amounts.txt
# 10
# 50
# 20
# 30
# ```
# 
# ```
# $ wc amounts.txt
#  4  4 12 amounts.txt
# ```
# Los números significan cantidad de **líneas**, **palabras** y **caracteres**, respectivamente. Cuatro líneas, cuatro palabras y ... espera! ¿Por qué obtenemos 12 caracteres si sólo podemos ver 8? Esto es porque la el cambio de una **nueva línea**  es también un caracter 👆
# Puedes especificar líneas con `-l`, palabras con `-w` y caracteres con `-c`.
# 
# 
# ```
# $ wc -l amounts.txt
#  4 amounts.txt
# ```
# ## <p style="color:#2C6A7F"> Tuberías  `|`
# Muchas veces podrías querer usar la salida de un comando como entrada de otro comando. A eso se le llama *pipeline* o tubería y podemos hacerlo con **la barra vertical** también llamada **pipe** `|`. 
# 
# Ahora imprime las líneas que contengan la letra `e` en el archivo `allfruits` en orden alfabético. Así es que primero tienes que encontrar las líneas con `grep` y luego ordenarlas alfabéticamente con `sort`.  *Recuerda que `allfruits` está en el directorio `Documents` así es que tienes que cambiarte de directorio o escribir la ruta al archivo.*
# 
# ```
# $ grep 'e' /root/sandbox/Documents/allfruits
# pear
# orange
# melon
# ```
# 
# Si quieres agregar la salida anterior como entrada del comando `sort` agrega `|`y luego `sort`.
# 
# 
# ```
# $ grep 'e' /root/sandbox/Documents/allfruits | sort
# melon
# orange
# pear
# ```
# 
# 
# El símbolo `|` tomará la salida de un comando y la usará en el siguiente comando. Pero qué tal si quieres simplemente ejecutar dos comandos diferentes? Por ejemplo, cambiar de directorio y luego buscar una cadena dentro de un archivo. En ese caso puedes usar un **punto y coma** `;` 
# 
# Ahora vamos a encontrar ¿cuántos caracteres contienen las palabras que tienen una `p` en el archivo `toygenes.txt` que está en el directorio `Practice`. Así es que primero ve al directorio `Practice`, luego busca las líneas con la letra `p`con `grep` y toma la salida como entrada de `cut` para seleccionar sólo la columna que contiene las palabras y luego cuenta los caracteres con `wc`.
#  
# 
# 
# ```
# $ cd Practice ; grep 'p' toygenes.txt | cut -f 1 | wc -c
# 6
# ```
# 
# En efecto, la palabra `apple` contiene `5` letras y es la única palabra que contiene una `p`. Esto será muy útil cuando empecemos a minar datos biológicos. 
# 
# 
# ## <p style="color:#2C6A7F"> `chmod`
# 
# En sistemas UNIX y derivados de UNIX todos los archivos y directorios pueden tener diferentes permisos para el **usuario** [dueño del archivo] `u`, el **grupo** [usuarios específicos asignados por el administrador] `g`, para los **otros** [cualquier otra persona] o para todos **all** [usuario, grupo y otros]. Esto te permite proteger tus archivos hasta de ti mismo. 
# 
# Los diferentes permisos son **reading** [lectura] `r`, **writing** [escritura] `w`, y **executing** [ejecución] `x`.
# 
# Para ver los permisos de tus archivos y directorios en el directorio `Documents`, cambia de directorio de trabajo `cd /root/sandbox/Documents` y luego teclea `ls -l`
# 
# 
# ```
# $ ls -l
# total 5
# drwxr-xr-x 2 root root  2 Apr 10 21:35 Genomes/
# drwxr-xr-x 2 root root  6 Apr 24 18:22 Practice/
# -rw-r--r-- 1 root root 87 Apr 24 17:02 Readme.copy
# -rw-r--r-- 1 root root 64 Apr 23 21:03 Readme.txt
# -rw-r--r-- 1 root root 31 Apr 24 20:26 allfruits
# -rw-r--r-- 1 root root 70 Apr 23 14:49 contents.txt
# -rw-r--r-- 1 root root 31 Apr 23 20:52 fruitall.copy
# -rw-r--r-- 1 root root 31 Apr 23 20:47 new_fruitall
# ```
# 
# Puedes ver cómo los permisos están distribuidos en diferentes posiciones en la siguiente imagen. 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/22.Permissions.png?raw=true)
# 
# La primera posición indica si es un **archivo** o un **directorio**, la siguientes tres posiciones pertenecen al **usuario** [dueño]. Si ella/el tiene permisos de lectura, escritura y ejecución verás `rwx` si alguno de esos permisos no está disponible, estará representado con un `-`. Las tres posiciones de en medio representan los permisos del **grupo**, y las últimas tres representan a los **otros** [los permisos de cualquier otra persona].
# 
# Existen dos maneras de cambiar los permisos. Una es a través de **caracteres** y la otra es a través de números, llamada el modo **octal**.
# 
# 
# 
# ### Modo de caracteres
# En este modo puedes cambiar los permisos con símbolos. Agrega `+`, elimina `-`, especifica un permiso `=`. Por ejemplo:
# 
# * `chmod +r myfile.txt`  agrega permisos de **r**ead [lectura] a **todos** 
# * `chmod g-w myfile.txt`  elimina permisos de **w**rite [escritura] al **groupo**
# * `chmod u+x myfile.txt` agrega permisos de e**x**ecute [ejecución] al **usuario**
# * `chmod u=rw, go=  myfile.txt` agrega permisos de **r**ead & **w**rite [lectura y escritura] al  **usuario** and elimina **r**ead, **w**rite & e**x**ecute al **grupo y a los otros**
# 
# ### Modo octal
# En el modo octal cada combinación de permisos representa un número. 
# 
# | Número | Binario | Lectura/read [r] | Escritura/write [w] | Ejecución/Execute (x) |
# |:------:|:------:|:--------:|:---------:|:-----------:|
# | 0      | 000    |      ❌    |      ❌     |       ❌      |
# | 1      | 001    |      ❌    |      ❌     |      👍      |
# | 2      | 010    |      ❌    |     👍     |       ❌      |
# | 3      | 011    |      ❌    |     👍     |      👍      |
# | 4      | 100    |     👍    |      ❌     |       ❌      |
# | 5      | 101    |     👍    |      ❌     |      👍      |
# | 6      | 110    |     👍    |     👍     |       ❌      |
# | 7      | 111    |     👍    |     👍     |      👍      |
# 
# Los permisos serán asignados por el número en la posición correspondiente. 
# 
# * `chmod 777 myfile.txt` dará permisos a todos 
# *  `chmod 766 myfile.txt` dará todos los permisos [lectura, escritura y ejecución] al **usuario** y permisos de **lectura y escritura** al **groupo y a los otros**
# *  `chmod 635 myfile.txt` da permisos de **lectura y escritura** al **usuario**, **escritura y ejecución** al **grupo**, y **lectura y ejecución** a los **otros**.
# *  `chmod 444 myfile.txt` permite a todos leer el archivo per elimina permisos de lectura y ejecución. **Esto es muy útil en bioinformática para proteger los archivos crudos de modificación no intencional, aún de ti mismo.**
# 
# Ahora vamos a ver los permisos del archivo `allfruits` y cambiarlos para darle todos los permisos a todos. Después verifica que se hayan cambiado los permisos correctamente.  
# 
# ```
# $ ls -l allfruits
# -rw-r--r-- 1 root root 31 Apr 24 20:26 allfruits
# $ chmod 777 allfruits
# $ ls -l allfruits
# -rwxrwxrwx 1 root root 31 Apr 24 20:26 allfruits*
# ```
# 
# El asterisco aparece en algunas configuraciones de `ls` para indicar que es un archivo ejecutable. 
# 
#     
# ---------
# 🔑 **En esta lección has aprendido a:**
# 
# * Contar caracteres, palabras y líneas con `wc`
# * Crear tuberías con `|`
# * Cambiar permisos con `chmod`
# 
# 

# In[ ]:





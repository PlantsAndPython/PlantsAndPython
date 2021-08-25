#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F"> 04. Trabajando con archivos
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de Aprendizaje**
# >Después de completar esta lección aprenderás a: 
# >
# > * Redirigir la salida `>` & `>>`
# > * Crear, escribir, ver y concatenar archivos con `cat`  
# > * Ver el contenido de archivos con `more`, `less`, `head`, y `tail`
# > 
# 
#  [![04. Working with Files](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide4.png?raw=true)](https://youtube.com/embed/oRmLSaVD3h8 "04. Working with Files")
# 
# Para esta lección ve a tu terminal virtual en CS50 sandbox [https://sandbox.cs50.io/](https://sandbox.cs50.io/).
# 
# 
# Algunos comandos dan una salida (*output*) que se imprime en la línea de comandos. Nosotros podemos redirigir la salida hacia un archivo con el símbolo `>`. La sintaxis es `comando > nombre_del _archivo`.  Si el archivo no existe, será creado. Pero si el archivo ya existe **se sobrescribirá**, así es que tienes que tener cuidado y asegurarte de que no sobrescribas un archivo por error.
# 
# Ahora vamos a tratar con el comando `ls` que enlista el contenido del directorio.
# 
# 
# Primero ve a tu directorio `home` con `cd`. Después si tecleas `ls` se imprimirá el contenido de tu directorio actual de trabajo. 
# 
# ```
# $ ls
# Documents/ Readme
# ```
# La salida se imprime en la pantalla. Ahora, redirige la salida al archivo `contents.txt`. Recuerda la sintaxis `ls > nombre_del_archivo`. 
# 
# ```
# $ ls > contents.txt
# ```
# 
# Esta vez no hay salida que se imprima a la pantalla. Podemos verificar que en verdad se fue al archivo viendo el contenido del archivo `contents.txt`. Da clic en `contents.txt` en la sección *Filetree* y el archivo se abrirá en la sección del editor. Podemos ver dos líneas de salida que fueron guardadas. También una tercera línea con el nombre del archivo. 
# 
# 
# <img src="https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/12.Files.Redir.png?raw=true" width=300\>
# 
# Si queremos redirigir la salida a un archivo que ya existe SIN sobrescribir el contenido previo, utilizamos `>>` y luego el nombre del archivo. Puedes ver cómo las nuevas líneas fueron agregadas al final del archivo.
# 
# 
# <img src="https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/13.Files.Append.png?raw=true" width=300\>
# 
# ## <p style="color:#2C6A7F">`cat`
# El comando `cat` command tiene diferentes funciones
# 
# * Crear un archivo
# * Escribir un archivo
# * Ver el contenido de un archivo
# * Agregar texto a un archivo existente
# * Concatenar archivos
# 
# Vamos a crear un archivo llamado `fruit1` así es que tienes que teclear
# 
# ```
# cat > fruit1
# ```
# Ahora vas a poder escribir el contenido. Después de escribirlo, puedes guardad los cambios y salir presionando las teclas `Ctrl` y `d`. 
# 
# ```
# pear
# mango
# ```
# Teclea `Ctrl` + `d` para guardar los cambios y salir
# 
# 
# Para ver el contenido del nuevo archivo sólo teclea `cat fruit1` y verás el contenido en la pantalla.
# 
# ```
# $ cat fruit1
# 
# pear
# mango
# ```
# 
# Ahora agrega la palabra `orange` en otra línea a `fruit1`
# 
# 
# ```
# $cat >> fruit1
# orange
# 
# # Ctrl + d para guardar y cerrar
# ```
# 
# Visualiza el contenido de `fruit1` 
# 
# ```
# $ cat fruit1
# pear
# mango
# orange
# ```
# 
# Ahora crea otro archivo `fruit2`
# 
# 
# ```
# $ cat > fruit2
# banana
# melon
# 
# #Ctrl + d
# ```
# Para **concatenar** archivos [unir el contenido de uno después del contenido de otro en un mismo archivo] tienes que ponerlos en el orden en el que quieres que se unan. La salida se irá a la pantalla, pero también puedes redirigirla a un nuevo archivo.
# 
# 
# 
# ```
# $ cat fruit1 fruit2
# pear
# mango
# orange
# banana
# melon
# ```
# 
# ```
# $ cat fruit1 fruit2 > fruitall
# ```
# 
# ## <p style="color:#2C6A7F">`more`
# 
# La función del comando `more` es visualizar el contenido de los archivos. 
# 
# Así es que para ver el contenido del archivo `fruitall` con `more`
# 
# ```
# $ more fruitall
# pear
# mango
# orange
# banana
# melon
# ```
# Como puedes ver, la salida se va a la pantalla de la línea de comandos. 
# 
# 
# ## <p style="color:#2C6A7F">`less`
# 
# Otro comando para ver el contenido de los archivos es `less`. Este es particularmente importante en bioinformática, ya que con él se pueden visualizar archivos enormes sin colapsar la computadora. *Si tratas de abrir un archivo de 50 Gb en un editor de texto normal, seguramente se congelará tu pantalla debido a la falta de memoria*. Vamos a ver el archivo `fruitall`.
# 
# 
# 
# ```
# $ less fruitall
# ```
# 
# Este comando te mostrará el contenido en una pantalla diferente. Si tu archivo no cabe en una sola pantalla puedes desplazarte a lo largo del archivo con las flechas o con la barra espaciadora. Para regresar a la pantalla de la línea de comandos teclea `q`.
# 
# 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/14.less.png?raw=true)
# 
# ## <p style="color:#2C6A7F">`head` & `tail`
# 
# Estos dos comandos también muestran el contenido de los archivos en la pantalla. Sin embargo, `head` te muestra las primeras lineas. Por defecto, las primeras 10, a menos que tú especifiques otro número. Por el contrario, `tail` te muestra las últimas líneas. Para especificar un número diferente de líneas puedes usar la opción `-n`.
# 
# 
# ```
# $ head -n 2 fruitall
# pear
# mango
# $ tail -n 2 fruitall
# banana
# melon
# $
# ```
# 
# -------
# 🔑 **En esta lección has aprendido a** 
# > * Redirigir la salida `>` & `>>`
# > * Crear, escribir, ver y concatenar archivos con `cat` 
# > * Ver el contenido de los archivos con  `more`, `less`, `head` y `tail`
# 
# 

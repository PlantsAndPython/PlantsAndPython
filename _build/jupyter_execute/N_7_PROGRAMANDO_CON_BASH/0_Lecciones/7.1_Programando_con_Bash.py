#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F"> 03. Programando con Bash
# 
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-No Comercial 4.0 Licencia Internacional</a>.
# 
#  
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de aprendizaje**
# >Después de completar esta lección aprenderás: 
# >
# >* ¿Qué es un script de bash?  
# >* Lo básico de la programación en bash
# >* ¿Cómo usar variables en bash?
# >* ¿Cómo hacer un for loop en bash?
# 
# Es posible que algunas veces quieras correr el mismo comando  muchas veces o una serie de comandos en muchos archivos. O tal vez quieras buscar no sólo una cadena si no una lista de cadenas, o iterar sobre algo algún número de veces. En estos casos, puedes escribir **scripts** en bash, así como lo harías en otros lenguajes de programación (e.g. python, perl). Un script es un programa que puede ser ejecutado por un interprete. En este caso el interprete sería bash. El script no tiene que ser compilado como los programas escritos en otros lenguajes como C o C++.
# El script más simple sería imprimir a la pantalla `Hello world!`. Vamos a crear un directorio llamado `Activity` en el directorio `Documents` y después crearemos un archivo que contendrá nuestro script y lo ejecutaremos con `sh`. 
# 
# ```
# $ cat > helloworld.sh
# echo Hello world!
# 
# $ sh helloworld.sh
# Hello world!
# ```
# 
# 
# ### <p style="color:#2C6A7F"> Buenas prácticas
# 
# Es una buena práctica agregar la extensión `.sh` a los scripts de bash. También es buena práctica agregar
# `#!` en la primera línea, seguido de la ruta del ejecutable de bash. De esa manera también podrás correr el script volviéndolo ejecutable y sin el comando `sh`. Finalmente también es recomendable agregar comentarios que expliquen tu código. También puedes agregar líneas vacías dónde necesites para que se vea limpio y organizado. Así es que tu primer archivo podría ser mejorado así.  
# 
# ```bash
# 
# #!/bin/bash
# 
# # This is my first script and will 
# # print Hello world! to the screen
# 
# echo Hello world!
# 
# ```
# 
# Ahora puedes ejecutarlo con `sh`
# 
# ```sh helloworld.sh```<br>
# 
# o con <br>
# 
# ```chmod +x helloworld.sh```<br>
# ```./myfirstscript.sh```<br>
# 
# Si quieres ejecutar una serie de comandos secuencialmente solamente agrega el siguiente comando a a la siguiente línea. 
# 
# 

# ```bash
# #!/bin/bash
# 
# # This is my first script and 
# # will print Hello world! to the screen
# 
# echo Hello world!
# echo This is my first file
# echo It is stored in the following path
# pwd
# 
# ```
# 
# ```
# $ sh helloworld.sh 
# Hello world!
# this is my first file
# it is stored in the following path
# /root/sandbox/Documents/Activity
# ```

# 
# ### <p style="color:#2C6A7F"> Variables
# 
# Una **variable** en la programación con el shell de bash, como en otros lenguajes,  es una ubicación en la memoria que es utilizada para contener un número, un carácter, una cadena, etc.. Los tipos de datos más utilizados para variables serían, entero [*integer*] (46), cadena [*string*] (apple), decimal o de punto flotante [*float*] (0.24), y un booleano [*boolean*] (FALSE). El tipo de dato de una variable tiene que estar definido cuando la variable se declara en lenguajes de programación de tipado fuerte. Sin embargo, Bash es un tipo de programación de tipado débil y no hay necesidad de definir la variable. 
# Variables are declared with the `=` sign, and are called with the `$` sign.
# 
# ```
# $ a=apple
# $ echo $a
# apple
# 
# ```
# Es recomendable usar comillas. En bash, las comillas sencillas y las dobles tienen diferente significado. 
# Las comillas dobles también son llamadas "comillas débiles". Si almacenas una variable la puedes llamar con las comillas dobles y te dará el contenido guardado en la variable.  
# 
# ```
# $ a=apple
# $ b="Value of a is $a"
# $ echo $b
# Value of a is apple
# ```
# 
# Las comillas sencillas o 'comillas fuertes' te darán una interpretación literal de lo que encierran. 
# ```
# $ a=apple
# $ b='Value of a is $a'
# $ echo $b
# Value of a is $a
# ```
# cuando no estás llamando a una variable o no estás usando expresiones regulares no hace ninguna diferencia usar sencillas o dobles. 
# 
# ```
# a='apple'
# ```
# o
# 
# ```
# a="apple"
# ```
# 
# Vamos a crear un script llamado `variable.sh` 
# 
# ```bash
# #!/bin/bash
# 
# #This script prints Hello world! 
# #to the screen and uses a variable.
# 
# Greet='Hello world!'
# echo "$Greet"
# ```
# ```
# $ sh variable.sh
# Hello world!
# ```
# 
# ### <p style="color:#2C6A7F"> Bucles
# Para iterar sobre comandos podemos utilizar bucles [*loops*]. El bucle **for** es representado en los siguientes ejemplos: 
# 
# ```bash
# for variable in 1 2 3 4 5 .. N
# do
# 	command1
# 	command2
# 	commandN
# done
# ```
# 
# ```bash
# for variable in file1 file2 file3
# do
# 	command1 on $variable
# 	command2
# 	commandN
# done
# ```
# Ahora vamos a crear un script con saludos con un bucle *for*. Ahora en lugar de imprimir `Hello world!` vamos a imprimir un saludo para cada continente. 
# 
# ```bash
# #!/bin/bash
# 
# #This script prints a greeting for each continent. 
# 
# continents="Africa Americas Antartica Asia Australia Europe"
# 
# for item in $continents
# do
#   echo "Hello $item" 
# done
# 
# ```
# 
# 
# La variable <font color="#2C6E3B"> continents </font> contiene 6 objetos `Africa` `Americas` `Antartica` `Asia` `Australia` `Europe`. En el bucle *for* la variable  <font color="#9E3147"> item </font> recorrerá cada uno de esos objetos de la variable <font color="#2C6E3B"> continents </font>, llamada con <font color="#2C6E3B"> $continents </font>.
# 
# Cada uno de ellos será impreso en cada uno de los ciclos del bucle con `echo` mientras son llamados con  <font color="#9E3147">$item </font> en cada iteración.
# 
# 
# 
# ```
# $ sh hellocontinents.sh 
# Hello Africa
# Hello Americas
# Hello Antartica
# Hello Asia
# Hello Australia
# Hello Europe
# ```
# 
# Si queremos guardar la salida de nuestro script en un sólo archivo podemos dirigir la salida con  `>>`
# 
# 
# 
# ```bash
# #!/bin/bash
# 
# #This script prints a greeting for each continent 
# #and saves the output to the file Greetings.txt 
# 
# continents="Africa Americas Antartica Asia Australia Europe"
# 
# for item in $continents
# do
#   echo "Hello $item" >> Greetings.txt
# done
# ```
# 
# Si queremos guardar la salida en diferentes archivos podríamos hacerlo así 
# 
# ```bash
# #!/bin/bash
# 
# #This script prints a greeting for each continent 
# #and saves the output into a different file for each continent.
# 
# continents="Africa Americas Antartica Asia Australia Europe"
# 
# for item in $continents
# do
#   echo "Hello $item" > Greet.$item
# done
# 
# ```
# 
# 
# ___
# 🔑 **En esta lección has aprendido**
# 
# * ¿Qué es un script de bash?  
# * Lo básico de la programación en bash
# * ¿Cómo usar variables en bash?
# * ¿Cómo hacer un bucle *for* en bash?
# 

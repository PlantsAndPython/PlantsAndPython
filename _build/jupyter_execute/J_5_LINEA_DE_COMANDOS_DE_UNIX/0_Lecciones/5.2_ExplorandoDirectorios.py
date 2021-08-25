#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#2C6A7F"> 03. Explorando directorios
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-No Comercial 4.0 Licencia Internacional</a>.
# 
# 
# 
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de aprendizaje**
# >
# >Después de completar esta lección aprenderás a:   
# >
# > * Identificar la arquitectura jerárquica de los archivos 
# > * Imprimir el directorio de trabajo
# > * Cambiar de directorio
# > * Usar rutas absolutas y relativas
# > * Crear directorios
# > * Completar con la tecla Tab  ↹
# > 
# 
# 
#  [![03.Exploring Folders](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide3.png?raw=true)](https://youtube.com/embed/HPDGwi95r78 "03. Exploring Folders")
# 
# ## <p style="color:#2C6A7F">`pwd`, `cd`, `ls`, `mkdir`
# 
# La estructura de los directorios en Linux es **jerárquica**. Entonces para hacer referencia a un directorio se utiliza el nombre del directorio secuencialmente más profundo conectado por diagonales `/`.
# 
# Por ejemplo, en la siguiente imagen, el directorio `project1` está dentro de `my_docs`, el cual está al mismo tiempo dentro del directorio `home`. Para hacer referencia a su ubicación, utilizamos  `/home/my_docs/project1`. Esta referencia de ubicación de archivos y directorios se le llama **ruta** o **path** en inglés.
# 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/01.01.path.png?raw=true)
# 
# Existe un símbolo llamado **prompt** o **símbolo del sistema** que aparece en la terminal cuando el sistema está listo para recibir una nueva solicitud. Dependiendo del *shell* que estés usando el símbolo del sistema va a variar. Por ejemplo, para **bash** el *prompt* es un símbolo de dolar `$`y para **zsh** el prompt es un signo de por ciento `%`. Si está conectado como el *superusuario* **root**, el cuál es el principal **administrador del sistema**, el *prompt* será un *hash* `#`.
# 
# 
# Ahora, vamos otra vez a tu terminal virtual en el [CS50 sandbox](https://sandbox.cs50.io/). Primero, necesitamos saber en qué directorio estamos trabajando. Es decir ¿cuál es ls ruta de nuestro **directorio de trabajo**? Para eso utilizamos  `pwd` en nuestra terminal. Entonces, teclea lo siguiente. Recuerda que no necesitas teclear el símbolo de `$` ya que ese es el *prompt* y ya está en la terminal.
# 
# **Nota:** Si en algún momento tu línea de comandos se atora y no puedes teclear nada, simplemente presiona `Ctrl` `c`  y cualquier proceso que se esté ejecutando será cancelado.
#  
# 
# ```
# $ pwd
# ```
# y el output es la ruta a to directorio de trabajo actual
# 
# ```
# /root/sandbox
# ```
# 
# Ahora, vamos a **cambiarnos de directorio**. Para movernos a otro directorio que está dentro del directorio en el que estamos trabajando; en otras palabras, para movernos a un directorio que está hacia adelante, tienes que teclear el comando `cd` espacio y el nombre del directorio.
# 
# 
# ```
# $ cd Documents
# ```
# y ahora verifícalo con `pwd`
# 
# ```
# $ pwd
# /root/sandbox/Documents
# ```
# 
# Ahora tu directorio de trabajo es `Documents`. Si quieres moverte un directorio atrás; es decir el directorio que contiene a tu directorio de trabajo actual, tienes que teclear `cd ..`.
# 
# ```
# $ cd ..
# $ pwd
# /root/sandbox
# ```
# En linux, podemos hacer referencia a la ubicación de un archivo o de un directorio, ya sea a través de una ruta **Absoluta**  o la ruta **Relativa**. Imagina que quieres darle instrucciones a un amiga para llegar de tu casa al supermercado. Entonces empiezas -ve derecho, después en el semáforo da vuelta a la izquierda y en el poste de luz da vuelta a la derecha para llegar al supermercado-. Esto sería similar a una ruta absoluta, la cual comienza desde el **primer directorio** en tu sistema que se llama **root** y está representado por una diagonal `/`.
# 
# Ahora imagina que tu amiga está perdida y te llama desde el poste de luz. Tú no le darías las mismas indicaciones. Ahora empezarías desde el poste de luz y no desde tu casa. Así es que probablemente dirías -da vuelta a la derecha y llegarás al supermercado-. Eso sería similar a una ruta **relativa**, la cual comienza desde tu **directorio de trabajo**.
# 
# 
# Now imagine that your friend is lost and calls you from the lamppost. You won't give her the same directions. You will start from the lamppost and not from your home. So you will probably say, 'turn right and you will reach the supermarket'. That would be similar to a **relative** path which starts from your **working directory**.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/01.02.AbsolutePath.png?raw=true)
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/01.02.RelatPath.png?raw=true)
# 
# Ahora, movámonos hacia atrás al directorio llamado `root` utilizando la **ruta absoluta**
# 
# ```
# $ cd /root
# $ pwd
# /root
# ```
# Ahora movámonos al directorio `root` del sistema; el cual es el primer directorio en tu sistema.
# 
# 
# ```
# $ cd /
# $ pwd
# /
# ```
# Ahora vamos a teclear `ls` para enlistar el contenido del directorio
# 
# 
# ```
# $ ls
# bin/   dev/  home/  lib32/  media/  opt/   root/  sbin/  src/  sys/  usr/  
# boot/  etc/  lib/   lib64/  mnt/    proc/  run/   snap/  srv/  tmp/  var/
# ```
# Ahora regresa a tu directorio `home`; que generalmente es el directorio que tiene tu nombre de usuario. En la terminal virtual sería `/root/sandbox/`
# 
# ```
# $ cd
# $ pwd
# /root/sandbox
# ```
# 
# Enlista el contenido de tu directorio `home` (o sandbox)
# 
# ```
# $ ls
# Documents/  Readme.txt
# ```
# 
# Ve a `Documents` y crea un nuevo directorio dentro de `Documents` llamado `Genomes`
# 
# 
# ```
# $ cd Documents
# $ mkdir Genomes
# ```
# Ve al directorio `Genomes` con la tecla de tabulación `TAB`  ↹
# 
# 
# ```
# $ cd TAB
# $ cd Genomes
# 
# ```
# ---------
# 🔑 **En esta lección has aprendido:** 
# 
# * La estructura jerárquica de los directorios de linux 
# * el comando `pwd`	 para imprimir el directorio de trabajo
# * el comando `cd`	para cambiar de directorio
# * las rutas Absoluta y Relativa 
# * el comando `mkdir`	para crear directorios
# * el comando `ls`  para enlistar el contenido de los directorios
# 
# 
# 

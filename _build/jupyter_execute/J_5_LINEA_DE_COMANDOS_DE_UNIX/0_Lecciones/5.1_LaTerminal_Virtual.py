#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F">02. Terminal Virtual
# 
# ***Autora:  Dra. Alejandra Rougon*** 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de Aprendizaje**
# 
# >Después de completar esta lección podrás:
# >
# >* Crear una cuenta de github
# >* Iniciar sesión en una terminal virtual en la plataforma CS50 sandbox
# >* Utilizar las diferentes secciones de la plataforma
# >* Crear un archivo y un directorio en tu terminal en línea
# 
# 
#  [![02.The virtual terminal](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/MiniaturasVideos/Slide2.png?raw=true)](https://youtube.com/embed/hab9-Mxag1I "02. The virtual Terminal")
# 
# 
# **CS50 sandbox** [https://sandbox.cs50.io/](https://sandbox.cs50.io/) es una plataforma donde podrás crear y compartir terminales virtuales. Esta plataforma es muy útil para aprender a utilizar la línea de comandos. Puedes ir directamente a la plataforma CS50 sandbox y darle presionar el botón ***create*** para abrir una nueva terminal. También puedes ir a una terminal específica que ya ha sido creada antes. Si creas una nueva los cambios se guardarán y estarán ahí la siguiente ves que entres a esa terminal. Si entras a una terminal que ya ha sido creada por otra persona los cambios que hagas serán eliminados y no estarán ahí la siguiente ves que entres a ella. 
# 
# Así es que primero crea una nueva terminal  en
# [CS50 sandbox](https://sandbox.cs50.io/) o entra directamente a una [Terminal virtual](https://bit.ly/3d9BRCG) que ya ha sido creada. 
# 
# Si no has iniciado con tu cuenta en github aparecerá la siguiente imagen.
# 
# <img src="https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/02.SignInSandbox.png?raw=true" width=400/>
# 
# Si ya tienes una cuenta en github sólo inicia sesión y da clic en el enlace de tu [Terminal virtual Terminal](https://bit.ly/3d9BRCG) de nuevo. Sin embargo si no tienes una cuenta sólo tienes que crear una.
# 
#  
# <img src="https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/03.CreateAccount.png?raw=true" width=400/>
# 
# Sólo necesitarás una cuenta de correo y una contraseña. Una vez creada puedes iniciar sesión y da clic de nuevo en la [Terminal virtual](https://bit.ly/3d9BRCG)
# 
# La siguiente imagen nos muestra  cómo se ve la terminal. En el lado izquierdo hay un ícono de una carpeta que abre la barra lateral de directorios. Puedes dar clic en el ícono para abrir y cerrar la barra. 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/01.OpenDirSidebar.png?raw=true)
# 
# Esta plataforma tiene tres secciones. Contiene un **editor de texto**, una **terminal** y un **explorador de archivos** también llamado ***Filetree** (árbol de archivos).  Estas tres herramientas son muy útiles para aprender a usar la línea de comandos. Si estás trabajando en tu computadora será importante que tengas estas tres herramientas abiertas también. Sólo ten en cuenta que algunos editores de texto (eg. Microsoft Word, Text Edit, Libre Office Writer) no funcionarán; ya que introducen caracteres ocultos. Existen muchos editores buenos disponibles que se utilizan para bioinformática. Aquí hay una lista de algunos de los más comunes. 
# 
# 
# | Editor de texto | Linux | Mac | Windows | Libre | Comentarios                                |
# |-------------|:-------:|:-----:|:---------:|:------:|-----------------------------------------|
# | [Atom](https://atom.io/)        | x     | x   | x       | x    | Altamente configurable                     |
# | [Gedit](https://wiki.gnome.org/Apps/Gedit)       | x     | x   | x       | x    | Funciones básicas                         |
# | [Notepad++](https://notepad-plus-plus.org/)   |       |     | x       | x    | Puede correr en otras plataformas a través de Wine |
# | [BBEdit](https://www.barebones.com/products/bbedit/)      |       | x   |         |      | Antes TextWrangler            |
# | [Sublime Text](https://www.sublimetext.com/) | x | x | x | x | Aunque tiene licencia, actualmente no tiene un tiempo límite de evaluación  |
# 
# Esta imagen muestra cómo las tres secciones están distribuidas en la **terminal virtual**
# 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/04.SandboxParts.png?raw=true)
# 
# Puedes crear **Nuevos Directorios** o **Nuevos Archivos** desde los tres punto en la barra de directorios *Filetree*.
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/08.FileDirectory.png?raw=true)
# 
# Con el signo `+` puedes crear archivos, en la parte de arriba, y crear nuevas terminales, en la parte de abajo.
# 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/05.SandboxCreate.png?raw=true)
# 
# También puedes mover para arriba y para abajo la línea de en medio para incrementar o disminuir el tamaño de la pantalla de la terminal o el editor.
# 
# 
# ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/06.BiggerScreen.png?raw=true)
# 
# Ahora vamos a crear un nuevo archivo usando el **editor de texto**. Es importante seguir algunas reglas cuando **nombremos un nuevo archivo**
# 
# 1. No debes usar caracteres especiales como `%`, `´`,  `*`, `|`, `\`, etc.
# 2. El guión bajo `_` y el punto `.` sí están permitidos. 
# 3. No debes usar espacios. En lugar de `My file` puedes usar `My_file` o `MyFile`
# 
# La extensión de un archivo no interferirá en el procesamiento. Si tienes un archivo de texto podrás trabajar con él en la línea de comando si la extensión es `.txt` o cualquier otra o aún sin extensión (`My_file.txt`, `My_file`, `My_file.hello`). Sin embargo, es una buena práctica nombrar un archivo de texto con la extensión `.txt` en caso de que quieras abrirlo con un editor de texto fuera de la línea de comandos. También de esa manera, podrás ser capaz de reconocer  qué tipo de archivo tienes sólo viendo la extensión. En Bioinformática trabajarás con archivos de texto pero que tienen diferentes formatos biológicos. Así que es importante agregar la extensión correspondiente al formato biológico (eg. `.fasta`, `.gff3`, `.sam`, etc.).
# 
# Crea un nuevo archivo llamado `Readme.txt` y agrega el siguiente texto  `Este es mi primer archivo de la lección de línea de comandos de Plants & Python`. No tienes que guardarlo, ya que todo lo que tecleas en esta plataforma se guarda automáticamente. En la sección *Filetree* verás tu archivo recién creado. Si posicionas el ratón en el área de los tres puntitos, encontrarás las opciones para renombrar (***renaming***), duplicar (***duplicating***), descargar (***downloading), o eliminar (***deleting**) tu archivo. Puedes cerrar tu archivo dando clic en el símbolo `x` en la sección del editor.
# 
#   ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/09.CreateReadme.png?raw=true)
# 
# Ahora crea un nuevo directorio llamado `Documents`. El *Filetree* se verá como esto.
# 
#   ![](https://github.com/alerougon/ObjectStorage/blob/main/PP_CommandLine/10.DocFolder.png?raw=true)
# 
# 	Nota: Los directorios también pueden ser llamados carpetas o folders.
# ---------
# 
# 🔑 **En esta lección has aprendido a:**
# 
# * Crear una cuenta de github
# * Iniciar sesión en una terminal virtual en la plataforma CS50 sandbox
# * Utilizar las diferentes secciones de la plataforma
# * Crear un archivo y un directorio en la terminal en línea
# 

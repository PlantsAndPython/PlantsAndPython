#!/usr/bin/env python
# coding: utf-8

# # Celdas de código
# 
# ***Traducción por Dr. Alejandra Rougon (UNAM ENES León, México)***
# _____

# ***Mira este video de 3:33 a 9:51***

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

# Para español, haga click en configuración,
# seleccione "español" debajo de los subtítulos.
# Traducción por Dra. Alejandra Rougon (UNAM ENES León, México)

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=3, seconds=33).total_seconds())
end=int(timedelta(hours=0, minutes=9, seconds=51).total_seconds())

YouTubeVideo("FrDYpLVuTkQ",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Aprenderás todo sobre cómo crear variables y cómo programar en las próximas lecciones. Pero hagamos un código muy simple para ver cómo funciona Jupyter. Vamos a crear código para calcular el área de un círculo. Crear variables en Jupyter es fácil, simplemente elige un nombre. Una vez que eliges un nombre, usa el signo igual '=' para asignarles un valor. Los valores asignados a las variables pueden ser cadenas de caracteres, se llaman cadenas (strings), o pueden ser números. Primero creemos una cadena de caracteres. Para crear una cadena, siempre usa comillas. Después establecemos el valor que será `"pi_is_a_number"`. Eso es lo que será nuestra variable `pi`. Una vez que pongas tu código en la celda, debes ejecutar la celda. Tienes que decirle a la celda que procese el código que contiene. Para ejecutar una celda, todo lo que debes hacer es presionar shift + enter. Puedes ver que aparece un número que dice que nuestra celda ha sido procesada y aparece una nueva celda debajo.

# In[2]:


pi = "pi_is_a_number"


# Tal vez queramos volver a comprobar que, de hecho, `pi` está configurado con el valor `"pi_is_a_number"`, por lo que simplemente escribe sólo `pi` y presiona shift + enter y la salida. Lo que nos devuelve Jupyter es `"pi_is_a_number"`. Así que hemos establecido que pi esté asignado a esa cadena.

# In[3]:


pi


# Pero quizás realmente queremos que `pi` sea un número. Entonces simplemente escribimos nuevamente `pi` igual a 3.14159 y presionamos shift + enter nuevamente. Queremos ve que se ha asignado a `pi` el valor correcto y ahora es 3.14159. 

# In[4]:


pi = 3.14159


# In[5]:


pi


# Ten en cuenta que es muy fácil para nosotros crear una variable, pero también es muy fácil para nosotros escribir sobre una variable y tomaen cuenta también que el orden en el que ejecutemos las celdas importa. Esto será importante más adelante cuando escribas código. El orden en que ejecutas las celdas es el código que estás ejecutando y afecta a la asignación de valores a variables y eso puede afectar mucho tu código. Entonces el orden sí importa.
# 
# Creemos algunas variables más. Creemos una variable `r` para el radio, configúrala igual a uno. Algo que es muy importante en la programación es 
# comentar. Si usas el hash `#` cualquier carácter que escribas después de él no será procesado por Python. Es una forma conveniente de dejar comentarios en tu código. Eso te puede ayudar a guiarte en el futuro para recordarlo que significa su código. Por eso, deberíamos entrar en la práctica de usar comentarios con frecuencia. Recordemos cuál era esta variable. Podemos escribir `# r es radio`. Puedes crear varias líneas 
# de código dentro de una celda. Vamos a crear otra variable. La llamaremos `A` de área. Importa si algo está en minúsculas o en mayúsculas. Sí que tienes que recordar cómo escribiste tus variables. Si esta es el área del círculo, digamos que es `pi` multiplicado por `r` al cuadrado. Observa que un asterisco, es para la multiplicación. Dos asteriscos es para exponente o potencia. Ahora podemos presionar shift + enter. Hemos 
# asignado el valor a `r`. Y usando `r` y `pi` entonces hemos calculado `A`. Así que veamos a qué es igual `A` y el área de nuestro círculo es igual a 3.14159, como esperábamos. 

# In[6]:


r = 1 # r is radius

A = pi*r**2


# In[7]:


A


# Cuando tienes código, es muy fácil reasignar los valores de las variables. Y de esta manera es realmente más fácil jugar 
# con las cosas y hacer cálculos. Ese es uno de los poderes de la programación. Así que demos un número arbitrario con un decimal complicado a nuestro radio. Y si recalculamos el área del círculo, ahora podemos ver que es un número mucho más diferente y complicado. 

# In[8]:


r = 4.234678236728465724 # r is radius

A = pi*r**2


# In[9]:


A


# Como viste, las matemáticas son triviales y fáciles de hacer en Python. `+` es para crear una suma, `-` es restar, como viste `*` es para multiplicar, `/` es para división, y `**` es para exponentes. También, en informática hay cosas llamadas declaraciones booleanas, que son muy importantes. Las declaraciones booleanas solo pueden evaluarse como `Verdadero` o `Falso`. Estas son declaraciones que crean condiciones de las que solo se puede decir `Verdadero` o `Falso`. Por ejemplo, tal vez queremos decir que 3 es mayor o igual `>=` a pi. Eso no es verdad, porque 3 es menor que pi, pero si evaluamos esta afirmación, nos da `Falso`.

# In[10]:


3 >= pi


# Entonces, si ahora decimos que una declaración booleana de 3 es menor o igual `<=` a pi, esa declaración será `Verdadero`.

# In[11]:


3 <= pi


# Y si dijimos que 3.14159 no es igual `!=` a pi, esa declaración es `Falso` porque 3.14159 es igual a pi. 

# In[12]:


3.14159 != pi


# Podríamos decir que 3.14159 es doble igual `==` a pi. Esta es una forma computacional de decir igual, porque estamos usando un solo signo igual `=` para asignar variables, pero aquí realmente queremos decir que 3.14159 es igual a pi, y esa es una declaración `Verdadera`.

# In[13]:


3.14159 == pi


# También aprenderás mucho sobre funciones. Le das entradas a funciones y ellas te regresan salidas. La función más simple es `print()`, que simplemente te devolverá el valor de una variable. Entonces podemos decir `print(pi)` y podemos ver que la función de impresión nos devuelve 3.14159 de la variable `pi`.

# In[14]:


print(pi)


# Así que en esta lección hasta aquí veremos sobre programar en celdas. Vas a aprender mucho más sobre programación en las siguientes lecciones.

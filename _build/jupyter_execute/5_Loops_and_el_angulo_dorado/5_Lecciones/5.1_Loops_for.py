#!/usr/bin/env python
# coding: utf-8

# # Lección 3.1

# ## Cómo escribir un loop `for`
# ____

# ***Mira este video de 2:35 a 7:19***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Erik Amézquita (Michigan State University)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=2, seconds=35).total_seconds())
end=int(timedelta(hours=0, minutes=7, seconds=19).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Escribir loops es fácil. Escribir bucles también es poderoso.
# 
# Para usar un loop `for`, solo escribe la primera línea. Es muy importante escribir esta línea exactamente con la sintaxis que se proporcionada. Siempre comenzamos con `for` y luego creamos una variable. A menudo usamos `i` como un índice que ya hemos usado antes, pero podemos llamar a esta variable como queramos. Empleamos entonces `i` y luego usualmente tenemos ya sea una secuencia de números enteros que pueden producir la función `range()` o incluso podemos poner en una lista. La idea es que estamos diciendo "para `i` dentro del rango o una lista" y vamos a iterar sobre la lista o la función `range()`. Esto también es importante: debemos terminar con dos puntos en la primera línea de nuestro loop `for`. Decimos así que "para `i` en el rango" hasta cierto número. Digamos 8 y `:`.
# 
# Si presionamos `Enter` después de esta línea, veremos que nuestro código ahora estará sangrado. Esta es otra pieza importante de sintaxis al escribir un loop `for`. El código dentro del loop debe estar sangrado. Dentro del loop, podremos poner todo lo que queramos, el cielo es el límite. Nuestro código va dentro del `for` y lo que hará el loop es iterar sobre los valores de `i`. Ello significa que "para `i` en" y el primer valor del `range()` va a ser 0. Así que `i` va a ser iniciado en 0. Cualquier código coloquemos aquí usando la variable `i` será procesado usando `i` igual a 0. Después de que el loop complete nuestro código interno, volveremos a subir e `i` ahora va a ser asignado al segundo valor, que será 1 en este caso. Y luego, cuando sea 1, ejecutaremos el código interno nuevamente, volveremos a iniciar el loop de nuevo. Después `i` será igual a 2 y vamos a seguir repitiendo el ciclo para todos los elementos en el rango o una lista como veremos más adelante. 
# 
# Así, si ejecutamos esto, presionando `shift` + `enter`, podemos ver que estamos imprimiendo `i` con cada iteración. Inicialmente es 0, por lo que
# se imprime 0. Luego voy a 1: imprime 1. Y llega hasta 7. En este contexto
# podemos ver que es exactamente la función de `range()`. Produzcamos una secuencia de enteros que podemos iterar en un loop `for`. 

# In[2]:


# ¡Escribir loops `for` es fácil!

for i in range(8): # First, say which values of "i" you would like to use

    # Your code using "i" goes here
    
    print(i)


# Recordemos que la función `range()` es como cortar e indexar como aprendimos antes. Ésta tiene un valor inicial y un valor final y un valor de paso. Recordemos que en python el inicio es inclusivo, por
# ejemplo, esto comenzará en -8, va a incrementar pero sin incluir 10 y lo hará en pasos de 2. Por ende, si decimos `for i` en esta secuencia de
# números, comenzará siendo `i` el primer valor, y por ser inclusivo, dicho valor es -8. Por lo tanto, el primer número a imprimir con `print()` debería ser -8. Iteramos por segunda ocasión. En esta ocasión, el siguiente valor de `i` debería ser -6, y deberíamos obtener un -6. Probablemente el código debería ir hasta 8 pero no 10 pues el valor final es exclusivo. Así que el último número con pasos de 2 en 2 debería ser 8.
# 
# Veamos qué obtenemos para la función. En efecto, comenzamos en -8, tenemos pasos de 2 en 2 que van hasta 10, pero sin incluír al 10 mismo. Así que el último el número es 8.
# 
# Notemos este comentario aquí, el cual indica que usemos la función `print()`. La razón es que, como veremos más adelante, cuando nuestro código se complique, es bueno cerciorarnos de que el loop se está ejecutando. Es bueno imprimir `i` para asegurarnos de que el loop se está
# procesando realmente. Así que ese es nuestro primer loop `for`, el loop `for` más simple. 

# In[3]:


# Recuerde, puede especificar inicio (incluido), parada (no incluido)
# y paso con rango, ¡al igual que cortar e indexar!

for i in range(-8,10,2): # inclusive of start, but not of the end
    
    print(i) # always use print to make sure loop worked!


#!/usr/bin/env python
# coding: utf-8

# # 3.5 Loops while

# ## Cómo escribir un loop while usando un contador
# ____

# ***Mira este video de 26:29 a 30:40***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Erik Amézquita (Michigan State University)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=26, seconds=29).total_seconds())
end=int(timedelta(hours=0, minutes=30, seconds=40).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Eso es todo respecto a loops `for`. Existe otro estilo importante de loop, conocido como el loop `while`, que está muy relacionado con un contador.
# 
# Así como podemos leer en voz alta un loop `for` y tiene sentido del mismo modo podemos leer el `while` de la misma manera. Básicamente dice que mientras un valor, llamémoslo `counter` es menor que 25, se ejecute el loop.
# 
# Así que se trata de un loop de tiempo continuo mientras la condición sea verdadera. Casi siempre un loop `while` tiene una declaración booleana.
# Una declaración booleana es una declaración matemática que es verdadera o falsa. No hay nada intermedio. Éstas son muy útiles, especialmente porque se ejecutará un loop `while` mientras la condición sea verdadera.
# 
# Entonces, si usamos nuestro contador `counter`, por ejemplo, establezcamos el contador inicialmente igual a 2. Vamos a inicializar, una lista de Fibonacci con dos elementos que necesitamos para calcular el tercero, y esta es la posición del índice 0, la posición del índice 1, y luego tenemos el índice en la posición 2. Entonces comenzaremos el
# contador en 2. Usaremos la línea única de código que acabamos de ver y la hemos usando para calcular la secuencia de Fibonacci y luego, cuando terminamos usaremos `+=` para hacer que el contador incremente a 3, y luego ejecutaremos el loop nuevamente, calculamos el código, agregamos el siguiente elemento a Fibonacci, el contador aumenta en uno, nuevamente.
# 
# 
# Eventualmente el `counter` será igual a 25 y cuando sea 25 ya no será cierta la condición de que el contador es menor que 25. Y cuando eso
# suceda, el loop no continuará.

# In[2]:


# Un loop while continúa MIENTRAS la condición es VERDADERA
# Una declaración booleana es VERDADERA o FALSA

fibonacci = [0,1]
counter = 2

while counter < 25: # Loop continues one more time IF this is TRUE
    
    fibonacci.append(fibonacci[counter-2] + fibonacci[counter-1])
    
    counter += 1


# Ejecutamos esto y podemos verificar la longitud de nuestra secuencia de Fibonacci que produjimos. Recordemos que tenemos los dos primeros elementos y luego vamos a subir a 25, pero sin incluirlos, que parece ser 24. Recordamos también que comenzamos en la posición 0 del índice. Así que entre las posiciones 0 y 24 deben haber 25 elementos y ese es el caso. 

# In[3]:


# Verificar la longitud de la secuencia

len(fibonacci)


# Y si imprimimos nuestra secuencia de Fibonacci con 25 elementos, podemos ver que de nuevo obtenemos la secuencia esperada. Confirmamos que 1 es la suma de 0 y 1; 2 es una suma de 1 y 1; 3 es la suma de 1 y 2; 5 es la suma de 2 y 3, y 8 es la suma de 3 y 5.

# In[4]:


# Recuperamos la secuencia de Fibonacci

print(fibonacci)


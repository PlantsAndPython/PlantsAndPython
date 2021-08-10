#!/usr/bin/env python
# coding: utf-8

# # Lección 3.4

# ## Cómo utilizar un loop `for` para calcular la suceción de Fibonacci 
# ____

# ***Mira este video de 20:31 a 26:29***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Erik Amézquita (Michigan State University)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=20, seconds=31).total_seconds())
end=int(timedelta(hours=0, minutes=26, seconds=29).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Así que veamos cómo podemos usar loops `for` para hacer algo matemáticamente útil. Intentemos calcular la secuencia de Fibonacci.
# 
# Acordémonos que cada número de la secuencia de Fibonacci es la suma de los dos valores anteriores. Si vamos a crear la secuencia de Fibonacci, es importante que no creemos una lista vacía inicialmente, sino que la inicializamos con dos valores iniciales. La razón es porque nosotros necesitamos dos valores para calcular el siguiente. Muchas personas comienzan con la secuencia de Fibonacci con 1 y 1, por lo que el siguiente valor sería 2. Después de eso, el siguiente valor es 3, después de eso, el el siguiente valor es 5. Pero también podemos comenzar la secuencia con 0 y 1, y porque comenzamos con índice 0 en python, tal vez esto tenga sentido y lo haremos de esta manera para este loop.
# 
# Así que tenemos definidos dos elementos en nuestra lista. Vamos a decir para `i` en el rango de 2 a 10. Es importante que comencemos con 2 porque 2 es el siguiente elemento de esta secuencia. Recordemos que la indexación indica que esta es la posición 0. Esta es la posición 1 y, por lo tanto, el siguiente número de la secuencia está en la posición 2. Entonces, comenzaremos en la siguiente posición de la secuencia, que es 2. La siguiente posición de la secuencia será la suma de estos dos números. Por ello, creamos una variable. Lo vamos a llamar `two_previous`. Queremos el número dos índices antes del índice del número actual en que estamos. Entonces, usando la indexación, esta sería la lista de Fibonacci `for i`, que en la primera iteración va a ser 2, recordemos, menos 2, porque queremos dos índices anteriores. Entonces, al principio, esta será la posición 0, que es exactamente lo que queremos que sea. Luego crearemos una variable llamada `one_previous` y tendrá `i-1`. Con `i` iniciando en 2, si restamos 1, tendremos la posición uno,
# que es exactamente lo que queremos. Podemos ver que va a ser apropiado para la posición que estamos tratando de calcular. Estos siempre nos darán el valor dos índices anteriores o el valor del índice anterior.
# 
# El siguiente valor, `new_value`, de la secuencia de Fibonacci, será `two_previous` más `one_previous`. Entonces creamos `new_value` como
# `two_previous` más `one_previous`. Luego anexamos `new_value` a la lista. Ahora, cuando pasamos al siguiente valor de `i`, este valor `new_value`,
# ahora será el nuevo valor `one_previous` y, por supuesto, siempre tendremos `two_previous`, los sumaremos de nuevo y agregaremos el nuevo `new_value`.
# 
# Tomemos un tiempo para revisar este loop y veamos si no tenemos problemas para entenderlo. Estamos utilizando todos los conceptos de índice que hemos practicado, la indexación que hemos aprendido antes, excepto
# que lo estamos ejecutando con este valor de i y estamos modificando el valor del índice en -2 o -1 para que podamos obtener los valores previos,
# los dos valores previos de nuestra lista para calcular el siguiente valor de la secuencia. Agregamos el siguiente valor de la secuencia y nuestra lista crece y crece a medida que seguimos ascendiendo. De nuevo siempre imprimimos `i`, solo para asegurarnos de que el loop esté funcionando.
# 
# Podemos ver que funcionó. Queríamos empezar en la segunda posición del índice, comienza en 2, y sube hasta el 10, pero sin incluirlo, hasta el 9.

# In[2]:


# usemos un loop `for` para calcular la secuencia de Fibonacci
# Cada valor en la secuencia de Fibonacci es la suma de los
# dos valores antes que él

# Necesitamos inicializar nuestra lista con dos valores,
# Porque necesitamos sumarlos para calcular el siguiente!

fibonacci = [0,1]

for i in range(2,10):
    
    two_previous = fibonacci[i-2]
    one_previous = fibonacci[i-1]
    new_value = two_previous + one_previous
    fibonacci.append(new_value)
    
    print(i) # always use print to make sure loop worked!


# Debemos de comprobar la longitud de nuestra secuencia de Fibonacci. Asegurémonos de hacerlo bien. Recordemos que comenzamos con dos elementos y luego vamos del 2 al 10. Así que esto sería 3, 4, 5, 6, 7, 8, 9,
# que son ocho elementos, por lo que 2 más 8 deben ser 10. La longitud de nuestra secuencia de Fibonacci debería ser 10 y lo es. 

# In[3]:


# Comprobar la longitud
# Empezamos con dos elementos
# Luego, range(2,10), por lo que 8 elementos más
# Debería ser 10
 
len(fibonacci)


# Finalmente revisemos la secuencia de Fibonacci. Este fue el elemento con el que comenzamos, 1 es la suma de 0 y 1, sigue que 2 es la suma de 1 y 1; 3 es la suma de 1 y 2; 5 es la suma de 2 y 3; 8 es la suma de 3 y 5. Parece ser que está funcionando.

# In[4]:


# comprobamos la secuencia!

fibonacci


# Vale la pena resaltar que siempre podemos hacer que su código sea más eficiente, pero a veces ayuda realmente primero escribir cada paso de manera individual. Después de escribir cada paso, siempre podemos retroceder e intentar ver si podemos hacerlo más eficiente.
# 
# Por ejemplo, vamos a cortar y pegar un poco para ver a que me refiero. Tenemos `two_previous` es igual a esto, `one_previous` es igual a esto y `new_value` es igual a `two_previous` más `one_previous`. Podríamos simplemente tomar `two_previous` y reemplazarlo aquí y podemos cortar `one_previous` y reemplazarlo aquí, de modo que estamos calculando ambos
# mientras calculamos `new_value`, pero luego notamos que solo estamos agregando el nuevo valor a la secuencia de Fibonacci. Así que podríamos poner `new_value` en la función `.append()` para agregar directamente a la secuencia de Fibonacci.

# In[5]:


# Siempre puedes hacer que tu código sea más eficiente

# Después de reducir el código

fibonacci = [0,1]

for i in range(2,10):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])


# Comparamos antes y después de hacer al loop más eficiente. Vemos que hemos reducido todo a una sola línea de código que podemos ejecutar y ver
# ¿obtenemos el mismo resultado? En efecto lo hacemos.
# 
# Recuperamos la secuencia de Fibonacci y podemos ver que simplemente reemplazamos las variables y redujimos las líneas en nuestro código
# pero siempre podemos escribir cada paso, lo cual a veces ayuda mucho para tratar de elaborar nuestras ideas a través del código.

# In[6]:


# Mismo resultado con código abreviado

fibonacci = [0,1]

for i in range(2,10):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

print(fibonacci)


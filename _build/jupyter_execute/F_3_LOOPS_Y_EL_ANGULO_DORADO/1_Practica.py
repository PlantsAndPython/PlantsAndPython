#!/usr/bin/env python
# coding: utf-8

# # Pr谩ctica con La raz贸n dorada calculada con loops 馃尰 
# 
# ***Traducci贸n por Erik Am茅zquita (Michigan State University, East Lansing, Michigan, USA)***
# _____

# ## De la sucesi贸n de Fibonacci a la raz贸n dorada

# Despu茅s de ver el video de arriba, en la celda de abajo, crea un loop `for` que calcule los primeros **100 n煤meros** de la sucesi贸n de Fibonacci.
# 
# Haz lo siguiente:
# 
# * Crea una lista ***fuera del*** loop `for` para guardar la sucesi贸n. Llamemos `fibonacci` a la lista.
# * Recuerda que debemos especificar los dos primeros n煤meros de la sucesi贸n (0 y 1) en la lista para calcular los t茅rminos subsiguientes.
# * Debemos comenzar a iterar en el tercer elemento (铆ndice = 2) de la lista para calcular el resto de la sucesi贸n.
# * Cada elemento de la sucesi贸n es la suma de los elementos `i-2` e `i-1`.

# In[1]:


# Escribe tu respuesta aqu铆



# En la celda de abajo, calcula la longitud de la lista `fibonacci` con  la funci贸n `len ()` (deber铆amos tener 100 elementos. De lo contrario, modifica el loop para asegurar que este sea el caso).

# In[2]:


# Determina la longitud de la lista Fibonacci:



# Una vez que conseguimos calcular la sucesi贸n de Fibonacci, 隆modifiquemos el c贸digo para calcular la raz贸n dorada $\phi$!
# 
# La raz贸n dorada se aproxima como la raz贸n del elemento `i` dividido por el elemento `i-1` de la sucesi贸n de Fibonacci. La aproximaci贸n de la raz贸n dorada `i/(i-1)` se vuelve m谩s precisa cuando evaluamos 铆ndice grandes. 隆Usemos nuestras habilidades de loops para aproximar la raz贸n dorada!
# 
# Copia y pega el c贸digo de la sucesi贸n de Fibonacci de arriba. En la celda a continuaci贸n, modif铆calo para hacer lo siguiente:
# 
# * Adem谩s de la lista de Fibonacci (rellenada previamente con 0 y 1 para calcular la secuencia) agreguemos otra lista vac铆a llamada `phi` fuera del loop  para almacenar nuestras aproximaciones de la raz贸n dorada.
# 
# * Esta vez, calculemos solo 52 elementos de la sucesi贸n de Fibonacci y 50 elementos de $\varphi$. 
# 
# - Todav铆a debemos comenzar en el tercer elemento (铆ndice = 2) para calcular la sucesi贸n de Fibonacci, por lo que debemos agregar dos iteraciones adicionales para asegurarse de obtener las 50 aproximaciones de $\varphi$ (porque a diferencia de la sucesi贸n de Fibonacci, esta lista `phi` comienza vac铆a).
# 
# * En el loop `for`, calculamos cada elemento de la sucesi贸n de Fibonacci como la suma de los elementos `(i-2)` + `(i-1)` y los a帽adimos a la lista de Fibonacci.
# 
# * Agregamos dentro del `for` un c谩lculo de $\phi$ como elementos `i/(i-1)` de la secuencia de Fibonacci.
# 
# 
# * **Importante**: para poder calcular $\varphi$ como se describe arriba, 隆el `i`-茅simo elemento de tu lista de Fibonacci no existe hasta que lo calcules! Aseg煤rate de calcular el pr贸ximo n煤mero de Fibonacci de la serie y agregarlo a la lista ***antes de*** calcular $\varphi$. Fibonacci primero, luego $\varphi$.

# In[3]:


# Tu respuesta aqu铆



# En la siguiente celda, con `print` imprime:
# 
# 1. La longitud `len()` de la lista `phi`
# 2. Imprime `phi`. La lista debe de aproximar el valor de la raz贸n dorada: 1.618033988749895

# In[4]:


# Tu respuesta aqu铆


# ## De la raz贸n dorada al 谩ngulo dorado

# La hermosa filotaxia en espiral de los girasoles y en 贸rganos laterales de otras plantas surge del 谩ngulo dorado. El 谩ngulo dorado se deriva de la raz贸n dorada. Si dos arcos en un c铆rculo se definen de manera que la longitud del arco `a` dividido por el arco` b` es la raz贸n dorada, entonces el 谩ngulo resultante es el 谩ngulo dorado. 
# 
# Como acabamos de ver, la raz贸n dorada es producto de la sucesi贸n de Fibonacci, 隆y as铆 es como los patrones inspiradores que se ven en un disco de girasol est谩n vinculados a la sucesi贸n de Fibonacci! 馃尰

# ![golden_angle.jpg](../images/golden_angle.jpg)

# Aproximemos el 谩ngulo dorado a partir de la raz贸n dorada.
# 
# Primero, obtengamos nuestra estimaci贸n m谩s precisa de la raz贸n dorada.
# 
# En la pr贸xima lecci贸n, usaremos la funci贸n `.pop()`, la cual se puede agregar al final de una lista. `.pop()` devolver谩 el 煤ltimo elemento de la lista. Como el 煤ltimo miembro de nuestra lista `phi` es la mejor aproximaci贸n de la raz贸n dorada que tenemos, 隆usemos `.pop()` para obtener ese valor! La forma en que se usa `.pop()` es la siguiente:
# 
# ```python
# my_variable = my_list.pop()
# ```
# 
# En la celda de abajo, crea una nueva variable llamada `golden_ratio` usando `.pop()` para aislar el 煤ltimo valor de la lista` phi`. Imprime el valor de `golden_ratio`.

# In[5]:


# Tu respu茅sta aqu铆



# La raz贸n dorada tiene algunas propiedades muy interesantes.
# 
# En la celda de abajo, haz `print()` de lo siguiente usando tu nueva variable `golden_ratio`:
# 
# * Imprime el valor de `golden_ratio`
# * Imprime el valor de `golden_ratio` elevado al cuadrado
# * Imprime el valor de `1/golden_ratio`
# 
# 驴Qu茅 observas que es similar entre todos los valores que acabas de calcular?

# In[6]:


# Respuesta aqu铆



# No solo todos los valores que acabamos de calcular terminan con los mismos decimales, sino que tambi茅n observamos que `golden_ratio**2 = 1 + golden_ratio`. Con esta informaci贸n, 隆descubramos c贸mo derivar el 谩ngulo dorado a partir de la raz贸n dorada!
# 
# Sea `f` la fracci贸n de la longitud de la circunferencia de un c铆rculo que est谩 ocupada por el arco` b`, donde la raz贸n de las longitudes de los arcos `a/b` es la raz贸n dorada.

# ```python
# golden_ratio = a/b
# f = b / (a + b) 
# f = (b/b) / ( (a/b) + (b/b) )
# f = 1 / (golden_ratio + 1)
# f = 1 / golden_ratio**2
# ```

# De los c谩lculos anteriores, podemos ver que la fracci贸n de la circunferencia del c铆rculo ocupado por el arco `b` que est谩 subtendido por el 谩ngulo dorado es `1/golden_ratio**2`.
# 
# En la celda a continuaci贸n, calculemos el 谩ngulo dorado a partir de la aproximaci贸n de la raz贸n dorada en grados como:
# 
# ```python
# golden_angle = 360*(1/golden_ratio**2)
# ```
# 
# Nuestra respuesta debe estar cerca de "137.50776405003785".

# In[7]:


# Respuesta aqu铆



# 隆Felicidades! 隆Calculamos el 谩ngulo dorado desde cero usando python! Utilizaremos el 谩ngulo dorado en la siguiente actividad para modelar el crecimiento de un girasol.

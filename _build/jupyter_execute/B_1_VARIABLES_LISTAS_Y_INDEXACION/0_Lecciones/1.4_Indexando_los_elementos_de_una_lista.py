#!/usr/bin/env python
# coding: utf-8

# # 1.4 Indexando los elementos de una lista
# ## ¿Cómo utilizar la indexación para acceder a elementos específicos de una lista?
# ______

# **Mira este video de 12:22 a 13:33**
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Alice Luckie (UNAM ENES León, México)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=12, seconds=22).total_seconds())
end=int(timedelta(hours=0, minutes=13, seconds=33).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# >💡 ***Recuerde:*** En el cuaderno anterior, creó una lista llamada `angiosperms` que contiene las cadenas de `wine`, `tequila` y `beer`. Vuelva a crear la lista en la celda de abajo para completar esta lección.

# In[2]:


# Crea la lista de angiospermas

wine = "Vitis_vinifera"
tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"

angiosperms = [wine, tequila, beer]


# Podemos usar la indexación para acceder a elementos específicos de la lista, tal como viste cómo podías acceder a los caracteres dentro de una cadena, y se hace exactamente de la misma manera.
# 
# Entonces, si tenemos nuestra lista de `angiosperms`, podemos imprimirla completa pero también podemos indexarla. Podemos indexar y ver cuál es el primer elemento. Es el elemento cero, ¿verdad ?, podemos ver cuál es el tercer elemento, que es la segunda posición del índice, o podemos intentar ver cuál es la lista completa. Recuerda que hay tres elementos que normalmente serían de cero a dos, pero tenemos que subir a tres, porque iremos hasta tres pero no incluirlo.
# 
# 
# Entonces, si miramos la lista completa, tenemos nuestros tres elementos allí. Con índice cero, pescamos solo el primer elemento. Con un índice de dos que acaba siendo el tercero, porque es cero, uno, dos que es la 
# cebada. Y luego podemos recuperar la lista completa especificando realmente cuatro posiciones diferentes porque la última posición tres subirá a allí pero no incluido.

# In[3]:


# Puede usar la indexación para acceder a elementos de una lista

print(angiosperms)

print(angiosperms[0])

print(angiosperms[2])

print(angiosperms[0:3])


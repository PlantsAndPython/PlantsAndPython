#!/usr/bin/env python
# coding: utf-8

# # Lección 1.3
# 
# ## ¿Cómo crear listas?
# - Utilizar paréntesis vacíos [ ]
# - Rellenar con variables o cadenas
# _______

# **Mira este video de 9:10 a 12:22**
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Alice Luckie (UNAM ENES León, México)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=9, seconds=10).total_seconds())
end=int(timedelta(hours=0, minutes=12, seconds=22).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# >💡 ***Recuerde:*** en el cuaderno anterior creó variables llamadas `wine`, `tequila` y `beer`. Cree las variables nuevamente en la celda de abajo para completar esta lección

# In[2]:


# Cree las variables wine, tequila, and beer

wine = "Vitis_vinifera"
tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"


# Entonces hicimos todas esas variables porque ahora vamos a llegar a algo llamado listas. Listas tal y como suenan. Son una lista de tipos de datos. Los tipos de datos pueden ser cadenas, ser números, ser enteros, flotantes, e incluso pueden ser listas y hablaremos sobre la creación de una lista de listas en un segundo. Puede poner cualquier cosa que desee en su lista. Crear listas es muy fácil. Solo usa corchetes vacíos . Estos corchetes no se tocarán otra palabra como cuando indexa y esto inicializará una lista vacía. Entonces simplemente llenamos los corchetes con variables o cadenas separados por comas.
# 
# Así que creemos una lista vacía. Creemos una variable llamada `angiosperms`, llamémosla como el nombre de las plantas con flores. Y lo vamos a igualar a una lista vacía. Y toda una lista vacía es solo un conjunto vacío de corchetes. Presionamos shift + enter y habremos creado nuestra nueva variable.

# In[3]:


# Creemos una lista vacía llamada angiospermas, o las plantas con flores

angiosperms = [ ]


# Es muy conveniente saber que todas estas variables que podemos tener, 
# son solo una colección de letras, tienen un nombre, y a veces pueden confundirte. ¿Que es lo que tengo? ¿Es una cadena, es una lista,
# es un numero? Aprendamos sobre nuestra segunda función en Python que se llama `type()`. Entonces en la función `type()` tenemos un conjunto de paréntesis y ponemos una entrada en él, una variable de algún tipo,
# y `type()` nos devolverá el tipo de variable que es. Así que acabamos de crear una lista vacía para nuestra variable `angiosperms` y de hecho lo que tenemos, es una lista.

# In[4]:


# Siempre podemos comprobar qué tipo de variable tenemos con la función type()
# Comprobemos si las angiospermas son una lista

type(angiosperms)


# Si quisieras probar esto, por ejemplo, `wine`, si recuerdas fue una cadena, es "Vitis_vinifera", es solo una colección de caracteres y no es una lista, es una cadena, por lo que `type()` le dirá con qué tipo de tipo de datos está trabajando.

# In[5]:


# A diferencia de la lista de angiospermas, el vino es una cadena

type(wine)


# Si miramos el contenido de nuestra lista de `angiosperms`, debería estar vacío, ¿Verdad?, no hemos puesto nada en él y, de hecho, solo obtenemos corchetes vacíos de vuelta.

# In[6]:


# Si miramos el contenido de nuestra lista de angiospermas,
# debe estar vacío

angiosperms


# Pero llenémoslo ahora. Llenar una lista es realmente fácil. Todo lo que haces es poner variables separado por comas. Entonces, en nuestra lista de `angiosperms` agregaremos `wine`, `tequila` y `beer`.

# In[7]:


# Completemos nuestra lista de angiospermas!
# Simplemente escribimos nuestras variables, separadas por comas

angiosperms = [wine, tequila, beer]


# Ejecutamos esa celda y ahora si vemos nuestras listas en ella porque pusimos vino, tequila y cerveza. Recuperamos los valores de esas variables, que son "Vitis_vinifera", "Agave_tequilana", y "Hordeum_vulgare". Así es como se crea una lista, un conjunto de corchetes vacíos. Pones en variables, números, cadenas, otras listas y, como te darás cuenta, cualquier cosa que desee.

# In[8]:


# Ahora, cuando miramos el contenido de las angiospermas
# deberíamos recuperar las variables que ingresamos

angiosperms


# Otra función conveniente es algo llamado `len()`, por longitud (length). Length te devolverá la longitud de una lista, cuántos elementos hay en 
# ella. Por ejemplo, sabemos que nuestra lista de angiospermas tiene tres elementos. Entonces, si ponemosla lista en la función `len()`, obtenemos
# Tres. 

# In[9]:


# Otra función conveniente es len()
# len() devuelve la longitud de una lista, cuántos elementos tiene
# Por ejemplo, nuestra lista de angiosperms tiene 3 elementos

len(angiosperms)


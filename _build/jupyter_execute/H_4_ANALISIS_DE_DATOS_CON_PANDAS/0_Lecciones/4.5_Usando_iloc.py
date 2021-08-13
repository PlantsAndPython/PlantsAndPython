#!/usr/bin/env python
# coding: utf-8

# # 4.5 Usando iloc

# ## Cómo usar `iloc` para aislar datos dentro de un marco de datos (filas primero, columnas segundo, inicio:final y corchetes)
# ______

# ***Mira este video de 12:06 a 16:25***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Guillermo Rodríguez Guerrero (UNAM ENES León, México).

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=12, seconds=6).total_seconds())
end=int(timedelta(hours=0, minutes=16, seconds=25).total_seconds())

YouTubeVideo("jEQRU55x0e4",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# > 💡 ***Recuerde:*** Importe `pandas` y lea el conjunto de datos a continuación para completar esta lección

# In[2]:


# Importe pandas

import pandas as pd


# In[3]:


# Decargue el conunto de datos del
# Jupyter Book para leer localmente o
# leer desde GitHub, a continuación:

data = pd.read_csv('https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/co2_mlo_weekly.csv')


# A continuación, veamos otra forma de encontrar datos específicos. y esto se llama función "iloc". Y esto usará filas y columnas para encontrar los datos que quieres. Es algo así como Excel, piensa en qué filas y columnas deseas aislar de los datos. Lo puedes hacer, tanto para las filas como para las columnas, puedes usar la indexación con la notación de dos puntos de inicio y final que aprendiste antes. 
# 
# Así que repasemos de nuevo como se ven nuestros datos, recuerda que usamos "head", que solo trae de vuelta las primeras cinco columnas, pero lo más importante es que te da los nombres de las columnas. Y podemos ver que la primera columna es "date", la segunda columna es "running_date", la tercera columna es "month", la cuarta es "year", y la quinta es "CO2ppm".

# In[4]:


# También podemos acceder a filas y columnas específicas
# usando indexación con .iloc ()

# Veamos los datos nuevamente usando .head ()

data.head()


# Entonces, todo lo que necesita saber sobre "iloc" es que la primera posición son las filas, la segunda posición son las columnas, y puedes usar la indexación para filas y columnas. 
# 
# Entonces, si solo usamos "data.iloc" y solo ingresamosun número, es la ranura de las filas. Recuerda, la indexación comienza en cero, por lo que esto debería devolvernos solo la primera fila de data.
# 
# Y tú puedes ver que esto es 13 de agosto de 2017, fecha de ejecución 1 , mes agosto, año 2017, y partes por millón 405.2, que es la primera fila de data. Entonces, las filas y 
# luego el índice nos dan la primera fila de data.

# In[5]:


# La primera posición en .iloc son las filas
# La segunda posición en .iloc son las columnas
# Usamos indexación y dos puntos start:end
# para hacer referencia a qué filas y columnas queremos

# La indexación comienza en 0, por lo que volvemos a la primera fila

data.iloc[0]


# Recuerda, uno negativo en la indexación es una forma de obtener el último elemento y, por lo tanto, si solo hacemos uno negativo
# de nuevo, posición de la fila, y volvemos a la última fila. Y puedes ver que es la última fila porque tiene la fecha de ejecución de 714.

# In[6]:


# -1 con indexación es el último elemento
# devuelve la última fila

data.iloc[-1]


# Podemos hacer referencia a filas y columnas, por lo que podríamos decir la última fila, y recuerda, si solo ponemos dos puntos, que deberían tener el inicio y el final, pero no ponemos cualquier número, solo vamos a obtener todos los valores, por lo que esta será la última fila pero todas las columnas. Y de 
# hecho eso es lo que obtenemos: la última fila, 714, pero todas las columnas, lo que equivale a poner un 1 negativo. Pero también funciona de esta manera porque formalmente hablando que queremos todas las columnas.

# In[7]:


# Podemos hacer referencia a la última fila y a todas las columnas.

data.iloc[-1, :] # start:end, but : refers to all columns


# En este caso, con solo dos puntos vacíos para las filas, estamos diciendo que queremos todas las filas, pero solo queremos la primera columna, la columna de índice cero, recuerda que es la fecha, así que obtenemos todas las fechas porque pedimos todas las filas de solo la primera columna.

# In[8]:


# Aquí ":" se refiere a todas las filas.
# para la primera columna referida con 0

data.iloc[:,0]


# También podríamos obtener todas las filas para la segunda columna, recuerda que la segunda columna es la fecha de ejecución, por lo que es de uno a 714.

# In[9]:


# También podríamos obtener todas las filas
# y la segunda columna, en el índice 1

data.iloc[:,1]


# Recuerda, puedes usar la indexación tanto para las filas como para las columnas. La indexación es inclusiva del inicio pero hasta el final y sin incluirlo. Entonces en este caso estamos diciendo que queremos las flas dos y tres porque vamos a subir pero sin incluir cuatro, así que estas son las filas dos y tres
# para columnas desde dos hasta el final, que sería la tercera columna hasta el final.
# 
# Como puedes ver obtenemos las filas dos y tres que incluyen el inicio también y sin incluir cuatro, las filas dos y tres, y
# obtenemos la segunda posición de índice de las columnas, que es la tercera columna hasta el final.

# In[10]:


# La indexación se puede utilizar tanto 
# para las filas como para las columnas

data.iloc[2:4, 2:] # indexing inclusive of start but not the end


# Puedes usar corchetes separados por comas para obtener filasmuy específicas en columnas muy específicas. Y que si quisieras
# posiciones de índice 0, 3, 5 y 7 para filas y posiciones de columna 0, 2 y 4? Y luego puedes ver que eso es exactamente lo que obtenemos:las filas indexadas por esos números aleatorios
# y luego la primera, tercera y quinta columnas, porque recuerda que la indexación comienza en cero.

# In[11]:


# Los corchetes entre corchetes se pueden utilizar 
# para hacer referencia a filas y columnas específicas

data.iloc[[0,3,5,7],[0,2,4]]


# Entonces, iloc es una forma muy específica de obtener
# datos muy específicos por fila o por columna.

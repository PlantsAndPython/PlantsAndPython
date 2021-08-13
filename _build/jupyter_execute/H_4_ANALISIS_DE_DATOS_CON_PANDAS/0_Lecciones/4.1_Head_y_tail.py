#!/usr/bin/env python
# coding: utf-8

# # 4.1 Head y tail

# ## Cómo evaluar rápidamente las propiedades del marco de datos, usando `head` y `tail`
# _____

# ***Mira este video de 2:25 a 4:12***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Guillermo Rodríguez Guerrero (UNAM ENES León, México).

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=2, seconds=25).total_seconds())
end=int(timedelta(hours=0, minutes=4, seconds=12).total_seconds())

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


# Ahora veamos cómo mirar nuestro marco de datos usando "head" y "tail".
# 
# Por lo tanto, es importante saber con qué se está trabajando 
# para ver el marco de datos y "head" y "tail" nos permite hacer eso. Así que recuerda que los datos se almacenan en el objeto data y usamos ".head" y lo que veremos es una vista previa de las primeras cinco filas y también obtendremos los nombres de las columnas.

# In[4]:


# Es importante saber con qué estás trabajando
# para "ver" el marco de datos
# .head() muestra las primeras filas y los nombres de las columnas

data.head()


# También podemos usar "tail". Y "tail", si "head" está al principio, entonces "tail" es el final. Y puedes ver que obtenemos las últimas filas de nuestro conjunto de datos. "tail" es muy útil para ver solo cuántas filas tienes en total. Recuerda que comenzamos con cero, entonces tenemos 714 filas o puntos de datos en este conjunto de datos.

# In[5]:


# .tail() muestra las últimas filas

data.tail()


# "Describe" es una función muy útil que te devuelve estadísticas resumidas para tus variables continuas. Entonces, si usamos "describe" en nuestros datos, lo que obtenemos es la fecha de ejecución, que fue solo desde el día uno hasta el 714, un número que aumenta para realizar un seguimiento del día; el año se incluye como una variable continua, aunque no queremos que sea una variable continua; y partes de CO2 por millón, es, por supuesto, una variable continua. Obtenemos cuánto de cada uno tenemos. Tenemos 714 de cada uno. Obtenemos la media de cada uno; la desviación estándar; el mínimo; los cuartiles en el 25,
# 50 y 75, cuartiles; y el valor máximo también. 

# In[6]:


# .describe() es muy útil, muestra estadísticas resumidas
# proporciona estadísticas para variables continuas

data.describe() 


# Así es como se lee en un marco de datos,
# cómo mirar rápidamente el marco de datos y obtener 
# estadísticas resumidas de las variables continuas.

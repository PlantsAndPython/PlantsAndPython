#!/usr/bin/env python
# coding: utf-8

# # Lección 4.4

# ## Cómo enmascarar datos (una declaración booleana para pescar los datos que desea, corchetes después de un marco de datos
# ____

# ***Mira este video de 8:06 a 12:06***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Guillermo Rodríguez Guerrero (UNAM ENES León, México).

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=8, seconds=6).total_seconds())
end=int(timedelta(hours=0, minutes=12, seconds=6).total_seconds())

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


# A continuación, hablaremos de algo llamado enmascaramiento. El enmascaramiento es muy importante y es una forma de encontrar datos específicos que cumplen un criterio y es una declaración booleana; recuerda, una declaración booleana es algo que solo se puede evaluar como Verdadero o Falso, para encontrar todos los datos en su marco de datos que sean verdaderos con respecto a la declaración booleana.
# 
# Así que esto es lo que hace el enmascaramiento: nos da datos específicos y, como dije, es muy simple, una máscara es solo una declaración booleana.
# 
# Entonces decimos que la máscara es igual a y luego tenemos una declaración booleana. Entonces, para los datos en la columna del mes, los meses, la declaración booleana es que es igual a agosto. Usamos un doble igual aquí porque recuerda, cuando usamos Python, puede tener menor o igual a, mayor o igual a, pero igual a igual es verdaderamente igual. Entonces, la declaración booleana es elmes de agosto, Verdadero o Falso, esa es la máscara, y estamos estableciendo esta declaración booleana 
# igual a la máscara. 
# 
# Entonces presionamos shift + enter y luego podemos ver qué es la máscara.

# In[4]:


# ¿Cómo obtenemos datos específicos?
# ¿Qué pasa si queremos todos los puntos de datos solo del mes de agosto?
# ¡Creamos una máscara!
# Una máscara es una declaración booleana donde los datos que desea son TRUE

mask = data['month']=='aug'


# Y lo que ves es la máscara, es que devuelve las filas del
# marco de datos que cumplen los criterios. Entonces, este es 
# un marco de datos grande, por lo que comienza desde el principio
# luego se rompe y luego llega hasta elfinal. Si recuerdas, el mes de agosto fue el primer valor de data. Así que puedes ver que estasfechas de agosto, eran las que estaban en la parte superior de del marco de datos, se evalúan como Verdadero. Pero luego 
# evalúan como Falso cuando el mes no es agosto.

# In[5]:


# La máscara devuelve qué filas se evalúan como TRUE para la declaración booleana

mask


# Podemos obtener todos los datos. Así que esto es todo lo que hace una máscara: está regresando para las filas que son Verdadero y Falso, pero si coloca la máscara dentro de los corchetes del marco de datos lo que obtienes es el marco de datos completo, esas filas del marco de datos que se evalúan como Verdadero.
# 
# Entonces, por ejemplo, aquí puedes ver lo que obtenemos son solo datos que son el mes de agosto. Estas fueron las únicas filas que cumplieron con la declaración booleana de ser Verdadero
# que eran agostos.
# 
# Así que eso es todo lo que es la máscara: recuerda que una máscara es solo una declaración booleana y ponemos la máscara entre paréntesis del marco de datos para devolver esas filas que se evalúan como Verdadero para la declaración booleana.

# In[6]:


# Si colocamos la máscara dentro de los corchetes del marco de datos
# luego se devuelven las filas donde la declaración es True

data[mask]


# Puedes utilizar esta técnica también con una columna. Por ejemplo, si dices que solo te interesan los valores de partes de CO2 por millón, te refieres a esa columna y los corchetes para obtenerla, pero tienes un segundo conjunto de corchetes con la máscara y cuando lo hagas solo habrás devuelto los valores de partes de CO2 por millón, ninguno del resto del marco de datos, porque especificaste esta columna específica.

# In[7]:


# Podemos limitar lo que se devuelve haciendo referencia a una columna específica.
# y colocando la máscara en un soporte doble

data['CO2ppm'][mask]


# Por lo general, viste que creamos una máscara, y la llamamos máscara, y estábamos escribiendo fuera de la máscara en nuestro código. Pero generalmente la gente no hace eso. Lo hacen mucho más simple, donde simplemente escriben la máscara.
# 
# Esta es la declaración booleana aquí, que he resaltado. Y ellos
# simplemente colocan la máscara en una línea de código con los datos o la columna específica que desean. Esto es un poco complicado de ver, pero recuerda siempre ir primero a la máscara y estará en el segundo conjunto de corchetes o estará en el primer conjunto de corchetes y es solo una declaración booleana. Y devolverá las filas que son verdaderas para la declaración booleana. Y esta es una forma que obtiene los datos específicos que deseas.

# In[8]:


# Por lo general, la máscara se escribe directamente en la línea de código.
# Mire siempre al segundo juego de corchetes para ver
# que es la mascara

data['CO2ppm'][data['month']=='aug']


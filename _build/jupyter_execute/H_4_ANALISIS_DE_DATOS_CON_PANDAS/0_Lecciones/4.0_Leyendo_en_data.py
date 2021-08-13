#!/usr/bin/env python
# coding: utf-8

# # 4.0 Leyendo en data
# 
# # Pandas, dataframes y seaborn 🐼

# ____
# 
# En las lecciones anteriores, nos hemos centrado en aprender los aspectos básicos de Python: listas, matplotlib y bucles. Los usamos para hacer modelos de filotaxia y girasoles en crecimiento.
# 
# Ahora, cambiamos nuestro enfoque de la programación y el modelado formales al análisis de datos. ¡El análisis de datos significa marcos de datos, pandas y seaborn!
# 
# A menudo, tus datos se parecerán mucho a una hoja de cálculo de Excel, con filas, columnas y encabezados de columna. Pero necesitamos más funcionalidad de la que puede proporcionar Excel. Ahí es donde entra pandas. Pandas se parece mucho a la versión Python de R, lo que significa que está diseñado para usar marcos de datos y tiene muchas capacidades estadísticas integradas. Para graficar, Seaborn es un módulo de graficación de Python que, aunque carece de la versatilidad de matplotlib, está construido para graficar teniendo en cuenta las necesidades estadísticas.
# 
# No podemos cubrir todo lo que hace pandas en unos pocos notebooks. Pero a medida que continúes tus estudios y necesite hacer algo específico con respecto a la limpieza o el análisis de datos, hay muchos [tutoriales](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html) ( incluyendo una [hoja de trucos](http://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)) que sin duda tendrá lo que necesitas. Y, por supuesto, ¡busca en Google tu pregunta! 
# 
# La mejor manera de utilizar seaborn es mirar la [galería de gráficos](https://seaborn.pydata.org/examples/index.html) y seleccionar lo que necesitas. La documentación y los ejemplos estarán allí. 
# 
# Mira el video a continuación para comenzar a usar pandas y seaborn. Analizaremos un conjunto de datos que examinan las fechas de cosecha en las vides europeas con respecto a un clima cálido más adelante en el notebook. Entonces, en este video, veremos las mediciones de los niveles de CO2 en ppm del [Observatorio Mauna Loa en Hawái](https://www.co2levels.org/#sources). Puedes descargar el conjunto de datos utilizado en el video [aquí](https://github.com/DanChitwood/PlantsAndPython/blob/master/co2_mlo_weekly.csv). 
# 
# Presta atención a los siguientes puntos:

# ## 🐍 Objetivos de aprendizaje de Python
# 
# - Cómo leer en un marco de datos usando `pandas` (*1:32*)
# - Cómo evaluar rápidamente las propiedades del marco de datos, usando `head` y` tail` (*2:28*)
# - Cómo seleccionar columnas de un marco de datos (*4:10*)
# - Cómo realizar estadísticas descriptivas usando `pandas` (` .min`, `.max`,` .std`, `.value_counts`) (*6:09*)
# - Cómo enmascarar datos (una declaración booleana para pescar los datos que desea, corchetes después de un marco de datos) (*8:00*)
# - Cómo usar `iloc` para aislar datos dentro de un marco de datos (filas primero, columnas segundo, inicio: final y corchetes) (*12:13*)
# - Trazado con `seaborn` (trazado especializado para estadísticas) (*16:32*)

# ## 🌻 Objetivos de aprendizaje de plantas
# 
# - Los niveles de CO2 están aumentando, lo que aumenta las temperaturas globales.
# - Las plantas responden a los aumentos de CO2 y temperatura.
# - En la siguiente actividad, examinaremos los efectos del calentamiento global en las plantas de cultivo.
# - Las estadísticas y la visualización de datos son técnicas poderosas para explorar las tendencias globales. 
# 

# ## Cómo leer en un marco de datos usando `pandas`
# ____

# ***Mira este video de 0:00 a 2:25***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Guillermo Rodríguez Guerrero (UNAM ENES León, México).

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=2, seconds=25).total_seconds())

YouTubeVideo("jEQRU55x0e4",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Entonces, primero aprendamos a leer en un marco de datos usando el módulo pandas.
# 
# Pandas generalmente se importa como pd, por lo que presiona shift + enter para importar pandas y la función más útil en pandas es probablemente read_csv (). Esta es una función que tomará los datos .csv y los leerá como un marco de datos. Los marcos de datos tienen filas y columnas y las columnas tienen nombres. De forma predeterminada, los archivos deben estar en el
# directorio de inicio, pero también puedes proporcionar la ruta
# al archivo. 
# 
# Entonces, por ejemplo, cargaré estos datos desde mi escritorio, así que agregué "./Desktop" y luego el nombre del archivo. Entonces presionamos shift + enter y ahora hemos creado una variable, data, que contiene nuestro marco de datos.
# 
# **En el video, el archivo se lee localmente desde el escritorio, pero aquí cargaremos los datos usando un enlace de GiHub donde se publican los datos.**

# In[2]:


# pandas generalmente se importan como "pd"

import pandas as pd


# In[3]:


# Una función útil es pd.read_csv ()
# que se lee en un CSV como un marco de datos
# Los marcos de datos tienen filas y columnas con nombres

# Por defecto, el archivo debe estar en su directorio de inicio
# pero también puedes proporcionar una ruta
# Por ejemplo, lo cargaré desde mi Desktop

# data = pd.read_csv("./Desktop/co2_mlo_weekly.csv")

# NOTE: en el video, el archivo se lee localmente desde el Desktop
# pero aquí cargaremos los datos usando un enlace de GitHub 
# donde se publican los datos

data = pd.read_csv('https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/co2_mlo_weekly.csv')


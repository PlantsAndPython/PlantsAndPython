#!/usr/bin/env python
# coding: utf-8

# # Lección 4.7

# ## Práctica con Pandas, Dataframes y Seaborn 🐼

# 
# ---
# ## Exploración de datos
# 
# ### Cargando e inspeccionando los datos
# 
# Después de visitar Michigan y aprender que se pueden cultivar uvas para vino (¡y que se puede hacer vino!) En un lugar tan frío, decides que te gustaría comenzar un viñedo allí. Has visto los viñedos y sabes que, aunque es posible cultivar uvas de vinificación allí, a veces hace demasiado frío. Uno se pregunta si, debido al cambio climático, Michigan pronto tendrá un clima más cálido y más adecuado para el cultivo de uvas.
# 
# Sabes que Europa tiene una larga historia de cultivo de uvas y te preguntas si mantuvieron registros que pudieran indicar cómo responden las uvas a los cambios de temperatura. Encuentras un [estudio](https://www.clim-past.net/8/1403/2012/cp-8-1403-2012.pdf) que ha recopilado numerosos registros de fechas de cosecha de uvas durante más de cuatro siglos y también una [base de datos](http://www.climatemonitor.it/?page_id=40210&lang=en) de anomalías de temperatura en Europa que se remontan a 1655.
# 
# Usando el conjunto de datos proporcionado, `grape_harvest.csv` (descarga [aquí](https://github.com/DanChitwood/PlantsAndPython/blob/master/grape_harvest.csv)), explora cómo la fecha de cosecha de la uva europea cambia con respecto a la temperatura a lo largo de siglos de datos.
# 
# Para comenzar, importa `pandas` en la celda siguiente: 

# In[1]:


# Importa pandas aquí



# Luego, lee en `grape_harvest.csv` usando la función `pd.read_csv()` un marco de datos de pandas.

# In[2]:


# Lee los datos de la cosecha aquí
# Coloca grape_harvest.csv en el mismo directorio desde el que estás ejecutando este .ipynb
# Si está en un directorio diferente, deberás especificar la ruta al archivo 

# Alternativamente, puede leer los datos de GitHub usando la siguiente URL:
# https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/grape_harvest.csv




# Ahora, escribe un código para inspeccionar las propiedades de los datos y luego responde las siguientes preguntas:
# 
# Usa una función de pandas para mirar las primeras cinco líneas de datos:

# In[3]:


# Pon tu código aquí



# Usa una función de pandas para ver las últimas cinco líneas de datos: 

# In[4]:


# Pon tu código aquí



# Usa una función de pandas para ver un resumen de las estadísticas (como el recuento, el mínimo, el máximo y la media) para columnas con datos continuos:

# In[5]:


# Pon tu código aquí



# Utiliza una función de pandas para obtener los nombres de las columnas. 

# In[6]:


# Pon tu código aquí



# Para una de las columnas que es una variable categórica, usa una función para enumerar todos los niveles para esa variable. 

# In[7]:


# Pon tu código aquí



# Para la variable categórica, también usa una función para determinar cuántas filas hay que representan cada nivel.

# In[8]:


# Pon tu código aquí


# ¿Cuántas filas hay en este conjunto de datos? 

# In[9]:


# Pon tu código aquí



# ¡Felicitaciones por leer los datos y explorar su estructura! En la siguiente actividad, exploraremos la relación entre las fechas de cosecha de la uva y el clima. 

#!/usr/bin/env python
# coding: utf-8

# # Lección 4.6

# ## Trazado con seaborn (trazado especializado para estadísticas)
# ______

# ***Mira este video de 16:25 a 25:29***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Guillermo Rodríguez Guerrero (UNAM ENES León, México).

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=16, seconds=25).total_seconds())
end=int(timedelta(hours=0, minutes=25, seconds=29).total_seconds())

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


# A continuación echemos un vistazo a seaborn, que es una 
# forma alternativa a matplotlib para ver tus datos. Y como verás, seaborn es mucho más especializado para graficar datos estadísticos que matplotlib.
# 
# 
# Entonces ya has visto cómo usar matplotlib antes. Carga en el módulo de esta manera. Pero para seaborn funciona mucho mejor con pandas. Como verás, funciona mucho mejor con marcos de datos y puedes realizarfunciones estadísticas muy sofisticadas y también es un poco más estético en producir figuras atractivas rápidamente que matplotlib. Así que importamos seaborn como sns.
# Además, seaborn tiene algo llamado estilos y puedes usarlos usando "sns.set" y puedes buscar los diferentes estilos. Y 
# es una forma fácil de cambiar, por ejemplo el fondo, las líneas de la cuadrícula, los ejes de los ticks y cosas por el estilo en los gráficos que realices. Así que presionamos shift + enter para importar seaborn.

# In[4]:


# Hemos visto cómo se puede usar matplotlib para trazar y visualizar datos

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Pero también hay otro paquete llamado seaborn
# seaborn es mejor que matplotlib con respecto a
# jugando bien con pandas y marcos de datos
# y para funciones estadísticas específicas

import seaborn as sns
sns.set() # sets different styles, for figures/presentation/poster


# Es útil mirar a través de la galería seaborn. Busque la grafica, la función o el estilo que necesita y observe el ejemplo.
# 
# Galería: [https://seaborn.pydata.org/examples/index.html](https://seaborn.pydata.org/examples/index.html)
#     
# Explore los estilos seaborn aquí: [http://seaborn.pydata.org/tutorial/aesthetics.html](http://seaborn.pydata.org/tutorial/aesthetics.html)

# Entonces, una de las funciones máscomunes para hacer diagramas en seabornse llama "lmplot()". Así que nosotros lo llamamos por "sns.lmplot()" y así de fáciles usar seaborn. Con solo hacer referencia a tu marco de datos, diciendo que datos son iguales a tu marco de datos, en nuestro caso es data, tan pronto como le digas a seaborn cuál es el marco de datos, puedes hacer referencia a tus datos por el nombre de la columna.
# 
# Entonces digamos que queremos diagrama lineal del modelo utilizando lmplot, donde el eje x es lacolumna "running_date" y el eje y son las partes de CO2 por millón y decimos que nuestro marco de datos es "data" y muy rápidamente seaborn llegará a este hermoso diagrama. Puedes ver los datos aquí. Veseste cíclico cíclico de partes por millón de CO2 esto sucede todos los años, tiene que ver con la variación estacional de la tierra, y esto se debe literalmente a que las plantas están 
# muriendo en el invierno en el hemisferio norte y viceversa en el hemisferio sur y la cantidad de dióxido de carbono que están absorbiendo y liberando y descomponiendo y otras cosas que contribuyen al CO2 crea estos estos ciclos realmente sorprendentes. Estos datos, si recuerdas, son de 2017,
# 2018 y 2019 y, aunque está subiendo y bajando, la tendencia general es subir. Entonces la función de gráfico lineal se refiere al modelado lineal, por lo que trazará tus datos como un gráfico de dispersión como puedes ver con estos puntos. Estos son los valores de CO2 que especificamos para nuestro eje y, pero automáticamente intentará ajustar una línea a tus datos. Una línea no es apropiada para la naturaleza cíclica de estos datos como puede ver. Tendrías que usar algo como una función sinusoidal para eso, pero puedes ver porque el nivel de CO2 está aumentando en general que la función lineal es apropiada por observar ese aumento general.

# In[5]:


# lm se refiere a "linear model"
# La función sns.lmplot ajustará una línea a sus datos

sns.lmplot(x='running_date', y='CO2ppm', data=data)


# Sinembargo, digamos que solo queremos el diagrama de dispersión,
# no queremos una línea en él. Entonces puedes ejecutar la 
# misma línea de código con lmplot() pero este argumento
# "fit_reg" es si seaborn debería intentar ajustarse a un 
# modelo lineal y se puede decir Falso. Entonces, si dices falso
# luego, se obtiene el diagrama de dispersión de partes de CO2 
# por millón. 

# In[6]:


# Pero tal vez no quieras la línea
# ¡Establezca fit_reg en False y obtendrá solo el diagrama de dispersión!

sns.lmplot(x='running_date', y='CO2ppm', data=data, fit_reg=False)


# Otra función realmente genial en seaborn es "distplot", esto es comoun diagrama de densidad o histograma y tú solo dices qué columna quieres crear el diagrama de histograma de densidad ysi queremos ver partes de CO2 por millón y obtendrás un hermoso histograma, pero lo más importante es que obtienes la densidad
# estimada de la distribución de los datos también.

# In[7]:


# Utilice sns.distplot () para trazar una gráfica de densidad / histograma

sns.distplot(data['CO2ppm'])


# Digamos que queremos ser mas específicos. Queremos observar las diferentes densidades de los años 2017, 2018 y 2019. Así que recuerda que ya convertimos el año en una variable categórica, pero podemos crear máscaras. Entonces vamos a decir que queremos los datos de CO2, verdad? Entonces nos referimos a la columna de CO2 como un stringn en los corchetes y luego ponemos un segundo par de corchetes con nuestra máscara. Decimos que queremos todos los datos para el CO2 para el año 2017. Entonces decimos dónde año, dónde es cierto que ese año es igual a 2017, y creamos un objeto para almacenar esos datos y lo llamamos año 2017. Hacemos lo mismo para el año 2018 y hacemos lo mismo para el año 2019. Así que ahora tenemos nuestros años separados.

# In[8]:


# ¿Qué pasa si queremos separar nuestros datos por categorías?
# Por ejemplo, ¿por año?

# Hacemos mascaras!

year2017 = data['CO2ppm'][data['year']==2017]
year2018 = data['CO2ppm'][data['year']==2018]
year2019 = data['CO2ppm'][data['year']==2019]


# Usamos enmascaramiento y es como matplotlib: puedes seguir llamando a las funciones de diagramas una tras otra y simplemente pegaránlos datos en la parte superior del diagrama que estás haciendo. Así que queremos un diagrama de densidad de losvalores de CO2 del año 2017, una gráfica de densidad del año 2018, y la gráfica de densidad del año 2019, y puedes ver que los teníamos todos combinados antes ahora está creando estos diferentes diagramas de densidad y podemos ver que hay diferencias claras en los niveles de CO2 entre años y que están aumentando.

# In[9]:


# Al igual que matplotlib, puede seguir llamando a una función
# para seguir trazando categorías de datos en el mismo gráfico

sns.distplot(year2017, label='2017')
sns.distplot(year2018, label='2018')
sns.distplot(year2019, label='2019')


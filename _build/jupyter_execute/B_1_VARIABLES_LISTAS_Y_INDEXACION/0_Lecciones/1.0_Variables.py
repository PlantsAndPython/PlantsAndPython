#!/usr/bin/env python
# coding: utf-8

# # Lección 1.0
# # Variables, funciones, listas e índices
# ______

# En nuestro primer video tutorial, vamos a aprender los fundamentos de Python. Aprenderás a crear una variable. Usarás funciones para procesar variables y crear salidas (outputs). Y aprenderás sobre la indexación, una forma de llevar un registro de los datos, acceder a ellos, modificarlos y utilizarlos.
# 
# Los objetivos de aprendizaje que se cubren en el video tutorial se describen a continuación. Se proporciona la marca de tiempo para cada objetivo. Siéntete libre de realizar los ejemplos del video y crear nuevas celdas en este cuaderno, puedes ir a tu propio ritmo. Pon pausa al vídeo y rebobínelo cuando sea necesario para repasar los conceptos que sean necesarios. Juega con tus propios ejemplos o datos y explora.
# 
# Hay objetivos de aprendizaje tanto para Python como para las plantas:

# ### 🐍 Objetivos de aprendizaje de Python
# 
# - **¿Cómo crear una variable?** (*1:15*)
#     - La variable no tiene comillas
#     - Una cadena siempre lleva comillas, ya sea " " o ' '
# - **Nuestra primera función: `print()`** (*2:31*)
#     - Los argumentos van dentro de los paréntesis
# - **¿Qué es la indexación?** (*4:05*)
#     - La indexación tiene la forma de [start:end]
#     - La indexación siempre empieza en cero
#     - El inicio es inclusivo
#     - El final no es inclusivo
#     - La indexación se puede utilizar para acceder a caracteres específicos en una `cadena' (string, en inglés)
# - **¿Cómo crear listas?** (*9:17*)
#     - Utilizar paréntesis vacíos [ ] 
#     - Rellenar con variables o cadenas
#     - Las funciones `type()` devuelven el tipo de datos (list, str, int, float)
#     - La función `len()` devuelve la longitud de una lista
# - **¿Cómo utilizar la indexación para acceder a elementos específicos de una lista?** (*12:25*)
# - **¿Cómo modificar listas?** (*13:36*)
#     - Los elementos de la lista pueden ser reasignados usando la indexación
#     - La función `.append()` puede utilizarse para añadir un elemento a una lista
# - **¿Cómo crear una lista de listas?** (*16:31*)
#     - Los elementos dentro de una lista de listas pueden ser indexados usando corchetes dobles
# 

# ### 🌻 Objetivos de aprendizaje en biología vegetal
# 
# - **Las plantas son esenciales para la vida humana** (*16:46*)
#     - Las plantas nos alimentan, nos visten, nos dan cobijo, nos medican y nos inspiran
#     - Las plantas regulan los ciclos globales del agua y el carbono
# - **Las plantas son diversas, más diversas de las que observamos en la tierra o las que tienen flores**
# - **Las plantas están organizadas jerárquicamente, lo que refleja la historia evolutiva**
# - **Las especies se denominan con un nombre de género y de especie**
# - **Las plantas se definen por un único y antiguo evento endosimbiótico del cuál surgieron los coloroplastos.**
# - **Una visión general de la evolución de las plantas**
#     - Algas rojas y verdes (Rhodophyta y Chlorophyta)
#     - Plantas no vasculares (briofitas: musgos, hepáticas y hornabeques)
#     - Plantas vasculares sin semilla (Licopitas, helechos/pteridofitas, gimnospermas)
#     - Plantas con semilla (Gimnospermas y Angiospermas)

# ## ¿Cómo crear una variable?
# ____

# ***Mira este video de 0:00 a 2:28***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Alice Luckie (UNAM ENES León, México)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=2, seconds=28).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# El primer tema que veremos es cómo crear una variable. Por favor, siéntase libre de escriba en su propio cuaderno de Jupyter o pause o rebobine el video para repasar un punto nuevamente. Una variable es un tipo de datos en Python que devuelve un valor. Este valor puede ser un número como un entero, flotante o puede ser una cadena. Una cadena es una serie de caracteres. Las variables no van entre comillas. Pueden ser una combinación de letras y números y se les asigna un valor. Las cadenas
# que son un tipo de valor, siempre tienen comillas. Las comillas pueden ser dobles marcas o ser comillas simples. Ahora, creemos dos variables, `genus` y `species`, y vamos a darle los valores de cadenas. `"Vitis"` para `genus` y `"_vinifera"` para `species`. Recuerde que para crear sus variables necesita ejecutar la celda Jupyter. Para hacerlo presiona shift y enter.

# In[2]:


# Una variable no tiene comillas
# Una cadena tiene comillas, dobles o simples
# Recordatorio: debes ejecutar una celda con shift + enter
# para crear sus variables

genus = "Vitis"
species = '_vinifera'


# Ahora que hemos creado nuestras variables, podemos ver cuáles son. Estas son capaces de devolvernos un valor. Entonces, por ejemplo, si escribimos `genus`, ahora que le hemos asignado un valor, y ejecutamos la celda con género obtendremos `"Vitis"`.

# In[3]:


# Ejecutar una celda con una variable imprimirá su valor

genus


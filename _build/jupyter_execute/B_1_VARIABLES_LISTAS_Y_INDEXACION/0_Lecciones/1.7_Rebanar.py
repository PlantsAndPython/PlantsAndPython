#!/usr/bin/env python
# coding: utf-8

# # 1.7 Rebanar
# # Rebanar y tipos de datos
# ____

# Acabas de aprender sobre listas e indexación. Pero la mayoría de los ejemplos eran con cadenas y nombres. ¿Qué pasa con los números?
# 
# En el siguiente video estarás usando listas con números. También aprenderás sobre slicing (rebanar o rebanado, en español), que lleva la indexación al siguiente nivel añadiendo un valor adicional `step` que puede devolver valores de cada enésimo término de una lista.
# 
# Los objetivos de aprendizaje para este vídeo son los siguientes:

# ### 🐍 Objetivos de aprendizaje de Python
# 
# - Usar números con listas (*1:04*)
# - El rebanado puede acceder a elementos de la lista con un inicio, un final y un paso
# - El inicio de una 'rebanada' es inclusivo, el final no lo es
# - Diferentes tipos de datos en Python: cadenas (strings), enteros(integers), flotantes(floats) (*3:11*)
# - Cómo comprobar qué tipo de datos está utilizando con type()
# - Puedes convertir diferentes tipos entre sí usando str(), int(), float()
# 
# ### 🌻 Objetivos de aprendizaje en biología vegetal
# - El ángulo de oro es un número irracional, derivado de la secuencia de Fibonacci, que subyace a la disposición en espiral de las hojas y otros órganos (filotaxia) en las plantas (*3:16*)

# ## Usar números con listas y cortar
# ________

# **Mira este video de 0:00 a 3:09**
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Marilyn Vásquez-Cruz (Langebio-Cinvestav, Irapuato, México)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=3, seconds=9).total_seconds())

YouTubeVideo("CIlwbP_QM1w",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Recuerda que las listas pueden incluir cualquier tipo de datos, incluso otras listas. Inicializamos una nueva lista con corchetes vacíos y luego ponemos números en ella. Así que hagamos una lista muy fácil y usemos números de índice reales con ella. Entonces, crearemos una lista llamada "números", entre paréntesis, y comenzará en 0, el primer índice, y pasará a 20. Presionamos shift + enter para crear la lista.

# In[2]:


# Recuerde, las listas pueden incluir cualquier tipo de datos,
# ¡incluso otras listas!
# Podemos inicializar una nueva lista con corchetes vacíos []
# y luego poner números

# Hagámoslo fácil y hagamos una lista
# con números de índice reales

numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# Anteriormente, aprendiste sobre indexación y uso de valores iniciales y finales. Con el corte hay un valor de paso adicional. El corte utiliza dos ":" y tres valores con los corchetes y tiene la forma de inicio, fin y paso. Entonces, usando nuestra lista de números, intentemos con un comienzo de 2 y final de 16 en un paso de 2 y veamos lo que obtenemos. Puedes ver que el inicio es inclusivo, comienza en 2 pero al final de 16 no es inclusivo, sube pero no incluye 16. Por lo que incluye 14. Y, puedes ver que también hay un paso de 2. Es cualquier otro número.

# In[3]:


# La indexación es más que [inicio: fin]
# Con el corte, hay un valor de "paso"
# El corte usa dos dos puntos y tres valores
# con la forma de [inicio: final: paso]

# Probemos start = 2, end = 16 y step = 2

numbers[2:16:2]


# Hagamos lo mismo pero con un paso de 3, y veamos qué obtenemos. Así que comenzamos en 2, no subimos a 16, solo a 14, y puedes ver que estamos usando pasos de tres.

# In[4]:


# Let's try the same again but with step = 3

numbers[2:16:3]


# Puedes hacer abreviaturas. Puedes dejar el número de inicio y la indexación siempre comenzará en cero. Si omites, la indexación del número final continuará hasta el final. Incluirá el último número y si omites los pasos, se utilizarán incrementos de 1. Como puedes ver aquí, omitimos el inicio, y aún comenzamos en 0 . Aquí, omitimos el número final y llegamos hasta el 20. Y aquí omitimos el paso y estamos usando incrementos de uno.

# In[5]:


# Si omite el número de inicio, la indexación comienza en 0

print(numbers[:16:3])

# Si omite el número final, la indexación continúa hasta el final

print(numbers[2::3])

# Si omite el número de paso, se utilizan incrementos de 1

print(numbers[2:16])


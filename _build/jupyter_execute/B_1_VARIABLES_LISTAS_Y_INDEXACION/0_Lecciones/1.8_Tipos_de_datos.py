#!/usr/bin/env python
# coding: utf-8

# # 1.8 Tipos de datos
# ## Diferentes tipos de datos en Python y conversión entre ellos
# ______

# **Mira este video de 3:10 a 7:15**
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Marilyn Vásquez-Cruz (Langebio-Cinvestav, Irapuato, México)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=3, seconds=10).total_seconds())
end=int(timedelta(hours=0, minutes=7, seconds=15).total_seconds())

YouTubeVideo("CIlwbP_QM1w",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Tomemos un número real, es una aproximación del ángulo dorado en grados. Lo obtuve de este sitio web en línea. El ángulo dorado se encuentra en todas partes en la naturaleza y se deriva de la secuencia de Fibonacci. Más adelante en este curso, aprenderemos más sobre la secuencia de Fibonacci, y utilízalo para aproximar el ángulo dorado para que podamos modelar el crecimiento de los girasoles. Pero por ahora aquí está esta aproximación de este número irracional . Y vamos a llamar a este objeto `golden_ang`. Entonces presionamos shift + enter para crearlo.

# In[2]:


# Tomemos un número real, una aproximación
# del ángulo dorado en grados

# De la Encylcopedia online of Integer Sequences
# https://oeis.org/A096627

# El ángulo dorado se deriva de la secuencia de Fibonacci,
# que aprenderemos y usaremos para aproximar este
# Valor más tarde para modelar el crecimiento de los girasoles.

golden_ang = 137.5077640500378546463487396283702776206886952699253696312384958261062333851951


# Podemos preguntar, recuerda, qué tipo de datos estamos usando con la función `type()`. Entonces, si hacemos esto con el ángulo dorado, vemos que obtenemos esta respuesta llamado "float".

# In[3]:


# Podemos preguntar qué tipo de datos es
# y obtenemos "flotar" de regreso

type(golden_ang)


# Así que hay tres tipos de datos principales en Python con los que trabajaremos. Ya has visto cadenas en el video anterior. Estas son conjuntos de caracteres pero hay dos tipos numéricos principales: son flotantes y enteros. Y la diferencia es muy sencilla. Los flotantes tienen decimales y los enteros no. Puedes convertir datos en diferentes tipos en Python usando las funciones `float()`, `int()` y `str()`. Por ejemplo, si convierte el ángulo dorado a un número entero se convierte en un número entero. Entonces tomamos el ángulo dorado, ponemos en la función `int()`, y usamos `print()`, y obtenemos solo 137 sin lugares decimales.

# In[4]:


# Hay 3 tipos de datos principales en Python
# Ya usaste cadenas, colecciones de caracteres
# Hay dos tipos numéricos principales: flotantes y enteros
# Los flotantes tienen decimales y los enteros no

# Puede convertir datos en diferentes tipos usando el
# funciones float(), int() y str()

# Si convierte golden_ang en un número entero, se convierte en un número entero

print(int(golden_ang))


# Puedes volver a convertir un número entero en un flotante, pero perderá la información decimal. Entonces de nuevo, si convertimos el ángulo dorado, un número irracional, primero en un entero, solo 137, y luego convertimos este 137 entero en un flotante, la respuesta que obtenemos es un decimal, pero es el punto cero porque perdimos toda la información decimal cuando usamos esa función entera.

# In[5]:


# Puede convertir el entero de nuevo a un flotante,
# pero pierde la información decimal

# Observe el decimal ".0"

float(int(golden_ang))


# Puedes convertir un entero o un flotante en una cadena, esto tiene sentido porque una cadena es solo un conjunto de caracteres, correcto, pueden ser números, por lo que puede usar la función `str()` para esto. Puedes usar `str()` en el ángulo dorado, crearemos una cadena del ángulo dorado, y podemos imprimirlo y ver de qué tipo es.
# 
# Y puedes ver que cuando imprimimos la cadena el ángulo dorado se parece al número, realmente no podemos notar la diferencia. Pero cuando usamos
# `type()` podemos ver de hecho que es una cadena.

# In[6]:


# Puede convertir un entero o un flotante en una cadena

str_golden_ang = str(golden_ang)

print(str_golden_ang)

type(str_golden_ang)


# Puedes convertir una cadena de números en números reales. Entonces, por ejemplo, si tienes la cadena de números de ángulos dorados y la conviertes en un flotador, será un número, un flotante.

# In[7]:


# Puedes convertir una cadena de números en números

print(float(str_golden_ang))

type(float(str_golden_ang))


# Pero no puedes convertir caracteres en números, sin embargo. Así que recuerda, si usamos comillas, eso crea una cadena verdadera y estas son letras por lo que es difícil imaginar cómo convertirlos en un número, pero tomemos la cadena de letras del ángulo dorado e intenta convertirla en un flotador. Y si hacemos eso, obtenemos un error y dice que no se puede convertir una cadena en un flotador, lo que podríamos haber predicho. 

# In[8]:


# Aunque no puedes convertir caracteres en números

float("golden_ang")


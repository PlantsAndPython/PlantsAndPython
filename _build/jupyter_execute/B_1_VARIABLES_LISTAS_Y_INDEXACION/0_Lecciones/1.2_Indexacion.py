#!/usr/bin/env python
# coding: utf-8

# # 1.2 Indexación
# 
# ## ¿Qué es la indexación?
# - La indexación tiene la forma de `[start:end]`
# - La indexación siempre empieza en cero
# - El inicio es inclusivo
# - El final no es inclusivo
# - La indexación se puede utilizar para acceder a caracteres específicos en una cadena ("string", en inglés) o lista

# **Mira este video de 3:35 a 9:10**
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Alice Luckie (UNAM ENES León, México)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=3, seconds=35).total_seconds())
end=int(timedelta(hours=0, minutes=9, seconds=10).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# >💡 ***Recuerde:*** En los cuadernos anteriores, creó variables llamadas `genus` y `species`. Vuelva a crear las variables en la celda de abajo para completar esta lección.

# In[2]:


# Crea la variable `genus`
# y la variable `species`

genus = "Vitis"
species = "_vinifera"


# Así es como creas una variable. Esta es su primera introducción al primer tipo de datos en Python: una cadena es una colección de caracteres.
# 
# Aprendamos un poco sobre indexación. Indexación es una forma de realizar un seguimiento de los caracteres de una cadena o de los elementos de una lista y de acceder a ellos, de lo cual aprenderemos pronto. La indexación toma la forma de corchetes y tiene un valor inicial y un valor final separados por dos puntos. El primer elemento de una serie en Python siempre es cero. No es uno. Empieza en cero. Un valor inicial de indexación es inclusivo. Es el número en sí, pero lo que es más importante, el valor final no es inclusivo. La indexación sube hasta el valor final pero no lo incluye. 
#     
# Así que recordemos: teníamos nuestro género variable. Recuerda que asignamos es el valor de la cadena de `"Vitis"`. Intentemos acceder a la primera letra de esa cadena, la "V". Tu primera intuición podría ser que al principio para llegar al primer elemento dirías "1". Entonces tomamos
# nuestro género variable, lo ponemos entre corchetes, y ponemos uno con la esperanza de recuperar el primer caracter. En su lugar, recuperamos el segundo carácter, la "i", no el primero, por lo que este es por qué es importante recordar que en Python el primer elemento para la indexación siempre comienza en cero.

# In[3]:


# Recuerde, nuestra variable de género es "Vitis"
# Intentemos acceder al primer elemento
# Puede pensar que el primer elemento es 1

genus[1]


# Entonces, si ponemos entre corchetes, ponemos un cero y tenemos nuestra variable género, cuando usamos cero ahora recuperamos la primera letra, que era una "V" y puedes ver cómo estás usando este número para decir qué letra de la cadena desea recuperar. 

# In[4]:


# Pero en Python el primer elemento es siempre 0

genus[0]


# También podemos acceder a múltiples elementos en una cadena usando indexación. Recuerde que la indexación toma la forma de corchetes. Tiene un comienzo, dos puntos y un valor final. Recuerde que el comienzo es inclusivo y el final no es inclusivo. Sube al valor del final pero no lo incluye. Así que intentemos recuperar todas las letras de "Vitis".
# 
# Hay cinco letras en "Vitis", por lo que podría pensar que necesitamos cinco posiciones a la derecha y recuerde que la indexación comienza en cero, por lo que cinco posiciones serían cero, uno, dos, tres, cuatro. Tal vez para recuperar todo el "Vitis", vamos de cero a cuatro.
# 
# Y ese no es el caso, y recuerde que la razón es porque el valor de inicio es inclusivo, por lo que este será un índice de 1, pero esto subirá al valor de 4 pero no estará incluido. Por ejemplo, este es el elemento 0, 1, 2 y 3. El cuarto elemento es "s" pero no sube a cuatro, simplemente llega hasta él.

# In[5]:


# También podemos acceder a múltiples elementos usando indexación
# La indexación toma la forma de [inicio: final]
# El inicio es inclusivo
# El final no es inclusivo
# "Vitis" tiene cinco caracteres
# Para acceder a todo el mundo, tal vez deberíamos intentar:

genus[0:4]


# Y para recuperar todo valor de "Vitis" de nuestro género variable tenemos 
# que recordar que el final no es inclusivo. Vamos a ir hasta él pero no lo incluiré. Entonces, si pasamos de 0 a 5, son 6 caracteres, pero recuerde que no incluye los cinco, simplemente va directo a él, y por eso obtenemos hasta la cuarta posición de la "s" e inclúyala ahora: cero, uno, dos, tres, cuatro, sin incluir cinco.

# In[6]:


# Pero recuerda, el final no es inclusivo
# Necesitamos agregar un valor más para incluir el último carácter

genus[0:5]


# Dado que los caracteres de una cadena se pueden indexar, se les asignan valores. Puedes hacer aritmética con cuerdas, lo crea o no. Así que 
# creemos algunas variables más para repasar para la siguiente sección y agreguemos el género más la especie juntos. Vamos a crear una nueva variable ahora y llamémosla vino. Entonces, si creamos nuestra nueva variable, vino, y decimos que es igual al género que era "Vitis", recuerda, más especie que es la cadena "_vinifera" podemos crear esa nueva variable y luego podemos imprimirla. Y veamos qué obtenemos. Luego, obtenemos "Vitis_vinifera" todos junto como uno porque los sumamos.

# In[7]:


# Debido a que los caracteres se pueden indexar, puede hacer artihmética con cadenas!
# Creemos algunas variables más para configurarnos para la siguiente sección
# Agreguemos `genus` + `species` y llamemos a la nueva variable "wine"

wine = genus + species

print(wine)


# Para la siguiente sección, creemos dos variables más. Llamemos a un tequila, para estar en el mismo tema y viene de la planta "Agave_tequilana" y tenemos cerveza y eso viene de cebada, "Hordeum_vulgare". Y recuerde ejecutar esta celda para que podamos recuperar esas variables.

# In[8]:


# Creemos también otras dos variables en el mismo tema

tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"


# Entonces vamos imprima nuestras variables para asegurarse de que estén 
# bien y recuerda que podemos poner múltiples variables en nuestra función de impresión entre paréntesis. Están separados por una coma y luego obtenemos los valores de nuestras tres variables. Para el vino obtenemos "Vitis_vinifera"; tequila, "Agave_tequilana", y para cerveza, "Hordeum_vulgare". Uvas, agaves y cebada. Tenga en cuenta que tenemos nombres comunes para todos estos: uvas, agave y cebada, pero tenemos estos muy científicos nombres en latín para estas especies y siempre hay algo llamado género, que es la primera palabra; y una segunda palabra, que se llama epíteto de especie, y juntas definen una especie.

# In[9]:


# Imprimamos nuestras variables para comprobar que están bien

print(wine, tequila, beer)


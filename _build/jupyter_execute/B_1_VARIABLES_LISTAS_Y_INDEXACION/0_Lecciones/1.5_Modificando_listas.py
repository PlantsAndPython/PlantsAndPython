#!/usr/bin/env python
# coding: utf-8

# # Lección 1.5
# ## ¿Cómo modificar listas?
# ____

# **Mira este video de 13:34 a 16:25**
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Alice Luckie (UNAM ENES León, México)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=13, seconds=34).total_seconds())
end=int(timedelta(hours=0, minutes=16, seconds=25).total_seconds())

YouTubeVideo("4XIllJVnT4Y",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# >💡 ***Recuerde:*** En el cuaderno anterior, creó una lista llamada `angiosperms` que contiene las cadenas de `wine`, `tequila` y `beer`. Vuelva a crear la lista en la celda de abajo para completar esta lección.

# In[2]:


# Cree la lista angiosperms

wine = "Vitis_vinifera"
tequila = "Agave_tequilana"
beer = "Hordeum_vulgare"

angiosperms = [wine, tequila, beer]


# Entonces, ¿cómo podemos modificar una lista? Los elementos de la lista simplemente se pueden reasignar usando indexación. Así, por ejemplo, 
# se pueden utilizar otras especies distintas de *Vitis vinifera* para hacer vino. Por ejemplo, algunas especies de las que hablaremos 
# más adelante en este curso, se utilizan para portainjertos en su lugar, o se hibridan con *Vitis vinifera* para hacer diferentes tipos de vino. Entonces tal vez no sea correcto de nuestra parte llamar al vino solo *Vitis vinifera* que específicamente, tal vez deberíamos decir que es todo *Vitis*. Así que intentemos convertir *Vitis vinifera* nuevamente en solo *Vitis*.
# 
# Para que podamos imprimir el primer elemento de nuestra lista de angiospermas con ceroy mira qué es, debería ser *Vitis vinifera*.
# Especificamos que estamos hablando del primer elemento de las angiospermas a través de la indexación, por lo que decimos índice de angiospermas cero, y simplemente lo igualamos a *Vitis*. Recuerda que sera actualmente establecido en *Vitis vinifera* pero luego cambia a *Vitis*. Entonces, si trazamos la lista de nuevo, no deberíamos tener *Vitis vinifera*, deberíamos tener solo *Vitis*.
# 
# Para que puedas ver eso el primer elemento es *Vitis vinifera*, lo reasignamos, y luego cuando volvemos a imprimir la lista se puede ver
# que esta vinifera se ha transformado en *Vitis*. Todo lo que hicimos fue usar un signo igual y especificó el primer elemento con cero.

# In[3]:


# Los elementos de la lista se pueden reasignar usando indexación
# Se pueden utilizar otras especies distintas de Vitis vinifera para elaborar vino.
# Por ejemplo, algunas especies de Vitis de las que hablaremos
# se utilizan como portainjertos
# Reasignemos "Vitis_vinifera" en nuestra lista a solo "Vitis"

print(angiosperms[0])

angiosperms[0] = "Vitis"

print(angiosperms)


# Otra forma de modificar listas que usaremos muy a menudo es la función llamada `.append().`
# 
# El primer paso para usar esto es agregar `.append()` después de un nombre de lista.
# 
# El segundo paso es agregar entre paréntesis el elemento adicional que le gustaría agregar a la lista. El elemento adjunto se agregará al final de la lista
# 
# Entonces, usando `len()`, ya sabemos que nuestra lista actual de angiospermas tiene tres elementos.

# In[4]:


# Otra forma de modificar listas es usando la función .append ()
# El paso 1 es agregar ".append ()" después de un nombre de lista
# El paso 2 es agregar entre paréntesis el elemento adicional
# que desea agregar a una lista
# El elemento adjunto se agregará al final de la lista
# Actualmente nuestra lista de angiospermas tiene 3 elementos

len(angiosperms)


# Pero digamos que queremos agregar arroz, utilizado para hacer sake, hasta el final de nuestra lista.
# 
# 
# Entonces, especificamos la lista y las `angiospermas`, esto función que usamos diciendo `append()`. Debería pensar en esto como que el `append()` va a modificar este nombre de lista y ponemos en el valor de cadena que queremos agregar, el nombre de arroz, que es `Oryza`. Entonces, si presionamos shift + enter, deberíamos agregar `Oryza` al final de nuestra lista de `angiosperms`.

# In[5]:


# Pero agreguemos arroz, usado para hacer sake, al final de nuestra lista

angiosperms.append("Oryza")


# Entonces imprimamos nuestra lista de angiospermas. Ahora ves que tenemos cuatro cosas. Oryza, se ha añadido arroz a la última posición y si imprimimos la longitud de nuestra nueva lista de angiospermas, vemos que son cuatro, no tres. Así que agregamos con éxito este valor al final de la lista.

# In[6]:


# Ahora, nuestra lista debería tener 4 elementos

print(angiosperms)

print(len(angiosperms))


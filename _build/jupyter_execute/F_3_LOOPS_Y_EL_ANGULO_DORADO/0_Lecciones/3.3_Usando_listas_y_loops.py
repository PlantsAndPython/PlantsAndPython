#!/usr/bin/env python
# coding: utf-8

# # Lección 3.3

# ## Cómo crear una lista vacía fuera de un loop y llenarla con resultados del loop
# ____

# ***Mira este video de 13:17 a 20:31***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Erik Amézquita (Michigan State University)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=13, seconds=17).total_seconds())
end=int(timedelta(hours=0, minutes=20, seconds=31).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Ahora que sabemos como tratar con una variable fuera del loop, aprendamos a crear una lista vacía fuera del loop y llenarla con resultados del loop.
# 
# Usemos el mismo loop `for` que hemos usado antes, `range()` de 0 a 12 paso 2, y tenemos un contador como lo teníamos antes con `+= i`.
# Lo que vamos a hacer ahora es crear listas vacías que están fuera de
# el loop. Creemos una llamada `i_values`. Al inicio va a estar vacía. No hay nada en ella, solo los corchetes vacíos como aprendimos antes, y creamos otra llamada `countup_values`. La idea es que usando la función `.append ()`, que aprendimos antes, si agregamos un `.append` a una lista podemos agregar los elementos entre paréntesis a la lista que se especifica. Vamos a agregar `i` a nuestra lista `i_values` con cada iteración del loop y agregamos los valores del contador a la lista
# `countup_values` usando también `.append()`. De nuevo vamos a imprimir `i` y `count_up` solo para asegurarnos de que nuestro loop se ejecuta como esperamos.
# 
# Podemos ver del `print()` que el loop corrió. También podemos ver que nuestro contador funcionó, pero además teníamos estas listas que creamos
# y estos valores debierían de haberse agregado a la lista con cada iteración del loop, así que vamos a asegurarnos de que las listas funcionaron.

# In[2]:


# Puede crear una lista vacía fuera del loop para almacenar variables
# Use la función .append () en el loop para agregar a una lista externa

count_up = 0
i_values = [] # store i values here
countup_values = [] # store count_up values here

for i in range(0,12,2):
    count_up += i
    i_values.append(i) # append to list i_values
    countup_values.append(count_up) # append to list countup_values
    
    print(i, count_up) # always use print to make sure loop worked!


# Si ordenamos imprimir `i_valores`, podemos ver que tenemos una lista que contiene los valores de `i` porque cada vez que se ejecuta el loop se agrega `i` a la lista `i_values`.

# In[3]:


print(i_values)


# Echemos un vistazo a nuestra lista `countup_values`, y es lo mismo: agregamos los valores después de haber usado el índice `i`, hemos agregado el valor revisado y actualizado de `count_up` a la lista `countup_values` y funcionó. 
# 
# Así que esta es una función muy conveniente que puede usar loops para procesar, calcular y crear nuevos valores basados en `i` y luego almacenar los resultados en una lista fuera del loop.

# In[4]:


print(countup_values)


# Hemos estado usando la función `range()` hasta ahora, pero es importante
# saber que podemos usar cualquier lista. Los valores de `i` no necesariamente tienen que estar en secuencia o tener un inicio o final o un paso como la función `range()`. Podemos simplemente crear una lista, y luego decir que para cada valor en la lista, iteraremos sobre los valores en secuencia de dicha lista.
# 
# Recordemos que la variable que usamos para denotar el iterador puede ser cualquier cosa que queramos. Aquí lo llamamos `val`. Estamos diciendo que `val` en la lista `i_values`. Simplemente iteramos a través de la lista como si estuviesemos indexando con ella. Primero vamos a imprimir únicamente. Vemos que la lista de `i_values` fue 0, 2, 4, 6, 8, 10
# y eso es lo que obtenemos e imprimimos.

# In[5]:


# Puede proporcionar la secuencia de números enteros loop `for` usando una lista
# Desde el loop anterior, i_values era 0, 2, 4, 6, 8, 10

for val in i_values:
    print(val) # always use print to make sure loop worked!


# De esa forma podemos construir un loop a partir de una lista de valores y podemos hacer todas las cosas que acabamos de discutir de procesamiento y almacenamiento, y lo que quiero decir por procesamiento es que el iterador `i`, `val`, o como sea que se llame, ya sea que esté iterando sobre un `range()` o sobre una lista, con los valores de `i` o `val` podemos hacer todo tipo de cálculos diferentes.
# 
# Exploremos todas las rutinas matemáticas que podamos pensar. Así por ejemplo, almacenemos nuestros valores nuevamente en una lista. Solo para saber cuáles eran los valores hagamos algunas matemáticas aquí. Vamos a agregar a la lista `multiply_2`, el valor multiplicado por 2. A la lista `exponent_2` fuera del loop, agregaremos el valor a la segunda potencia. Recordemos que la forma en que denotamos potenciación en python es con dos asteriscos. También vamos a crear algunos números realmente grandes. Creemos una lista llamada `exponent_val` y a ésta vamos a agregar `val` a la potencia `val`. Vamos a imprimir `val` cada vez sólo para asegurarnos de que nuestro loop está funcionando.

# In[6]:


# Podemos construir un loop a partir de una lista de valores.

vals = [] # Store loop "val"s here
multiply_2 = [] # Store val*2 here
exponent_2 = [] # Store val**2 here
exponent_val = [] # Store val**val here

for val in i_values:
    vals.append(val) # append to vals
    multiply_2.append(val*2) # append to multiply_2
    exponent_2.append(val**2) # append to exponent_2
    exponent_val.append(val**val) # append to exponent_val
    
    print(val) # always use print to make sure loop worked!


# Recordemos que esta lista `i_values` es 0, 2, 4, 6, 8, 10. Pero ahora tenemos todas estas listas: `multiply_2`, `exponent_2`, `exponent_val`,
# y realmente queremos comprobar que éstas obtuvieron eso, que fueron procesadas correctamente. Para verificar estas listas, debemos imprimirlas. 
# 
# Vamos a agregar algunas habilidades a la función `print()`. Podemos utilizar entre comillas la barra invertida n (`"\n"`) para crear un salto de línea para la función `print()`. Ya sabemos que si separamos con una coma que creará un espacio. Entonces vamos a decir "The values are: ", y luego vamos a poner la lista desde aquí, `vals`, para que podamos ver cuál es la lista de `vals`. Después ponemos una coma y vamos a decir entre comillas barra invertida n (`"\n"`) para así crear un salto de línea para que podamos realmente leer algunos de estos resultados. A continuación, diremos "val\*2 values are: ". Así que estamos multiplicando por 2, ¿verdad? Vamos a tomar la lista `multiply_2` y luego de esta coma, vamos a poner la lista `multiply_2`. Y luego de nuevo un salto de línea, entonces vamos a decir "val\*\*2 values are: " y a poner nuestra lista de segunda potencia. Y luego vamos a decir "val\*\*val values are: " y vamos a poner nuestra lista `exponent_val`. Usando esta barra invertida n (`"\n"`), podemos ver que obtenemos estos saltos de línea que realmente nos ayudan a leer los resultados.

# In[7]:


# Puede utilizar "\ n" como salto de línea para la función print

print("The vals are:", vals, "\n","val*2 values are:", multiply_2, "\n",
      "val**2 values are:", exponent_2, "\n", "val**val values are:", exponent_val)


# Así vemos que los valores son 0, 2, 4, 6, 8, 10. Si multiplicamos esos valores por 2, se verán así. Si los elevamos a la segunda potencia se ven así. Y si los elevamos a la potencia de si mismos, obtienemos algunos realmente enormes en poco tiempo. Lo importante que debemos saber es que, si creamos estas listas vacías y luego usamos la iteración sobre `range()` o sobre una lista de valores, y procesamos matemáticamente y utilizamos el código, podemos utilizar estos iteradores de formas muy creativas para definir muchas funcionalidades en python. En muchos sentidos, los loops están realmente en el corazón de la programación porque estamos automatizando una rutina para procesar muchas cosas rápidamente y crear conjuntos de datos muy grandes.

#!/usr/bin/env python
# coding: utf-8

# # 3.0 La funci贸n range
# 
# # La raz贸n dorada calculada con loops 馃尰 

# ___

# Las plantas exhiben patrones hermosos: desde los patrones de ramificaci贸n de los 谩rboles hasta las formas de las hojas y los patrones en espiral de un girasol. Este 煤ltimo patr贸n, las espirales, surge de la filotaxia (que literalmente significa "hoja" + "arreglo"). La filotaxia es m谩s que el arreglo de las flores de un girasol, es la disposici贸n de todos los 贸rganos laterales (hojas y partes de flores). Hay muchos m谩s patrones adem谩s de la espiral, pero para esta lecci贸n y la siguiente, nos centraremos en la filotaxia en espiral y trataremos de recrear los patrones inspiradores en las cabezas de girasoles.
# 
# 驴Cu谩l es la sucesi贸n de Fibonacci? 驴C贸mo se relaciona con los patrones en espiral que se encuentran en los girasoles y en todas las plantas terrestres? La sucesi贸n de Fibonacci es una serie de n煤meros que comienza con "0, 1" o "1, 1". Despu茅s de los dos primeros n煤meros, el siguiente n煤mero se define como la suma de los dos anteriores. Entonces, de `0, 1` surge la sucesi贸n `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,. . .`. 
# 
# Al observar un girasol, surgen patrones filot谩cticos en espiral que se proyectan en un disco, patrones de brazos en espiral que emanan del centro. Estos se llaman _parastichies_ y surgen de vecinos cercanos en el patr贸n filot谩ctico general que est谩n separados por *n* primordios secuenciales, donde *n* es un t茅rmino de la sucesi贸n de Fibonacci. 
# 
# Por ejemplo, en una familia parastichy de 5, la espiral surge de conectar cada quinto primordio. Una de las conexiones m谩s fuertes entre la filotaxia y la secuencia de Fibonacci es que las familias parastichy que van en direcciones opuestas son n煤meros consecutivos de la sucesi贸n de Fibonacci.
# 
# Pero la conexi贸n entre la sucesi贸n de Fibonacci y la filotaxia en espiral es incluso m谩s fuerte que las familias parastichy. La raz贸n dorada (tambi茅n llamada raz贸n 谩urea) se puede aproximar como la raz贸n de dos n煤meros de Fibbonaci consecutivos. La aproximaci贸n se vuelve m谩s precisa a medida que avanzamos en la sucesi贸n. El valor de la raz贸n dorada es $$\varphi=\frac{1 + \sqrt{5}}{2}\approx1.61.$$
# 
# Si la circunferencia de un c铆rculo se divide en dos arcos, la raz贸n de cuyas longitudes forman la raz贸n dorada, el 谩ngulo resultante se llama el 谩ngulo dorado. El valor del 谩ngulo dorado es 
# 
# $$\pi(3 - \sqrt {5})\;\text{radianes 贸 } 180(3 - \sqrt{5})\approx137.5^\circ.$$ 
# 
# El valor del 谩ngulo entre primordios sucesivos en filotaxia en espiral es el 谩ngulo dorado.
# 
# En esta lecci贸n aproximaremos los valores de la raz贸n dorada y el 谩ngulo dorado usando loops. En la siguiente actividad, usaremos el valor del 谩ngulo dorado para recrear una cabeza de girasol.

# ![parastichy.jpg](../../images/parastichy.jpg)

# ___
# ## 'Looping' hacia la raz贸n dorada

# Las computadoras son realmente buenas para realizar tareas repetitivas. Un loop es una de las principales formas en que le decimos a una computadora que ejecute un fragmento de c贸digo una y otra vez.
# 
# Los loops vienen de dos maneras: 
# - loops `for`
# - loops `while` 
# 
# Un loop `for` iterar谩 sobre un fragmento de c贸digo ***por*** un n煤mero espec铆fico de veces. Un loop `while` seguir谩 iterando sobre un fragmento de c贸digo ***mientras*** una condici贸n sea verdadera.
# 
# No es estrictamente cierto que el loops simplemente repita lo mismo una y otra vez. M谩s bien, est谩 iterando sobre un *铆ndice*. Un 铆ndice es un recuento de cu谩ntas veces se repiti贸 el ciclo, `0, 1, 2, 3,...` (recordemos que toda la indexaci贸n comienza con 0 en python). El 铆ndice es un valor que usamos para variar, con cada iteraci贸n, lo que hace el loop. 
# 
# El 铆ndice podr铆a ser simplemente un recuento que contin煤a sucesivamente +1 con cada iteraci贸n. O bien usamos el 铆ndice para obtener otros valores. Por ejemplo, el 铆ndice de un loop podr铆a usarse para iterar sobre los elementos de una lista, que pueden ser cualquier valor que elijamos. Podr铆amos realizar una funci贸n matem谩tica en cada valor del 铆ndice del loop para transformarlo en otro conjunto de valores que necesitemos.
#  
# Dos formas comunes de iterar sobre un loop son usando la funci贸n `range ()` o simplemente una lista. La funci贸n `range ()` toma un valor de inicio, parada y paso, o simplemente el valor de parada por s铆 mismo. Por ejemplo, `range (2,10,3)` dar铆a como resultado `2,5,8`, comenzando en 2 agregando 3 para cada paso hasta detenerse en un valor ***estrictamente menor*** a 10. Tambi茅n podemos proporcionar simplemente un valor de parada para el rango. Por ejemplo, `range(3)` producir铆a `0,1,2`. Es importante recordar con `range ()` que el inicio es inclusivo y la parada es exclusiva.
# 
# Los loops `for` tienen una estructura estricta, en la que se proporciona un nombre arbitrario para la variable iterable, y un conjunto de valores sobre los que iterar esa variable. La primera l铆nea termina en un `:` y el c贸digo dentro del loop est谩 sangrado. Python es sensible tanto al `:` como a la sangr铆a. Por ejemplo:
# 
# ```python
# for i in range(start, stop, step):
#     # Tu c贸digo aqu铆
#     # Usemos print mientras tanto
#     print(i)
#     
# for val in my_list:
#     # Tu c贸digo aqu铆
#     # Usemos print mientras tanto
#     print(val)
# ```
# 
# A diferencia de un loop `for`, un loop `while` seguir谩 iterando ***mientras*** una condici贸n sea verdadera y dejar谩 de iterar cuando dicha condici贸n ya no lo sea. Una forma com煤n de estructurar un loop `while` es agregar un contador. Un contador es una variable fuera del ciclo que aumentar谩 su valor cada vez que se ejecute el ciclo. 
# 
# Configuramos un loop `while` para que se ejecute hasta que el contador supere un cierto valor. El valor del contador aumenta con el signo `+=`, que es equivalente a `counter = counter + 1` en el ejemplo que se muestra a continuaci贸n. Una forma de pensar en `+=` es que agrega un valor al valor anterior del contador para llegar a un nuevo valor de contador.
# 
# A continuaci贸n se muestra un ejemplo de un loop `while` con un contador:
# 
# ```python
# counter = 0
# 
# while counter < 20:
#     # Tu c贸digo aqu铆
#     # Usemos print mientras tanto
#     print(counter)
#     # Incrementemos el counter cada vez que el loop itera
#     counter += 1
# ```
# 
# Vale la pena invertir algo de tiempo en comprender los loops 隆son un elemento clave de la codificaci贸n en python! Los loops se vuelven muy poderosos cuando se usan inteligentemente con el c贸digo dentro de ellos, y tambi茅n al crear valores y listas fuera de los loops que los loops modifican a medida que se ejecutan.
# 
# Prestemos atenci贸n a la forma en que se usan los loops en el tutorial a continuaci贸n, y c贸mo se pueden usar para calcular algo como la sucesi贸n de Fibonacci.

# ## 馃悕 Objetivos de aprendizaje de python
# 
# - La funci贸n `range ()` y c贸mo 茅sta produce una sucesi贸n de enteros para iterar en un loop (*1:20*)
# - C贸mo escribir un loop `for` (*2:40*)
# - C贸mo utilizar el signo `+=` en un contador (*7:25*)
# - C贸mo crear una lista vac铆a fuera de un loop y llenarla con resultados del loop (*13:09*)
# - C贸mo utilizar un loop `for` para calcular la suceci贸n de Fibonacci (*20:33*)
# - C贸mo escribir un loop `while` usando un contador (*26:29*)

# ## 馃尰 Objetivos de aprendizaje de plantas
# 
# - 隆Las plantas son computadoras!
# - 脡stas producen resultados de forma iterativa (como hojas y flores), al igual que lo hacen los loops.
# - El modelado computacional intenta replicar fen贸menos de la naturaleza. Ning煤n modelo es perfecto.
# - El 谩ngulo dorado que usan las plantas y que calcularemos se basa en matem谩ticas computacionales.
# - Usaremos los girasoles y el 谩ngulo dorado como inspiraci贸n para aprender de las plantas.

# ## La funci贸n `range()` y c贸mo 茅sta produce una sucesi贸n de enteros para iterar en un loop

# ***Mira este video de 0:00 a 2:35***
# 
# Para espa帽ol, haga click en configuraci贸n, seleccione "espa帽ol" debajo de los subt铆tulos.
# 
# Traducci贸n por Erik Am茅zquita (Michigan State University)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=2, seconds=35).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripci贸n del video.***

# Empecemos entonces. Empezaremos con la funci贸n `range()` y c贸mo se usa para producir una sucesi贸n de enteros sobre los que iteramos en un loop.
# 
# Este es un buen momento para repasar la funci贸n de ayuda. Si tenemos algunas dudas sobre qu茅 hace cierta funci贸n, podemos simplemente escribir el signo `?` delante de ella. Si presionamos `Shift` + `Enter`, obtenemos un peque帽o cuadro de ayuda. Puede no ser tan 煤til, pero intentar谩 decirte algo. Por ejemplo, podemos ver que las entradas a la funci贸n `range()` son inicio, parada y paso. Esto es muy parecido a indexaci贸n y segmentaci贸n que hemos aprendido antes y dice que devuelve un objeto que produce una secuencia de enteros desde el inicio, inclusivo, hasta el final, exclusivo, con tama帽o de paso. Y esto casi suena exactamente como la indexaci贸n y el corte que aprendimos antes.

# In[2]:


# 驴Qu茅 es la funci贸n range ()?
# Si tiene alguna duda, utilice la funci贸n de ayuda con un "?"

get_ipython().run_line_magic('pinfo', 'range')

# range(start, stop[, step]) -> range object
# Return an object that produces a sequence of integers
# from start (inclusive) to stop (exclusive) by step.  
# range(i, j) produces i, i+1, i+2, ..., j-1
# start defaults to 0, and stop is omitted! 
# range(4) produces 0, 1, 2, 3
# These are exactly the valid indices for a list of 4 elements
# When step is given, it specifies the increment (or decrement)


# Basado en ello intentemos ejecutar una funci贸n `range()`. Pongamos el n煤mero 8. Quiz谩s basado en nuestra indexaci贸n anterior esperar铆amos que nos devolviese 0, 1, 2, 3, 4, 5, 6, 7. Pero ese no es el caso. En cambio, solo nos da un rango de 0 a 8, que es algo de que esperar铆amos bas谩ndonos en poner 8 all铆. Y bueno, esto es un poco inesperado.
# 
# As铆 que exploremos m谩s, y como veremos, `range()` solo funciona realmente en el contexto de un loop.

# In[3]:


# 隆As铆 que probemos la funci贸n de rango!

print(range(8))


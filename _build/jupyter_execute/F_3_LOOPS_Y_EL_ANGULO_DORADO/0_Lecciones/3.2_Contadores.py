#!/usr/bin/env python
# coding: utf-8

# # 3.2 Contadores

# ## Cómo utilizar el signo `+=` en un contador
# ____

# ***Mira este video de 7:20 a 13:17***
# 
# Para español, haga click en configuración, seleccione "español" debajo de los subtítulos.
# 
# Traducción por Erik Amézquita (Michigan State University)

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=7, seconds=20).total_seconds())
end=int(timedelta(hours=0, minutes=13, seconds=17).total_seconds())

YouTubeVideo("Cvi3dByz9SE",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# Veamos más trucos que podemos usar con loops `for`, incluido un signo `+=` como contador. 
# 
# Podemos poner una variable o, como veremos muy pronto, incluso una lista, fuera de un loop. Luego podemos ejecutar nuestro loop y podemos modificar la variable fuera del loop. De ese modo, la variable se actualizará continuamente a medida que se modifica en cada iteración del loop. Algo muy habitual es crear un contador. Por ejemplo, si creamos una variable,
# llamémosle `count_up`, y la inicializamos en 0, si ejecutamos nuestro loop, podríamos, por ejemplo agregar `i` al contador `count_up` cada
# vez que se itere el loop, de modo que cada vez que se ejecuta el loop,
# agregaremos `i` al contador. De ese modo el valor de `count_up` va a cambiar. Aunque inicialmente su valor es 0, observemos que lo declaramos
# con valor 0 fuera del loop, y cuando ejecutemos nuestro loop, el contador se modificará y básicamente estará ignorando cuál era ese valor inicial para que podamos modificar constantemente el valor del contador a medida que se ejecuta el loop.
# 
# Esto es un poco engañoso con respecto a las matemáticas porque esto no es matemáticas, esta es una afirmación matemáticamente falsa, pero es importante saber cómo funciona. Por ejemplo, aquí tenemos una función `range()` que comienza en 0 y va a 12 y pasos de 2 en 2. La secuencia irá entonces 0, 2, 4, 6, 8. El contador `count_up` se establece inicialmente
# en 0 y, por lo tanto, la primera vez que el loop corre será 0. Asi mismo, `i` será 0, por lo que `count_up` se establecerá nuevamente en 0. En la segunda iteración, `count_up` sigue siendo 0, pero ahora `i` es 2: así que `count_up` sigue siendo 0, pero ahora `i` es 2, por lo que `count_up` se convierte en 2. Si ejecutamos el loop de nuevo, entonces `i` será 4. Ahora `count_up` es 2 y vamos a agregarle 4, por lo que ahora `count_up`
# será 6. Básicamente esto es como decir "tomaremos el valor del contador previo a cualquier modificación con `i`, y luego restableceremos el contador al nuevo valor añadiéndole `i`. En este loop `for` pondremos
# una línea en la que imprimimos tanto `i` como `count_up`, para que podamos rastrear lo que está haciendo el loop. 
# 
# Así podemos ver que para el `range` de 0 a 12, con pasos de 2, va 0, 2, 4, 6, 8, 10, como era de esperar. Estos son los valores de `i`. Por otro lado, `count_up` es inicialmente 0, luego agregamos 0 a 0 y todavía estamos en 0, pero luego en la siguiente iteración `i` se establece como 2. Como `count_up` es 0, al agregarle 2, el contador es 2 ahora. En la siguiente iteración, el contador está en 2, pero ahora `i` es 4 y entonces el contador se convierte en 6. En la siguiente iteración, el valor de `i` se convierte en 6, lo sumamos al contador de 6 y obtenemos 12. Y así sucesivamente. Entonces podemos ver que `i` es agregado al valor anterior de `count_up`, pero luego el contador se actualiza cada vez que ejecutamos el loop. 

# In[2]:


# Podemos crear una variable fuera del loop y hacer que el loop la modifique
# La variable puede comenzar en 0 y "contar" cada iteración del loop

count_up = 0

for i in range(0, 12, 2):
    
    count_up = count_up + i
    
    print(i, count_up) # always use print to make sure loop worked!


# Esta notación es muy útil, ya que podemos ver que hemos creamos un contador. De cierto modo éste registra cuántas veces se ha ejecutado nuestro loop lo cual es muy conveniente. Puesto que es tan conveniente, tenemos que pensar en la notación. Como vemos aquí, sabemos que esta notación no es la mejor en el sentido matemático, pues técnicamente no son iguales. Por ello, la gente creó un nuevo signo matemático, y se
# llama signo más igual (`+=`). Así que básicamente esta instrucción de que `count_up` más `i` será el nuevo valor de `count_up` es equivalente a
# más igual. Podemos decir simplemente `count_up` "más igual" `i`. Básicamente vamos a agregar `i` al valor que `count_up` tenga en ese momento y luego actualizaremos el valor de `count_up`. Esa es la única diferencia entre estos dos loops y si ejecutamos este segundo loop, podemos ver que los resultados son los mismas. Así que `+=` es una forma de actualizar el valor actual del contador y revisarlo cada vez que se ejecuta el loop.

# In[3]:


# El signo + = es lo mismo que agregar "i" al contador

count_up = 0

for i in range(0, 12, 2):
    count_up +=  i
    print(i, count_up) # always use print to make sure loop worked!


# El `+=` a es la versión más utilizada de esta notación, pero podemos usar todas las demás operaciones aritméticas. Por ejemplo, podemos usar menos igual `-=` en su lugar. Si usamos `-=`, podemos ver que el índice `i` se resta del contador `count_up` con cada iteración. 

# In[4]:


# También puede usar un signo - =

count_up = 0

for i in range(0, 12, 2):
    count_up -=  i
    print(i, count_up) # always use print to make sure loop worked!


# Podemos multiplicar de igual manera, pero puedes ver que no es algo muy útil al empezar con 0. Si empiezas con el contador en 0, ocurre que cualquier `i` por él se vuelve 0. Así que no vemos mucha actividad en él.

# In[5]:


# O puede usar un signo * =
# Pero no es útil a comenzar de 0

count_up = 0

for i in range(0, 12, 2):
    count_up *=  i
    print(i, count_up) # always use print to make sure loop worked!


# Pero, si por ejemplo, inicializamos el contador igual a 1, entonces podemos ver cómo cada vez se multiplica por `i` y se actualiza.

# In[6]:


# Aquí está el signo * = que comienza en 1

count_up = 1 # change to 1 to get results with *=

for i in range(1, 12, 2):
    count_up *=  i
    print(i, count_up) # always use print to make sure loop worked!


# También podemos hacer una división igual `/=` y como podemos imaginar, dividiendo por `i` con cada iteración, obtenemos un valor que disminuye rápidamente y que se vuelve infinitamente pequeño.

# In[7]:


# O puede usar un signo / =

count_up = 1 

for i in range(1, 12, 2):
    count_up /=  i
    print(i, count_up) # always use print to make sure loop worked!


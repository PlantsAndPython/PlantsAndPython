#!/usr/bin/env python
# coding: utf-8

# # Activity 3: Cómo construir un girasol 🌻 

# ___

# En esta actividad, aprenderemos a codificar el intrincado y hermoso conjunto de floretes en una cabeza de girasol, exploraremos la como la disposición de los floretes tiende al ángulo dorado y crearemos animaciones de un girasol en crecimiento.
# 
# Como tarea previa a esta actividad, debemos leer el ["Capítulo 4 - Phyllotaxis"](http://algorithmicbotany.org/papers/abop/abop-ch4.pdf) de [*The Algorithmic Beauty of Plants*](http://algorithmicbotany.org/papers/#abop). La inspiración y la teoría detrás de la codificación que harás hoy viene de ahí. 
# 
# Las fórmulas también provienen del capítulo, pero éstas a su vez derivan del trabajo clásico de Vogel, "A better way to construct the sunflower head". Ambos trabajos forman la base de la actividad de hoy. Echa un vistazo al texto si tienes la oportunidad (no es estrictamente necesario) para familiarizarte con algunas de las matemáticas que usaremos en la actividad de hoy.
# 
# > **Referencias:**
# >
# > P. Prusinkiewicz and A. Lindenmayer. [The algorithmic beauty of plants](http://algorithmicbotany.org/papers/#abop). Springer-Verlag, Berlin, Heidelberg, 1990. ISBN:0-387-97297-8
# >
# > H. Vogel. [A better way to construct the sunflower head](https://doi.org/10.1016/0025-5564(79)90080-4). *Mathematical Biosciences*, 44:179–189, 1979.

# ___
# ## La fórmula de un girasol
# 
# Del capítulo de *The Algorithmic Beauty of Plants* que leímos, aprendimos que Vogel propuso las siguientes fórmulas para calcular el ángulo y el radio de cada flor en la cabeza de un girasol:
# 
# ```python
# theta = n * phi
# r = sqrt(n)
# ```
# 
# Donde `n` es el número ordenado de cada florete en una cabeza de girasol, `theta` es el ángulo de la flor, `phi` es el ángulo dorado y `r` es el radio, la distancia entre la flor y el centro del girasol. Debemos pensar que cada florete secuencial tiene un "giro" de `phi` y que tiene un radio más largo que el anterior, siguiendo una función de raíz cuadrada.
# 
# También recuerdemos de nuevo de trigonometría que en un triángulo rectángulo, `cos` y` sin` son los lados adyacentes y opuestos divididos por la hipotenusa respectivamente. En el contexto de un plano cartesiano radial centrado en (0,0), para recuperar las coordenadas `x` e` y` usamos las siguientes ecuaciones:
# 
# ```python
# x = r * cos(theta)
# y = r * sin(theta)
# ```
# 
# Finalmente, trabajaremos en radianes, no en grados. Recordemos también de la trigonometría que para convertir grados en radianes, multiplicamos grados por $\displaystyle\frac{\pi}{180}$.

# ___
# ## ¡Construye un girasol!
# 
# Usando las ecuaciones anteriores, ¡construye un girasol!
# 
# Pero primero, dado que usaremos mucho el ángulo dorado, hagamos que sea una variable. En la celda de abajo, se proporciona el ángulo dorado en grados. Crea una nueva variable llamada `phi` que sea el ángulo dorado en radianes.
# 
# Sería conveniente tener $\pi$. La celda de abajo importa el módulo `math`, ¡que probablemente necesitaremos a menudo! Para recuperar el valor de $\pi$, simplemente escribe `math.pi`. También necesitaremos `math` para las funciones `math.sqrt()`, `math.cos()` y `math.sin()` en esta lección.

# In[1]:


import math  

# From the online encyclopedia of integer sequences: 
# https://oeis.org/A096627

golden_angle = 137.5077640500378546463487396283702776206886952699253696312384958261062333851951

# Calcula el ángulo dorado en radianes
# Llama a la variable phi


# A continuación, escribe un loop `for` para calcular las coordenadas  `x` e `y` de cada flor.
# 
# **Haz lo siguiente:**
# 
# * Crea dos listas para las coordenadas fuera del ciclo: una lista para los valores `x` y una lista para los valores` y`
# * El ciclo `for` debe iterarse 1000 veces, calculando los valores de las coordenadas` x` e `y` para 1000 floretes
# * Dentro del loop, para cada florete, calcula:
#    * Radio
#    * Theta
#    * valor de la coordenada x
#    * valor de la coordenada y
# * Agrega los valores de las coordenadas `x` e` y` a sus respectivas listas

# In[2]:


# Escribe tu respuesta aquí



# Luego, grafica los resultados con `matplotlib.`
# 
# * Presta atención al tamaño de los puntos, que no se superpongan demasiado pero que tampoco sean demasiado pequeños.
# * Elige un color apropiado.
# * Ajusta la transparencia de forma adecuada.
# * Considera igualar la escala de los ejes x e y
# * Remueve los ejes
# * Siempre cuida la estética, ***especialmente*** al trazar girasoles.

# In[3]:


# Siempre se debe importar matplotlib
# y usar la opcion inline

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Realiza tu gráfico aquí


# ___
# ## ¡La importancia del ángulo!

# Del capítulo de *The Algorithmic Beauty of Plants* sabemos que la acumulación de floretes en un girasol es extremadamente sensible al valor exacto del ángulo dorado. Un poco más o un poco menos y la disposición bellamente espaciada a simple vista se destruye. Esto se debe a las propiedades matemáticas especiales del ángulo dorado.
# 
# En este ejercicio, tomaremos las flores de girasol que acabamos de crear usando su loop `for` y crearemos una animación, donde el valor del ángulo dorado se desvía $\pm1$ grados en 100 pasos. Usando esta animación, observaremos la sensibilidad del empaque de floretes en un girasol al ángulo dorado, y cómo esta sensibilidad varía más cerca y más lejos del centro.
# 
# ¡Nuestra estrategia será crear un loop dentro del loop! La lógica es la siguiente: ya hemos creado un bucle que calculará todas las coordenadas `x` e` y` en un girasol. ¡Pon ese loop en otro loop! El loop exterior iterará sobre las desviaciones del ángulo dorado. Entonces, el flujo se verá así:
# 
# 1. El loop exterior crea un nuevo valor de ángulo,
# 2. El loop interno calcula todos los valores de las coordenadas `x` e` y` para el nuevo valor del ángulo,
# 3. Salimos del loop interior, y estamos de vuelta en el loop exterior,
# 4. El código anterior para trazar un girasol traza los floretes para el ángulo actual,
# 5. ¡El loop exterior se repite con un nuevo valor de ángulo y forma un nuevo cuadro de la animación!
# 
# Solo una cosa más. 
# 
# Estaremos iterando en 100 pasos desde -1 a +1 grados del ángulo dorado. ¿Cómo se especifica un número determinado de pasos entre dos valores? Una función para hacer esto es `linspace()`, del módulo `numpy`. `linspace()` toma un valor de inicio (inclusivo), un valor de parada (inclusivo) y un número de pasos para iterar incrementalmente sobre el intervalo. ¡Usemos esto en el loop exterior para ajustar minuciosamente el valor del ángulo $\pm1$ grados del ángulo dorado!
# 
# En la celda a continuación, se proporciona un pseudocódigo para guiar la construcción del loop dentro del loop. Recuerda usar el código anterior (con algunas modificaciones) para calcular los valores de las coordenadas `x` e` y` y para trazar el girasol.
# 
# Este ejercicio está destinado a que dediques tiempo a pensar en cómo funcionan los loops complejos y en cómo modificar y ajustar el código para diferentes propósitos. 
# 
# Si tienes éxito, ¡crearás una hermosa animación de girasol!
# 
# ¡Sigue el pseudocódigo y completa las partes que faltan!

# In[4]:


# Importes para la animación
from IPython.display import display, clear_output 
import time  

# Importa numpy para usar linspace
import numpy as np

# Para la animación, necesitamos un lienzo
fig = plt.figure(figsize=(10,10)) 

# Usamos linspace() para cream incrementos de -1 a +1
for i in np.linspace(-1, 1, 100):
    
    # Crea una nueva variable "new_angle"
    # "new_angle" será golden_angle + i
    # Recuerda que el nuevo ángulo debe ser en radianes!
    
    
    
    # Aquí podemos reciclar nuestro loop anterior para
    # calcular las coordenadas x e y
    # theta debe ser calculado con nuestro ángulo nuevo
    # Recuerda que python toma en cuenta la sangría
    # Doble sangría indicará un loop dentro de un loop
    # Mantén las listas de coordenadas x e y fuera del loop interno
    # pero dentro del loop externo
    # Como antes, calcularemos la posición de 1000 floretes
    
    # Recicla tu loop anterior
    
    
    
    
    
    
    
    
    # Hemos concluido el loop interno
    # Es hora de movernos al loop externo
    
    
    # Usa tu código para graficar el girasol
    
    

    # Este código crea la animación
    time.sleep(0.1) 
    clear_output(wait=True)
    display(fig)
    fig.clear()


# ___
# ## ¡Pero los girasoles crecen!
# 
# Todavía no hemos terminado. ¡En el mundo real los girasoles también crecen! Los floretes surgen de un meristemo (una población de células madre) en el centro del girasol. En la periferia del meristemo apical del brote en el centro del girasol, se determina que las células se convertirán en una flor. Llamamos "pluripotencia" a la capacidad de las células, como los meristemos, para producir diferentes tipos de tejidos. Decimos que las células están "determinadas" o "predestinadas" a convertirse en un tipo particular de tejido a medida que pierden pluripotencia. Las células "diferenciadas" ya se han convertido en un tejido particular. Después de que una flor se ha diferenciado, se aleja del centro del girasol.
# 
# En las gráficas anteriores, los floretes de la periferia fueron los primeros en surgir y fueron "empujados" desde el centro por todos los demás floretes que surgieron posteriormente. ¡Creemos una animación en la que veamos florecer floretes en el centro y moverse hacia afuera!
# 
# Vas a:
# 
# 1. Crear listas `thetas` y` radii` como antes. Simplemente usaremos el código previo para calcular las thetas y los radios.
# 
# 1. Una vez que nace, una flor ***siempre*** mantiene la misma theta. Pero el radio se hace cada vez más amplio.
# 
# 1. Nuestro primer loop creará listas de theta y radios que aumentan de longitud con cada iteración. Comenzaremos con un florete, luego dos, y así sucesivamente, y con cada florete adicional, los radios de los primeros floretes serán cada vez más amplios. Comenzaremos sin floretes y cultivaremos nuestro girasol, agregando más y más. Este loop toma un miembro más de las listas `thetas` y `radii` con cada iteración.
# 
# 1. Sin embargo, hay un problema. Cada vez que agregamos más elementos a nuestras listas, los "thethas" y "radios" más antiguos (asociados a flores únicos) se hallan **al inicio** de las listas `thetas` y `radii`. ¡Los "radios" más antiguos son los radios más cortos, pero los "thetas" más antiguos deben corresponder a radios amplios!
# 
# 1. Usaremos la función `.reverse ()`, que invierte el orden de los elementos de una lista. Lo que esto hará es asegurar que los "thetas" más antiguos de la lista `thetas` correspondan a los radios más amplios de la lista `radii`.
# 
# 1. Recapitulando: agregamos una flor más con cada iteración. Pero el primer florete siempre tendría el radio más corto, a menos que invirtiéramos la lista de radios. Al invertir la lista de radios, el primer florete tendrá un radio creciente.
# 
# Sigue el razonamiento anterior y asegúrese de comprenderlo. En las celdas siguientes se proporciona un pseudocódigo con comentarios. Usando este esqueleto, completa el resto del código. El código consta de dos partes:
# 
# 1. Primero, usando un loop `for`, crea dos listas: `thetas` y `radii`. Estas listas deben contener **750** valores theta y radio para floretes.
# 
# 2. Con el pseudocódigo proporcionado, crea una animación de un girasol en crecimiento.

# In[5]:


# Crea las listas vacías thetas y radii
# Con un loop, llena las listas con los valores correspondietes a 750 floretes
# Puedes usar código previo

# Escribe tu respuesta



# In[6]:


# Completa el código siguiente para crear una animación de cómo crecen los floretes en un girasol
# Presta atención a ambos loops y cual es el propósito de cada uno
# Presta atención a los índices de cada lista
# Observa como se usa la función .reverse()
# Observa como el código crea una animación cuadro por cuadro del crecimiento de un girasol

# Escribe tu respuesta

# Importes para animar el resultado
from IPython.display import display, clear_output
import time  

# Para la animación, debemos de establecer un canvas/figure
fig = plt.figure()

for i in range(len(radii)):

    xlist = []
    ylist = []
    
    # Aquí seleccionamos los thetas del momento
    current_thetas = thetPs[0:(i+1)]
    
    # Aquí seleccionamos los radios correspondientes a los thetas anteriores
    # Cada vez que iteramos el loop, esta lista va de menor a mayor
    
    current_radii = radii[0:(i+1)]
    # Por ello, debemos de revertir el orden
    # De ese modo, los valores ahora van de mayor a menor
    # Los floretes con los primeros thetas deben de corresponder a los radios más amplios
    
    current_radii.reverse()

    for n in range (i+1): 
        
        # Para cada florete n, calcula r y theta, coordenadas x e y
        # añade las coordenadas a listas respectivas

        
        
        
        
        
        
        
    # Hemos salido del loop interno
    # Estamos de vuelta en el loop externo
    

    
    # Usa el código previo para graficar el girasol
    
    
    
    # Con estas líneas creamos una animación
    time.sleep(0.001) 
    clear_output(wait=True)
    display(fig)
    fig.clear()

# Closes the figure animation once complete
# plt.close()


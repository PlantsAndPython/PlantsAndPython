#!/usr/bin/env python
# coding: utf-8

# ## Instalar Anaconda y usar Jupyter notebooks
# Traducción por Dra. Alejandra Rougon (UNAM ENES León, México)  
# _____

# ***Mira este video de 0:00 a 3:33***

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

# Para español, haga click en configuración,
# seleccione "español" debajo de los subtítulos.
# Traducción por Dra. Alejandra Rougon (UNAM ENES León, México)

from IPython.display import YouTubeVideo
from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=0).total_seconds())
end=int(timedelta(hours=0, minutes=3, seconds=33).total_seconds())

YouTubeVideo("FrDYpLVuTkQ",start=start,end=end,width=640,height=360)


# ***La siguiente es una transcripción del video.***

# En este tutorial aprenderemos a descargar Anaconda y empezaremos a usar los Jupyter notebooks. El primer paso, por supuesto, es descargar e instalar Anaconda. Con Anaconda vendrán Python, Jupyter y varios módulos de Python que son necesarios para que hagamos los análisis.
# 
# **Ve a [https://docs.anaconda.com/anaconda/install](https://docs.anaconda.com/anaconda/install)**
# 
# Este enlace puede cambiar con el tiempo, pero si puedes encontrar Anaconda y dónde descargarlo e instalarlo, siempre debería haber instrucciones. Una vez en la página de instalación, haz clic en el enlace específico para tu sistema operativo. Por ejemplo, si estás utilizando Windows, haz clic en "Instalar en Windows" y habrá instrucciones detalladas para descargarlo e instalarlo. Lo mismo para macOS y para Linux.
# 
# Una vez que hayas seguido las instrucciones, y hayas descargado e instalado Anaconda, debes poder cargar Jupyter. Para cargar Jupyter en macOS o linux hay una aplicación llamada terminal que te lleva a la terminal. En Windows, debes ir a la consola de comandos. Una vez que estés en la línea de comandos simplemente escribe "jupyter" y recuerde que lleva una "y" no una "i". Es jupyter con una "y", espacio, "notebook": "jupyter notebook". Y presiona enter. Jupyter debería cargarse. 

# ![terminal.png](attachment:terminal.png)

# Se cargará en el navegador. Por ejemplo, yo estoy usando Chrome. Jupyter no utiliza Internet. Corre localmente en tu propia computadora y solo usa el navegador para mostrar la interfaz.
# 
# La interfaz de Jupyter te muestra tu directorio de inicio o cualquier directorio que hayas elegido para que se muestre. Una vez que estés aquí en la interfaz de Jupyter, puedes ir a la esquina derecha bajo nuevo y crea un nuevo 'notebook'. 

# ![interface.png](attachment:interface.png)

# Puedes hacer clic en el título en la parte superior y darle un nombre. Puede ser, por ejemplo, "my_jupyter_notebook" y también puedes cambiarle el nombre.

# ![name_file_1.png](attachment:name_file_1.png)

# ![name_file_2.png](attachment:name_file_2.png)

# Los Jupyter notebooks contienen celdas. Las celdas son todo lo que es un Jupyter notebook, por lo que es importante poder crearlos y eliminarlos. Algunos atajos realmente convenientes son "a", "b" y "x". "a" y "b" crearán una nueva celda arriba o abajo. Entonces, si haces clic en el lado izquierdo de la celda cerca de la barra azul y presionas "a" crearás una celda arriba. Si presiona "b", crearás una nueva celda abajo. Es fácil crear tantas celdas como desees. "x" es una forma conveniente de eliminaruna celda.

# ![new_cell_4.jpg](attachment:new_cell_4.jpg)

# Hay dos tipos principales de celdas en Jupyter. Hay celdas de código y 
# celdas de 'markdown'. Por defecto, las celdas que aparecen son las de código. Y puedes cambiarlas aquí en este menú desplegable. Esta es una celda de código, pero podemos cámbiarla a una celda de markdown. Observa que cuando creamos una celda de markdown, el pequeño mensaje de la izquierda desaparece. También puede usar atajos para convertir entre celdas de código y markdown. Usas "m" para cambiarlo a markdown y 
# presionas "y" para cambiarlo de nuevo a código.

# ![cell_type_3.jpg](attachment:cell_type_3.jpg)

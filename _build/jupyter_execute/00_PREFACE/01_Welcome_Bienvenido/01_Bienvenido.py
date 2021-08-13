#!/usr/bin/env python
# coding: utf-8

# # Bienvenid@ a Plants & Python
# *una serie de lecciones de programación, biología vegetal, cómputo, y bioinformática*
# 
# ***Traducción por Dr. Alejandra Rougon (UNAM ENES León, México)***
# ____

# In[1]:


# Para reproducir el siguiente tutorial, presiona shift + enter

# Para español, haga click en configuración,
# seleccione "español" debajo de los subtítulos.
# Traducción por Dr. Alejandra Rougon (UNAM ENES León, México)

from IPython.display import YouTubeVideo

YouTubeVideo("wXAf_XSNeZ4",width=640,height=360)


# ***La siguiente es una transcripción del video.***

# ______
# ## Motivación y razonamiento
# 
# **En estas lecciones se asume que no tienes experiencia previa en biología vegetal o programación.** Es imposible enseñar la amplitud de la biología vegetal y la ciencia de datos en unas pocas lecciones. Más bien, estas lecciones seleccionan ejemplos en los que los enfoques matemáticos y de modelización se intercalan con la biología de las plantas.
# 
# La programación en biología vegetal puede resultar intimidante para quienes no tienen experiencia previa. Estos materiales están diseñados para hacer que estas disciplinas no se sientan pesadas. **Una diversidad de perspectivas es vital para combatir los mayores desafíos denuestro tiempo y no hay lugar para guardarse ideas o avergonzarse. Tus contribuciones a la comunidad de ciencias computacionales en plantas son necesarias y valiosas.** 
# 
# Estos materiales solo tienen la intención de ser una introducción para que **desarrolles ***tus*** habilidades** para **lograr el impacto que buscas.** No hay respuestas incorrectas: usa estos materiales de la manera que te sean útiles para promover tu educación y tu carrera. Comparte estos materiales con otros con el mismo espíritu y difunde tu conocimiento. 
# 
# Sobre todo, ***disfruta*** de la forma en que las matemáticas y el modelado pueden revelar la belleza subyacente de las plantas. 
# 
# ______
# ## Las plantas nos inspiran
# 
# Los conceptos matemáticos y computacionales en estas lecciones están inspirados en plantas.
# 
# **Las plantas son las computadoras originales:** ***iterativamente*** producen órganos como hojas y flores con formas complejas dispuestas con precisión en patrones exquisitos.
# 
# **Las plantas son los matemáticos originales:** ***calculan*** números como la proporción áurea, intrínseca a cómo crecen y se desarrollan.
# 
# La morfología de las plantas está codificada por el ADN a nivel genómico y las hermosas formas que producen las plantas son el resultado de 
# complejos patrones de expresión de genes espacio-temporales. Las plantas han desarrollado una diversidad inimaginable durante millones de años que la humanidad ha utilizado para alimentarse, vestirse, abrigarse y medicarse. Además, las plantas mantienen la biodiversidad de la tierra, contribuyendo a los ecosistemas prósperos. Las plantas responden a su entorno, ambos evolucionando a lo largo de cientos de millones de años 
# y respondiendo a la actual crisis climática a lo largo de solo décadas.
# 
# _______
# ## Conceptos básicos de programación y bioinformática
# 
# La primera mitad de este curso cubre Python y los conceptos básicos de programación. Aprenderá sobre variables, funciones, listas e indexación. Cómo visualizar sus datos usando matplotlib. Cómo calcular el ángulo dorado con bucles (loops), modelar el crecimiento de un girasol, y cómo analizar datos usando pandas. Algunos de los ejemplos de estas lecciones incluyen el graficado de las formas de diferentes especies de vid, el
# modelado del crecimiento de los girasoles y la búsqueda de patrones en su forma. También, veremos las fechas de cosecha de las vides en Europa durante siglos y analizaremos cómo un planeta en calentamiento ha adelantado sus fechas de cosecha.
# 
# En la segunda mitad del curso, estarás aprendiendo sobre computo en bioinformática. Aprenderás a utilizar la línea de comandos; cómo acceder a recursos informáticos de alto rendimiento y cómo almacenar, editar, manipular y usar secuencias biológicas como el ADN. También aprenderás
# cómo ensamblar genomas, hacer análisis de genómica comparativa, y deexpresión génica de lecturas cortas. 
# 
# ______
# ## Python y Jupyter
# 
# La estructura de estas lecciones están, por supuesto, basadas en Python. Python esun lenguaje de codificación versátil. Es muy bueno para modelado y para cómputo. También contiene Biopython, que contiene herramientas para genómica y bioinformática las cuales aprenderás a usar. El 
# otro lenguaje de codificación que se usa a menudo en biología es R. R es mejor para necesidades especializadas como estadísticas, mientras que Python es mucho más diverso. Aunque las lecciones de programación que aprenderás en estecurso se pueden transferir a R. 
# 
# Nuestras lecciones tendrán lugar en un entorno llamado Jupyter. En los cuadernos de Jupyter (Jupyter notebook) se facilita el aprendizaje de programación. También permite la investigación, reproducibilidad y el compartir código. Dentro de los cuadernos encontrarás los videos tutoriales, como este, que están destinados a permitirte repasar los conceptos a su propio ritmo. Y, por favor, siéntete libre de detener y regresar el video y repasar el material según sea necesario.
# 
# Este curso reúne a biólogos de plantas que pueden no saber programar y a científicos de datos que tal vez no conozcan la biología o la biología de las plantas. Si estás familiarizado con los temas presentados siempre ve más allá, con mayor profundidad. Busca en lasíntesis entre la biología vegetal y la ciencia de datos. ¿Cuál es la biología subyacente del 
# problema no resuelto? ¿Qué conceptos matemáticos quedan por ser explorados? ¿Cuál es el gran desafío? Siempre puedes llevar este material al siguiente nivel, si ya dominas lo que se está presentando. Investiga más y amplía los límites del conocimiento. De nuevo, sobre todo encuentra alegría en la forma en que las matemáticas y el modelado revelan la belleza subyacente de las plantas.
# 
# ***¡Gracias y los mejores deseos en tu viaje de aprendizaje e investigación!***

#!/usr/bin/env python
# coding: utf-8

# # Cómo usar este Jupyter Book
# ***Traducción por Juan Manuel Gómez Parra (East Lansing, Michigan, USA)***
# _____________
# Los materiales didácticos de *Plants&Python* están contenidos en su totalidad en este sitio web. El sitio funciona con [Jupyter Book](https://jupyterbook.org/intro.html), un proyecto de código abierto diseñado para mostrar, formatear y hacer interactivas las colecciones de [Jupyter notebooks](https://jupyter.org/). Todo lo que se necesita para utilizar estos materiales de aprendizaje es 1) acceso a Internet y 2) un ordenador personal para ejecutar Jupyter localmente.
# 
# A la izquierda encontrará un índice que organiza los cuadernos y que puede utilizar para navegar por el sitio web. Haz clic en cualquier título o subtítulo para acceder al cuaderno asociado. Por ejemplo, antes de este cuaderno en el prefacio hay cuadernos **Welcome : Bienvenid@** que explican la motivación del curso y la filosofía del mismo, así como una colección de cuadernos titulada **Getting Started : Empezando**, que explican cómo descargar Anaconda, cargar y ejecutar cuadernos Jupyter localmente en tu ordenador, y cómo escribir tu primer código Python en Jupyter utilizando celdas de codificación y markdown. Estos cuadernos tienen vídeos de youtube incrustados, así como texto y código que transcriben el contenido de los vídeos. Estas transcripciones están pensadas para mejorar la experiencia del video tutorial y ver el código escrito en un cuaderno Jupyter mientras lo ves y lo sigues. Para aquellos que nunca han codificado antes o usado un cuaderno Jupyter, el video tutorial y las instrucciones en los cuadernos **Getting Started : Empezando** están pensados para hacer el proceso auto-explicativo.
# 
# ## Características del cuaderno Jupyter
# _________
# 
# Hay varias formas de interactuar y utilizar este cuaderno Jupyter. En la esquina superior derecha, hay varios iconos con utilidades que puedes utilizar.
# 
# ### <i class="fa fa-download" aria-hidden="true"></i> Descargar cuadernos Jupyter o PDFs.
# 
# La forma preferida de utilizar estos materiales es descargarlos del sitio web *Plants&Python* y ejecutarlos localmente en tu propio ordenador. Para cualquier cuaderno, puedes hacer clic en el símbolo de descarga y descargar el cuaderno Jupyter como un archivo iPython, `.ipynb`. Además, puede descargar el archivo, tal como se muestra en línea con el código ejecutado, como un PDF, `.pdf`.
# 
# ### <i class="fa fa-github" aria-hidden="true"></i> Ir al repositorio de github o abrir una incidencia
# 
# Los cuadernos subyacentes a las páginas web del Libro Jupyter están alojados en [github](https://github.com/), un servicio de alojamiento de repositorios de código. Si haces clic en la opción `repository`, accederás al repositorio de github y podrás descargar los archivos `.ipynb` utilizados para crear esta página web. También puedes optar por abrir una incidencia en github si encuentras errores o fallos en los materiales.
# 
# ### <i class="fa fa-expand" aria-hidden="true"></i> Entrar en el modo de pantalla completa
# 
# Siempre puedes hacer clic en el icono del modo de pantalla completa para entrar en el modo de pantalla completa.
# 
# ### <i class="fa fa-rocket" aria-hidden="true"></i> Utilizar Jupyter en línea
# 
# El icono del cohete le permite utilizar el código de los cuadernos Jupyter Book de forma interactiva en línea. De nuevo, la forma preferida de utilizar estos materiales es descargar el archivo `.ipynb` y ejecutar los cuadernos localmente. Sin embargo, es posible que haya algún problema con tu ordenador, que te falte memoria o que haya problemas de compatibilidad al ejecutar los cuadernos descargados en tu ordenador. En cualquiera de estos casos, ejecutar el código en el sitio web de forma virtual es una opción.
# 
# La primera opción para ejecutar el código virtualmente en línea es [binder](https://mybinder.org/), que hace que los cuadernos Jupyter en un repositorio de github sean interactivos. Alternativamente, ¡no tienes que dejar el sitio web para ejecutar binder! También puedes seleccionar la opción *Live Code* para ejecutar binder en la página web en la que ya estás. Una nota de precaución: ¡Binder tarda mucho tiempo en cargarse y ponerse en marcha!
# 
# Una alternativa a binder que tarda menos en cargarse es [Google Colab](https://colab.research.google.com). Al igual que binder, si haces clic en esta opción, serás llevado al entorno de Google Colab y podrás ejecutar y editar el código mostrado en el Jupyter Book.
# 
# ## Organización del material de aprendizaje
# ___________
# 
# El curso está dividido en tres secciones principales. Las primeras cuatro lecciones cubren los ***esenciales de codificación*** en Python por el Dr. Dan Chitwood. Estos son los objetivos mínimos de aprendizaje necesarios para utilizar Python de forma significativa. La siguiente sección enseña ***línea de comandos*** utilizando una terminal virtual por la Dra. Alejandra Rougon. Estas lecciones permiten a los estudiantes conocer los comandos de Unix y familiarizarse con la interfaz de la línea de comandos. El último conjunto de lecciones cubre ***bioinformática*** por el Dr. Bob VanBuren.
# 
# Cada conjunto de materiales de aprendizaje es ligeramente diferente, para adaptarse a cada una de las áreas temáticas. Pero hay similitudes en el diseño desde la perspectiva de una clase invertida:
# 
# 1. Hay **lecciones previas a la clase** que se centran en videos tutoriales. Los vídeos están pensados para enseñar a los estudiantes no sólo los objetivos de aprendizaje, sino para ***mostrar*** cómo se ejecuta el código en la práctica. Los vídeos están subtitulados (tanto en inglés como en español para las lecciones *esenciales de codificación* y *línea de comandos*). En el Jupyter Book hay transcripciones tanto en texto como en código de lo que se trata en los vídeos, lo que permite a los estudiantes seguirlos.
# 
# 2. También hay **prácticas previas a la clase** que los estudiantes utilizan para comprobar su dominio de los objetivos de aprendizaje que aprenden en los videotutoriales. En una clase, estas se entregan a los instructores antes de la actividad en clase del día siguiente y se utilizan para proporcionar retroalimentación individualizada a los estudiantes.
# 
# 3. Por último, hay **actividades en clase**. Se trata de ejercicios creativos y exploratorios centrados en ejemplos de plantas que los estudiantes completan en clase como grupo. Estas actividades son deliberadamente abiertas, sin respuestas incorrectas, y tienen por objeto aplicar los objetivos de aprendizaje de las lecciones y la práctica.
# 
# Estas actividades están estructuradas para una clase tradicional, pero también pueden ser utilizadas por los autodidactas. También señalamos que *Plants&Python* se diseñó durante la pandemia y se enseñó en múltiples ocasiones a nivel de grado y postgrado de forma virtual e internacional. Al no asumir ningún conocimiento de codificación y comenzar con instrucciones de cómo descargar Anaconda, estos materiales de aprendizaje están diseñados para ser lo más autoexplicativos posible, adecuados para diferentes contextos y propósitos. En la práctica, asignar una lección por día es un ritmo rápido y supone una curva de aprendizaje muy pronunciada. Sin embargo, los comentarios de los estudiantes indican que aprecian estar ***expuestos*** y ***inmersos*** en la codificación. Dominar la codificación, por supuesto, es un proceso continuo, de por vida. El propósito de *Plants&Python* es conseguir que los estudiantes se pongan en marcha lo antes posible con la codificación y que sirva de referencia a la que puedan volver a medida que avancen en sus carreras. Los materiales se ofrecen tal como son y esperamos que los estudiantes se lleven algo, lo que sea, que sirva para sus objetivos e impactos previstos.

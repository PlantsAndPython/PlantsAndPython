#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F">7.0 Trabajando de manera remota
# ***Autora:  Alejandra Rougon*** 
# 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Este trabajo está bajo la licencia <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Atribución-NonComercial 4.0 Licencia Internacional</a>.
# 
# 
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Objetivos de aprendizaje**
# >Después de completar esta lección aprenderás a:
# >
# >* a conectarte con `ssh` a un cluster o servidor remoto
# >* a transferir archivos por `scp`
# 
# 
# Los análisis genómicos involucran el trabajo con archivos con gran cantidad de datos y algunas veces los procesos requieren grandes recursos computacionales, que la mayoría de las computadoras personales no tienen. Por eso es muy probable que te tengas que conectar a un **Cluster de Alto Rendimiento [HPC]** para realizar algunos análisis. 
# 
# Para es propósito te puedes conectar con el protocolo **secure shell** a través del comando `ssh`. El administrador del cluster debe darte to dirección de ip, la cual se verá como esta `167.257.186.44`, tu nombre de usuario y contraseña.  
# 
# Algunas instituciones tienen un dominio asociado con la dirección ip. En ese caso puedes utilizar el dominio [`my.institution.edu`] en lugar de la dirección ip.
# 
# La sintaxis es `ssh user@ip_address`
# El puerto de conexión por defecto es el 22. Sin embargo por razones de seguridad algunas veces se cambia. Si ese es el caso, el administrador del cluster te lo hará saber y tu podrás especificar la opción con `-p`
# 
# ```
# ssh -p port user@ip_address
# ```
# Después de presionar enter se te pedirá la contraseña [password].
# 
# Para copiar de tu **computadora local a la computadora remota [servidor/cluster]** tienes que estar en una terminal en tu computadora local. Si ya estás conectado por `ssh` en esa terminal, no funcionará. Tienes que especificar la ubicación en el servidor remoto con la **ruta absoluta** después de `:`
# 
# ```
# scp local_file user@remote_ip_address:/location/where/file/will/be/copied
# ```
# 
# Por el contrario si quieres copiar **del servidor remoto a tu computadora**. Recuerda que la ruta en el servidor remoto tiene que ser la absoluta y va escrita después de `:`
# 
# ```
# scp user@remote_ip_address:/location_of_file/file_to_copy /location/where/file/will/be/copied
# ```
# 
# Con el comando `scp` el puerto es especificado con `-P`
# 
# ___
# 🔑 **En esta lección has aprendido**
# 
# * a conectarte con `ssh` a un cluster o servidor remoto
# * a transferir archivos por `scp`
# 
# 
# 
# 

# In[ ]:





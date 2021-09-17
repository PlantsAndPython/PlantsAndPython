#!/usr/bin/env python
# coding: utf-8

# 
# # <p style="color:#2C6A7F">7.0 Working Remotely 
# 
# ***Author:  Alejandra Rougon*** 
# 
# 
# 
# 
# <p style="color:#9D994B"><a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
# 
# > ### <p style="color:#2C6A7F"> 🔍 **Learning objectives**
# >After completing this lesson you will learn: 
# >
# >* how to work remotely with `ssh`
# >* how to transfer files with `scp`
# 
# Genomic analysis involve working with large data files and sometimes processes require high computational resources that most personal computers don't have. That is why, it is very likely that you will have to connect to a **High Performance Computing Cluster** to carry out some analysis. 
# 
# For that purpose you can connect through the **secure shell protocol** through the command `ssh`. The cluster's administrator should give you the ip address, which looks like `167.257.186.44`, the user name and password. 
# 
# Some institutions have a domain associated with the ip address. So in that case you can put the domain [e.g.  `my.institution.edu` ]  instead of the ip address. 
# 
# The syntax is `ssh user@ip_address` or `ssh user@my.institution.edu`.
# The default connection port is 22. However for security reasons that port is sometimes changed. If that is the case, the cluster administrator will let you know and you can indicate the port with option `-p`
# 
# ```
# ssh -p port user@ip_address
# ```
# After hitting enter you will be asked to type your password.
# 
# To copy **from your local computer to a remote computer** you have to be in a terminal in your local computer. If you are already connected by ssh it won't work. You have to specify the location with the **absolute path** in the remote server after `:` 
# 
# ```
# scp local_file user@remote_ip_address:/location/where/file/will/be/copied
# ```
# 
# 
# On the contrary if you want to copy **from the remote server to your local computer**. Remember that the path in the remote server has to be specified with the **absolute path** after `:`
# 
# ```
# scp user@remote_ip_address:/location_of_file/file_to_copy /location/where/file/will/be/copied
# ```
# 
# With the command `scp` the port is specified with uppercase  `-P`
# 
# ___
# 🔑 **In this lesson you have**
# 
# 
# * how to work remotely with `ssh`
# * how to transfer files with `scp`
# 
# 
# 
# 
# 
# 

# In[ ]:





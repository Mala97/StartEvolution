#! /usr/bin/env python3

# coding:utf-8

from os import path, name
import logging as log

log.basicConfig(level=log.DEBUG)

def launch_analysis(data_file):
   directory = path.dirname(path.dirname(__file__)) # we get the right path.=> (Obtenir le chemin)
   path_to_file = path.join(directory, "data", data_file) # with this path, we go inside the folder `data` and get the file.

   try:
      with open(path_to_file,"r") as f:
         lecture = f.readline()
         log.debug("Yeah!, vous lisez la premiere ligne. Voici le contenu du fichier csv:\n{}".format(lecture))
   
   except FileNotFoundError as e:
      log.critical("Ow! Here's error:{}".format(e))   

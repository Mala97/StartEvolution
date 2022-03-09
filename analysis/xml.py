#! /usr/bin/env python 3

# coding: utf-8

from os import path, name
import logging as lg


def launch_analysis(data_file):
	path_to_file = path.join("data", data_file)
	filename = path.basename(path_to_file)
	directory = path.dirname(path_to_file)

	lg.info("Opening data_file {} vers le fichier:{}".format(filename, directory))


	with open(path_to_file, "r") as fichier:
		lecture = fichier.readline()

	print("OW! Yeah Here's the file contenu xml:{}".format(lecture))
	
if __name__ == '__main__':
	launch_analysis("SyceronBrut.xml")		
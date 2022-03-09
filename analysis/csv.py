#! /usr/bin/env python 3

# coding: utf-8

from os import path, name
import logging as lg
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class SetMembers:
	"""docstring SetMembers"""
	def __init__(self, name):
		self.name = name

	def data_from_csv(self, csv_file):
		lg.info("Opening data file {}".format(csv_file))
		self.dataframe = pd.read_csv(csv_file, sep=";")	

	def data_from_dataframe(self, dataframe):
		self.dataframe = dataframe

	def display_chart(self):
			data = self.dataframe
			female_mps = data[data.sexe == "F"]
			male_mps = data[data.sexe == "H"]
			counts = [len(female_mps), len(male_mps)]
			counts = np.array(counts)
			nb_mps = counts.sum()
			proportions = counts / nb_mps

			labels = ["Female ({})". format(counts[0]), "Male ({})".format(counts[1])] 	
			fig, ax = plt.subplots()
			ax.axis("equal")
			ax.pie(proportions, labels = labels, autopct = "%1.2f%%")
			plt.title("{} ({} MPs)".format(self.name, nb_mps))
			plt.show()

	def split_by_political_party(self):
		result = {}
		data = self.dataframe
		all_parties = data["parti_financier"].dropna().unique()

		for party in all_parties:
			data_subset = data[data.parti_financier == party]
			subset = SetMembers('MPs from party "{}"'.format(party))
			subset.data_from_dataframe(data_subset)
			result[party] = subset

		return result		

def launch_analysis(data_file, by_party = False):
				XData = SetMembers("ALL MPs")
				XData.data_from_csv(path.join("data", data_file))
				XData.display_chart()

				if by_party:
					for party, s in XData.split_by_political_party().items():
						s.display_chart()

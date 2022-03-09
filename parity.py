#! /usr/bin/env python 3

# coding: utf-8

import logging as lg
import argparse
import analysis.csv as c_an
import analysis.xml as x_an


lg.basicConfig(level=lg.DEBUG)

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--extension", help="""File's contenu CSV or XML""")
	parser.add_argument("-d", "--datafile", help=""" CSV containing of data members parliament""")

	return parser.parse_args()


def main():
    args = parse_arguments()
    try:
        datafile = args.datafile
        #import pdb; pdb.set_trace()    # Python debugeur
        if datafile == None:
            raise Warning('You must indicate a datafile!')   # Pouvoir relancer l'erreur deleguer

        else:
            try:
                if args.extension == 'xml':
                    x_an.launch_analysis(datafile)
                elif args.extension == 'csv':
                    c_an.launch_analysis(datafile)

            except FileNotFoundError as e:
                lg.critical("Ow :( The file was not found. Here is the original message of the exception :", e)

            finally:
                lg.info('[-][-][-][-][-][-] Analysis is over [-][-][-][-][-][-]')

    except Warning as e:
        lg.info(e)	    	
   
if __name__ == "__main__":
    main()
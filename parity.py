#! /usr/bin/env python3

# coding: utf-8

import argparse   # Arguments

#import des modules
import analysis.csv as c_an
import analysis.xml as x_an


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type de fichiers a analyser? C'est CSV ou XML""")
    parser.add_argument("-d", "--datafile",  help="""CSV, un fichier contient des informations 
    	                    aux sujets des membres et parlements""")
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
                print("Ow :( The file was not found. Here is the original message of the exception :", e)

            finally:
                print('[-][-][-][-][-][-] Analysis is over [-][-][-][-][-][-]')

    except Warning as e:
        print(e)	    	
   
if __name__ == "__main__":
    main()
import pandas as pd


df4 = pd.read_csv('Data.csv', sep='\t', low_memory=False)
# on garde les lignes pour lesquelles la colonne "coutries" est égale à "France"
France = df4[df4['countries'] == 'France']

# on split le dataframe en 4 dataframes de 1/4 de la taille du dataframe initial
Fr1 = France[:int(len(France)/4)]
Fr2 = France[int(len(France)/4):int(len(France)/2)]
Fr3 = France[int(len(France)/2):int(3*len(France)/4)]
Fr4 = France[int(3*len(France)/4):]

# on exporte les 4 dataframes en csv
Fr1.to_csv('France1.csv', sep=',', index=False)
Fr2.to_csv('France2.csv', sep=',', index=False)
Fr3.to_csv('France3.csv', sep=',', index=False)
Fr4.to_csv('France4.csv', sep=',', index=False)

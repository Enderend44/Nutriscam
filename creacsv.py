import pandas as pd
import csv
Data = pd.read_csv("Tri1.csv", sep=",", low_memory=False)

# on crée un dataframe avec uniquement les colonnes qui nous intéresse : 
# allergens et allergenes_en
df = Data[["categories","categories_tags","categories_en"]]



print(df.head(50))
#print(df.describe())
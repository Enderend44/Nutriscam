#Ouvre Tri1.csv et le stocke dans df1
import csv
import pandas as pd

df1 = pd.read_csv('Tri1.csv')

# Ne garde que les colonnes code, url, product_name, generic_name, brands, categories_en, ingredients_text, allergens, 
# serving_size, energy_100g, fat_100g, saturated-fat_100g, carbohydrates_100g, sugars_100g, fiber_100g, proteins_100g, salt_100g, 
# nutriscore_score, nutriscore_grade, ecoscore_score, ecoscore_grade et sauvegarde ça dans df2 sans utiliser de boucle

df2 = df1[['code', 'url', 'product_name', 'generic_name', 'brands', 'categories_en', 'ingredients_text', 'allergens', 'serving_size', 'energy_100g', 'fat_100g', 'saturated-fat_100g', 'carbohydrates_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'salt_100g', 'nutriscore_score', 'nutriscore_grade', 'ecoscore_score', 'ecoscore_grade']]

# Supprime les lignes avec des valeurs manquantes et sauvegarde ça dans df3
df3 = df2.dropna()

#Sauvegarde le résultat en créant Triavance.csv
df3.to_csv('Triavance.csv', index=False)


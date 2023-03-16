# On réalise les traitements sur les 4 dataframes

import pandas as pd
import numpy as np

# on importe les 4 dataframes
df1 = pd.read_csv('France1.csv', sep=',', low_memory=False)
df2 = pd.read_csv('France2.csv', sep=',', low_memory=False)
df3 = pd.read_csv('France3.csv', sep=',', low_memory=False)
df4 = pd.read_csv('France4.csv', sep=',', low_memory=False)




# on supprime les colonnes inutiles : creator,created_t,created_datetime,last_modified_t,last_modified_datetime,last_modified_by,last_image_t,last_image_datetime,image_url,image_small_url,image_ingredients_url,image_ingredients_small_url,image_nutrition_url,image_nutrition_small_url,unique_scans_n,popularity_tags,completeness,states,states_tags,states_en
df1 = df1.drop(['creator','created_t','created_datetime','last_modified_t','last_modified_datetime','last_modified_by','last_image_t','last_image_datetime','image_url','image_small_url','image_ingredients_url','image_ingredients_small_url','image_nutrition_url','image_nutrition_small_url','unique_scans_n','popularity_tags','completeness','states','states_tags','states_en'], axis=1)
df2 = df2.drop(['creator','created_t','created_datetime','last_modified_t','last_modified_datetime','last_modified_by','last_image_t','last_image_datetime','image_url','image_small_url','image_ingredients_url','image_ingredients_small_url','image_nutrition_url','image_nutrition_small_url','unique_scans_n','popularity_tags','completeness','states','states_tags','states_en'], axis=1)
df3 = df3.drop(['creator','created_t','created_datetime','last_modified_t','last_modified_datetime','last_modified_by','last_image_t','last_image_datetime','image_url','image_small_url','image_ingredients_url','image_ingredients_small_url','image_nutrition_url','image_nutrition_small_url','unique_scans_n','popularity_tags','completeness','states','states_tags','states_en'], axis=1)
df4 = df4.drop(['creator','created_t','created_datetime','last_modified_t','last_modified_datetime','last_modified_by','last_image_t','last_image_datetime','image_url','image_small_url','image_ingredients_url','image_ingredients_small_url','image_nutrition_url','image_nutrition_small_url','unique_scans_n','popularity_tags','completeness','states','states_tags','states_en'], axis=1)

# on catégorise les colonnes, ici zero_features est une liste de colonnes dont les valeurs manquantes sont remplacées par 0, Inconnu_features est une liste de colonnes dont les valeurs manquantes sont remplacées par None, mode_features est une liste de colonnes dont les valeurs manquantes sont remplacées par la valeur la plus fréquente

# les colonnes dont les valeurs manquantes sont remplacées par 0 sont : energy-kj_100g,energy-kcal_100g,energy_100g,energy-from-fat_100g,fat_100g,saturated-fat_100g,butyric-acid_100g,caproic-acid_100g,caprylic-acid_100g,capric-acid_100g,lauric-acid_100g,myristic-acid_100g,palmitic-acid_100g,stearic-acid_100g,arachidic-acid_100g,behenic-acid_100g,lignoceric-acid_100g,cerotic-acid_100g,montanic-acid_100g,melissic-acid_100g,unsaturated-fat_100g,monounsaturated-fat_100g,polyunsaturated-fat_100g,omega-3-fat_100g,alpha-linolenic-acid_100g,eicosapentaenoic-acid_100g,docosahexaenoic-acid_100g,omega-6-fat_100g,linoleic-acid_100g,arachidonic-acid_100g,gamma-linolenic-acid_100g,dihomo-gamma-linolenic-acid_100g,omega-9-fat_100g,oleic-acid_100g,elaidic-acid_100g,gondoic-acid_100g,mead-acid_100g,erucic-acid_100g,nervonic-acid_100g,trans-fat_100g,cholesterol_100g,carbohydrates_100g,sugars_100g,added-sugars_100g,sucrose_100g,glucose_100g,fructose_100g,lactose_100g,maltose_100g,maltodextrins_100g,starch_100g,polyols_100g,erythritol_100g,fiber_100g,soluble-fiber_100g,insoluble-fiber_100g,proteins_100g,casein_100g,serum-proteins_100g,nucleotides_100g,salt_100g,added-salt_100g,sodium_100g,alcohol_100g,vitamin-a_100g,beta-carotene_100g,vitamin-d_100g,vitamin-e_100g,vitamin-k_100g,vitamin-c_100g,vitamin-b1_100g,vitamin-b2_100g,vitamin-pp_100g,vitamin-b6_100g,vitamin-b9_100g,folates_100g,vitamin-b12_100g,biotin_100g,pantothenic-acid_100g,silica_100g,bicarbonate_100g,potassium_100g,chloride_100g,calcium_100g,phosphorus_100g,iron_100g,magnesium_100g,zinc_100g,copper_100g,manganese_100g,fluoride_100g,selenium_100g,chromium_100g,molybdenum_100g,iodine_100g,caffeine_100g,taurine_100g,ph_100g,fruits-vegetables-nuts_100g,fruits-vegetables-nuts-dried_100g,fruits-vegetables-nuts-estimate_100g,fruits-vegetables-nuts-estimate-from-ingredients_100g,collagen-meat-protein-ratio_100g,cocoa_100g,chlorophyl_100g,carbon-footprint_100g,carbon-footprint-from-meat-or-fish_100g,nutrition-score-fr_100g,nutrition-score-uk_100g,glycemic-index_100g,water-hardness_100g,choline_100g,phylloquinone_100g,beta-glucan_100g,inositol_100g,carnitine_100g

zero_features = ['energy-kj_100g', 'energy-kcal_100g', 'energy_100g', 'energy-from-fat_100g', 'fat_100g', 'saturated-fat_100g', 'butyric-acid_100g', 'caproic-acid_100g', 'caprylic-acid_100g', 'capric-acid_100g', 'lauric-acid_100g', 'myristic-acid_100g', 'palmitic-acid_100g', 'stearic-acid_100g', 'arachidic-acid_100g', 'behenic-acid_100g', 'lignoceric-acid_100g', 'cerotic-acid_100g', 'montanic-acid_100g', 'melissic-acid_100g', 'unsaturated-fat_100g', 'monounsaturated-fat_100g', 'polyunsaturated-fat_100g', 'omega-3-fat_100g', 'alpha-linolenic-acid_100g', 'eicosapentaenoic-acid_100g', 'docosahexaenoic-acid_100g', 'omega-6-fat_100g', 'linoleic-acid_100g', 'arachidonic-acid_100g', 'gamma-linolenic-acid_100g', 'dihomo-gamma-linolenic-acid_100g', 'omega-9-fat_100g', 'oleic-acid_100g', 'elaidic-acid_100g', 'gondoic-acid_100g', 'mead-acid_100g', 'erucic-acid_100g', 'nervonic-acid_100g', 'trans-fat_100g', 'cholesterol_100g', 'carbohydrates_100g', 'sugars_100g', 'added-sugars_100g', 'sucrose_100g', 'glucose_100g', 'fructose_100g', 'lactose_100g', 'maltose_100g', 'maltodextrins_100g', 'starch_100g', 'polyols_100g', 'erythritol_100g', 'fiber_100g', 'soluble-fiber_100g', 'insoluble-fiber_100g', 'proteins_100g', 'casein_100g', 'serum-proteins_100g', 'nucleotides_100g', 'salt_100g', 'added-salt_100g', 'sodium_100g', 'alcohol_100g', 'vitamin-a_100g', 'beta-carotene_100g', 'vitamin-d_100g', 'vitamin-e_100g', 'vitamin-k_100g', 'vitamin-c_100g', 'vitamin-b1_100g', 'vitamin-b2_100g', 'vitamin-pp_100g', 'vitamin-b6_100g', 'vitamin-b9_100g', 'folates_100g', 'vitamin-b12_100g', 'biotin_100g', 'pantothenic-acid_100g', 'silica_100g', 'bicarbonate_100g', 'potassium_100g', 'chloride_100g', 'calcium_100g', 'phosphorus_100g','iron_100g', 'magnesium_100g', 'zinc_100g', 'copper_100g', 'manganese_100g', 'fluoride_100g', 'selenium_100g', 'chromium_100g', 'molybdenum_100g', 'iodine_100g', 'caffeine_100g', 'taurine_100g', 'ph_100g', 'fruits-vegetables-nuts_100g', 'fruits-vegetables-nuts-dried_100g', 'fruits-vegetables-nuts-estimate_100g', 'fruits-vegetables-nuts-estimate-from-ingredients_100g', 'collagen-meat-protein-ratio_100g', 'cocoa_100g', 'chlorophyl_100g', 'carbon-footprint_100g', 'carbon-footprint-from-meat-or-fish_100g', 'nutrition-score-fr_100g', 'nutrition-score-uk_100g', 'glycemic-index_100g', 'water-hardness_100g', 'choline_100g', 'phylloquinone_100g', 'beta-glucan_100g', 'inositol_100g', 'carnitine_100g']
Inconnu_features = ['product_name','abbreviated_product_name','generic_name','packaging', 'packaging_tags', 'packaging_en', 'packaging_text', 'brands', 'brands_tags', 'categories', 'categories_tags', 'categories_en', 'origins', 'origins_tags', 'origins_en', 'manufacturing_places', 'manufacturing_places_tags', 'labels', 'labels_tags', 'labels_en']
mode_features = ['']


df1[Inconnu_features]=df1[Inconnu_features].fillna('Inconnu')
df1[zero_features]=df1[zero_features].fillna(0)
# df1[mode_features]=df1[mode_features].fillna(df1.mode().iloc[0])

total = df1.isnull().sum().sort_values(ascending=False)
pd.DataFrame(data={'Missing': total}).head(2)




# on enregistre les 4 dataframes en csv
df1.to_csv('Tri1.csv', sep=',', index=False)
df2.to_csv('Tri2.csv', sep=',', index=False)
df3.to_csv('Tri3.csv', sep=',', index=False)
df4.to_csv('Tri4.csv', sep=',', index=False)





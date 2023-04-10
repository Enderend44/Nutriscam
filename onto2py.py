from owlready2 import *

# Chargez votre ontologie depuis un fichier local ou une URL
# Remplacez 'mon_ontologie.owl' par le nom de votre fichier ou l'URL
onto = get_ontology("Nutriscam.owl").load()

import csv

# On recherche les IRI des classes à partir de leurs labels
def find_class_by_label(ontology, label):
    for cls in ontology.classes():
        if label.lower() in [l.lower() for l in cls.label]:
            return cls
    return None
# On crée un dictionnaire pour stocker IRI des classes et leurs labels
classes = {}
for cls in onto.classes():
    classes[cls.label[0]] = cls

# On crée une fonction pour ajouter des instances à partir d'un fichier CSV
def add_instances_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Créez les instances pour chaque classe
            produit = classes['Produit']()
            valeur_nutritionnelle = classes['ValeurNutritionnelle']()
            nutriscore = classes['Nutriscore']()
            ecoscore = classes['Ecoscore']()

            # Remplissez les propriétés de données pour chaque instance
            produit.code = row['code']
            produit.url = row['url']
            produit.product_name = row['product_name']
            produit.generic_name = row['generic_name']
            produit.brands = row['brands']
            produit.categories_en = row['categories_en']
            produit.ingredients_text = row['ingredients_text']
            produit.allergens = row['allergens']
            produit.serving_size = row['serving_size']

            valeur_nutritionnelle.energy_100g = float(row['energy_100g'])
            valeur_nutritionnelle.fat_100g = float(row['fat_100g'])
            valeur_nutritionnelle.saturated_fat_100g = float(row['saturated-fat_100g'])
            valeur_nutritionnelle.carbohydrates_100g = float(row['carbohydrates_100g'])
            valeur_nutritionnelle.sugars_100g = float(row['sugars_100g'])
            valeur_nutritionnelle.fiber_100g = float(row['fiber_100g'])
            valeur_nutritionnelle.proteins_100g = float(row['proteins_100g'])
            valeur_nutritionnelle.salt_100g = float(row['salt_100g'])

            nutriscore.nutriscore_score = float(row['nutriscore_score'])
            nutriscore.nutriscore_grade = row['nutriscore_grade']

            ecoscore.ecoscore_score = float(row['ecoscore_score'])
            ecoscore.ecoscore_grade = row['ecoscore_grade']

            # Établissez des relations entre les instances
            produit.aValeurNutritionnelle = [valeur_nutritionnelle]
            produit.aNutriscore = [nutriscore]
            produit.aEcoscore = [ecoscore]

add_instances_from_csv('Triavance.csv')

# Enregistrez votre ontologie avec les nouvelles instances
onto.save(file = "Test2.owl", format = "rdfxml")
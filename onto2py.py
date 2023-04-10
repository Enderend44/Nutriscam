import pandas as pd
from owlready2 import *

# Charger l'ontologie
onto = get_ontology("test.owl").load()

# # Lire le fichier CSV
# data = pd.read_csv("Tri1.csv")

# # Parcourir les lignes du fichier CSV
# for index, row in data.iterrows():
#     # Créer une instance pour chaque élément du fichier CSV
    
#     # Exemple pour la classe CategoriePNNS
#     categorie_pnns_instance = onto.CategoriePNNS("CategoriePNNS_" + str(index))
#     categorie_pnns_instance.pnns_groups_1 = row["pnns_groups_1"]
#     categorie_pnns_instance.pnns_groups_2 = row["pnns_groups_2"]

#     # Ajoutez d'autres instances pour les autres classes ici, en suivant le même modèle que ci-dessus

#     # Exemple pour la classe Fibres
#     fibres_instance = onto.Fibres("Fibres_" + str(index))
#     fibres_instance.fiber = row["fiber_100g"]
#     fibres_instance.soluble_fiber = row["soluble-fiber_100g"]
#     fibres_instance.insoluble_fiber = row["insoluble-fiber_100g"]

#     # Répétez ce processus pour les autres classes en utilisant les colonnes correspondantes du fichier CSV

# # Enregistrez les modifications dans l'ontologie
# onto.save("test1.owl")

# # Afficher les classes de l'ontologie
print(onto.classes())



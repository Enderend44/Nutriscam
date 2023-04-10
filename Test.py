import pandas as pd
from owlready2 import get_ontology, Thing

# Charger l'ontologie
onto = get_ontology("path/to/your/ontology.owl").load()

# Lire le fichier CSV
data = pd.read_csv("Tri1.csv")

# Fonction pour trouver une classe à partir de son label
def find_class_by_label(ontology, label):
    for cls in ontology.classes():
        if label.lower() in [l.lower() for l in cls.label]:
            return cls
    return None

# Parcourir les données du fichier CSV et créer des instances des classes correspondantes
for index, row in data.iterrows():
    product_name = row['product_name']

    # Trouver la classe correspondant à la colonne "pnns_groups_1"
    pnns_groups_1_label = row['pnns_groups_1']
    pnns_groups_1_class = find_class_by_label(onto, pnns_groups_1_label)

    # Si la classe existe, créer une instance
    if pnns_groups_1_class:
        instance = pnns_groups_1_class(product_name)
        # Vous pouvez également ajouter d'autres attributs à l'instance ici, si nécessaire

    # Répétez ce processus pour d'autres colonnes/labels, en créant des instances pour chaque classe trouvée

# Sauvegarder l'ontologie peuplée dans un nouveau fichier
onto.save("path/to/your/populated_ontology.owl")

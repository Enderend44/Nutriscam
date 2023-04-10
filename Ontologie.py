import pandas as pd
import csv
from owlready2 import *
# Définir la langue par défaut sur le français
default_world.lang = "fr"

onto = get_ontology("Nutriscam.owl").load()

with open("Tri1.csv", "r",errors='ignore') as csvfile:
    data = list(csv.reader(csvfile))


iri_to_class_name = {
    "http://webprotege.stanford.edu/RCGJPHmSnNuQSWDrtMccvYr": "Aliment",
    "http://webprotege.stanford.edu/RNtNNQ79ZuN49EGyfTYaM3": "Conservateurs",
    "http://webprotege.stanford.edu/R7xdD60RKCLzf6nGvx2MTkj": "Sulfites",
    "http://webprotege.stanford.edu/R858QxE6t8X6oOUVXdTZ2Ek": "fruits&légumes",
    "http://webprotege.stanford.edu/R9as6o4uTZXqhuWUWzB0HQl": "féculents",
    "http://webprotege.stanford.edu/Rz1ZVRYLqbznQAaM7iSC4t": "Arachides",
    "http://webprotege.stanford.edu/RsrEVVPMeJTdXsfSZz9omS": "FruitsACoques",
    "http://webprotege.stanford.edu/RDa89whCXzJ9r4ZvDxd5zrx": "Gluten",
    "http://webprotege.stanford.edu/RCSoY12Al8EPdJsXAU5N0ag": "Moutarde",
    "http://webprotege.stanford.edu/R19zzpOPvzcHg29RHd9bH7": "ProduitsABaseDeLupin",
    "http://webprotege.stanford.edu/RDSYQxS0L3XW8o3R1K9NN2o": "ProduitsABaseDeSésame",
    "http://webprotege.stanford.edu/R6TcPOAM47OGh5qJwQGG1K": "Sésame",
    "http://webprotege.stanford.edu/R7Jkppb30KTkysmnF8jYmjU": "matièresGrasses",
    "http://webprotege.stanford.edu/R7OwroFFhej2o0pvcTwiTS2": "produitsLaitiers",
    "http://webprotege.stanford.edu/RDOnDRi1wucmvCNIQlOTvSP": "produitsLaitiersAllergènes",
    "http://webprotege.stanford.edu/R7YA1y6yU39k3LY0fZCaAri": "produitsSucrés",
    "http://webprotege.stanford.edu/RBJNCZ3TNW3r5KXyNrqp8Hw": "viandesPoissonsOeufs",
    "http://webprotege.stanford.edu/R7gAhkV5hbRttllBosGMeuH": "Crustacés",
    "http://webprotege.stanford.edu/RHD4wDIrmFizn6cVtvZCo3": "Oeufs",
    "http://webprotege.stanford.edu/R7gvqsUgizCYCXq3bGsY5XK": "Poissons",
    "http://webprotege.stanford.edu/R7kAijCbZuNi5fC4e4NMFWv": "ProduitsBaseDeMollusques",
    "http://webprotege.stanford.edu/RDwyMO5T3Al1xV5y4tqa2hV": "Soja",
    "http://webprotege.stanford.edu/R7zTTOH30vV22IqAwnQPov7": "alimentContenantDuPoisson",
    "http://webprotege.stanford.edu/R89s3J7rNffMeYlRMFvtJ1V": "Caracteristique",
    "http://webprotege.stanford.edu/R8JLlFzd5MXgW2MC4t0ehXU": "CaracteristiqueGeographique",
    "http://webprotege.stanford.edu/R8Po6rr8P7IbBOrdFjb3WCO": "pays",
    "http://webprotege.stanford.edu/RDfbsiHTdIl30JNJvppZ0Zu": "region",
    "http://webprotege.stanford.edu/R8Sd8DjATvMR9GSp0CON4Cq": "CaracteristiqueOrganoleptique",
    "http://webprotege.stanford.edu/R8ilb5H8SbRxFV5VyJccDrB": "aspect",
    "http://webprotege.stanford.edu/R91KeM3VAuCr8sJUjF8aoh6": "aspectSonore",
    "http://webprotege.stanford.edu/RC4n2YF4RgbnBvWyZmMd42r": "gout",
    "http://webprotege.stanford.edu/R91UAeAXX3C3EOVGedE1R8O": "odeur",
    "http://webprotege.stanford.edu/R9A1wvRMFCMnveEpnqyMTwA": "poids",
    "http://webprotege.stanford.edu/RCV4Va31chvSHsnBJSkYuwx": "texture",
    "http://webprotege.stanford.edu/R9A92RaLlWUtGor4Z7J0ftN": "caractéristiquesApprovisionnement",
    "http://webprotege.stanford.edu/R9Ec9ZQCICx2ovK9Umw2npO": "cout",
    "http://webprotege.stanford.edu/R9WBvxYt7yccTJb6JTyZgyt": "modeConditionnement",
    "http://webprotege.stanford.edu/R9dgOFDfDfkcylHpoKBMFve": "modeConservation",
    "http://webprotege.stanford.edu/R9eZvH7P9kr9wKsgj6XA4aE": "typerDeProvenance",
    "http://webprotege.stanford.edu/RB0bWpiwTXyOWxoMuQLbgdD": "caractéristiquesDeQualité",
    "http://webprotege.stanford.edu.R9fbC6Zjk2dj5l8Drc97iex": "label",
    "http://webprotege.stanford.edu.R9iK1QMwrQif8LwBy16s7B5": "saison",
    "http://webprotege.stanford.edu.RB88GetLOjFanxLo0bwrtWl": "caractéristiquesNutritionnelles",
    "http://webprotege.stanford.edu.RB8vtDgF82S9YgHChlX5GkT": "catégoriePNNS",
    "http://webprotege.stanford.edu.RB9Jim0xHrSus9zTS3cpNO8": "ValeursNutritionnelles",
    "http://webprotege.stanford.edu.RBt1ohiRz2ACtiIhkVYI0yQ": "macronutriments",
    "http://webprotege.stanford.edu.RBJm4dkaBj2cJQbV67eqhPN": "glucides",
    "http://webprotege.stanford.edu.RBQRx49iCaSD0RDCSMDiDGC": "glucidescomplexes(sucres lents)",
    "http://webprotege.stanford.edu.RBofXX9wFU57cSD4ITCI7Mr": "glucidesSimples(sucres rapides)",
    "http://webprotege.stanford.edu.RBruxg1GxR7mfcIjkWJ8rvQ": "lipides",
    "http://webprotege.stanford.edu.RCAZWObr0NhjBqn9UgIvRRP": "insaturés(AGI)",
    "http://webprotege.stanford.edu.RC862TnWZDTQbTTNcakIFy2": "saturés(AGS)",
    "http://webprotege.stanford.edu.RCDuUF5ydjKTYyHfaVGmjT2": "protéines",
    "http://webprotege.stanford.edu.RCMYbtE4PDmF563Qm4ANQqa": "micronutriments",
    "http://webprotege.stanford.edu.RCMo4d3Qmulu0HpYoM4oK6V": "fibres",
    "http://webprotege.stanford.edu.RCY9jM1HvHBDgfnk12WNXEc": "vitamines/minéraux",
    "http://webprotege.stanford.edu.RCY9jM1HvHBDgfnk12WNXEc": "minéraux",
    "http://webprotege.stanford.edu.RCY9jM1HvHBDgfnk12WNXEc": "calcium",
    "http://webprotege.stanford.edu.RCd9DpJgsBGaFoWJLsNId4w": "chlore",
    "http://webprotege.stanford.edu.RCjEAtXOFnXdAMXGXMac9lR": "chrome",
    "http://webprotege.stanford.edu.RCwDNmCLRsIaZOYoQAkyNRs": "cuivre",
    "http://webprotege.stanford.edu.RCypWSQ1xvqBueHDdgYFq4g": "fer",
    "http://webprotege.stanford.edu.RDAqlNmkIdlTVnJ9TO9Ay9p": "magnésium",
    "http://webprotege.stanford.edu.RDBmU7gNyHNApC3efz2ejPN": "potassium",
    "http://webprotege.stanford.edu.RDEayPLh0w5BETh45GPQZd4": "sodium",
    "http://webprotege.stanford.edu.RDetfDr62MWl4h0FmjYJBoo": "zinc",
    "http://webprotege.stanford.edu.RDjFanxKz5N94F8dXn5AGMu": "vitamines",
    "http://webprotege.stanford.edu.RFCdSXHZCs7Sr5eavBJj1q": "vitamineA",
    "http://webprotege.stanford.edu.RGr04VpmAxhoH5hITGEoX2": "vitamineB",
    "http://webprotege.stanford.edu.RHSG9GZAduVtar0KKF9P77": "vitamineC",
    "http://webprotege.stanford.edu.RPFAEYdAGB00agz4KcjbHI": "vitamineD",
    "http://webprotege.stanford.edu.RdG1Rg3IZMZjCK5RlasPYU": "vitamineE",
    "http://webprotege.stanford.edu.RehqfRvSjtKVeW0Ih8ZePb": "vitamineK",
    "http://webprotege.stanford.edu.Rf63fpCq7SEcFCyH7NSLLk": "ObjectifAffiché",
    "http://webprotege.stanford.edu.RqqTl5hocUgH904v9V58qa": "MaintienDePoids",
    "http://webprotege.stanford.edu.RvVIvrnGpwFyAApkiq4W0u": "PerteDePoids",
    "http://webprotege.stanford.edu.RwE97YsEqeyt0AkUHWsLpb": "priseDeMasse",
    "http://webprotege.stanford.edu.RwiKzel6u0kf8erZR5eTHP":"Personne",
    "http://webprotege.stanford.edu.RwxDfOjUHNOQOIiLM6kX0K":
    "http://webprotege.stanford.edu.Rz7EzXXYf4dVZFEH4YQcX4":
}

# On peut maintenant utilser iri_to_class_name pour récupérer le nom de la classe à partir de son IRI et ainsi creer les instances des classes 

# Parcours du dictionnaire iri_to_class_name pour attribuer les labels RDFS
for iri, class_name in iri_to_class_name.items():
    # Trouver la classe correspondante dans l'ontologie
    cls = onto.search_one(iri=iri)
    
    # Attribuer le nom de la classe en tant que label RDFS
    if cls:
        cls.label = class_name

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


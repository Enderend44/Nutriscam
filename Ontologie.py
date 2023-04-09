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
    "http://webprotege.stanford.edu/R9xEW9F6N5FGf0QNJ6b5m6j": "CaracteristiquesNutritionnelles",
    "http://webprotege.stanford.edu/RB5UfIpUcWZ2QY1YnqgL3z": "calories",
    "http://webprotege.stanford.edu/RB8AeuD8axpVEzYgxcFptx1": "glucides",
    "http://webprotege.stanford.edu/RB8N8oyPmC0gD2hLdCqdvrX": "lipides",
    "http://webprotege.stanford.edu/RB9IYfoOci7xOx9WbX36g1": "proteines",
    "http://webprotege.stanford.edu/RD7G2tAaLX7toAByjAAuV7": "CaracteristiquesSocioEconomiques",
    "http://webprotege.stanford.edu/R9LoA3M1q3Kjg5ey6QGjZm": "caractéristiquesDuConsommateur",
    "http://webprotege.stanford.edu/RDw0CukP6OYNApF0N6dMfj9": "caractéristiquesDuDistributeur",
    "http://webprotege.stanford.edu/RDw1cEjK9FhWTFP7iWJx8oo": "caractéristiquesDuProducteur",
    "http://webprotege.stanford.edu/RE5TTD6xN8EgX9ZkKfjKmiR": "Certification",
    "http://webprotege.stanford.edu/RE8Za6JXa6oZKjRnQ6UdP6o": "certificationBio",
    "http://webprotege.stanford.edu/RE9jPb4O5W8J5pbHQfjGyC5": "certificationFairTrade",
    "http://webprotege.stanford.edu/RDw8OOBDI51LrM0YrA7OQx0": "EconomieCirculaire",
    "http://webprotege.stanford.edu/RE6YsR6R7GcJW9XHWHNU1l1": "Label",
    "http://webprotege.stanford.edu/RE7Pxg2QZx9XURD3qZ3V7NC": "labelRouge",
    "http://webprotege.stanford.edu/RE8XfOTNlC5Gn0J6Ky0w6RU": "labelBleu",
    "http://webprotege.stanford.edu/RE9c4Orrkmf8fm5W5g5FhS5": "labelVert",
    "http://webprotege.stanford.edu/REEkcihH8W5EK5D5C5S5h5S": "SansAllergènes",
    "http://webprotege.stanford.edu/RE61A6F3U6q5X5Q5S5h5S5S": "SansAllergènesSpécifiques",
    "http://webprotege.stanford.edu/RE7S5h5S5S5S5S5S5S5S5S5": "SansGluten",
    "http://webprotege.stanford.edu/RE7V7NC5h5S5S5S5S5S5S5S": "SansLactose",
    "http://webprotege.stanford.edu/RE7W6RU5h5S5S5S5S5S5S5S": "SansOeufs",
    "http://webprotege.stanford.edu/RE7X5Q5S5h5S5S5S5S5S5S5": "Végétalien",
    "http://webprotege.stanford.edu/RE7Y1l15h5S5S5S5S5S5S5S": "Végétarien",
}

# On peut maintenant utilser iri_to_class_name pour récupérer le nom de la classe à partir de son IRI et ainsi creer les instances des classes 

def   create_instances ( ontology ,   iri_to_class_name ):
            for   iri   in   iri_to_class_name . keys ():
                ontology . create_entity ( iri_to_class_name [ iri ],   iri )
            return   ontology

# on sauvegarde l'ontologie
ontology   =   create_instances ( onto ,   iri_to_class_name )
ontology . save ( "test.owl" )

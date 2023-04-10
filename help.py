import pandas as pd
from owlready2 import *

# Charger l'ontologie
onto = get_ontology("Nutriscam.owl").load()

#afficher les classes de l'ontologie

for cls in onto.classes():
    print(cls)

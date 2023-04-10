from owlready2 import *

# Chargez votre ontologie depuis un fichier local ou une URL
# Remplacez 'mon_ontologie.owl' par le nom de votre fichier ou l'URL
onto = get_ontology("Test2.owl").load()

instance_code = 'R71wMar2MzSzF2vGd3rXT6e'
produit_instance = onto.search_one(code=instance_code)

if produit_instance:
    print(f"Code: {produit_instance.code}")
    print(f"URL: {produit_instance.url}")
    print(f"Product Name: {produit_instance.product_name}")
    print(f"Generic Name: {produit_instance.generic_name}")
    print(f"Brands: {produit_instance.brands}")
    print(f"Categories: {produit_instance.categories_en}")
    print(f"Ingredients Text: {produit_instance.ingredients_text}")
    print(f"Allergens: {produit_instance.allergens}")
    print(f"Serving Size: {produit_instance.serving_size}")

else:
    print("Produit non trouvé")
import { Condition, ConditionTypeString, Feature, FeaturesENUM } from "./types/GlobalTypes";

export const conditions: Feature[] = [
	{
		name: FeaturesENUM.PRODUCT_NAME,
		displayName: "Nom du produit",
		type: 0
	},
	{
		name: FeaturesENUM.GENERIC_NAME,
		displayName: "Nom généric",
		type: 0
	},
	{
		name: FeaturesENUM.BRANDS,
		displayName: "Nom de la marque",
		type: 0
	},
	{
		name: FeaturesENUM.CATEGORIES_EN,
		displayName: "Catégorie (anglais)",
		type: 0,
	},
	{
		name: FeaturesENUM.INGREDIENTS_TEXT,
		displayName: "Ingrédients",
		type: 0,
	},
	{
		name: FeaturesENUM.ALLERGENS,
		displayName: "Allergènes",
		type: 0,
	},
	{
		name: FeaturesENUM.ENERGY_100G,
		displayName: "Energie 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.FAT_100G,
		displayName: "Gras pour 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.SATURATED_FAT_100G,
		displayName: "Gras saturé pour 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.CARBOHYDRATES_100G,
		displayName: "Carbohydrates pour 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.SUGARS_100G,
		displayName: "Sucres pour 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.FIBER_100G,
		displayName: "Fibres pour 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.PROTEINS_100G,
		displayName: "Protéines pour 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.SALT_100G,
		displayName: "Sel pour 100G",
		type: 1,
	},
	{
		name: FeaturesENUM.NUTRISCORE_SCORE,
		displayName: "Nutriscore",
		type: 1,
	},
	{
		name: FeaturesENUM.NUTRISCORE_GRADE,
		displayName: "Nutriscore note",
		type: 0,
	},
	{
		name: FeaturesENUM.ECOSCORE_SCORE,
		displayName: "Ecoscore",
		type: 1,
	},
	{
		name: FeaturesENUM.ECOSCORE_GRADE,
		displayName: "Ecoscore note",
		type: 0,
	},
]
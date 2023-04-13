export enum FeaturesENUM {
	PRODUCT_NAME,
	GENERIC_NAME,
	BRANDS,
	CATEGORIES_EN,
	INGREDIENTS_TEXT,
	ALLERGENS,
	ENERGY_100G,
	FAT_100G,
	SATURATED_FAT_100G,
	CARBOHYDRATES_100G,
	SUGARS_100G,
	FIBER_100G,
	PROTEINS_100G,
	SALT_100G,
	NUTRISCORE_SCORE,
	NUTRISCORE_GRADE,
	ECOSCORE_SCORE,
	ECOSCORE_GRADE,
}

export type Feature = {
	name: FeaturesENUM
	displayName: string
	type: 0 | 1
	prefillList?: string[]
}

export enum ConditionTypeString {
	EGAL = "Egal au texte",
	CONTIENT = "Contient le texte"
}

export type ConditionType = ConditionTypeNumber | ConditionTypeString;

export enum ConditionTypeNumber {
	PLUS = "Plus (+)",
	MOINS = "Moins (-)",
	EGAL = "Egal (=)"
}

export type Condition = {
	feature: Feature,
	selected: ConditionTypeString | ConditionTypeNumber
	value: number | string
}

export type Display = {
	code:               number;
	url:                string;
	product_name:       string;
	generic_name:       string;
	brands:             string;
	categories_en:      string;
	ingredients_text:   string;
	allergens:          string;
	serving_size:       string;
	energy_100g:        number;
	fat_100g:           number;
	saturated_fat_100g: number;
	carbohydrates_100g: number;
	sugars_100g:        number;
	fiber_100g:         number;
	proteins_100g:      number;
	salt_100g:          number;
	nutriscore_score:   number;
	nutriscore_grade:   string;
	ecoscore_score:     number;
	ecoscore_grade:     string;
}
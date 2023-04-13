import { conditions } from "@/const";
import {
  Condition,
  ConditionTypeNumber,
  ConditionTypeString,
  Feature,
} from "@/types/GlobalTypes";
import { useEffect, useState } from "react";
import { RiCloseFill } from "react-icons/ri";

export default function SelectCondition({
  addCondition,
  close,
}: {
  addCondition: (condition: Condition) => void;
  close: () => void;
}) {
  const [feature, setFeature] = useState<Feature>();
  const [condition, setCondition] = useState<
    ConditionTypeNumber | ConditionTypeString
  >();
  const [value, setValue] = useState<string | number>("");

  const handleConditionChange = (
    event: React.ChangeEvent<HTMLSelectElement>
  ) => {
    let selectedCondition: ConditionTypeNumber | ConditionTypeString;

    if (feature?.type === 0) {
      selectedCondition = event.target.value as unknown as ConditionTypeString;
    } else {
      selectedCondition = event.target.value as ConditionTypeNumber;
    }

    setCondition(selectedCondition);
  };

  const handleFeatureChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedFeature = conditions.find(
      (condition) => condition.displayName === event.target.value
    );
    setFeature(selectedFeature);
    setCondition(
      selectedFeature?.type == 0
        ? ConditionTypeString.CONTIENT
        : ConditionTypeNumber.PLUS
    );
  };

  const handleValueChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValue(event.target.value);
  };

  return (
    <div className="w-fit h-fit px-14 py-14 bg-[#FFDCC8] rounded-lg justify-center items-center flex flex-col gap-4">
      <button
        onClick={() => close()}
        className="absolute top-4 right-4 text-[#A6DAB9] rounded-md p-2 "
      >
        <RiCloseFill className="text-3xl" />
      </button>
      <span></span>
      <select
        value={feature?.displayName}
        onChange={handleFeatureChange}
        className="block w-auto mt-1 rounded-md bg-[#A6DAB9]  shadow-sm p-2"
      >
        <option className="" value="">
          Selectionnez une feature
        </option>
        {conditions.map((condition, key) => (
          <option
            className="bg-[#A6DAB9] hover:bg-white p-2"
            key={key}
            value={condition.displayName}
          >
            {condition.displayName}
          </option>
        ))}
      </select>
      {condition && (
        <div className="flex flex-col gap-4 w-full items-center">
          <select
            className="block w-auto mt-1 rounded-md bg-[#A6DAB9]  shadow-sm p-2"
            value={condition}
            onChange={handleConditionChange}
          >
            {Object.values(
              feature?.type == 0 ? ConditionTypeString : ConditionTypeNumber
            ).map((condition) => (
              <option key={condition} value={condition}>
                {condition}
              </option>
            ))}
          </select>
          <input
            className="bg-[#A6DAB9] text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
            type={feature?.type === 0 ? "text" : "number"}
            value={value}
            onChange={handleValueChange}
          />
          <button onClick={() => {

						if (!feature)
							return

						addCondition({
							feature: feature,
							selected: condition,
							value: value
						})

						close()
					}}  className="button-2">Ajouter</button>
        </div>
      )}
    </div>
  );
}

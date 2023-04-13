import SelectCondition from "@/components/SelectCondition";
import Table from "@/components/Table";
import Background from "@/components/containers/Background";
import { usePopUpContext } from "@/components/containers/PopUpContainer";
import useExplore from "@/hooks/useExplore";
import { Condition } from "@/types/GlobalTypes";
import { useReactTable } from "@tanstack/react-table";
import { useEffect, useState } from "react";
import {
  AiFillCaretLeft,
  AiFillCaretRight,
  AiOutlineArrowRight,
} from "react-icons/ai";
import { RiCloseFill } from "react-icons/ri";
import { pageSize } from "./api/explore";
export default function Explore() {
  const [conditions, setConditions] = useState<Condition[]>([]);
  const [page, setPage] = useState(1);

  const popUp = usePopUpContext();
  const explore = useExplore(conditions, page);

	useEffect(() => {
		console.log(explore)
	}, [explore])

  return (
    <div className="w-full pb-40 max-w-[1200px] h-fit z-50 items-center justify-center flex flex-col gap-4 mt-10">
      <div>
        {conditions.length == 0 ? (
          <span>Aucune condition sur la recherche</span>
        ) : (
          <div className="flex flex-row flex-wrap gap-4">
            {conditions.map((condition, index) => (
              <div
                key={index}
                className="button-1 flex flex-row items-center justify-center"
              >
                <span className="flex flex-row items-center justify-center gap-2">
                  {condition.feature.displayName} <AiOutlineArrowRight />{" "}
                  {condition.selected} <AiOutlineArrowRight />
                  {condition.value}
                </span>
                <button
                  className="ml-4"
                  onClick={() =>
                    setConditions(
                      conditions.filter(
                        (e) =>
                          !(
                            e.feature == condition.feature &&
                            e.selected == condition.selected &&
                            e.value == condition.value
                          )
                      )
                    )
                  }
                >
                  <RiCloseFill className="text-3xl" />
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
      <button
        onClick={() =>
          popUp.setPopUp(
            <SelectCondition
              close={() => popUp.setPopUp(undefined)}
              addCondition={(condition: Condition) => {
                setConditions((p) => [...p, condition]);
                setPage(1);
              }}
            />
          )
        }
        className="button-2"
      >
        Ajouter une condition
      </button>
      <div className="w-[100px] flex flex-row justify-between">
        {explore.length != 0 && page != 1 && (
          <button onClick={() => setPage((page) => page - 1)}>
            <AiFillCaretLeft />
          </button>
        )}
				{explore.length != 0 && (
          <button className="ml-auto" onClick={() => setPage((page) => page + 1)}>
						<AiFillCaretRight />
					</button>
        )}
        
      </div>

      <Table data={explore} />
    </div>
  );
}

import { ConditionsQuery } from "@/pages/api/explore";
import { Condition, Display } from "@/types/GlobalTypes";
import axios from "axios";
import { useQuery } from "react-query";

const useExplore = (conditions : Condition[], page: number) => {

	const explore = useQuery(
		["explore", conditions, page],
		() => {

			const query : ConditionsQuery = {
				conditions: conditions,
				page: page
			}

			return axios<Display[]>({
				method: "post",
				url: "/api/explore",
				data: query
			})
				.then((r) => r.data)
				.catch((e) => {
					throw new Error(e);
				});

			
		},
		{
			cacheTime: 0,
		}
	);
	if (explore.data)
		return explore.data

	return [];
};

export default useExplore;
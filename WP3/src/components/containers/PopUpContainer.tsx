import useOnClickOutside from "@/hooks/useOnClickOutside";
import { motion } from "framer-motion";
import { createContext, createRef, ReactElement, useContext, useRef, useState } from "react";

type contextType = {
	popUp: ReactElement | undefined;
	setPopUp: (popUp: ReactElement | undefined) => void;
};

const Context = createContext<contextType>({
	popUp: undefined,
	setPopUp: () => { },
});

export const usePopUpContext = () => useContext(Context);

export default function PopUpContainer({
	children,
}: {
	children: JSX.Element;
}) {
	const [element, setElement] = useState<ReactElement | undefined>(undefined);
	const clickRef = createRef<HTMLDivElement>();
	useOnClickOutside(clickRef, () => setElement(undefined));

	return (
		<Context.Provider
			value={{
				popUp: element,
				setPopUp: setElement,
			}}
		>
			{element != undefined && (
        <div className="fixed z-[600] w-full h-screen bg-[rgba(0,0,0,0.424)] backdrop-blur-sm flex justify-center items-center">
				<motion.div
						initial={{
							scale: 0.7,
							opacity: 0,
							translateY: "-50%",
						}}
						animate={{ scale: 1, opacity: 1, translateY: "0%" }}
						className="w-fit h-fit" ref={clickRef}>
						{element}
					</motion.div>
				</div>
			)}
			{children}
		</Context.Provider>
	);
}

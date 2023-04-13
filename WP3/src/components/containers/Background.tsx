import { motion } from "framer-motion";
import Image from "next/image";
import Link from "next/link";

export default function Background({ children }: { children: JSX.Element }) {
	return (
		<main
			className={
				"bg-[#fffaf6] w-full min-h-screen flex flex-col items-center text-default"
			}
		>
			<motion.div
				initial={{
					opacity: 0,
				}}
				animate={{
					opacity: 1,
				}}
				transition={{
					delay: 2,
					duration: 1,
				}}
			>
				{" "}
				<Image
					className="absolute right-10"
					width={260}
					height={30}
					alt=""
					src={"/assets-2.jpg"}
				/>
				<Image
					className="absolute bottom-16 left-32"
					width={260}
					height={30}
					alt=""
					src={"/assets-3.jpg"}
				/>
			</motion.div>

			<motion.div
				initial={{
					opacity: 0,
				}}
				animate={{
					opacity: 1,
				}}
				transition={{
					duration: 1,
				}}
			>
				<Image
					className="absolute bottom-1/2 translate-y-30 -translate-x-1/2 left-1/2"
					width={600}
					height={30}
					alt=""
					src={"/assets-4.jpg"}
				/>
			</motion.div>
			<motion.div
				initial={{
					opacity: 0,
				}}
				animate={{
					opacity: 1,
				}}
				transition={{
					delay: 0.5,
					duration: 1,
				}}
				className="pt-20 flex flex-col items-center justify-center z-10"
			>
				<Link href="/">
					<Image width={270} height={30} alt="" src={"/nutriscam.png"} />
				</Link>

			</motion.div>


			{children}
		</main>
	)
}
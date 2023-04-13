/* eslint-disable react/no-unescaped-entities */
import Background from "@/components/containers/Background";
import { motion } from "framer-motion";
import Image from "next/image";
import Link from "next/link";
import { AiFillGithub } from "react-icons/ai";

export default function Home() {
  return (
    <div className="max-w-[660px] text-center mt-10 z-50">
      <motion.span
        initial={{
          opacity: 0,
        }}
        animate={{
          opacity: 1,
        }}
        transition={{
          delay: 1,
          duration: 1,
        }}
        className="font-title text-5xl"
      >
        Bienvenue sur NutriScam
      </motion.span>

      <motion.a
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
        className="flex flex-row gap-2 items-center w-fit mt-4 ml-auto mr-auto"
        href="https://github.com/Enderend44/Nutriscam"
      >
        <AiFillGithub className="text-3xl" /> Github
      </motion.a>
      <motion.div
        initial={{
          opacity: 0,
        }}
        animate={{
          opacity: 1,
        }}
        transition={{
          delay: 1.5,
          duration: 1,
        }}
        className="bg-[#ead2ca] w-fit h-fit px-5 py-8 rounded-lg mt-10 flex flex-col items-center justify-center"
      >
        <span className="">
          NutriScam est un site web innovant qui permet d'évaluer la qualité nutritionnelle des aliments.
          <br />
          <br /> Notre objectif est de fournir des informations précises et
          fiables sur les produits alimentaires pour aider les consommateurs
          à faire des choix plus sains.
        </span>

        <div className="flex flex-row gap-4 w-full items-center justify-center pt-6">
          <Link href={"/explore"} className="button-2">
            Tester
          </Link>
        </div>
      </motion.div>
    </div>
  );
}

import Background from "@/components/containers/Background";
import PopUpContainer from "@/components/containers/PopUpContainer";
import "@/styles/globals.css";
import type { AppProps } from "next/app";
import Head from "next/head";
import { createClient } from "@supabase/supabase-js";
import { QueryClient, QueryClientProvider } from "react-query";

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL as string;
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY as string;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
const queryClient = new QueryClient();

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Nutriscam</title>
      </Head>
      <QueryClientProvider client={queryClient}>
        <Background>
          <PopUpContainer>
            <Component {...pageProps} />
          </PopUpContainer>
        </Background>
      </QueryClientProvider>
    </>
  );
}

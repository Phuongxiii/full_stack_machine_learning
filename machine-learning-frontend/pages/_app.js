/** @format */

import "../styles/globals.css";
import { ChakraProvider, Container, useColorModeValue } from "@chakra-ui/react";
import NavBar from "./common/NavBar";

function MyApp({ Component, pageProps }) {
	return (
		<ChakraProvider>
			<NavBar />
			<Component {...pageProps} />
		</ChakraProvider>
	);
}

export default MyApp;

/** @format */

import { Center, Container, useColorModeValue } from "@chakra-ui/react";
import Paint from "./components/paint";

const WordRecognition = () => {
	return (
		<Container
			maxW='full'
			h='100vh'
			background={useColorModeValue("#F7ECDE", "#2C3333")}>
			<Paint />
			<Center>Word Recognition</Center>
		</Container>
	);
};

export default WordRecognition;

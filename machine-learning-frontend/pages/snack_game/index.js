/** @format */

import { Center, Container, useColorModeValue } from "@chakra-ui/react";

const SnackGame = () => {
	return (
		<Container
			maxW='full'
			h='100vh'
			background={useColorModeValue("#F7ECDE", "#2C3333")}>
			<Center>Snack Game</Center>
		</Container>
	);
};

export default SnackGame;

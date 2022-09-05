/** @format */

import { Center, Container, useColorModeValue } from "@chakra-ui/react";

const Portfolio = () => {
	return (
		<Container
			maxW='full'
			h='100vh'
			background={useColorModeValue("#F7ECDE", "#2C3333")}>
			<Center>Portfolio</Center>
		</Container>
	);
};

export default Portfolio;

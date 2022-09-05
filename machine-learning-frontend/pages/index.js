/** @format */

import { Center, Container, useColorModeValue } from "@chakra-ui/react";

export default function Home() {
	return (
		<Container
			maxW='full'
			h='100vh'
			background={useColorModeValue("#F7ECDE", "#2C3333")}>
			<Center>Hello World!</Center>
		</Container>
	);
}

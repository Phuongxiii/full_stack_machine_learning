/** @format */

import {
	Box,
	Button,
	Container,
	List,
	ListItem,
	useColorMode,
	useColorModeValue,
} from "@chakra-ui/react";
import { SunIcon, MoonIcon } from "@chakra-ui/icons";
import styled from "@emotion/styled";
import { css } from "@emotion/react";
import Link from "next/link";
import LinkPrimary from "./link";

const dynamicStyle = (props) =>
	css`
		color: ${props.color};
	`;

const Logo = styled.h1`
	font-size: 28px;
	${dynamicStyle}
	font-family: "DynaPuff", cursive;
`;

const NavBar = () => {
	const { colorMode, toggleColorMode } = useColorMode();
	return (
		<Container
			maxW='full'
			h='48px'
			background={useColorModeValue("#E9DAC1", "#395B64")}>
			<Box
				display='flex'
				margin='auto'
				justifyContent='space-between'
				maxW='80%'
				alignItems='center'
				alignContent='center'>
				<Logo color={useColorModeValue("#54BAB9", "#E7F6F2")}>
					<Link href='/'>Phuong Nguyen</Link>
				</Logo>
				<Box w={2}></Box>
				<List
					display='flex'
					justifyContent='space-between'
					color={useColorModeValue("#54BAB9", "#E7F6F2")}>
					<ListItem m={2}>
						<LinkPrimary link='/word_recognition'>
							Word Recognition
						</LinkPrimary>
					</ListItem>
					<ListItem m={2}>
						<LinkPrimary link='/snack_game'>Snack Game</LinkPrimary>
					</ListItem>
					<ListItem m={2}>
						<LinkPrimary link='/portfolio'>Portfolio</LinkPrimary>
					</ListItem>
				</List>
				<Button onClick={toggleColorMode} size='sm'>
					{colorMode === "light" ? <SunIcon /> : <MoonIcon />}
				</Button>
			</Box>
		</Container>
	);
};

export default NavBar;

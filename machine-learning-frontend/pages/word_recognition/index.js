/** @format */

import {
	Box,
	Center,
	Container,
	Switch,
	useColorModeValue,
} from "@chakra-ui/react";
import { useState } from "react";
import FileImage from "./components/FileImage";
import Paint from "./components/paint";

const WordRecognition = () => {
	const [fileOrPaint, ToggleFileOrPaint] = useState(false);
	return (
		<Container
			maxW='full'
            top={48}
			h='100vh'
			background={useColorModeValue("#F7ECDE", "#2C3333")}>
			{fileOrPaint ? <FileImage /> : <Paint />}
			<Center m={6}>
				Paint
				<Switch
					m={2}
					checked={fileOrPaint}
					onChange={() => ToggleFileOrPaint((value) => !value)}
				/>
				File
			</Center>
		</Container>
	);
};

export default WordRecognition;

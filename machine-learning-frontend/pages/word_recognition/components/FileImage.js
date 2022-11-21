/** @format */

import {
	FormControl,
	FormLabel,
	FormErrorMessage,
	Center,
	FormHelperText,
	Input,
	Box,
	VStack,
	Button,
	Image,
} from "@chakra-ui/react";
import React, { useState } from "react";
import postImage from "./method/postImage";

export default function FileImage() {
	const [base64String, setBase64String] = useState("");
	const [label, setLabel] = useState("");
	const [fileImage, setFileImage] = useState(false);
	function getBase64(file, cb) {
		let reader = new FileReader();
		reader.readAsDataURL(file);
		reader.onload = function () {
			cb(reader.result);
		};
		setFileImage(true);
		reader.onerror = function (error) {
			console.log("Error: ", error);
		};
	}
	return (
		<Center m={6}>
			<VStack>
				<FormControl>
					<Input
						type='file'
						name='file'
						onChange={(file) => {
							getBase64(file.target.files[0], (value) => {
								setBase64String(value);
							});
						}}
					/>
				</FormControl>
				{fileImage && <Image src={base64String} />}
				<Button
					onClick={(e) => {
						postImage(base64String, setLabel);
					}}>
					Predict
				</Button>
				<Box p={2} backgroundColor='gray.300' fontSize='24px'>
					{`Label: ${label}`}
				</Box>
			</VStack>
		</Center>
	);
}

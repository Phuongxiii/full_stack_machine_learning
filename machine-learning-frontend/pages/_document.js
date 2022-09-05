/** @format */

import React from "react";
import { ColorModeScript } from "@chakra-ui/react";
import NextDocument, { Html, Head, Main, NextScript } from "next/document";
import theme from "./lib/theme";

export default class Document extends NextDocument {
	render() {
		return (
			<Html lang='en'>
				<Head>
					<title>Project</title>
					<link
						rel='preconnect'
						href='https://fonts.googleapis.com'></link>
					<link
						rel='preconnect'
						href='https://fonts.gstatic.com'></link>
					<link
						href='https://fonts.googleapis.com/css2?family=DynaPuff:wght@400;500;600;700&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Shadows+Into+Light&display=swap'
						rel='stylesheet'></link>
				</Head>
				<body>
					{/* 👇 Here's the script */}
					<ColorModeScript
						initialColorMode={theme.config.initialColorMode}
					/>
					<Main />
					<NextScript />
				</body>
			</Html>
		);
	}
}

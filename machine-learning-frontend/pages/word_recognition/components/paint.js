/** @format */

import { Box, Button, Center, VStack } from "@chakra-ui/react";
import React, { useState, useEffect, useRef } from "react";

const Paint = () => {
	const canvasRef = useRef();
	const [isDraw, setIsDraw] = useState(false);
	const [count, setCount] = useState(0);
	const [x, setX] = useState(null);
	const [y, setY] = useState(null);

	useEffect(() => {
		const canvas = canvasRef.current;
		const context = canvas.getContext("2d");
		console.log(window.innerWidth);
		context.fillStyle = "#fff";
		context.fillRect(0, 0, canvas.width, canvas.height);
	}, [count]);
	function startDraw(event) {
		setIsDraw(true);
	}
	function Draw(event) {
		if (isDraw) {
			const canvas = canvasRef.current;
			const context = canvas.getContext("2d");
			context.fillStyle = "#000";
			context.fillRect(
				event.clientX - (window.innerWidth - 732) / 2,
				event.clientY - 48,
				15,
				15
			);
		} else {
		}
	}
	function endDraw(event) {
		setIsDraw(false);
	}
	function clear() {
		const canvas = canvasRef.current;
		const context = canvas.getContext("2d");
		context.clearRect(0, 0, canvas.width, canvas.height);
		setCount(count + 1);
	}
	function downloadImage() {
		const canvas = canvasRef.current;
		let canvasUrl = canvas.toDataURL("image/png", 0.5);
		console.log(canvasUrl);
		const createEl = document.createElement("a");
		createEl.href = canvasUrl;
		createEl.download = "download-this-canvas";
		createEl.click();
		createEl.remove();
	}
	return (
		<Center>
			<VStack>
				<canvas
					width='720px'
					height='480px'
					ref={canvasRef}
					onMouseDown={startDraw}
					onMouseMove={Draw}
					onMouseUp={endDraw}
					style={{
						background: "#fff",
					}}
				/>
				<Button onClick={clear}>Restart</Button>
				<Button onClick={downloadImage}>Download</Button>
			</VStack>
		</Center>
	);
};

export default Paint;

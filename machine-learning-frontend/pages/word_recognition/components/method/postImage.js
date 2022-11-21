/** @format */
import axios from "axios";

export default async function postImage(base64String, callBack) {
	const path = "http://127.0.0.1:8000/word_recognition/predict/";
	const data = new FormData();
	data.append("image", base64String);
	data.append("title", "image");
	data.append("label", "image");
	await axios
		.post(path, data)
		.then((value) => {
			console.log(value.data.image);
			callBack(value.data.image);
		})
		.catch(function (error) {
			console.log(error.message);
		});
}

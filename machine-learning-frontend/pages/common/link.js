/** @format */

import Link from "next/link";

const LinkPrimary = (props) => {
	return <Link href={props.link}>{props.children}</Link>;
};

export default LinkPrimary;

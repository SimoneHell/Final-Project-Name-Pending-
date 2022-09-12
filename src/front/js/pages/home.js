import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	//const { store, actions } = useContext(Context);
	const { store, actions } = useContext(Context);
	console.log(store)

	return (
		
		<div className="text-center mt-5">
			{store.users.map((item, index) => {
				return (
				<p>{item.id}</p>)
			})}
			<h1> Esto es una prueba menor </h1>
		</div>
	);
};

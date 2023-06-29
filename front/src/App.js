import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import logo from './logo.svg';
import './App.css';

function App() {
	const [users, setUsers] = useState([]);

	async function test() {
		try {
			console.log("test de chamada 1");
			const response = await axios.get('http://localhost:5000/users');
			var listaObjetos = response.data;
			console.log("test de chamada");
			//com esse vc atualiza o elemento a = b 
			setUsers([ ...listaObjetos]);
			// com esse vc adiciona sem excluir os dados anteriores a = a + b 
			// setUsers([...users, ...listaObjetos]);
		} catch (err) {
			console.log("erro de chamada");
		}
	}

	useEffect(() => {
		test();
	}, []);

	return (
		<div>
			<h1>
				{console.log(users)}
				<div>
					{users.map((user) => (
						<div>
							<p>email: {user.email}</p>
							<p>senha: {user.password}</p>
							<p>nome completo:{user.fullname}</p>
							<p>nome de usuario: {user.username}</p>
							<hr />
						</div>

					))}
				</div>
				<button onClick={test}>
					Chamada de usuários
				</button>
			</h1>
		</div>
	);
}

export default App;

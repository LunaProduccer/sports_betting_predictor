import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import PredictionForm from './components/predictionform.jsx';

function App() {
	const [count, setCount] = useState(0);

	return (
		<>
			<div>
				<PredictionForm />
			</div>
		</>
	);
}

export default App;

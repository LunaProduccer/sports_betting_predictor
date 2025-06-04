import React, { useState } from 'react';
import { predictionMatchResult } from '../api';

const PredictionForm = () => {
	const [formData, setFormData] = useState({
		goalsFor: '',
		goalsAgainst: '',
		possession: '',
		shotsOnTarget: '',
		shotsTotal: '',
		corners: '',
		fouls: '',
		yellowCards: '',
		redCards: '',
	});

	const [loading, setLoading] = useState(false);
	const [prediction, setPrediction] = useState(null);
	const [error, setError] = useState('');
	const [success, setSuccess] = useState(false);

	const handleInputChange = (e) => {
		const { name, value } = e.target;
		setFormData((prev) => ({
			...prev,
			[name]: value,
		}));
	};

	const handleSubmit = async (e) => {
		e.preventDefault();
		setLoading(true);
		setError('');
		setSuccess(false);

		try {
			const result = await predictionMatchResult(formData);
			setPrediction(result);
			setSuccess(true);
			setLoading(false);
		} catch (err) {
			setError(err.message || 'Error al obtener predicción');
			setLoading(false);
		}
	};

	const resetForm = () => {
		setFormData({
			goalsFor: '',
			goalsAgainst: '',
			possession: '',
			shotsOnTarget: '',
			shotsTotal: '',
			corners: '',
			fouls: '',
			yellowCards: '',
			redCards: '',
		});
		setPrediction(null);
		setError('');
		setSuccess(false);
	};

	return (
		<div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
			<h2 className="text-3xl font-bold text-center mb-8 text-gray-800">
				Predicción de Resultado
			</h2>

			<div onSubmit={handleSubmit} className="space-y-6">
				<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Goles a Favor
						</label>
						<input
							type="number"
							name="goalsFor"
							value={formData.goalsFor}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Goles en Contra
						</label>
						<input
							type="number"
							name="goalsAgainst"
							value={formData.goalsAgainst}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Posesión (%)
						</label>
						<input
							type="number"
							name="possession"
							value={formData.possession}
							onChange={handleInputChange}
							min="0"
							max="100"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Tiros a Puerta
						</label>
						<input
							type="number"
							name="shotsOnTarget"
							value={formData.shotsOnTarget}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Tiros Totales
						</label>
						<input
							type="number"
							name="shotsTotal"
							value={formData.shotsTotal}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Córners
						</label>
						<input
							type="number"
							name="corners"
							value={formData.corners}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Faltas
						</label>
						<input
							type="number"
							name="fouls"
							value={formData.fouls}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Tarjetas Amarillas
						</label>
						<input
							type="number"
							name="yellowCards"
							value={formData.yellowCards}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>

					<div className="space-y-2">
						<label className="block text-sm font-medium text-gray-700">
							Tarjetas Rojas
						</label>
						<input
							type="number"
							name="redCards"
							value={formData.redCards}
							onChange={handleInputChange}
							min="0"
							required
							className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
						/>
					</div>
				</div>

				<div className="flex flex-col sm:flex-row gap-4 justify-center">
					<button
						onClick={handleSubmit}
						disabled={loading}
						className="px-8 py-3 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
					>
						{loading ? 'Prediciendo...' : 'Predecir Resultado'}
					</button>

					<button
						onClick={resetForm}
						className="px-8 py-3 bg-gray-600 text-white font-semibold rounded-md hover:bg-gray-700 transition-colors"
					>
						Resetear
					</button>
				</div>
			</div>

			{/* Loading overlay */}
			{loading && (
				<div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
					<div className="bg-white p-6 rounded-lg flex flex-col items-center">
						<div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
						<p className="text-gray-700">Analizando datos...</p>
					</div>
				</div>
			)}

			{/* Success message */}
			{success && !loading && (
				<div className="mt-6 p-4 bg-green-100 border border-green-400 text-green-700 rounded-md">
					✅ Predicción obtenida exitosamente
				</div>
			)}

			{error && (
				<div className="mt-6 p-4 bg-red-100 border border-red-400 text-red-700 rounded-md">
					{error}
				</div>
			)}

			{prediction && (
				<div className="mt-6 p-6 bg-green-50 border border-green-200 rounded-md">
					<h3 className="text-xl font-bold text-green-800 mb-4">
						Resultado Predicho
					</h3>
					<div className="flex flex-col sm:flex-row sm:items-center sm:justify-between">
						<span className="text-2xl font-bold text-green-700">
							{prediction.result}
						</span>
						<span className="text-lg text-green-600">
							Probabilidad: {(prediction.probability * 100).toFixed(1)}%
						</span>
					</div>
				</div>
			)}
		</div>
	);
};

export default PredictionForm;

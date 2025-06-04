// src/api.js
import axios from 'axios';

const API_BASE_URL =
	import.meta.env.VITE_API_BACKEND_URL || 'http://localhost:5000';

export const predictionMatchResult = async (matchStats) => {
	try {
		const response = await axios.post(`${API_BASE_URL}/predict`, matchStats, {
			headers: {
				'Content-Type': 'application/json',
			},
		});
		return response.data;
	} catch (error) {
		console.error('Error making prediction:', error);
		throw new Error(
			error.response?.data?.message || 'Error al obtener predicción',
		);
	}
};

// Función adicional para verificar estado del backend
export const checkBackendHealth = async () => {
	try {
		const response = await axios.get(`${API_BASE_URL}/health`);
		return response.data;
	} catch (error) {
		throw new Error('Backend no disponible');
	}
};

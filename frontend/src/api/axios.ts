import axios from 'axios';
import { useAuthStore } from '../store/auth';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

api.interceptors.request.use(
  (config) => {
    const token = useAuthStore.getState().token;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export default api; 
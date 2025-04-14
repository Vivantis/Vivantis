import api from '../api/axios';

interface TokenResponse {
  access: string;
  refresh?: string;
}

export async function login(username: string, password: string): Promise<TokenResponse> {
  const response = await api.post('/token/', { username, password });
  return response.data;
}

export async function getPerfil(): Promise<any> {
  const response = await api.get('/perfil/');
  return response.data;
} 
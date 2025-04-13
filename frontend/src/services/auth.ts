interface AuthResponse {
  access: string;
  refresh: string;
}

interface UserProfile {
  id: number;
  username: string;
  email: string;
  is_administrador_geral?: boolean;
  is_morador?: boolean;
  is_portaria?: boolean;
}

export const authService = {
  async login(username: string, password: string): Promise<AuthResponse> {
    const response = await fetch('http://localhost:8000/api/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      throw new Error('Credenciais inválidas');
    }

    const data = await response.json();
    return data;
  },

  async getUserProfile(token: string): Promise<UserProfile> {
    const response = await fetch('http://localhost:8000/api/perfil/', {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error('Erro ao obter perfil do usuário');
    }

    return await response.json();
  },

  setTokens(access: string, refresh: string) {
    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
  },

  getAccessToken() {
    return localStorage.getItem('accessToken');
  },

  clearTokens() {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
  }
};

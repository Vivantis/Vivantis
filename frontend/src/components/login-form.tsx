'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { authService } from '@/services/auth'

export function LoginForm() {
  const router = useRouter()
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setIsLoading(true)

    try {
      // Tenta fazer login
      const authResponse = await authService.login(username, password)
      
      // Salva os tokens
      authService.setTokens(authResponse.access, authResponse.refresh)
      
      // Obtém o perfil do usuário
      const userProfile = await authService.getUserProfile(authResponse.access)
      
      // Redireciona baseado no tipo de usuário
      if (userProfile.is_administrador_geral) {
        router.push('/admin/dashboard')
      } else if (userProfile.is_morador) {
        router.push('/morador/dashboard')
      } else if (userProfile.is_portaria) {
        router.push('/portaria/dashboard')
      } else {
        router.push('/dashboard')
      }
    } catch (error) {
      setError('Usuário ou senha inválidos')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <form
      onSubmit={handleLogin}
      className="w-full max-w-sm bg-white dark:bg-gray-800 shadow-md rounded px-8 pt-6 pb-8"
    >
      <h2 className="text-2xl font-bold mb-6 text-center text-gray-800 dark:text-white">
        Acesso ao sistema
      </h2>
      <div className="mb-4">
        <label className="block text-sm font-bold mb-2 text-gray-700 dark:text-gray-300">
          Usuário
        </label>
        <input
          type="text"
          className="w-full px-3 py-2 border rounded shadow-sm focus:outline-none focus:ring"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
      </div>
      <div className="mb-6">
        <label className="block text-sm font-bold mb-2 text-gray-700 dark:text-gray-300">
          Senha
        </label>
        <input
          type="password"
          className="w-full px-3 py-2 border rounded shadow-sm focus:outline-none focus:ring"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>
      {error && <p className="text-red-500 text-sm mb-4">{error}</p>}
      <button
        type="submit"
        disabled={isLoading}
        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded disabled:opacity-50"
      >
        {isLoading ? 'Entrando...' : 'Entrar'}
      </button>
    </form>
  )
}

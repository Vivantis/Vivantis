'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

export function LoginForm() {
  const router = useRouter()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')

    const res = await fetch('http://localhost:8000/api/token/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: email, password }),
    })

    if (res.ok) {
      const data = await res.json()
      localStorage.setItem('token', data.access)
      router.push('/dashboard')
    } else {
      setError('Usuário ou senha inválidos.')
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
          E-mail
        </label>
        <input
          type="email"
          className="w-full px-3 py-2 border rounded shadow-sm focus:outline-none focus:ring"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
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
        className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Entrar
      </button>
    </form>
  )
}

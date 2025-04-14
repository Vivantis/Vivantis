import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/auth';
import { login } from '../services/auth.service';

const loginSchema = z.object({
  username: z.string().min(1, 'Usuário obrigatório'),
  password: z.string().min(1, 'Senha obrigatória'),
});

type LoginForm = z.infer<typeof loginSchema>;

export default function LoginPage() {
  const { register, handleSubmit, formState: { errors } } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
  });
  const setToken = useAuthStore((state) => state.setToken);
  const navigate = useNavigate();

  async function onSubmit(data: LoginForm) {
    try {
      const { access } = await login(data.username, data.password);
      setToken(access);
      navigate('/dashboard');
    } catch (err) {
      alert('Falha no login');
    }
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form onSubmit={handleSubmit(onSubmit)} className="bg-white p-8 shadow-md rounded w-96">
        <h2 className="text-2xl font-bold mb-6">Login</h2>

        <div className="mb-4">
          <label className="block mb-1">Usuário</label>
          <input type="text" {...register('username')} className="w-full border rounded px-3 py-2" />
          {errors.username && <p className="text-red-500 text-sm">{errors.username.message}</p>}
        </div>

        <div className="mb-4">
          <label className="block mb-1">Senha</label>
          <input type="password" {...register('password')} className="w-full border rounded px-3 py-2" />
          {errors.password && <p className="text-red-500 text-sm">{errors.password.message}</p>}
        </div>

        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded w-full">
          Entrar
        </button>
      </form>
    </div>
  );
}
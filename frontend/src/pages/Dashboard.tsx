import LayoutDashboard from '../layouts/LayoutDashboard';
import { useEffect, useState } from 'react';
import { getPerfil } from '../services/auth.service';

export default function DashboardPage() {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    getPerfil().then(setUser);
  }, []);

  return (
    <LayoutDashboard>
      <div className="p-4">
        <h2 className="text-xl font-bold">Dashboard</h2>
        {user ? (
          <p className="mt-4">Bem-vindo, <strong>{user.username}</strong>!</p>
        ) : (
          <p className="text-gray-500">Carregando perfil...</p>
        )}
      </div>
    </LayoutDashboard>
  );
} 
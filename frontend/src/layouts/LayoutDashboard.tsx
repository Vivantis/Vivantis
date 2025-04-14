import { ReactNode } from 'react';

export default function LayoutDashboard({ children }: { children: ReactNode }) {
  return (
    <div className="flex min-h-screen">
      <aside className="w-64 bg-gray-900 text-white p-4">
        <h2 className="text-xl font-bold mb-4">Vivantis</h2>
        <nav className="space-y-2">
          <a href="/dashboard" className="block">Dashboard</a>
          <a href="#" className="block">Moradores</a>
          <a href="#" className="block">Reservas</a>
          <a href="#" className="block">Ocorrências</a>
        </nav>
      </aside>
      <main className="flex-1 bg-gray-100">
        <header className="bg-white p-4 border-b border-gray-200 shadow-sm">
          <h1 className="text-lg font-medium">Painel</h1>
        </header>
        <section className="p-6">{children}</section>
      </main>
    </div>
  );
} 
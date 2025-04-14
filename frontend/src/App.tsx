import { Route, Routes, Navigate } from 'react-router-dom';
import LoginPage from './pages/Login';
import DashboardPage from './pages/Dashboard';
import { useAuthStore } from './store/auth';
import { ReactNode } from 'react';

function PrivateRoute({ children }: { children: ReactNode }) {
  const token = useAuthStore((state) => state.token);
  return token ? children : <Navigate to="/login" />;
}

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route
        path="/dashboard"
        element={
          <PrivateRoute>
            <DashboardPage />
          </PrivateRoute>
        }
      />
    </Routes>
  );
}

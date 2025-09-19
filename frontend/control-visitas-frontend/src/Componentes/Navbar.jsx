import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-blue-700 text-white px-6 py-3 flex justify-between items-center shadow">
      <h1 className="text-xl font-bold">Control de Visitas</h1>
      <div className="flex gap-6">
        <Link to="/" className="hover:underline">Home</Link>
        <Link to="/dashboard" className="hover:underline">Dashboard</Link>
        <Link to="/visitantes" className="hover:underline">Visitantes</Link>
      </div>
    </nav>
  );
}


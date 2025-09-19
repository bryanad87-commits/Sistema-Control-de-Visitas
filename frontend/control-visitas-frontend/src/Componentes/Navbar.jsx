import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-blue-600 shadow-md">
      <div className="container mx-auto flex justify-between items-center py-3 px-6">
        {/* Logo o título */}
        <h1 className="text-white text-xl font-bold">Control de Visitas</h1>

        {/* Enlaces */}
        <ul className="flex space-x-6 text-white font-medium">
          <li>
            <Link 
              to="/" 
              className="hover:text-yellow-300 transition-colors duration-300"
            >
              Inicio
            </Link>
          </li>
          <li>
            <Link 
              to="/dashboard" 
              className="hover:text-yellow-300 transition-colors duration-300"
            >
              Dashboard
            </Link>
          </li>
          <li>
            <Link 
              to="/visitantes" 
              className="hover:text-yellow-300 transition-colors duration-300"
            >
              Visitantes
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;

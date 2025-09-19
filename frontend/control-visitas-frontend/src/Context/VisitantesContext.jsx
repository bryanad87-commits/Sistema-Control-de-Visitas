import { createContext, useState } from "react";

export const VisitantesContext = createContext();

export function VisitantesProvider({ children }) {
  const [visitantes, setVisitantes] = useState([]);
  const [usuario, setUsuario] = useState(null);

  const agregarVisitante = (visitante) => {
    setVisitantes([...visitantes, visitante]);
  };

  const login = (nombreUsuario) => setUsuario(nombreUsuario);
  const logout = () => setUsuario(null);

  return (
    <VisitantesContext.Provider
      value={{ visitantes, agregarVisitante, usuario, login, logout }}
    >
      {children}
    </VisitantesContext.Provider>
  );
}

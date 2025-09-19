import { useContext } from "react"; 
import { VisitantesContext } from "../Context/VisitantesContext";

export default function Dashboard() {
  const { visitantes } = useContext(VisitantesContext);

  const usuario = localStorage.getItem("usuario") || "Invitado";

  const total = visitantes.length;
  const departamentosUnicos = [...new Set(visitantes.map(v => v.departamento))].length;
  const hoy = new Date().toLocaleDateString();
  const visitasHoy = visitantes.filter(v => v.fecha === hoy).length;

  return (
    <div className="max-w-5xl mx-auto p-6">
      <h2 className="text-2xl font-semibold mb-6">Dashboard</h2>
      <p className="text-lg mb-6">👋 Bienvenido, <span className="font-bold">{usuario}</span></p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded shadow text-center">
          <h3 className="text-lg font-semibold">Visitas de Hoy</h3>
          <p className="text-3xl font-bold text-blue-600">{visitasHoy}</p>
        </div>
        <div className="bg-white p-6 rounded shadow text-center">
          <h3 className="text-lg font-semibold">Total Visitantes</h3>
          <p className="text-3xl font-bold text-green-600">{total}</p>
        </div>
        <div className="bg-white p-6 rounded shadow text-center">
          <h3 className="text-lg font-semibold">Departamentos Visitados</h3>
          <p className="text-3xl font-bold text-purple-600">{departamentosUnicos}</p>
        </div>
      </div>
    </div>
  );
}

import { useContext } from "react";
import { VisitantesContext } from "../Context/VisitantesContext";

export default function Visitantes() {
  const { visitantes } = useContext(VisitantesContext);

  return (
    <div className="max-w-5xl mx-auto p-6">
      <h2 className="text-2xl font-semibold mb-6">Lista de Visitantes</h2>
      <div className="overflow-x-auto">
        <table className="w-full border border-gray-300 rounded shadow">
          <thead className="bg-blue-600 text-white">
            <tr>
              <th className="px-4 py-2">Nombre</th>
              <th className="px-4 py-2">DNI</th>
              <th className="px-4 py-2">Departamento</th>
              <th className="px-4 py-2">Fecha</th>
            </tr>
          </thead>
          <tbody>
            {visitantes.map((v, i) => (
              <tr key={i} className="border-t hover:bg-gray-100">
                <td className="px-4 py-2">{v.nombre}</td>
                <td className="px-4 py-2">{v.dni}</td>
                <td className="px-4 py-2">{v.departamento}</td>
                <td className="px-4 py-2">{v.fecha}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

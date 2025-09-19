// src/components/TicketModal.jsx
import { jsPDF } from "jspdf";
import jspdfBarcode from "jspdf-barcode";

export default function TicketModal({ visitante, visible, onClose }) {
  if (!visible || !visitante) return null;

  const { nombre, fecha, hora, codigo } = visitante;

  const descargarPDF = () => {
    const doc = new jsPDF();
    doc.setFontSize(16);
    doc.text("Ticket de Visita", 20, 20);
    doc.setFontSize(12);
    doc.text(`Visitante: ${nombre}`, 20, 40);
    doc.text(`Fecha: ${fecha}`, 20, 50);
    doc.text(`Hora: ${hora}`, 20, 60);
    doc.text(`Ticket #: ${codigo}`, 20, 70);

    // Código de barras
    jspdfBarcode(doc, codigo, {
      x: 20,
      y: 90,
      variant: "CODE128",
    });

    doc.save(`ticket_${codigo}.pdf`);
  };

  const imprimir = () => {
    const ventana = window.open("", "", "width=600,height=800");
    ventana.document.write("<html><head><title>Ticket</title></head><body>");
    ventana.document.write(`<h3>Ticket de Visita</h3>
      <p>Visitante: ${nombre}</p>
      <p>Fecha: ${fecha}</p>
      <p>Hora: ${hora}</p>
      <p>Ticket #: ${codigo}</p>
      <img src="https://barcode.tec-it.com/barcode.ashx?data=${codigo}&code=Code128&translate-esc=on" alt="barcode" />
    `);
    ventana.document.write("</body></html>");
    ventana.document.close();
    ventana.print();
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <h3>Ticket de Visita</h3>
        <p><b>Visitante:</b> {nombre}</p>
        <p><b>Fecha:</b> {fecha}</p>
        <p><b>Hora:</b> {hora}</p>
        <p><b>Código:</b> {codigo}</p>
        <div style={{ marginTop: "20px" }}>
          <button onClick={descargarPDF}>📄 Descargar PDF</button>
          <button onClick={imprimir}>🖨️ Imprimir</button>
          <button onClick={onClose}>❌ Cerrar</button>
        </div>
      </div>
    </div>
  );
}

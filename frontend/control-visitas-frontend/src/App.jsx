import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Inicio from "./Paginas/Home";
import Dashboard from "./Paginas/Dashboard";
import Visitantes from "./Paginas/Visitantes";
import Navbar from "./Componentes/Navbar";
import Home from "./Paginas/Home";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container mx-auto">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/visitantes" element={<Visitantes />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

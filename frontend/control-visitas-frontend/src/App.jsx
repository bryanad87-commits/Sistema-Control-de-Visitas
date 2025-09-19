import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./Componentes/Navbar";
import Home from "./Paginas/Home";
import Dashboard from "./Paginas/Dashboard";
import Visitantes from "./Paginas/Visitantes";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Navbar />
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

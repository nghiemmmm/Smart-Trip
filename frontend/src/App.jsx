import React from "react";
import './App.css';
import { Routes, Route } from 'react-router-dom';

import Home from './components/home'; 
import About from './components/About';
import Contact from './components/Contact';           // ✅ Bỏ comment
import ProtectedRoute from './components/ProtectedRoute'; // ✅ Sửa tên

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={
          <ProtectedRoute>                        // ✅ Sửa tên đúng
            <Contact />                           // ✅ Đảm bảo Contact tồn tại
          </ProtectedRoute>
        } />
      </Routes>
    </div>
  );
}

export default App;

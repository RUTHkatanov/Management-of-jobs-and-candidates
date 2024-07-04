import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Candidate from './candidate.jsx';
import Recruiting from './Recuring.jsx';
import Menu from './Menu.jsx'
import './App.css';

export const DataContext = React.createContext({});

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Menu />} />
        <Route path="/candidate" element={<Candidate />} />
        <Route path="/recuruiting" element={<Recruiting />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

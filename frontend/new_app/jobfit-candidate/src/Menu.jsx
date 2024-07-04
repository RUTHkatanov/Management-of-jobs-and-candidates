import React from 'react';
import { useNavigate } from 'react-router-dom';

function Menu() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center mt-4">
      <button 
        className="bg-blue-500 text-white p-2 rounded-md m-2"
        onClick={() => navigate('/candidate')}
      >
        Candidate
      </button>
      <button 
        className="bg-blue-500 text-white p-2 rounded-md m-2"
        onClick={() => navigate('/recuruiting')}
      >
        Recruiting
      </button>
    </div>
  );
}

export default Menu;
import React from 'react';

function Welcome({ nextStep }) {
  return (
    <div>
      <h1>Welcome</h1>
      <button onClick={nextStep}>Enter</button>
    </div>
  );
}

export default Welcome;

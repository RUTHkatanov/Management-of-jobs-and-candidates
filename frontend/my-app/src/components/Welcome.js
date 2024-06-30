import React from 'react';

function Welcome({ nextStep }) {
  return (
    <div>
      <h1>ברוך הבא!</h1>
      <button onClick={nextStep}>המשך</button>
    </div>
  );
}

export default Welcome;

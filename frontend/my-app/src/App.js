import React, { useState } from 'react';
import Welcome from './components/Welcome';
import UserForm from './components/UserForm';
import SuccessMessage from './components/SuccessMessage';

function App() {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    idNumber: ''
  });

  const nextStep = () => {
    setStep(step + 1);
  };

  const handleFormChange = (input) => (e) => {
    setFormData({ ...formData, [input]: e.target.value });
  };

  switch (step) {
    case 1:
      return <Welcome nextStep={nextStep} />;
    case 2:
      return (
        <UserForm 
          nextStep={nextStep}
          handleFormChange={handleFormChange}
          formData={formData}
        />
      );
    case 3:
      return <SuccessMessage />;
    default:
      return <Welcome nextStep={nextStep} />;
  }
}

export default App;

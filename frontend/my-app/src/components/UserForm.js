// components/UserForm.js
import React from 'react';

function UserForm({ nextStep, handleFormChange, formData }) {
  return (
    <div>
      <h2>הכנסת פרטי המשתמש</h2>
      <form>
        <label>
          שם פרטי:
          <input type="text" onChange={handleFormChange('firstName')} value={formData.firstName} />
        </label>
        <br />
        <label>
          שם משפחה:
          <input type="text" onChange={handleFormChange('lastName')} value={formData.lastName} />
        </label>
        <br />
        <label>
          ת.ז:
          <input type="text" onChange={handleFormChange('idNumber')} value={formData.idNumber} />
        </label>
        <br />
        <button type="button" onClick={nextStep}>שלח</button>
      </form>
    </div>
  );
}

export default UserForm;

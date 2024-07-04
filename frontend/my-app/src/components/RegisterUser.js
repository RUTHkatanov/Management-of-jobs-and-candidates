import React, { useState } from 'react';
import axios from 'axios';

const RegisterUser = () => {
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/register', formData)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="fullName" placeholder="שם מלא" onChange={handleChange} required />
      <input type="email" name="email" placeholder="אימייל" onChange={handleChange} required />
      <input type="password" name="password" placeholder="סיסמה" onChange={handleChange} required />
      <button type="submit">הירשם</button>
    </form>
  );
};

export default RegisterUser;

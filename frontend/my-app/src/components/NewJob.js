import React, { useState } from 'react';
import axios from 'axios';

const NewJob = () => {
  const [jobData, setJobData] = useState({
    jobTitle: '',
    jobDescription: '',
    jobRequirements: ''
  });

  const handleChange = (e) => {
    setJobData({ ...jobData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/new-job', jobData)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="jobTitle" placeholder="שם המשרה" onChange={handleChange} required />
      <textarea name="jobDescription" placeholder="תיאור המשרה" onChange={handleChange} required></textarea>
      <textarea name="jobRequirements" placeholder="דרישות בסיסיות" onChange={handleChange} required></textarea>
      <button type="submit">הוסף משרה</button>
    </form>
  );
};

export default NewJob;

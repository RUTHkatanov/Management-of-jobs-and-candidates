import React, { useState, useEffect } from 'react';

const NewJobPage = () => {
  const [questions, setQuestions] = useState([]);
  const [formData, setFormData] = useState({});

  useEffect(() => {
    // Fetch questions from backend API
    fetch('https://your-backend-api.com/questions')
      .then(response => response.json())
      .then(data => setQuestions(data))
      .catch(error => console.error('Error fetching questions:', error));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Submit form data to backend API
    fetch('https://your-backend-api.com/submit-application', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => console.log('Success:', data))
      .catch(error => console.error('Error submitting form:', error));
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">New Job Application</h1>
      <form className="bg-white p-6 rounded-lg shadow-md" onSubmit={handleSubmit}>
        <h2 className="text-2xl font-semibold mb-4">Personal Details</h2>

        <label className="block mb-2">
          Full Name:
          <input
            type="text"
            name="fullName"
            className="w-full border border-gray-300 p-2 rounded mt-1"
            onChange={handleChange}
          />
        </label>

        <label className="block mb-2">
          Email:
          <input
            type="email"
            name="email"
            className="w-full border border-gray-300 p-2 rounded mt-1"
            onChange={handleChange}
          />
        </label>

        <label className="block mb-2">
          Phone Number:
          <input
            type="text"
            name="phoneNumber"
            className="w-full border border-gray-300 p-2 rounded mt-1"
            onChange={handleChange}
          />
        </label>

        <h2 className="text-2xl font-semibold my-4">Resume Details</h2>

        <label className="block mb-2">
          Education:
          <textarea
            name="education"
            className="w-full border border-gray-300 p-2 rounded mt-1"
            onChange={handleChange}
          ></textarea>
        </label>

        <label className="block mb-2">
          Work Experience:
          <textarea
            name="workExperience"
            className="w-full border border-gray-300 p-2 rounded mt-1"
            onChange={handleChange}
          ></textarea>
        </label>

        <label className="block mb-2">
          Skills:
          <textarea
            name="skills"
            className="w-full border border-gray-300 p-2 rounded mt-1"
            onChange={handleChange}
          ></textarea>
        </label>

        <h2 className="text-2xl font-semibold my-4">Additional Questions</h2>

        {questions.map((question, index) => (
          <label key={index} className="block mb-2">
            {question.text}
            <textarea
              name={`question_${index}`}
              className="w-full border border-gray-300 p-2 rounded mt-1"
              onChange={handleChange}
            ></textarea>
          </label>
        ))}

        <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded mt-4">
          Submit 
        </button>
      </form>
    </div>
  );
};

export default NewJobPage;

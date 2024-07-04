import React from 'react';

const ViewJobsPage = () => {
  const jobs = [
    {
      name: 'Software Developer',
      description: 'Develop and maintain software applications.',
      criteria: 'BSc in Computer Science, 2 years of experience, knowledge of React and Node.js.',
    },
    {
      name: 'Project Manager',
      description: 'Manage projects from inception to completion.',
      criteria: 'PMP certification, 5 years of experience, excellent communication skills.',
    },
    // Add more job objects here as needed
  ];

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">View Jobs</h1>
      <table className="min-w-full bg-white rounded-lg shadow-md">
        <thead>
          <tr>
            <th className="py-2 px-4 border-b-2 border-gray-300">Job Name</th>
            <th className="py-2 px-4 border-b-2 border-gray-300">Description</th>
            <th className="py-2 px-4 border-b-2 border-gray-300">Criteria</th>
          </tr>
        </thead>
        <tbody>
          {jobs.map((job, index) => (
            <tr key={index}>
              <td className="py-2 px-4 border-b border-gray-300">{job.name}</td>
              <td className="py-2 px-4 border-b border-gray-300">{job.description}</td>
              <td className="py-2 px-4 border-b border-gray-300">{job.criteria}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ViewJobsPage;

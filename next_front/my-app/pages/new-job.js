import React from 'react';

const NewJobPage = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">New Job Posting</h1>
      <form className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Job Details</h2>

        <label className="block mb-2">
          Job Name:
          <input type="text" className="w-full border border-gray-300 p-2 rounded mt-1" />
        </label>

        <label className="block mb-2">
          Job Description:
          <textarea className="w-full border border-gray-300 p-2 rounded mt-1" placeholder="Brief job description"></textarea>
        </label>

        <h2 className="text-2xl font-semibold my-4">Basic Criteria</h2>

        <label className="block mb-2">
          Minimum Qualifications:
          <textarea className="w-full border border-gray-300 p-2 rounded mt-1" placeholder="List the minimum qualifications"></textarea>
        </label>

        <label className="block mb-2">
          Preferred Skills:
          <textarea className="w-full border border-gray-300 p-2 rounded mt-1" placeholder="List the preferred skills"></textarea>
        </label>

        <label className="block mb-2">
          Experience Required:
          <textarea className="w-full border border-gray-300 p-2 rounded mt-1" placeholder="Describe the experience required"></textarea>
        </label>

        <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded mt-4">
          Post Job
        </button>
      </form>
    </div>
  );
};

export default NewJobPage;

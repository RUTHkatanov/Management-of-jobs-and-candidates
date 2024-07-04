import React from 'react';
import Link from 'next/link';

const HomePage = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Welcome to the Main Page</h1>
      <p className="text-lg mb-4">Click on the buttons below to navigate:</p>

      <div className="flex flex-col items-center space-y-4">
        <Link href="/register"
          className="btn px-4 py-2 bg-blue-500 text-white rounded relative">
          Register User
          <span className="absolute inset-0 border border-white rounded pointer-events-none"></span>

        </Link>

        <Link href="/new-job" className="btn px-4 py-2 bg-blue-500 text-white rounded relative">
            Create New Job
            <span className="absolute inset-0 border border-white rounded pointer-events-none"></span>
         </Link>

        <Link href="/view-jobs"  className="btn px-4 py-2 bg-blue-500 text-white rounded relative">
            View Jobs
            <span className="absolute inset-0 border border-white rounded pointer-events-none"></span>
        </Link>
      </div>
    </div>
  );
};

export default HomePage;

import React from 'react';
import Link from 'next/link';

const HomePage = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Welcome to the Main Page</h1>
      <p className="text-lg mb-4">Click on the buttons below to navigate:</p>

      <div className="grid grid-cols-1 gap-4">
        <Link href="/register">
          <button className="btn">Register User</button>
        </Link>

        <Link href="/upload-resume">
          <button className="btn">Upload Resume</button>
        </Link>

        <Link href="/new-job">
          <button className="btn">Create New Job</button>
        </Link>

        <Link href="/view-jobs">
          <button className="btn">View Jobs</button>
        </Link>

        <Link href="/resume-form">
          <button className="btn">Resume Form</button>
        </Link>
      </div>
    </div>
  );
};

export default HomePage;

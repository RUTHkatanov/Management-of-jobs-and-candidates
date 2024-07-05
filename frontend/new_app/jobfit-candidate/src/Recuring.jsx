import React, { useState, useEffect } from 'react';
import axios from "axios"

function Recruiting() {
    const [jobs, setJobs] = useState([]);
    const [jobName, setJobName] = useState('');
    const [jobDescription, setJobDescription] = useState('');
    const [jobRequirements, setJobRequirements] = useState('');

    useEffect(() => {
        fetchJobs();
    }, []);

    const fetchJobs = async () => {
        try {
            const response = await axios.get('http://localhost:8001/api/v1/tasks');
            setJobs(response.data);
        } catch (error) {
            console.error("Error fetching jobs: ", error);
        }
    };

    const handleCreateJob = async () => {
        try {
            const response = await axios.post('http://localhost:8001/api/v1/tasks', { title: jobName, description: jobDescription });
            setJobs([...jobs, response.data]);
            setJobName('');
            setJobDescription('');
            setJobRequirements('');
        } catch (error) {
            console.error("Error creating job: ", error);
        }
    };

    const handleUpdateJob = (index) => {
        const updatedJobs = jobs.map((job, i) =>
            i === index ? { ...job, title: jobName, description: jobDescription } : job
        );
        setJobs(updatedJobs);
        setJobName('');
        setJobDescription('');
        setJobRequirements('');
    };

    const handleDeleteJob = async (index, id) => {
        try {
            await axios.delete(`http://localhost:8001/api/v1/tasks/${id}`);
            const updatedJobs = jobs.filter((_, i) => i !== index);
            setJobs(updatedJobs);
        } catch (error) {
            console.error("Error deleting job: ", error);
        }
    };

    const handleSelectJob = (index) => {
        const selectedJob = jobs[index];
        setJobName(selectedJob.title);
        setJobDescription(selectedJob.description);
        setJobRequirements(selectedJob.requirements);
    };

    return (
        <div className="flex flex-col items-center mt-4">
            <h1 className="text-2xl mb-4">Job management</h1>
            <div className="bg-purple-200 p-4 rounded-md w-1/2 mb-4">
                <h2 className="text-xl mb-2">Create job</h2>
                <input
                    type="text"
                    placeholder="Job name"
                    value={jobName}
                    onChange={(e) => setJobName(e.target.value)}
                    className="mb-2 p-2 border rounded-md w-full"
                />
                <textarea
                    placeholder="Job description"
                    value={jobDescription}
                    onChange={(e) => setJobDescription(e.target.value)}
                    className="mb-2 p-2 border rounded-md w-full"
                />
                <textarea
                    placeholder="Job requirements"
                    value={jobRequirements}
                    onChange={(e) => setJobRequirements(e.target.value)}
                    className="mb-2 p-2 border rounded-md w-full"
                />
                <button
                    onClick={handleCreateJob}
                    className="bg-purple-900 text-white p-2 rounded-md mr-2"
                >
                    Create job
                </button>
            </div>

            <div className="bg-purple-200 p-4 rounded-md w-1/2 mb-4">
                <h2 className="text-xl mb-2">List of jobs</h2>
                {jobs.length === 0 ? (
                    <p>No jobs available</p>
                ) : (
                    jobs.map((job, index) => (
                        <div key={index} className="mb-4 p-2 border rounded-md">
                            <h3 className="text-lg">{job.title}</h3>
                            <p>{job.description}</p>
                            <p>{job.requirements}</p>
                            <button
                                onClick={() => handleSelectJob(index)}
                                className="bg-blue-500 text-white p-2 rounded-md mr-2"
                            >
                                Edit
                            </button>
                            <button
                                onClick={() => handleDeleteJob(index, job._id)}
                                className="bg-red-500 text-white p-2 rounded-md"
                            >
                                Delete
                            </button>
                            <button
                                onClick={() => handleUpdateJob(index)}
                                className="bg-yellow-500 text-white p-2 rounded-md"
                            >
                                Update
                            </button>
                        </div>
                    ))
                )}
            </div>

            <div className="bg-purple-200 p-4 rounded-md w-1/2 mb-4">
                <h2 className="text-xl mb-2">Characterization of requirements for the model</h2>
                <textarea
                    placeholder="Requirements for the model"
                    value={jobRequirements}
                    onChange={(e) => setJobRequirements(e.target.value)}
                    className="mb-2 p-2 border rounded-md w-full"
                />
                <button
                    onClick={handleCreateJob}
                    className="bg-purple-900 text-white p-2 rounded-md"
                >
                    Publish
                </button>
            </div>
        </div>
    );
}

export default Recruiting;

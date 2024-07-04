import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ViewJobs = () => {
  const [jobs, setJobs] = useState([]);
  const [selectedJob, setSelectedJob] = useState(null);

  useEffect(() => {
    axios.get('/api/jobs')
      .then(response => {
        setJobs(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const handleJobClick = (job) => {
    setSelectedJob(job);
  };

  return (
    <div>
      <ul>
        {jobs.map(job => (
          <li key={job.id} onClick={() => handleJobClick(job)}>
            {job.jobTitle}
          </li>
        ))}
      </ul>
      {selectedJob && (
        <div>
          <h2>{selectedJob.jobTitle}</h2>
          <p>{selectedJob.jobDescription}</p>
          <p>{selectedJob.jobRequirements}</p>
          <h3>מועמדים מתאימים:</h3>
          <ul>
            {selectedJob.candidates.map(candidate => (
              <li key={candidate.id}>
                {candidate.name} - {candidate.matchPercentage}%
                <a href={candidate.cvLink}>הורד קורות חיים</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ViewJobs;

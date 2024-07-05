import React, { useRef, useState } from 'react';
import axios from 'axios';
import { Loader } from '@mantine/core';

function Candidate() {
  const fileInputRef = useRef(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [matchScore, setMatchScore] = useState(null);
  const [loading, setLoading] = useState(false)
  const handleFileUpload = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    // Generate a random match score between 1 and 3
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true)
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await axios.post('/api/candidate/file', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        setMatchScore(response.data);

        console.log(response.data);
      } catch (error) {
        console.error(error);
      }finally{
        setLoading(false)
      }
    }
  };

  const handleCancel = () => {
    setSelectedFile(null);
    setMatchScore(null);
  };

  return (
    <>
      {/* <MantineProvider theme={theme}> */}
        <div className="flex flex-col items-center mt-4">
          <div className="absolute left-1/2 transform -translate-x-1/2 text-white">
            JobFit
          </div>
          <div className="min-h-40 w-full p-20 bg-purple-500">
            <div className="bg-purple-700 p-2 rounded-xl text-3xl text-center text-white">
              Job details
            </div>
          </div>
          <div className="text-3xl mt-4 mb-2 text-purple-700">
            Submitting a nomination
          </div>
          <form className="bg-purple-200 rounded-md p-3 text-center">
            <input
              type="file"
              accept=".pdf"
              ref={fileInputRef}
              style={{ display: 'none' }}
              onChange={handleFileChange}
            />
            <button
              type="button"
              className="bg-purple-700 text-white p-2 rounded-md"
              onClick={handleFileUpload}
            >
              Upload CV
            </button>
            {/* {loading &&  <Loader color="blue" />} */}
            {selectedFile && (
              <div className="mt-4">
                <span className="block text-gray-800 mb-2">{selectedFile.name}</span>
                <div className="bg-white p-2 rounded-md mb-4">
                {matchScore &&  <span className="block text-gray-800 text-center">Initial candidacy matching score: {matchScore}</span>}
                </div>
                <div className="flex justify-center space-x-4">
                  <button
                    type="button"
                    className="bg-green-500 text-white p-2 rounded-md ml-8"
                    onClick={handleSubmit}
                  >
                    Submit
                  </button>
                  <button
                    type="button"
                    className="bg-red-500 text-white p-2 rounded-md"
                    onClick={handleCancel}
                  >
                    Cancel
                  </button>
                </div>
              </div>
            )}
          </form>
          </div>
      {/* </MantineProvider> */}
    </>
  );
}

export default Candidate;

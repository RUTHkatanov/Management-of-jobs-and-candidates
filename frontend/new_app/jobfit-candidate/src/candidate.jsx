import React, { useRef, useState } from 'react';

function Candidate() {
  const fileInputRef = useRef(null);
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileUpload = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = () => {
    if (selectedFile) {
      // Handle file submission logic here
      console.log('Submitting file:', selectedFile.name);
      // Clear selected file after submission if needed
      setSelectedFile(null);
    }
  };

  const handleCancel = () => {
    setSelectedFile(null);
  };

  return (
    <>
      <div className="flex flex-col items-center mt-4">
        <div className="absolute left-1/2 transform -translate-x-1/2 text-white">
          JobFit
        </div>
        <div className="min-h-40 w-full p-20 bg-purple-500">
          <div className="bg-purple-700 p-2 rounded-xl text-3xl text-center text-white">
            פרטי משרה
          </div>
        </div>
        <div className="text-3xl mt-4 mb-2 text-purple-700">
          חלק למועמד
        </div>
        <form className="bg-purple-200 rounded-md p-3">
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
            העלה קובץ קורות חיים
          </button>
          {selectedFile && (
            <div className="mt-2">
              <span className="block text-gray-800">{selectedFile.name}</span>
              <div className="mt-2">
                <button
                  type="button"
                  className="bg-green-500 text-white p-2 rounded-md mr-2"
                  onClick={handleSubmit}
                >
                  הגש
                </button>
                <button
                  type="button"
                  className="bg-red-500 text-white p-2 rounded-md"
                  onClick={handleCancel}
                >
                  בטל הגשה
                </button>
              </div>
            </div>
          )}
        </form>
      </div>
    </>
  );
}

export default Candidate;

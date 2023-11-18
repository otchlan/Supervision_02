import React, { useState } from 'react';

import '../index.css'

const TextInput = () => {
  const [url, setUrl] = useState('');

  const handleInputChange = (e) => {
    setUrl(e.target.value);
  };

  const handleSendButtonClick = () => {
    // Add your logic for handling the link here
    console.log('Link sent:', url);
  };

  return (
    <div className="container mx-auto mt-4 p-6 bg-red-100 rounded-md shadow-md">
      <div className="flex items-center">
        <input
          type="text"
          className="border rounded-l p-3 w-64 focus:outline-none text-black"
          placeholder="Paste link here"
          value={url}
          onChange={handleInputChange}
        />
        <button
          className="bg-blue-500 text-white p-3 rounded-r hover:bg-blue-600 focus:outline-none"
          onClick={handleSendButtonClick}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default TextInput;

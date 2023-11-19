import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGlobe } from '@fortawesome/free-solid-svg-icons';

const Input = ({ label, onEnter, ...props }) => {
  const [inputValue, setInputValue] = useState('');

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      if(onEnter) {
        onEnter(e.target.value);
      }

      setInputValue('');  
    }
  };

  const handleChange = (e) => {
    setInputValue(e.target.value);
  };

  return (
    <div className="flex flex-col space-y-1 w-full justify-center items-center mt-4">
      <label className="text-sm font-semibold text-gray-600">
        <FontAwesomeIcon icon={faGlobe} /> &nbsp;
        {label}
      </label>
      <input
        className="w-1/2 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        value={inputValue}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
        {...props}
      />
     
    </div>
  );
};

export default Input;

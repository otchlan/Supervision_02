import React, { useState } from 'react';
import '../index.css';

const LinksList = ({data}) => {
 
  return (
    <ul className="bg-gray-100 rounded-md shadow-md p-4">
      {data.map((item, index) => (
        <li
          key={index}
          className="flex items-center justify-between border-b border-gray-200 py-2 hover:bg-gray-200 transition-all"
        >
          <span className="text-gray-700">{item}</span>
          <button className="text-red-500 hover:text-red-700">Delete</button>
        </li>
      ))}
    </ul>
  );
};

export default LinksList;

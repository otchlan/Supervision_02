import React, { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFolder } from '@fortawesome/free-solid-svg-icons';

const FolderPicker = () => {
  const [folderPath, setFolderPath] = useState('');

  useEffect(() => {
    const savedPath = localStorage.getItem('folderPath');
    if (savedPath) {
      setFolderPath(savedPath);
    }
  }, []);

  const handlePathChange = (e) => {
    const newPath = e.target.value;
    setFolderPath(newPath);
    localStorage.setItem('folderPath', newPath);
  };

  return (
    <div className="flex justify-center items-center w-full divide-y">
      <div className="p-4 ">
        <FontAwesomeIcon icon={faFolder}></FontAwesomeIcon> &nbsp; 
        <span>Podaj ścieżke</span>
        <input
          type="text"
          value={folderPath}
          onChange={handlePathChange}
          placeholder="Wpisz ścieżkę folderu"
          className="border border-gray-300 rounded py-2 px-4 ml-2 "
        />
        {folderPath && <p className="mt-2 text-gray-700 w-full">Wybrana ścieżka: {folderPath}</p>}
      </div>
    </div>
  );
};

export default FolderPicker;

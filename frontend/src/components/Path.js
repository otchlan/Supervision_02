import React, { useState, useEffect } from 'react';

const FolderPicker = () => {
  const [folderPath, setFolderPath] = useState('');

  useEffect(() => {
    const savedPath = localStorage.getItem('folderPath');
    if (savedPath) {
      setFolderPath(savedPath);
    }
  }, []);

  const handlePathChange = (e) => {
    setFolderPath(e.target.value);
    localStorage.setItem('folderPath', e.target.value);
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="p-4 max-w-xs mx-auto">
      <input
          type="text"
          value={folderPath}
          onChange={handlePathChange}
          placeholder="Wklej ścieżkę folderu tutaj"
          className="block w-full text-sm p-2 border border-gray-300 rounded"
        />
        {folderPath && <p className="mt-2 text-gray-700">Wybrana ścieżka: {folderPath}</p>}
      </div>
    </div>
  );
};

export default FolderPicker;

import React from 'react';

const BusyDialog = ({ isOpen }) => {
  if (!isOpen) return null;

  return (
    <div className=" fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50" style={{top: "-5%"}}>
      <div className="bg-white p-6 rounded-lg shadow-lg flex flex-col items-center" style={{ transform: 'translate(-50%, -50%)', position: 'fixed', top: '50%', left: '50%' }}>
        {/* Spinner */}
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
        
        <h2 className="text-lg font-semibold mt-4">Proszę czekać...</h2>
        <p className="text-gray-500">Trwa analizowanie danych.</p>
      </div>
    </div>
  );
};

export default BusyDialog;

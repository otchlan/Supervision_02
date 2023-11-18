import React, { useState, useEffect } from 'react';

const TabsMenu = ({ components }) => {
  const [selectedComponentIndex, setSelectedComponentIndex] = useState(() => {
    const storedIndex = parseInt(localStorage.getItem('selectedComponentIndex'), 10);
    return !isNaN(storedIndex) && storedIndex >= 0 && storedIndex < components.length
      ? storedIndex
      : 0;
  });

  useEffect(() => {
    localStorage.setItem('selectedComponentIndex', selectedComponentIndex.toString());
  }, [selectedComponentIndex]);

  const handleComponentChange = (index) => {
    setSelectedComponentIndex(index);
  };

  const selectedComponent = components[selectedComponentIndex];

  return (
    <div className="flex">
      {/* Menu on the right */}
      <div className="flex-1 mr-8">
        <h2 className="text-xl font-bold mb-4">Wybierz firmę:</h2>
        <ul className="list-none p-0">
          {components.map((Component, index) => (
            <li
              key={Component.id}
              onClick={() => handleComponentChange(index)}
              className={`cursor-pointer py-2 px-4 mb-2 rounded ${
                selectedComponentIndex === index
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-300 text-gray-800'
              } hover:bg-blue-400 transition-colors duration-300`}
              style={{ backgroundColor: selectedComponentIndex === index ? '#3182ce' : '#cbd5e0' }}
            >
              {Component.displayName || Component.name || `Component ${Component.id}`}
            </li>
          ))}
        </ul>
      </div>

      {/* Display selected component on the left */}
      <div className="flex-2">
        <h2 className="text-xl font-bold mb-4">Selected Component</h2>
        <div className="p-4 border rounded bg-gray-100">
          {selectedComponent && (
            React.isValidElement(selectedComponent) ? (
              selectedComponent
            ) : (
              React.createElement(selectedComponent)
            )
          )}
        </div>
      </div>
    </div>
  );
};

export default TabsMenu;

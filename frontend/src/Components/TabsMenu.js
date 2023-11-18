import React, { useState, useEffect } from 'react';

const TabsMenu = ({ components }) => {
  const [selectedComponent, setSelectedComponent] = useState(() => {
    const storedComponent = localStorage.getItem('selectedComponent');
    return storedComponent && components.includes(storedComponent)
      ? storedComponent
      : (components[0] || null);
  });

  useEffect(() => {
    localStorage.setItem('selectedComponent', selectedComponent);
  }, [selectedComponent]);

  const handleComponentChange = (component) => {
    setSelectedComponent(() => component);
  };

  return (
    <div className="flex">
      {/* Menu on the right */}
      <div style={{ flex: 1, marginRight: '20px' }}>
        <h2 className="text-xl font-bold mb-4">Wybierz firmę:</h2>
        <ul className="list-none p-0">
          {components.map((Component, index) => (
            <li
              key={index}
              onClick={() => handleComponentChange(Component)}
              className={`cursor-pointer py-2 px-4 mb-2 rounded ${
                selectedComponent === Component
                  ? 'bg-blue-500 text-black'
                  : 'bg-gray-200 text-black'
              } hover:bg-blue-400`}
            >
              {Component.displayName || Component.name || `Component ${index + 1}`}
            </li>
          ))}
        </ul>
      </div>

      {/* Display selected component on the left */}
      <div style={{ flex: 2 }}>
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

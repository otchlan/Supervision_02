import React from 'react';


function extractLastSubpath(url) {
    // Używamy obiektu URL, aby upewnić się, że rozwiązanie działa poprawnie dla różnych formatów URL
    const urlObject = new URL(url);
    const pathname = urlObject.pathname;
  
    // Rozdzielamy ścieżkę na części i zwracamy ostatnią z nich
    const parts = pathname.split('/');
    return parts[parts.length - 1];
  }
  
  

const Files = ({ items, onCheck }) => {
  return (
    <div className="mt-2 flex flex-col space-y-4 justify-center items-center">
      {items.map((item, index) => (
        <span
          key={index}
          href={item.href}
          className="file-list-bg p-2 w-1/2 rounded cursor-pointer"
          onClick={() => onCheck(item.href)}
        >
          {extractLastSubpath(item.href)}
          
        </span>
      ))}
    </div>
  );
};

export default Files;

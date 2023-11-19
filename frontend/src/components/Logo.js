import React from 'react';

import logo from "../images/logo.svg"

const Logo = ({ url }) => {
  return (
    <div className="flex justify-center items-center">
      <img 
        src={logo}
        heght="100"
        alt="Wyświetlane zdjęcie"
        className=""
      />
    </div>
  );
};

export default Logo;

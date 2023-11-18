import React from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFaceDizzy } from '@fortawesome/free-solid-svg-icons';


const Missing = ({text='brak'}) => {
  return (
    <p className="mt-4 text-sm text-gray-500">
        <FontAwesomeIcon icon={faFaceDizzy}></FontAwesomeIcon> &nbsp; 
        {text}
    </p>
  );
};

export default Missing;

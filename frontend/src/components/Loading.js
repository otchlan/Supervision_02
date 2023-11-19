import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons';


const Loading = ({text}) => {
    return (
        <div className="flex flex-col justify-center items-center mt-8">
            <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-yellow-500"></div>
            <span className="mt-4">
                <FontAwesomeIcon icon={faMagnifyingGlass}></FontAwesomeIcon> &nbsp;
                {text}
            </span>
        </div>
    );
}

export default Loading;

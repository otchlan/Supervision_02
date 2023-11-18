import React from 'react';

const Loading = ({text}) => {
    return (
        <div className="flex flex-col justify-center items-center mt-4">
            <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-yellow-500"></div>
            <span className="mt-4">{text}</span>
        </div>
    );
}

export default Loading;

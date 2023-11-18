import React from 'react';

const MainPage = ({ children }) => {
    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">Hello!</h1>
            {children}
        </div>
    );
}

export default MainPage;

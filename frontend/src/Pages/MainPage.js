import React, { useEffect, useState } from 'react';

import Companies from '../components/Companies';
import Output from '../components/Output';


const MainPage = ({ children }) => {
    let [companies, setCompanies] = useState([])

    const handleOnAnalyze = (companies) => [
        setCompanies(companies)
    ]
 
    return (
        <div className=" w-full h-full  mx-auto p-4">
            <h1 className="pb-2 pt-2 text-4xl font-bold text-bg rounded shadow-xl">SFCR Lighter</h1>   
            <Companies onAnalyze={handleOnAnalyze}></Companies>

            {companies.map(company =>
                    <Output company={company} ></Output>
                )
            }
        </div>
    );
}

export default MainPage;

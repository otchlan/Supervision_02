import React, { useEffect, useState } from 'react';

import { sitemap, analyze } from '../util/request';
import Companies from '../components/Companies';
import Output from '../components/Output';
import Loading from '../components/Loading';
import Path from '../components/Path';


const MainPage = ({ children }) => {
    let [company, setCompany] = useState(null)

    const handleOnCompany = (company) => [
        setCompany(company)
    ]
  
    return (
        <div className=" w-full h-full  mx-auto p-4">
            < h1 className="text-3xl font-bold underline">
                Lynx
            </h1>            
            <Companies onCompany={handleOnCompany}></Companies>
            <Output company={company} ></Output>
        </div>
    );
}

export default MainPage;

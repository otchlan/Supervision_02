import React, {useEffect, useState} from 'react';

import { COMPANIES } from '../util/request';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHouseChimneyCrack } from '@fortawesome/free-solid-svg-icons';


function Companies({onCompany}) {
    let [companies, setCompanies] = useState([])

    useEffect(() => {
         fetch(COMPANIES, {
            method: 'GET', 
            headers: {
              'Content-Type': 'application/json' 
            },
        }).then(response => {
            return response.json()
        }).then(jData => {
            setCompanies(jData["companies"])
        })
    }, [])


  return (
    <div className="mt-2">   
     <FontAwesomeIcon icon={faHouseChimneyCrack}></FontAwesomeIcon> &nbsp; 
        <span>Zakłady</span>     
        <div class="flex flex-wrap justify-center mt-1">
            {companies.map((company, index) => (
            <div key={index} onClick={() => {
                onCompany(company)
            }}>
<span class="bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-purple-900 dark:text-purple-300 hover:cursor-pointer hover:bg-purple-200 dark:hover:bg-purple-800">
                {company.name}
                    </span>
            </div>
        ))}
        </div>
    </div>
  );
};

export default Companies;

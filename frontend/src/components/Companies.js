import React, { useEffect, useState } from 'react';
import { useSprings, animated, config } from 'react-spring';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHouseChimneyCrack, faSearch } from '@fortawesome/free-solid-svg-icons';
import { COMPANIES } from '../util/request';


function Companies({ onAnalyze }) {
    const [companies, setCompanies] = useState([]);
    const [selectedCompanies, setSelectedCompanies] = useState([]);

    useEffect(() => {
        fetch(COMPANIES, {
            method: 'GET', 
            headers: {
              'Content-Type': 'application/json' 
            },
        }).then(response => {
            return response.json();
        }).then(jData => {
            setCompanies(jData["companies"]);
        });
    }, []);

    const toggleCompany = (company) => {
        if (selectedCompanies.includes(company)) {
            setSelectedCompanies(selectedCompanies.filter(c => c !== company));
        } else {
            setSelectedCompanies([...selectedCompanies, company]);
        }
    };

    const springs = useSprings(
        companies.length,
        companies.map((_, index) => ({
            from: { opacity: 0, transform: 'scale(0)' },
            to: { opacity: 1, transform: 'scale(1)' },
            delay: index * 100,
            config: { ...config.wobbly, tension: 150, friction: 17 }
        }))
    );

    return (
        <div className="mt-2">   
            <FontAwesomeIcon icon={faHouseChimneyCrack}></FontAwesomeIcon> &nbsp; 
            <span>Zakłady</span>     
            <div className="flex flex-wrap justify-center mt-1">
                {springs.map((props, index) => {
                    const company = companies[index];
                    const isSelected = selectedCompanies.includes(company);
                    return (
                        <animated.div 
                            key={company.id} 
                            style={props} 
                            onClick={() => toggleCompany(company)}>
                            <span 
                                className={`text-xs font-medium me-2 px-2.5 py-0.5 rounded hover:cursor-pointer ${
                                    isSelected ? 'bg-green-300 text-green-800' : 'bg-purple-100 text-purple-800'
                                }`}>
                                {company.name}
                            </span>
                        </animated.div>
                    );
                })}
            </div>
            <button 
                disabled={selectedCompanies.length === 0} 
                onClick={() => onAnalyze(selectedCompanies)} 
                className={`mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ml-4 
                            ${selectedCompanies.length === 0 ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-700'}`}>
                <FontAwesomeIcon icon={faSearch}></FontAwesomeIcon> &nbsp; 
                Szukaj
            </button>

        </div>
    );
}

export default Companies;

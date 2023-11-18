import React, { useEffect, useState } from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFile } from '@fortawesome/free-solid-svg-icons';

import { sitemap, analyze } from '../util/request';
import Files from './Files';

import Loading from './Loading';
import Missing from './Missing';


const Output = ({company}) => {
    let [output, setOutput] = useState(null)
    let [processing, setProcessing] = useState(false)
    
    const getOutput = () => {
        if (company === null) return

        setProcessing(true)
        setOutput(null)

        sitemap(company.url).then(jData => {
            setOutput(jData.links)
            setProcessing(false)
        })
    }

    useEffect(getOutput, [company])

    const handleOnCheck = (file) => {
        analyze(file).then(jData => {
            console.log(jData)
        })
    }

    if (company === null) return null

    return (
        <div className="mt-4">
            <h2>
                <FontAwesomeIcon icon={faFile}></FontAwesomeIcon> &nbsp; 
                Wyniki SFCR dla 
                <span class="ms-1 font-bold text-yellow-500">
                {company.name}
                </span>
            </h2>
            {output != null &&    
                <span className="mt-4">
                    <Files items={output} onCheck={handleOnCheck}></Files>
                </span>
            }

            {processing &&
                <Loading text="Szukam..."></Loading>
            }

            {output !== null && output.length === 0 &&
                <Missing text="Nie udało się znaleźć"></Missing>
            }
            
        </div>
    );
}

export default Output;

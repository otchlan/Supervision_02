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
        analyze({
            company: company,
            file: file,
            path: localStorage.setItem('folderPath', "")
        }).then(jData => {
            console.log(jData)
        })
    }

    if (company === null) return null

    return (
        <div className="mt-4">
             {output != null && 
             <> 
                <h2>
                    <FontAwesomeIcon icon={faFile}></FontAwesomeIcon> &nbsp; 
                    Wyniki SFCR dla 
                    <span class="ms-1 font-bold text-yellow-500">
                    {company.name}
                    <span class="inline-flex me-1 items-center justify-center w-4 h-4 ms-2 p-2 text-xs font-semibold text-blue-800 bg-blue-200 rounded-full">
                        {output.length}
                    </span>
                    </span>
                </h2>
             
                <span className="mt-4 divide-y">
                    <Files items={output} onCheck={(file) => handleOnCheck(file)}></Files>
                </span>
                </>
            }

            {processing &&
                <Loading text={`Analizuję ${company.name}`}></Loading>
            }

            {output !== null && output.length === 0 &&
                <Missing text="Wygląda na to, że ta firma nie udostępniła swoich sprawozdań "></Missing>
            }
            
        </div>
    );
}

export default Output;

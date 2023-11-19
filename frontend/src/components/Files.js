import React, {useState} from 'react';

import { useSprings, animated } from 'react-spring';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFilePdf, faCodeCompare, faCog } from '@fortawesome/free-solid-svg-icons';
import BusyDialog from '../dialog/BusyDialog';


function extractLastSubpath(url) {
    const urlObject = new URL(url);
    const pathname = urlObject.pathname;
  
    const parts = pathname.split('/');
    return parts[parts.length - 1];
  }
  
  const File = ({ item, index, onCheck, onAnalyze, isChecked }) => {
    return (
      <div className={`relative flex items-center justify-between p-2 w-full rounded ${isChecked ? 'bg-blue-100' : ''}`}>
        <div className="flex items-center">
          <input
            type="checkbox"
            checked={isChecked}
            onChange={() => onCheck(item)}
            className="mr-2"
          />
          <FontAwesomeIcon icon={faFilePdf} color="white" className="ps-2"></FontAwesomeIcon>
          <span key={index} href={item.href} className="ml-2">
            {extractLastSubpath(item.href)}
          </span>
        </div>
        <button onClick={() => onAnalyze(item)} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded text-xs">
          <FontAwesomeIcon icon={faCog} /> Analizuj
        </button>
      </div>
    );
  };
  

  const Files = ({ items }) => {
    const [selectedItems, setSelectedItems] = useState([]);
    let [processing, setProcessing] = useState(false)
  
    const handleCheck = (item) => {
      if (selectedItems.includes(item)) {
        setSelectedItems(selectedItems.filter(i => i !== item));
      } else {
        setSelectedItems([...selectedItems, item]);
      }
    };

    const handleAnalyze = (item) => {
        setProcessing(true)
        setTimeout(() => {
            setProcessing(false)
        }, 2500)
    }
  
    const springs = useSprings(
      items.length,
      items.map((_, index) => ({
        from: { opacity: 0, transform: 'translateY(-20px)' },
        to: { opacity: 1, transform: 'translateY(0)' },
        delay: index * 100,
        config: { tension: 170, friction: 14 }
      }))
    );
  
    return (
      <div className="mt-2 flex flex-col space-y-4 justify-center items-center">
        {springs.map((props, index) => (
          <animated.div key={items[index].href} style={props} className="flex cursor-pointer justify-between file-list-bg p-2 items-center w-1/2 rounded">
            <File 
              item={items[index]} 
              index={index} 
              onCheck={handleCheck} 
              onAnalyze={() => handleAnalyze(items[index])}
              isChecked={selectedItems.includes(items[index])}
            />
          </animated.div>
        ))}
        {selectedItems.length >= 2 &&
            <button 
                onClick={handleAnalyze}
                className="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                <FontAwesomeIcon icon={faCodeCompare}></FontAwesomeIcon> &nbsp; 
                Porównaj
            </button>
        }

        <BusyDialog isOpen={processing}></BusyDialog>

      </div>
    );
  };
  
export default Files;

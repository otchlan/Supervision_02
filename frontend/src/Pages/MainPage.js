import React, { useState } from 'react';

import '../index.css'
import TextInput from "../Components/TextInput"
import TextInput2 from "../Components/TextInput2"
import LinksList from "../Components/LinksList"
import TabsMenu from "../Components/TabsMenu"

const MainPage = ({ children }) => {
    
    const data = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
  
    const components = [TextInput, TextInput2];

  return (
    <div className="container mx-auto p-4 mt-4" style={{ position: 'absolute', left: 0, top: 0 }}>
        
        {/*
        <TextInput />
        <LinksList data={data} />
        */}
        <TabsMenu components={components}/>
        
        
    </div>
  );
};

export default MainPage;

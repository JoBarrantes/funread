import React, { useState } from "react";
import './TemplateImage.css';
import ButtonNav from "../ButtonNav/ButtonNav";
import Form from 'react-bootstrap/Form';


function TemplateImage (){

    const [file, setFile] = useState();
    function handleChange(e) {
        console.log(e.target.files);
        setFile(URL.createObjectURL(e.target.files[0]));
    }

    return (
        
        <div id="template">
            <ul>
                <li>
                    {/*<input size="lg" type="text" placeholder="Write here" id="title"/>*/}
                    <Form.Control size="lg" type="text" placeholder="Write here" />
                </li>
                <li>
                    <input type="file" onChange={handleChange}/>
                </li>
                <li>
                    <img src={file} id="image"/>
                </li>
            </ul>
        </div>
      
    );
};

export default TemplateImage; 


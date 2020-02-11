import {sections} from './sections.js';
import React from 'react';
import ReactDOM from 'react-dom';
import Character from './character/main.jsx';

window.onload = () => {
    ReactDOM.render(
        <Character />,
        document.getElementById('character')
    );
}

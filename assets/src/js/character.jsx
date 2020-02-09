import {sections} from './sections.js';
import React from 'react';
import ReactDOM from 'react-dom';
import Character from './character/main.jsx';

window.onload = () => {
    sections.hideAll();

    ReactDOM.render(
        <Character />,
        document.getElementById('character')
    );

    document.querySelectorAll('.character-controls-btn').forEach((btnEl, i) => {
        btnEl.addEventListener('click', (e) => {
            let target = e.currentTarget.getAttribute('id').substr(10);
            sections.show(target);
        });
    });
}

import {sections} from './sections.js';

window.onload = () => {
    sections.hideAll();

    document.querySelector('#new_character_form--cancel').addEventListener('click', () => {
        sections.hideAll();
    });

    document.querySelector('#new_character').addEventListener('click', () => {
        sections.show('#new_character_form');
    });

    document.querySelectorAll('#character-list .character-list--entry').forEach((charEl, i) => {
        charEl.addEventListener('click', (e) => {
            let url_part = e.currentTarget.getAttribute('data-href');
            document.location = document.location.origin + url_part;
        })
    });

};

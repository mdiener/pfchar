import {sections} from './sections.js';
import {controls} from './character/controls.js';

window.onload = () => {
    sections.hideAll();
    sections.show('#character--main');
};

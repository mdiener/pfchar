import {controls} from '../view/controls.js';
import Character from '../model/character.js';
import BasicsControl from './basics.js';

export let main = () => {
    let char = new Character();
    char.load().then(() => {
        let basicsController = new BasicsControl(char);
    });
}

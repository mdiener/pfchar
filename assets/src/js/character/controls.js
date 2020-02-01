import {sections} from '../sections.js';


class Controls {
    constructor() {
        document.querySelectorAll('.character-controls-btn').forEach((btnEl, i) => {
            btnEl.addEventListener('click', (e) => {
                let id = e.currentTarget.getAttribute('id');
                let target = id.split('--');
                if (target[0] == 'controls') this._goTo(target[1]);
            });
        });
    }

    _goBack() {
        let sectionEls = document.querySelectorAll('.section.character-section');
        let index = 0;

        sectionEls.forEach((sectionEl, i) => {
            if (sectionEl.classList.contains('visible')) {
                index = i;
            }
        });

        sections.hideAll()
        if (index == 0) {
            sections.show('#' + sectionEls[sectionEls.length - 1].getAttribute('id'));
        } else {
            sections.show('#' + sectionEls[index - 1].getAttribute('id'))
        }
    }

    _goForward() {
        let sectionEls = document.querySelectorAll('.section.character-section');
        let index = 0;

        sectionEls.forEach((sectionEl, i) => {
            if (sectionEl.classList.contains('visible')) {
                index = i;
            }
        });

        sections.hideAll()
        if (index == sectionEls.length - 1) {
            sections.show('#' + sectionEls[0].getAttribute('id'));
        } else {
            sections.show('#' + sectionEls[index + 1].getAttribute('id'))
        }
    }

    _goTo(target) {
        if (target == 'back') {
            this._goBack();
        } else if (target == 'forward') {
            this._goForward();
        } else {
            sections.hideAll();
            sections.show('#character--' + target);
        }
    }
}


export var controls = new Controls()

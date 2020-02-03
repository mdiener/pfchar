import {sections} from '../../sections.js';

class Controls {
    constructor() {
        sections.hideAll();
        sections.show('#character--main');

        document.querySelectorAll('.character-controls-btn').forEach((btnEl, i) => {
            btnEl.addEventListener('click', (e) => {
                let id = e.currentTarget.getAttribute('id');
                let target = id.split('--');
                if (target[0] == 'controls') this.goTo(target[1]);
            });
        });
    }

    goBack() {
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

    goForward() {
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

    goTo(target) {
        if (target == 'back') {
            this.goBack();
        } else if (target == 'forward') {
            this.goForward();
        } else {
            sections.hideAll();
            sections.show('#character--' + target);
        }
    }
}


export var controls = new Controls()

export default class BasicsView {
    constructor(controller) {
        self._controller = controller;

        this._nameEl = document.querySelector('#basics--name input');
        this._alignmentEl = document.querySelector('#basics--alignment input');
        this._raceEl = document.querySelector('#basics--race input');
        this._deityEl = document.querySelector('#basics--deity input');
        this._sizeEl = document.querySelector('#basics--size input');
        this._genderEl = document.querySelector('#basics--gender input');
        this._ageEl = document.querySelector('#basics--age input');
        this._heightEl = document.querySelector('#basics--height input');
        this._weightEl = document.querySelector('#basics--weight input');
        this._hairEl = document.querySelector('#basics--hair input');
        this._eyesEl = document.querySelector('#basics--eyes input');
        this._homelandEl = document.querySelector('#basics--homeland input');

        this._registerEvents();
    }

    update(data) {
        this._nameEl.value = data.name;
        this._alignmentEl.value = data.alignment;
        this._raceEl.value = data.race;
        this._deityEl.value = data.deity;
        this._sizeEl.value = data.size;
        this._genderEl.value = data.gender;
        this._ageEl.value = data.age;
        this._heightEl.value = data.height;
        this._weightEl.value = data.weight;
        this._hairEl.value = data.hair;
        this._eyesEl.value = data.eyes;
        this._homelandEl.value = data.homeland;
    }

    _registerEvents() {
        document.querySelectorAll('#basics input').forEach((inputEl, i) => {
            inputEl.addEventListener('input', (e) => {
                let target = e.currentTarget.parentElement.getAttribute('id').substr(8);
                let value = e.currentTarget.value;
                self._controller.inputEvent(target, value);
            });
        });
    }
}

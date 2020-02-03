import BasicsView from '../view/basics.js';


export default class BasicsControl {
    constructor(charModel) {
        this._charModel = charModel;

        let view = new BasicsView(this);
        view.update(this._charModel.basics);
    }

    inputEvent(target, value) {
        this._charModel.set('basics.' + target, value);
    }
}

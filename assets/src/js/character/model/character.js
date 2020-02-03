export default class Character {
    constructor() {
        this._charid = document.querySelector('#character').getAttribute('data-charid');
    }

    load() {
        let url = document.location.origin + '/rest/character/' + this._charid;

        return new Promise((resolve, reject) => {
            window.fetch(url).then((resp) => resp.json()).then((data) => {
                if (data.status == 'error') {
                    reject();
                    return;
                }

                this._data = data;
                resolve();
            });
        })
    }

    _save_value(path, value) {
        let url = document.location.origin + '/rest/character/' + this._charid;

        window.fetch(url, {
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': JSON.stringify({
                'path': path,
                'value': value
            })
        });
    }

    set(path, value) {
        this._save_value(path, value);
    }

    get basics() {
        return this._data.basics;
    }
}

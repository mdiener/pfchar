class Character {
    constructor() {
        this._charid = document.querySelector('#character').getAttribute('data-charid');
    }

    load() {
        let url = document.location.origin + '/rest/character/' + this._charid;

        return new Promise((resolve, reject) => {
            window.fetch(url).then((resp) => resp.json()).then((data) => {
                if (data.status == 'error') {
                    reject(data.message);
                    return;
                }

                resolve(data);
            });
        });
    }

    set(path, value) {
        let url = document.location.origin + '/rest/character/' + this._charid;

        return new Promise((resolve, reject) => {
            window.fetch(url, {
                'method': 'POST',
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': JSON.stringify({
                    'path': path,
                    'value': value
                })
            }).then((resp) => {
                if (resp.ok) {
                    resolve();
                } else {
                    reject();
                }
            });
        });
    }
}

export const char = new Character();

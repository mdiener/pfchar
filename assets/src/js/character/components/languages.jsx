import React from 'react';

export class CharacterLanguages extends React.Component {
    constructor(props) {
        super(props);

        this.onLanguageCLicked = this.onLanguageCLicked.bind(this);
    }

    renderLanguages(languages) {
        let list = [];
        languages.forEach((language, i) => {
            list.push((
                <span className="list--entry" onClick={this.onLanguageCLicked}>{language}</span>
            ))
        });

        return list;
    }

    onLanguageCLicked(e) {
        let lang = e.currentTarget.textContent;
        let known = this.props.languages.known;
        let available = this.props.languages.available;

        if (known.includes(lang)) {
            known.splice(known.indexOf(lang), 1);
        } else {
            known.push(lang);
        }

        this.props.onChange('languages.known', known);
    }

    render() {
        return (
            <div id="character--languages" className="list list--add-remove">
                <div className="list--remove">
                    <span>Known:</span>
                    {this.renderLanguages(this.props.languages.known)}
                </div>
                <div className="list--add">
                    <span>Available:</span>
                    {this.renderLanguages(this.props.languages.available)}
                </div>
            </div>
        )
    }
}

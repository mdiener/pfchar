import React from 'react';
import {CharacterInput, CharacterNumberInput, CharacterSelectInput} from './inputs.jsx';


export default class Classes extends React.Component {
    constructor(props) {
        super(props);

        this._onClassAdded = this._onClassAdded.bind(this);
        this._onClassLevelChanged = this._onClassLevelChanged.bind(this);
    }

    _getClassComponents(classes) {
        let componentList = [];
        Object.keys(classes).forEach((key) => {
            componentList.push((
                <div key={key} className="flex-box-container">
                    <CharacterInput readOnly={true} value={key} />
                    <CharacterNumberInput pathFragment={key} value={classes[key]} onChange={this._onClassLevelChanged} min={0} />
                </div>
            ))
        });

        return componentList;
    }

    _onClassLevelChanged(path, value) {
        this.props.onChange('classes.' + path, value);
    }

    _onClassAdded(path, value) {
        this.props.onChange('classes.' + value, 1);
    }

    render() {
        let classList = ['occultist']
        Object.keys(this.props.data).forEach((key) => {
            if (classList.includes(key)) classList.splice(classList.indexOf(key), 1);
        });

        return (
            <div className="classes">
                <div className="classes--descriptor flex-box-container">
                    <span>Class</span>
                    <span>Level</span>
                </div>
                {this._getClassComponents(this.props.data)}
                <div className="classes--new">
                    <CharacterSelectInput pathFragment="" onChange={this._onClassAdded} firstHidden={'Select New Class'} selectOptions={classList} />
                </div>
            </div>
        )
    }
}

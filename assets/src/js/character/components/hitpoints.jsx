import React from 'react';
import {CharacterNumberInput, CharacterInput} from './inputs.jsx';


export default class Hitpoints extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(path, value) {
        this.props.onChange('hitpoints.' + path, value);
    }

    render() {
        return (
            <div className="hitpoints">
                <p>Hitpoints</p>
                <div className="input-field-group flex-box-container">
                    <CharacterNumberInput pathFragment={'total'} value={this.props.data.total} descriptor={'Total'} descriptorPosition={'below'} onChange={this.onChange} />
                    <CharacterNumberInput pathFragment={'dr'} value={this.props.data.dr} descriptor={'DR'} descriptorPosition={'below'} onChange={this.onChange} />
                    <CharacterNumberInput pathFragment={'current'} value={this.props.data.current} descriptor={'Current HP'} descriptorPosition={'below'} onChange={this.onChange} />
                </div>
            </div>
        );
    }
}

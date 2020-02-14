import React from 'react';
import {CharacterNumberInput, CharacterInput} from './inputs.jsx';


export default class Initiative extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(path, value) {
        this.props.onChange('initiative.' + path, value);
    }

    render() {
        return (
            <div className="initiative flex-box-container">
                <div className="plaque">
                    <span className="text">Initiative</span>
                </div>
                <CharacterNumberInput className="input-field-box" pathFragment={'adjust'} onChange={this.onChange} descriptor={'Adjust'} descriptorPosition={'inside'} value={this.props.data.adjust} />
                <CharacterNumberInput className="input-field-box" readOnly={true} descriptor={'DEX Mod'} descriptorPosition={'inside'} value={this.props.data.dexmod} />
                <CharacterNumberInput className="input-field-box" readOnly={true} descriptor={'Bonus'} descriptorPosition={'inside'} value={this.props.data.bonus.total} />
                <CharacterNumberInput className="total input-field-box" readOnly={true} descriptor={'Total'} descriptorPosition={'inside'} value={this.props.data.total} />
            </div>
        );
    }
}

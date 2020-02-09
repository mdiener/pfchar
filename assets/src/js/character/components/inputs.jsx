import React from 'react';
import {TextInput, NumberInput} from '../../components/inputs.jsx';


export class CharacterInput extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    getCSSClasses() {
        let cssClasses = ['input-field', 'character-input'];

        if (this.props.descriptor) {
            if (this.props.descriptorPosition == 'inside') {
                cssClasses.push('descriptor-inside');
            } else {
                cssClasses.push('descriptor-below');
            }
        }

        return cssClasses.join(' ');
    }

    onChange(value) {
        let path = this.props.pathFragment;

        this.props.onChange(path, value);
    }

    render() {
        if (this.props.descriptor) {
            return (
                <div className={this.getCSSClasses()}>
                    <TextInput value={this.props.value} readOnly={this.props.readOnly} onChange={this.onChange} />
                    <span className="descriptor">{this.props.descriptor}</span>
                </div>
            )
        } else {
            return (
                <div className={this.getCSSClasses()}>
                    <TextInput value={this.props.value} readOnly={this.props.readOnly} onChange={this.onChange} />
                </div>
            )
        }
    }
}


export class CharacterNumberInput extends CharacterInput {
    render() {
        if (this.props.descriptor) {
            return (
                <div className={this.getCSSClasses()}>
                    <NumberInput value={this.props.value} readOnly={this.props.readOnly} min={this.props.min} max={this.props.max} onChange={this.onChange} />
                    <span className="descriptor">{this.props.descriptor}</span>
                </div>
            )
        } else {
            return (
                <div className={this.getCSSClasses()}>
                    <NumberInput value={this.props.value} readOnly={this.props.readOnly} min={this.props.min} max={this.props.max} onChange={this.onChange} />
                </div>
            )
        }
    }
}

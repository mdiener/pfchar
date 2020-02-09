import React from 'react';

export class TextInput extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(e) {
        this.props.onChange(e.currentTarget.value);
    }

    render() {
        return (
            <input type="text" value={this.props.value} readOnly={this.props.readOnly} onChange={this.onChange} />
        )
    }
}


export class NumberInput extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(e) {
        this.props.onChange(e.currentTarget.value);
    }

    render() {
        if (typeof this.props.min == 'number' && typeof this.props.max == 'number') {
            return (
                <input type="number" value={this.props.value} readOnly={this.props.readOnly} min={this.props.min} max={this.props.max} onChange={this.onChange} />
            )
        } else if (typeof this.props.min == 'number') {
            return (
                <input type="number" value={this.props.value} readOnly={this.props.readOnly} min={this.props.min} onChange={this.onChange} />
            )
        } else if (typeof this.props.max == 'number') {
            return (
                <input type="number" value={this.props.value} readOnly={this.props.readOnly} max={this.props.max} onChange={this.onChange} />
            )
        } else {
            return (
                <input type="number" value={this.props.value} readOnly={this.props.readOnly} onChange={this.onChange} />
            )
        }
    }
}

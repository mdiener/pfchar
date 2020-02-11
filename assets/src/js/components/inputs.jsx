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


export class SelectInput extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(e) {
        this.props.onChange(e.currentTarget.value);
    }

    _options(selectOptions, firstHidden) {
        let options = [];

        if (firstHidden) {
            options.push((
                <option key='none' hidden>{this.props.firstHidden}</option>
            ));
        }

        selectOptions.forEach((option, i) => {
            if (option instanceof Array) {
                options.push((
                    <option key={i} value={option[0]}>{option[1]}</option>
                ));
            } else {
                options.push((
                    <option key={i} value={option}>{option[0].toUpperCase() + option.substr(1)}</option>
                ))
            }

        });

        return options;
    }

    render() {
        return (
            <select onChange={this.onChange} defaultValue={this.props.value}>
                {this._options(this.props.selectOptions, this.props.firstHidden)}
            </select>
        )
    }
}


export class Button extends React.Component {
    constructor(props) {
        super(props);

        this.onClick = this.onClick.bind(this);
    }

    onClick(e) {
        this.props.onClick(this.props.onClickValue)
    }

    render() {
        let className = 'btn ' + this.props.className;

        return (
            <button onClick={this.onClick} className={className}>{this.props.value}</button>
        )
    }
}

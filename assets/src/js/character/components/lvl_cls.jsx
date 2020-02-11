import React from 'react';
import Level from './level.jsx';
import Classes from './classes.jsx';


export default class LevelAndClasses extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(path, value) {
        this.props.onChange('exp.' + path, value);
    }

    render() {
        return (
            <div id="lvl-classes">
                <Level data={this.props.data.exp} onChange={this.onChange} />
                <Classes data={this.props.data.exp.classes} onChange={this.onChange} />
            </div>
        )
    }
}

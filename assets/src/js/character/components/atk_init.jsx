import React from 'react';
import Attacks from './attacks.jsx';
import Initiative from './initiative.jsx';


export default class AttackAndInitiative extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="attack-initiative">
                <Initiative data={this.props.data.initiative} dexMod={this.props.data.dexMod} onChange={this.props.onChange} />
                <Attacks data={this.props.data.attack} onChange={this.props.onChange} />
            </div>
        );
    }
}

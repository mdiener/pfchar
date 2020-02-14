import React from 'react';
import Attributes from './attributes.jsx';
import Hitpoints from './hitpoints.jsx';


export default class AttributesAndHP extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="attributes-hitpoints">
                <Attributes data={this.props.data.attributes} onChange={this.props.onChange} />
                <Hitpoints data={this.props.data.hitpoints} onChange={this.props.onChange} />
            </div>
        );
    }
}

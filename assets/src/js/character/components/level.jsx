import React from 'react';
import {CharacterInput, CharacterNumberInput, CharacterSelectInput} from './inputs.jsx';


export default class Level extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(path, value) {
        this.props.onChange(path, value);
    }

    render() {
        let growthOptions = [['slow', 'Slow'], ['medium', 'Medium'], ['fast', 'Fast']];

        return (
            <div className="level">
                <p>You are encouraged to set experience when leveling up instead of level, as setting level will reset experience to whatever base line that level has.</p>
                <div className="flex-box-container">
                    <CharacterNumberInput pathFragment="level" value={this.props.data.level} descriptor={'Level'} descriptorPosition={'below'} onChange={this.onChange} min={0} />
                    <CharacterNumberInput pathFragment="experience" value={this.props.data.experience} descriptor={'Experience'} descriptorPosition={'below'} onChange={this.onChange} min={0} />
                    <CharacterNumberInput value={this.props.data.nextLevel} descriptor={'Exp To LvlUp'} descriptorPosition={'below'} readOnly={true} />
                    <CharacterSelectInput pathFragment="growth" value={this.props.data.growth} descriptor={'Growth'} onChange={this.onChange} selectOptions={growthOptions} />
                </div>
            </div>
        )
    }
}

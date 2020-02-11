import React from 'react';
import {CharacterInput, CharacterNumberInput} from './inputs.jsx';
import {CharacterLanguages} from './languages.jsx';


export default class Basics extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(path, value) {
        path = 'basics.' + path
        this.props.onChange(path, value);
    }

    render() {
        return (
            <div id="basics">
                <p>Basic Character Information</p>
                <CharacterInput value={this.props.data.name} descriptor={'Name'} descriptorPosition={'below'} />
                <div className="input-field-group flex-box-container">
                    <div className="column-50">
                        <CharacterInput pathFragment="alignment" value={this.props.data.alignment} descriptor={'Alignment'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="race" value={this.props.data.race} descriptor={'Race'} descriptorPosition={'below'} readOnly={true} onChange={this.onChange} />
                        <CharacterInput pathFragment="deity" value={this.props.data.deity} descriptor={'Deity'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="size" value={this.props.data.size} descriptor={'Size'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="gender" value={this.props.data.gender} descriptor={'Gender'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="age" value={this.props.data.age} descriptor={'Age'} descriptorPosition={'below'} onChange={this.onChange} />
                    </div>
                    <div className="column-50">
                        <CharacterInput pathFragment="height" value={this.props.data.height} descriptor={'Height'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="weight" value={this.props.data.weight} descriptor={'Weight'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="hair" value={this.props.data.hair} descriptor={'Hair'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="eyes" value={this.props.data.eyes} descriptor={'Eyes'} descriptorPosition={'below'} onChange={this.onChange} />
                        <CharacterInput pathFragment="homeland" value={this.props.data.homeland} descriptor={'Homeland'} descriptorPosition={'below'} onChange={this.onChange} />
                    </div>
                </div>
                <div className="speed">
                    <p>Character Speed</p>
                    <div className="input-field-group flex-box-container">
                        <div className="column-50">
                            <CharacterInput pathFragment="speed.base" value={this.props.data.speed.base} descriptor={'Base'} descriptorPosition={'below'} onChange={this.onChange} />
                            <CharacterInput pathFragment="speed.armor" value={this.props.data.speed.armor} descriptor={'Armor'} descriptorPosition={'below'} onChange={this.onChange} />
                            <CharacterInput pathFragment="speed.fly" value={this.props.data.speed.fly} descriptor={'Fly'} descriptorPosition={'below'} onChange={this.onChange} />
                        </div>
                        <div className="column-50">
                            <CharacterInput pathFragment="speed.swim" value={this.props.data.speed.swim} descriptor={'Swim'} descriptorPosition={'below'} onChange={this.onChange} />
                            <CharacterInput pathFragment="speed.climb" value={this.props.data.speed.climb} descriptor={'Climb'} descriptorPosition={'below'} onChange={this.onChange} />
                            <CharacterInput pathFragment="speed.burrow" value={this.props.data.speed.burrow} descriptor={'Burrow'} descriptorPosition={'below'} onChange={this.onChange} />
                        </div>
                    </div>
                </div>
                <CharacterLanguages languages={this.props.data.languages} onChange={this.onChange} />
            </div>
        )
    }
}

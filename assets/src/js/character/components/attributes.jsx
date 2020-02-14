import React from 'react';
import {CharacterNumberInput, CharacterInput} from './inputs.jsx';


class Attribute extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    _getAttr(score, bonus, adjust) {
        let attr = {
            score: score,
            adjust: adjust,
            bonus: bonus.total,
            totalPoints: 0,
            modifier: ''
        };

        attr.totalPoints = attr.score + attr.adjust + attr.bonus;
        let mod = (attr.totalPoints - 10) / 2;
        if (mod < 0) {
            attr.modifier = Math.ceil(mod).toString();
        } else {
            attr.modifier = '+' + Math.floor(mod).toString();
        }

        return attr;
    }

    onChange(path, value) {
        this.props.onChange(this.props.shortName.toLowerCase() + '.' + path, value);
    }

    render() {
        let attr = this.props.data
        if (attr.modifier < 0) {
            attr.modifier = attr.modifier.toString();
        } else {
            attr.modifier = '+' + attr.modifier.toString();
        }

        return (
            <div className="attribute flex-box-container">
                <div className="plaque">
                    <span className="text-top">{this.props.shortName}</span>
                    <span className="text-bottom">{this.props.longName}</span>
                </div>
                <CharacterNumberInput pathFragment="score" className="input-field-box" onChange={this.onChange} value={attr.score} min={0} />
                <CharacterNumberInput pathFragment="adjust" className="input-field-box" onChange={this.onChange} value={attr.adjust} />
                <CharacterNumberInput className="input-field-box" readOnly={true} value={attr.bonus.total} />
                <CharacterNumberInput className="total input-field-box" readOnly={true} value={attr.total} />
                <CharacterInput className="total input-field-box" readOnly={true} value={attr.modifier} />
            </div>
        )
    }
}


export default class AttributesAndHP extends React.Component {
    constructor(props) {
        super(props);

        this.onChange = this.onChange.bind(this);
    }

    onChange(path, value) {
        this.props.onChange('attributes.' + path, value);
    }

    render() {
        return (
            <div className="attributes">
                <p>Attributes</p>
                <div className="attribute--descriptors flex-box-container">
                    <span className="attribute--descriptor">Ability Name</span>
                    <span className="attribute--descriptor">Ability Score</span>
                    <span className="attribute--descriptor">Adjustment</span>
                    <span className="attribute--descriptor">Bonus Modifier</span>
                    <span className="attribute--descriptor">Total Points</span>
                    <span className="attribute--descriptor">Ability Modifier</span>
                </div>
                <Attribute shortName={'STR'} longName={'Strength'} data={this.props.data.str} onChange={this.onChange} />
                <Attribute shortName={'DEX'} longName={'Dexterity'} data={this.props.data.dex} onChange={this.onChange} />
                <Attribute shortName={'CON'} longName={'Constitution'} data={this.props.data.con} onChange={this.onChange} />
                <Attribute shortName={'INT'} longName={'Intelligence'} data={this.props.data.int} onChange={this.onChange} />
                <Attribute shortName={'WIS'} longName={'Wisdom'} data={this.props.data.wis} onChange={this.onChange} />
                <Attribute shortName={'CHA'} longName={'Charisam'} data={this.props.data.cha} onChange={this.onChange} />
            </div>
        );
    }
}

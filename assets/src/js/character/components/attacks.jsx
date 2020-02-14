import React from 'react';
import {CharacterNumberInput} from './inputs.jsx';


export default class Attacks extends React.Component {
    constructor(props) {
        super(props);
    }

    _attacks(data) {
        let atks = [];

        data.forEach((attack, i) => {
            atks.push((
                <div key={i} className="attack">
                    <p>Attack {i + 1}</p>
                    <div className="bab input-group flex-box-container">
                        <div className="plaque"><span className="text">Base Atack Bonus</span></div>
                        <CharacterNumberInput className="input-field-box" value={attack.bab} readOnly={true} />
                    </div>
                    <div className="cmb input-group flex-box-container">
                        <div className="plaque"><span className="text">CMB</span></div>
                        <CharacterNumberInput className="input-field-box" value={attack.bab} readOnly={true} descriptor={'BAB'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="input-field-box" value={attack.cmb.strmod} readOnly={true} descriptor={'STR'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="input-field-box" value={attack.cmb.bonus.total} readOnly={true} descriptor={'Bonus'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="total input-field-box" value={attack.cmb.total} readOnly={true} descriptor={'Total'} descriptorPosition={'inside'} />
                    </div>
                    <div className="cmd input-group flex-box-container">
                        <div className="plaque"><span className="text">CMD</span></div>
                        <CharacterNumberInput className="input-field-box" value={attack.bab} readOnly={true} descriptor={'BAB'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="input-field-box" value={attack.cmd.strmod} readOnly={true} descriptor={'STR'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="input-field-box" value={attack.cmd.dexmod} readOnly={true} descriptor={'DEX'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="input-field-box" value={attack.cmd.bonus.total} readOnly={true} descriptor={'Bonus'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="input-field-box" value={attack.cmd.base} readOnly={true} descriptor={'Base'} descriptorPosition={'inside'} />
                        <CharacterNumberInput className="total input-field-box" value={attack.cmd.total} readOnly={true} descriptor={'Total'} descriptorPosition={'inside'} />
                    </div>
                </div>
            ))
        });

        return atks;
    }

    render() {
        return (
            <div className="attacks">
                {this._attacks(this.props.data)}
            </div>
        );
    }
}

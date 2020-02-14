import React from 'react';
import {char} from './fetch/character.js';
import Basics from './components/basics.jsx';
import LevelAndClasses from './components/lvl_cls.jsx';
import AttributesAndHP from './components/attr_hp.jsx';
import AttackAndInitiative from './components/atk_init.jsx';
import {Button} from '../components/inputs.jsx';


export default class Character extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            isLoaded: false,
            charData: null,
            error: null,
            activeView: 'basics'
        }

        this.onChange = this.onChange.bind(this);
        this._changeView = this._changeView.bind(this);
        this.onChangeReload = this.onChangeReload.bind(this);
    }

    _load() {
        char.load().then(data => {
            this.setState({
                isLoaded: true,
                charData: data
            });
        }, error => {
            this.setState({
                isLoaded: true,
                error: error
            });
        });
    }

    _getActiveView(viewName) {
        let data = null;

        switch (viewName) {
            case 'basics':
                return (<Basics data={this.state.charData.basics} onChange={this.onChange} />);
                break;
            case 'lvl-classes':
                data = {
                    classes: this.state.charData.classes,
                    exp: this.state.charData.exp
                };
                return (<LevelAndClasses data={data} onChange={this.onChangeReload} />);
                break;
            case 'attr-hp':
                data = {
                    attributes: this._sumupAttributes(this.state.charData.attributes),
                    hitpoints: this.state.charData.hitpoints
                };
                return (<AttributesAndHP data={data} onChange={this.onChange} />);
                break;
            case 'atk-init':
                let attrs = this._sumupAttributes(this.state.charData.attributes);
                data = {
                    attack: this._sumupAttack(this.state.charData.attack, attrs.dex.modifier, attrs.str.modifier),
                    initiative: this._sumupInitiative(this.state.charData.initiative, attrs.dex.modifier)
                };
                return (<AttackAndInitiative data={data} onChange={this.onChange} />);
                break;
            case 'saves-ac':
                let attrs = this._sumupAttributes(this.state.charData.attributes);
                data = {
                    saves: this._sumupSaves(this.state.charData.saves, attrs),
                    ac: this._sumupAC(this.state.charData.ac, attrs.dex.modifier)
                }
        }
    }

    _changeView(view) {
        this.setState({
            activeView: view
        });
    }

    componentDidMount() {
        this._load();
    }

    onChangeReload(path, value) {
        if (path.startsWith('exp')) {
            char.set(path, value).then(() => {
                this._load();
            }, () => {
                this._load();
            });
        }
    }

    onChange(path, value) {
        this.setState({
            charData: this._update_data(this.state.charData, path.split('.'), value)
        });

        char.set(path, value);
    }

    _update_data(data, path, value) {
        if (path[0] in data) {
            if (path.length > 1) {
                let base = path.splice(0, 1)
                this._update_data(data[base[0]], path, value)
            } else {
                data[path[0]] = value;
            }
        }

        return data;
    }

    _sumupAttributes(attributes) {
        let attrs = {};

        Object.keys(attributes).forEach((key) => {
            attrs[key] = {
                total: 0,
                modifier: 0,
                bonus: attributes[key].bonus,
                adjust: attributes[key].adjust,
                score: attributes[key].score
            }

            attrs[key].total = attributes[key].score + attributes[key].adjust + attributes[key].bonus.total;
            let mod = (attrs[key].total - 10) / 2;
            if (mod < 0) {
                attrs[key].modifier = Math.ceil(mod);
            } else {
                attrs[key].modifier = Math.floor(mod);
            }
        });

        return attrs;
    }

    _sumupAttack(attack, dexmod, strmod) {
        let atks = [];

        attack.bab.forEach((bab) => {
            atks.push({
                bab: bab,
                cmb: {
                    bonus: attack.cmb.bonus,
                    strmod: strmod,
                    total: bab + attack.cmb.bonus.total + strmod
                },
                cmd: {
                    bonus: attack.cmd.bonus,
                    strmod: strmod,
                    dexmod: dexmod,
                    base: 10,
                    total: bab + attack.cmd.bonus.total + strmod + dexmod + 10
                }
            });
        });

        return atks;
    }

    _sumupInitiative(initiative, dexmod) {
        return {
            dexmod: dexmod,
            total: initiative.adjust + initiative.bonus.total + dexmod,
            adjust: initiative.adjust,
            bonus: initiative.bonus
        };
    }

    _sumupSaves(saves, attrs) {
        return {
            fortitude: {
                base: saves.fortitude.base,
                bonus: saves.fortitude.bonus,
                adjust: saves.fortitude.adjust,
                magic: saves.fortitude.magic,
                conmod: attrs.con.modifier,
                total: saves.fortitude.bae + saves.fortitude.bonus.total + saves.fortitude.adjust + saves.fortitude.magic + attrs.con.modifier
            },
            reflex: {
                base: saves.reflex.base,
                bonus: saves.reflex.bonus,
                adjust: saves.reflex.adjust,
                magic: saves.reflex.magic,
                dexmod: attrs.dex.modifier,
                total: saves.reflex.bae + saves.reflex.bonus.total + saves.reflex.adjust + saves.reflex.magic + attrs.con.modifier
            },
            will: {
                base: saves.will.base,
                bonus: saves.will.bonus,
                adjust: saves.will.adjust,
                magic: saves.will.magic,
                wismod: attrs.wis.modifier,
                total: saves.will.bae + saves.will.bonus.total + saves.will.adjust + saves.will.magic + attrs.con.modifier
            }
        }
    }

    _sumupAC(ac, dexmod) {
        shield = 0;
        armor = 0;

        return {
            ac: {
                base: ac.base,
                dexmod: dexmod,
                armor: 0,
                shield: 0,
                deflection: ac.deflection_modifier,
                dodge: ac.dodge_bonus,
                natural: ac.natural_armor,
                adjust: ac.adjust,
                bonus: ac.bonus,
                total: ac.base + dexmod + armor + shield + ac.deflection_modifier + ac.dodge_bonus + ac.natural_armor + ac.adjust + ac.bonus.total
            },
            touch: {
                adjust: ac.touch_adjust,
                total: ac.base + dexmod + ac.deflection_modifier + ac.dodge_bonus + ac.natural_armor + ac.adjust + ac.bonus.total
            }
        }
    }

    render() {
        let {isLoaded, charData, error} = this.state;

        if (!isLoaded) {
            return (
                <div className="not-loaded">
                    <p>Character Loading ...</p>
                </div>
            );
        } else if (error != null) {
            return (
                <div className="error">
                    <h1>Error Loading Character</h1>
                    <p>Your character could not be loaded. The following error occurred:</p>
                    <p>{error}</p>
                </div>
            );
        } else {
            return (
                <div>
                    <div id="controls">
                        <Button onClick={this._changeView} className="character-controls-btn" value="Basics" onClickValue={'basics'} />
                        <Button onClick={this._changeView} className="character-controls-btn" value="Level & Classes" onClickValue={'lvl-classes'} />
                        <Button onClick={this._changeView} className="character-controls-btn" value="Attributes & HP" onClickValue={'attr-hp'} />
                        <Button onClick={this._changeView} className="character-controls-btn" value="Attack & Initiative" onClickValue={'atk-init'} />
                        <Button onClick={this._changeView} className="character-controls-btn" value="AC & Savings" onClickValue={'ac-savings'} />
                        <Button onClick={this._changeView} className="character-controls-btn" value="Skills" onClickValue={'skills'} />
                    </div>
                    <div id="char">
                        {this._getActiveView(this.state.activeView)}
                    </div>
                </div>
            );
        }
    }
}

import React from 'react';
import {char} from './fetch/character.js';
import Basics from './components/basics.jsx';
import LevelAndClasses from './components/lvl_cls.jsx';
import AttributesAndHP from './components/attr_hp.jsx';
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
                        <Button onClick={this._changeView} className="character-controls-btn" value="Attack & Initiative" onClickValue={'att-init'} />
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

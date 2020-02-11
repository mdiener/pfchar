import React from 'react';
import {char} from './fetch/character.js';
import Basics from './components/basics.jsx';
import LevelAndClasses from './components/lvl_cls.jsx';
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
        let basics = this.state.charData.basics;
        let lvlCls = {
            classes: this.state.charData.classes,
            exp: this.state.charData.exp
        };

        switch (viewName) {
            case 'basics': return (<Basics data={basics} onChange={this.onChange} />); break;
            case 'lvl-classes': return (<LevelAndClasses data={lvlCls} onChange={this.onChangeReload} />); break;
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

    render() {
        let {isLoaded, charData, error} = this.state;

        if (!isLoaded) {
            return (
                <div className="not-loaded">
                    <p>Character Loading ...</p>
                </div>
            )
        } else if (error != null) {
            return (
                <div className="error">
                    <h1>Error Loading Character</h1>
                    <p>Your character could not be loaded. The following error occurred:</p>
                    <p>{error}</p>
                </div>
            )
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

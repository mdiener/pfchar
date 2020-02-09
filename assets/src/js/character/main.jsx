import React from 'react';
import Basics from './components/basics.jsx';
import {char} from './fetch/character.js';


export default class Character extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            isLoaded: false,
            charData: null,
            error: null
        }

        this.onChange = this.onChange.bind(this);
    }

    componentDidMount() {
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
                <Basics basics={charData.basics} onChange={this.onChange} />
            );
        }
    }
}

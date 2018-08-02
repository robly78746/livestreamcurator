import React, { Component } from 'react';

class TwitchStream extends Component {
    constructor(props) {
        super(props);
        this.id = this.props.channel + 'Twitch';
    }
    componentDidMount() {
        const options = {
            width: this.props.width,
            height: this.props.height,
            channel: this.props.channel
        };
        var player = new window.Twitch.Player(this.id, options);
    }
    render() {
        return (
            <div id={this.id}></div>
        );
    }
}

TwitchStream.defaultProps = {
    width: '400',
    height: '300',
}

export default TwitchStream;
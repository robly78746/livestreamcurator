import React, { Component } from 'react';
import LivestreamerList from '../presentational/livestreamerList';

// list of live streamers
// state: different sorts or filters
class SortableLivestreamerList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            livestreams: this.props.livestreams
        }
        this.sort = this.sort.bind(this);
    }
    componentDidMount() {
        this.sort((a, b) => a.name.localeCompare(b.name));
    }
    sort(compareFunction) {
        var sortedLivestreams = [...this.state.livestreams];
        sortedLivestreams.sort(compareFunction);
        this.setState({
            livestreams: sortedLivestreams
        });
    }
    render() {
        return (
            <LivestreamerList livestreams={this.state.livestreams}/>
        );
    }
}

SortableLivestreamerList.defaultProps = {
    livestreams: []
}

export default SortableLivestreamerList;
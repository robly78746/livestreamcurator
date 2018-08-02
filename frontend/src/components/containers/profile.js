import React, { Component } from 'react';
import SortableLivestreamerList from './sortableLivestreamerList';
import { apiClient } from '../../util/ApiClient';

class Profile extends Component{
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            livestreams: []
        };
    }
    componentDidMount() {
        apiClient().get("users?username=" + this.props.match.params.username)
            .then(
                (response) => {
                    apiClient().get("users/" + response.data.results[0].id + "/livestreams").then(
                        (response) => {
                            this.setState({
                                livestreams: response.data.results,
                                isLoaded: true
                            });
                        },
                        (error) => {
                            this.setState({
                                isLoaded: true,
                                error
                            });
                        }
                    );
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            );
    }
    render() {
        const { error, isLoaded, livestreams } = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <SortableLivestreamerList livestreams={livestreams}/>
            );
        }
    }
}

export default Profile;
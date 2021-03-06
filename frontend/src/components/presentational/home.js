import React, { Component } from 'react';
import { loggedIn } from '../../util/Auth';
import SortableLivestreamerList from '../containers/sortableLivestreamerList';
import { apiClient } from '../../util/ApiClient';

class Home extends Component{
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            livestreams: []
        };
    }
    componentDidMount() {
        apiClient().get("user")
            .then(
                (response) => {
                    apiClient().get("users/" + response.data.id + "/livestreams").then(
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
        if (loggedIn()) {
            if (error) {
                return <div>Error: {error.message}</div>;
            } else if (!isLoaded) {
                return <div>Loading...</div>;
            } else {
                return (
                    <SortableLivestreamerList livestreams={livestreams}/>
                );
            }
        } else {
            return (
                <p>About</p>
            );
        }
        
        
        
        
    }
}

export default Home;
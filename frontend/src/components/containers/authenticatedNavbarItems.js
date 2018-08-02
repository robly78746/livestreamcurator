import React, { Component } from 'react';
import DropdownLink from '../presentational/dropdownLink';
import { apiClient } from '../../util/ApiClient';
import NavDropdownMenu from '../presentational/navDropdownMenu';
import { signout } from '../../util/Auth';

class AuthenticatedNavbarItems extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            username: ""
        };
    }
    
    componentDidMount() {
        apiClient().get("user")
            .then(
                (response) => {
                    this.setState({
                        isLoaded: true,
                        username: response.data.username
                    });
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
        const { error, isLoaded, username } = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <React.Fragment>
                    <NavDropdownMenu label={username}>
                        <DropdownLink to="#" label="Sign out" onClick={signout}/>
                    </NavDropdownMenu>
                </React.Fragment>
            );
        }
    }
}

export default AuthenticatedNavbarItems;
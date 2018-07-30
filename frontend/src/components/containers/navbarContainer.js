import React, { Component } from 'react';
import Navbar from '../presentational/navbar';
import { connect } from 'react-redux'; 
import UnauthenticatedNavbarItems from '../presentational/unauthenticatedNavbarItems';
import AuthenticatedNavbarItems from './authenticatedNavbarItems';

class NavbarContainer extends Component {
    
    render() {
        const loggedIn = this.props.token === null;
        const navbarItems = loggedIn ? <UnauthenticatedNavbarItems/> : <AuthenticatedNavbarItems/>;
        return (
            <Navbar siteLabel="Livestream Curator">
                {navbarItems}
            </Navbar>
        );
    }
}

const mapStateToProps = (state) => {
    return {token: state.token};
};

export default connect(mapStateToProps)(NavbarContainer);
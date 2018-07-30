import NavLink from './navLink';
import React from 'react';

export default function UnauthenticatedNavbarItems(props) {
    return (
        <React.Fragment>
            <NavLink location="/signup" label="Sign up"/>
            <NavLink location="/login" label="Log in"/>
        </React.Fragment>
    );
}
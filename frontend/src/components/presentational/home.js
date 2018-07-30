import React from 'react';
import { loggedIn } from '../../util/Auth';

export default function Home (){
    if (loggedIn()) {
        return (
            <p>Welcome</p>
        );
    } else {
        return (
            <p>About</p>
        );
    }
}
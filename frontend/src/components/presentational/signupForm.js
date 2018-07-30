import React from 'react';
import UsernamePasswordForm from '../containers/usernamePasswordForm';
import { signup } from '../../util/Auth';

export default function SignupForm (){
    return (
        <UsernamePasswordForm submitAction={signup} submitLabel="Sign up"/>
    );
}
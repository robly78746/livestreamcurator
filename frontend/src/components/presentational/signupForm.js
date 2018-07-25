import React, { Component } from 'react';
import UsernamePasswordForm from '../containers/usernamePasswordForm';
import { signup } from '../../util/Auth';

export default function LoginForm (){
    return (
        <UsernamePasswordForm submitAction={signup} submitLabel="Sign up"/>
    );
}
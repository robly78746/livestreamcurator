import React, { Component } from 'react';
import UsernamePasswordForm from '../containers/usernamePasswordForm';
import { login } from '../../util/Auth';

export default function LoginForm (){
    return (
        <UsernamePasswordForm submitAction={login} submitLabel="Login"/>
    );
}
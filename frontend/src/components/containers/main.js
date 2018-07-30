import React from 'react';
import { Switch, Route } from 'react-router-dom';
import LoginForm from '../presentational/loginForm';
import SignupForm from '../presentational/signupForm';
import Home from '../presentational/home';

export default function Main (){
    return (
        <main className="container-fluid text-color">
            <Switch>
                <Route exact path='/' component={Home}/>
                <Route path='/login' component={LoginForm}/>
                <Route path='/signup' component={SignupForm}/>
            </Switch>
        </main>
    );
}
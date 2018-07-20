import React, { Component } from 'react';
import { login } from '../../util/Auth';
import UsernameField from './usernameField';
import PasswordField from './passwordField';

class LoginForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }
    
    handleSubmit(event) {
        login(this.state.username, this.state.password);
        event.preventDefault();
    }
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <UsernameField handleChange={this.handleChange}/>
                <PasswordField handleChange={this.handleChange}/>
                <input type="submit" value="Login" />
            </form>
        );
    }
}

export default LoginForm;
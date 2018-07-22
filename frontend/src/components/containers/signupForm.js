import React, { Component } from 'react';
import { signup } from '../../util/Auth';
import UsernameField from './usernameField';
import PasswordField from './passwordField';

class SignupForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: '',
            confirmPassword: '',
            passwordsMatch: true
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.confirmPasswords = this.confirmPasswords.bind(this);
        this.passwordsMatch = true;
    }
    
    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }
    
    handleSubmit(event) {
        signup(this.state.username, this.state.password);
        event.preventDefault();
    }
    
    handlePasswordChange(event) {
        this.setState({[event.target.name]: event.target.value}, this.confirmPasswords);
    }
    
    confirmPasswords() {
        this.setState({passwordsMatch:this.state.password === this.state.confirmPassword});
    }
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <UsernameField handleChange={this.handleChange}/>
                <PasswordField handleChange={this.handlePasswordChange}/>
                <PasswordField handleChange={this.handlePasswordChange} placeholder='Confirm Password' name='confirmPassword'/>
                <input type="submit" value="Sign up" disabled={!this.state.passwordsMatch} />
            </form>
        );
    }
}

export default SignupForm;
import React, { Component } from 'react';
import FormErrors from '../presentational/formErrors';
import UsernameField from '../presentational/usernameField';
import PasswordField from '../presentational/passwordField';

class UsernamePasswordForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            formErrors: {},
            formValid: false,
            username: '',
            password: '',
            usernameValid: false,
            passwordValid: false,
            showPassword: false
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.validateForm = this.validateForm.bind(this);
    }
    
    handleChange(event, valid=true, errors=[]) {
        const name = event.target.name;
        const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
        let newFormErrors = this.state.formErrors;
        newFormErrors[name] = errors;
        let validKeyName = name + 'Valid';
        this.setState({formErrors: newFormErrors, [validKeyName]: valid, [name]: value}, this.validateForm);
    }
    
    validateForm() {
        this.setState({formValid: this.state.usernameValid && this.state.passwordValid});
    }
    
    handleSubmit(event) {
        this.props.submitAction(this.state.username, this.state.password);
        event.preventDefault();
    }
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <FormErrors errors={this.state.formErrors} />
                <UsernameField
                    handleChange={this.handleChange}
                    value={this.state.username}/>
                <PasswordField
                    handleChange={this.handleChange}
                    value={this.state.password}
                    showPassword={this.state.showPassword}/>
                <input type="submit" value={this.props.submitLabel} disabled={!this.state.formValid}/>
            </form>
        );
    }
}



export default UsernamePasswordForm;
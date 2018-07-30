import React, { Component } from 'react';
import FormErrors from '../presentational/formErrors';
import UsernameField from '../presentational/usernameField';
import PasswordField from '../presentational/passwordField';
import { withRouter } from 'react-router-dom';
import _ from 'lodash';

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
    
    handleChange(event, valid=true, errors=null) {
        const name = event.target.name;
        const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
        let newFormErrors = this.state.formErrors;
        let idLookup = {}
        if (name in newFormErrors) {
            idLookup = newFormErrors[name].map((error) => {
                let message = error.message
                error = {[message]: error.id};
                return error;
            });
        }
        
        //add id to error messages for iteration
        let errorsWithId = [];
        if (errors !== null) {
            errorsWithId = errors.map((error) => {
                if (error in idLookup){
                    return {message: error, id: idLookup[error]};
                }
                return {message: error, id: _.uniqueId()};
            });
        }
        
        newFormErrors[name] = errorsWithId;
        let validKeyName = name + 'Valid';
        this.setState({formErrors: newFormErrors, [validKeyName]: valid, [name]: value}, this.validateForm);
    }
    
    validateForm() {
        this.setState({formValid: this.state.usernameValid && this.state.passwordValid});
    }
    
    handleSubmit(event) {
        event.preventDefault();
        this.props.submitAction(this.state.username, this.state.password);
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



export default withRouter(UsernamePasswordForm);
import React, { Component } from 'react';
import ControlledInputField from './controlledInputField';
import { validate_password } from '../../util/Validation';
import _ from 'lodash';

class PasswordField extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.handleShowPasswordToggle = this.handleShowPasswordToggle.bind(this);
    }
    
    handleChange(event) {
        const value = event.target.value;
        let validation = validate_password(value);
        let valid = validation.valid;
        let errors = validation.errors;
        
        //add id to error messages for iteration
        errors = errors.map((error) => {
            let message = error
            error = {message: message, id: _.uniqueId()};
            return error;
        });
        
        this.props.handleChange(event, valid, errors);
    }
    
    handleShowPasswordToggle(event) {
        this.props.handleChange(event);
    }
    
    render() {
        return (
            <div>
                <ControlledInputField
                    handleChange={this.handleChange}
                    name='password'
                    displayName='Password'
                    value={this.props.value}/>
                <ControlledInputField
                    handleChange={this.handleShowPasswordToggle}
                    type='checkbox'
                    displayName='Show password'
                    label={true}
                    name='showPassword'
                    checked={this.props.showPassword}/>
            </div>
        );
    }
}

export default PasswordField;
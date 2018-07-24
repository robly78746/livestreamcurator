import React, { Component } from 'react';
import ControlledInputField from './controlledInputField';
import { validate_username } from '../../util/Validation';
import _ from 'lodash';

class UsernameField extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        const value = event.target.value;
        let validation = validate_username(value);
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
    
    render() {
        return (
            <ControlledInputField
                handleChange={this.handleChange}
                name='username'
                displayName='Username'
                value={this.props.value}/>
        );
    }
}

export default UsernameField;
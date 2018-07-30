import React, { Component } from 'react';
import ControlledInputField from './controlledInputField';
import { validate_username } from '../../util/Validation';

class UsernameField extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        const value = event.target.value;
        let validation = validate_username(value);
        this.props.handleChange(event, validation.valid, validation.errors);
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
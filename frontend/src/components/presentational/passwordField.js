import React, { Component } from 'react';
import ControlledInputField from './controlledInputField';
import { validate_password } from '../../util/Validation';

class PasswordField extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        const value = event.target.value;
        let validation = validate_password(value);
        this.props.handleChange(event, validation.valid, validation.errors);
    }
    
    render() {
        return (
            <div>
                <ControlledInputField
                    handleChange={this.handleChange}
                    name='password'
                    displayName='Password'
                    value={this.props.value}
                    type={this.props.showPassword ? 'text' : 'password'}/>
                <ControlledInputField
                    handleChange={this.props.handleChange}
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
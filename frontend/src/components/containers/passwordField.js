import React, { Component } from 'react';

class PasswordField extends Component {
    constructor(props) {
        super(props);
        this.state = {
            password: ''
        };
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        this.props.handleChange(event);
        this.setState({[event.target.name]: event.target.value});
        //password validation
    }
    
    render() {
        return (
            <input placeholder={this.props.placeholder} name={this.props.name} onChange={this.props.handleChange} type='password'/>
        );
    }
}

PasswordField.defaultProps = {
    placeholder: 'Password',
    name: 'password'
};

export default PasswordField;
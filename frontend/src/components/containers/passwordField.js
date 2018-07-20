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
            <input label='Password' name='password' onChange={this.props.handleChange} type='password'/>
        );
    }
}

export default PasswordField;
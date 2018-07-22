import React, { Component } from 'react';

class UsernameField extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: ''
        };
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleChange(event) {
        this.props.handleChange(event);
        this.setState({[event.target.name]: event.target.value});
        //username validation
    }
    
    render() {
        return (
            <input placeholder='Username' name='username' onChange={this.props.handleChange}/>
        );
    }
}

export default UsernameField;
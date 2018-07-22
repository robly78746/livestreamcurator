import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import LoginForm from './components/containers/loginForm';
import SignupForm from './components/containers/signupForm';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <SignupForm />
        <LoginForm />
      </div>
    );
  }
}

export default App;

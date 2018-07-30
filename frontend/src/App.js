import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/lib/integration/react';
import { persistor, store } from './store';
import './App.css';
import LoadingView from './components/presentational/loadingView';
import NavbarContainer from './components/containers/navbarContainer';
import Main from './components/containers/main';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <PersistGate loading={<LoadingView />} persistor={persistor}>
          <NavbarContainer />
          <Main />
        </PersistGate>
      </Provider>
    );
  }
}

export default App;

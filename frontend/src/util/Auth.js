import axios from 'axios';
import _ from 'lodash';
import { URL, LOGIN, SIGNUP } from '../config/Api';

export function InvalidCredentialsException(message) {
    this.message = message;
    this.name = 'InvalidCredentialsException';
}

export function signup(username, password) {
    return axios
        .post(URL + SIGNUP, {
            username,
            password
        }).then(function (response) {
            login(username, password);
        })
        .catch(function (error) {
          // raise different exception if due to invalid credentials
          if (_.get(error, 'response.status') === 400) {
            throw new InvalidCredentialsException(error);
          }
          throw error;
        });
}

export function login(username, password) {
  return axios
    .post(URL + LOGIN, {
      username,
      password
    })
    .then(function (response) {
        token = response.data.token;
        console.log(token);
    })
    .catch(function (error) {
      // raise different exception if due to invalid credentials
      if (_.get(error, 'response.status') === 400) {
        throw new InvalidCredentialsException(error);
      }
      throw error;
    });
}

export var token = '';
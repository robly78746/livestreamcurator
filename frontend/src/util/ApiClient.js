import axios from 'axios';
import { URL } from '../config/Api';
import { token } from './Auth';

export const apiClient = function() {
    const params = {
        baseURL: URL,
        headers: {'Authorization': 'Token ' + token}
    };
    return axios.create(params);
}
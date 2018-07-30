import * as actionType from './types';

export const setToken = (data) => {
  return {
    type: actionType.SET_TOKEN,
    data
  }
}

export const unsetToken = () => {
  return {
    type: actionType.UNSET_TOKEN
  }
}
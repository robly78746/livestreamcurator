const USERNAME_REGEX = /^[+\-@._0-9a-zA-Z]*$/
const INVALID_CHARACTERS_USERNAME_ERROR_MESSAGE = "Username can only contain letters, numbers, and @ . + - _ characters."
const BLANK_USERNAME_ERROR_MESSAGE = "Username cannot be blank."
const BLANK_PASSWORD_ERROR_MESSAGE = "Password cannot be blank."
export function validate_username(username) {
    var errors = [];
    const containsValidCharacters = USERNAME_REGEX.test(username);
    if (!containsValidCharacters) {
        errors.push(INVALID_CHARACTERS_USERNAME_ERROR_MESSAGE);
    }
    const notBlank = username.length > 0;
    if (!notBlank) {
        errors.push(BLANK_USERNAME_ERROR_MESSAGE);
    }
    
    const valid = containsValidCharacters && notBlank;
    
    const result = {valid:valid, errors: errors}
    return result;
}

export function validate_password(password) {
    var errors = [];
    const notBlank = password.length > 0;
    if (!notBlank) {
        errors.push(BLANK_PASSWORD_ERROR_MESSAGE);
    }
    const result = {valid: notBlank, errors: errors};
    return result;
}
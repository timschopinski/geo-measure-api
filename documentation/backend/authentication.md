## This documentation provides an overview of the registration, login, and logout processes in the authentication system.

### Table of Contents
- Registration
- Login
- Logout


# Registration
- Endpoint URL: `/api/users/registration/`
- Method: `POST`
- Permission: `AllowAny`

### Description:
The registration process allows new users to create an account. Users need to provide their first name, last name, email, and password.

### Request Body
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password1": "Password123",
  "password2": "Password123"
}
```

### Validation
- Email: `Must be unique. If the email already exists, an error is raised.`
- Passwords: `Must be at least 8 characters long, contain at least one numeral and one letter, and both password fields must match.`
- 
### Responses
201 Created:
json
Copy code
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}
400 Bad Request:
```json
{
  "email": ["A user with this email already exists."],
  "password1": ["Password must contain at least one numeral."],
  "password2": ["The two password fields did not match."]
}
```

## Login

- Endpoint URL: `/api/users/login/`
- Method: `POST`
- Permission: `AllowAny`

### Description
The login process authenticates users using their email and password. Upon successful authentication, a token is generated or refreshed.

### Request Body
```json
{
  "email": "john.doe@example.com",
  "password": "Password123"
}
```
### Validation
- Email and Password: `Must match a registered user. If the credentials are invalid or the account is disabled, appropriate errors are returned.`

### Responses

200 OK:
```json
{
  "key": "abc123def456ghi789jkl"
}
```
400 Bad Request:
```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```
400 Bad Request (Disabled Account):
```json
{
  "non_field_errors": ["User account is disabled."]
}
```

# Logout
- Endpoint URL: `/api/users/logout/`
- Method: `POST`
- Permission: `IsAuthenticated`

Description
The logout process invalidates the user's token, effectively logging them out.

### Request Body
No request body required.

### Responses
200 OK:
```json
{
  "detail": "Successfully logged out."
}
```
400 Bad Request:
```json
{
  "detail": "You should be logged in to logout. Check whether the token is passed."
}
```

## Token Expiration
Tokens are set to expire after a specified duration (settings.TOKEN_EXPIRED_AFTER_SECONDS). Upon expiration, tokens are refreshed. If an expired token is used for authentication, an appropriate error is returned and the token is deleted.

## Example Usage

Include the token in the Authorization header for authenticated requests
```python
headers = {
    'Authorization': 'Token abc123def456ghi789jkl'
}
response = requests.post('http://example.com/api/users/logout/', headers=headers)
```

This documentation outlines the essential components of the authentication system, including the endpoints for user registration, login, and logout, as well as the expected request formats and possible responses. This should serve as a guide for developers interacting with the authentication API.

# Farm API

## Overview
Farm API provides endpoints for managing farms, farmers, crops, and authentication. It allows users to register, log in, and manage farm-related resources.

## Base URL
```sh
http://localhost:8000/api/v1
```

## Authentication
The API uses JWT authentication. To access protected routes, include the token in the `Authorization` header:
```sh
Authorization: Bearer <your_token>
```

### Obtain Token
**Endpoint:** `/login/`
- **Method:** `POST`
- **Description:** Obtain a JWT token by providing valid credentials.
- **Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```
- **Response:**
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### Refresh Token
**Endpoint:** `/refresh/`
- **Method:** `POST`
- **Description:** Refresh an expired JWT access token.
- **Request Body:**
```json
{
  "refresh": "your_refresh_token"
}
```

## Endpoints

### Farmers
#### Retrieve all farmers
- **Endpoint:** `/farmers/`
- **Method:** `GET`
- **Description:** Fetches all farmers.

#### Create a farmer
- **Endpoint:** `/farmers/`
- **Method:** `POST`
- **Request Body:**
```json
{
  "farmer_name": "John Doe",
  "national_id": "123456789",
  "location": "Nairobi",
  "farm_type": 1,
  "crop": 2,
  "created_by": 1
}
```

### Crops
#### Retrieve all crops
- **Endpoint:** `/crop/`
- **Method:** `GET`

#### Create a crop
- **Endpoint:** `/crop/`
- **Method:** `POST`
- **Request Body:**
```json
{
  "name": "Maize"
}
```

#### Retrieve a specific crop
- **Endpoint:** `/crop/{id}/`
- **Method:** `GET`

#### Update a crop
- **Endpoint:** `/crop/{id}/`
- **Method:** `PUT` or `PATCH`
- **Request Body:**
```json
{
  "name": "Wheat"
}
```

#### Delete a crop
- **Endpoint:** `/crop/{id}/`
- **Method:** `DELETE`

### Farm Types
#### Retrieve all farm types
- **Endpoint:** `/farmtype/`
- **Method:** `GET`

#### Create a farm type
- **Endpoint:** `/farmtype/`
- **Method:** `POST`
- **Request Body:**
```json
{
  "name": "Dairy Farm"
}
```

#### Retrieve, update, or delete a farm type
- **Endpoint:** `/farmtype/{id}/`
- **Methods:** `GET`, `PUT`, `PATCH`, `DELETE`

### User Registration
#### Register a new user
- **Endpoint:** `/register/`
- **Method:** `POST`
- **Request Body:**
```json
{
  "username": "newuser",
  "password": "securepassword",
  "role": "clerk"
}
```

#### Response
```json
{
  "successful": true,
  "narration": "User registered successfully",
  "status": 201,
  "body": {
    "id": 1,
    "username": "newuser",
    "email": "newuser@example.com"
  }
}
```

## License
This API is licensed under the [License Name].


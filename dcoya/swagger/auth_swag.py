signup_swag = {
    "tags": ["authentication"],
    "summary": "Register a new user",
    "description": "Register a new user. Username minimum 3 and maximum 10 characters. No white space allowed. Password minimum 8 and maximum 15 characters. No white space allowed.",
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "User created"
        },
        "400": {
            "description": "Invalid data"
        }
    }
}

login_swag = {
    "tags": ["authentication"],
    "summary": "login user",
    "description": "Try to login user by username and password. On success return JWT token",
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "required": True,
            "schema": {
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Login success"
        },
        "400": {
            "description": "Invalid data"
        },
        "401": {
            "description": "Login failed"
        },
        "404": {
            "description": "User not found"
        }
    }
}